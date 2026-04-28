#!/usr/bin/env python3
"""Semi-automatic pipeline for EHR benchmark survey work.

Features:
1. Bootstrap a paper workspace from a paper link.
2. Download/cache the PDF and extracted text.
3. Create a standard summary filename and skeleton Markdown file.
4. Audit example-search coverage for drafted summaries.
5. Sync benchmark names from a completed summary into the local registry.

This script intentionally uses only the Python standard library plus local
command-line tools (`curl`, `pdftotext`) to avoid environment drift.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SUMMARIES_DIR = ROOT / "summaries"
PAPERS_DIR = ROOT / "papers"
REGISTRY_PATH = ROOT / "registry" / "ehr_benchmark_registry.yaml"
REPORTS_DIR = ROOT / "reports"


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def http_get(url: str, timeout: int = 30) -> tuple[bytes, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; ehr-benchmark-pipeline/1.0)"
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content_type = resp.headers.get("Content-Type", "")
        return resp.read(), content_type


def extract_meta(html_text: str, names: list[str]) -> str | None:
    for name in names:
        patterns = [
            rf'<meta[^>]+name=["\']{re.escape(name)}["\'][^>]+content=["\']([^"\']+)["\']',
            rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']{re.escape(name)}["\']',
            rf'<meta[^>]+property=["\']{re.escape(name)}["\'][^>]+content=["\']([^"\']+)["\']',
            rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']{re.escape(name)}["\']',
        ]
        for pattern in patterns:
            match = re.search(pattern, html_text, flags=re.IGNORECASE)
            if match:
                return html.unescape(match.group(1)).strip()
    return None


def extract_html_title(html_text: str) -> str | None:
    match = re.search(r"<title[^>]*>(.*?)</title>", html_text, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    title = re.sub(r"\s+", " ", html.unescape(match.group(1))).strip()
    return title or None


def detect_arxiv_id(url: str) -> str | None:
    patterns = [
        r"arxiv\.org/abs/([0-9]+\.[0-9]+)",
        r"arxiv\.org/pdf/([0-9]+\.[0-9]+)(?:\.pdf)?",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def discover_paper_urls(input_url: str) -> dict[str, str | None]:
    arxiv_id = detect_arxiv_id(input_url)
    if arxiv_id:
        return {
            "paper_url": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            "arxiv_id": arxiv_id,
        }

    if input_url.lower().endswith(".pdf"):
        return {"paper_url": input_url, "pdf_url": input_url, "arxiv_id": None}

    return {"paper_url": input_url, "pdf_url": None, "arxiv_id": None}


def discover_metadata(input_url: str) -> dict[str, Any]:
    urls = discover_paper_urls(input_url)
    paper_url = urls["paper_url"] or input_url
    pdf_url = urls["pdf_url"]
    arxiv_id = urls["arxiv_id"]

    title = None
    year = None
    page_content_type = None
    page_fetched = False

    if paper_url and not paper_url.lower().endswith(".pdf"):
        try:
            data, page_content_type = http_get(paper_url)
            if "html" in page_content_type.lower():
                page_fetched = True
                html_text = data.decode("utf-8", errors="replace")
                title = extract_meta(
                    html_text,
                    ["citation_title", "og:title", "dc.title", "twitter:title"],
                )
                if not title:
                    title = extract_html_title(html_text)
                if title and "arXiv.org" in title:
                    title = re.sub(r"\s*\|\s*arXiv.*$", "", title).strip()
                    title = re.sub(r"\s*\(arXiv:.*\)\s*$", "", title).strip()

                year_raw = extract_meta(
                    html_text,
                    [
                        "citation_publication_date",
                        "citation_date",
                        "dc.date",
                        "article:published_time",
                    ],
                )
                if year_raw:
                    year_match = re.search(r"(19|20)\d{2}", year_raw)
                    if year_match:
                        year = int(year_match.group(0))

                if not pdf_url:
                    pdf_url = extract_meta(html_text, ["citation_pdf_url"])
                    if not pdf_url:
                        pdf_match = re.search(
                            r'href=["\']([^"\']+\.pdf(?:\?[^"\']*)?)["\']',
                            html_text,
                            flags=re.IGNORECASE,
                        )
                        if pdf_match:
                            pdf_url = urllib.parse.urljoin(paper_url, pdf_match.group(1))
        except Exception as exc:  # pragma: no cover - network errors are expected sometimes
            eprint(f"warning: unable to fetch metadata page {paper_url}: {exc}")

    if not title and paper_url and paper_url.lower().endswith(".pdf"):
        filename = Path(urllib.parse.urlparse(paper_url).path).name
        title = re.sub(r"\.pdf$", "", filename, flags=re.IGNORECASE)

    if not year and arxiv_id:
        year = 2000 + int(arxiv_id[:2])

    return {
        "paper_url": paper_url,
        "pdf_url": pdf_url,
        "arxiv_id": arxiv_id,
        "title": title,
        "year": year,
        "page_content_type": page_content_type,
        "page_fetched": page_fetched,
    }


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "paper"


def build_paper_key(title: str | None, year: int | None, fallback: str | None) -> str:
    if title:
        slug = slugify(title)
    elif fallback:
        slug = slugify(fallback)
    else:
        slug = "paper"
    return f"{year}_{slug}" if year else slug


def run_command(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def write_text(path: Path, content: str, force: bool = False) -> None:
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def download_file(url: str, destination: Path, force: bool = False) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not force:
        return
    cmd = ["curl", "-L", url, "-o", str(destination)]
    run_command(cmd)


def extract_pdf_text(pdf_path: Path, txt_path: Path, force: bool = False) -> None:
    if txt_path.exists() and not force:
        return
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("pdftotext is required but was not found in PATH")
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    run_command([pdftotext, str(pdf_path), str(txt_path)])


def build_summary_skeleton(metadata: dict[str, Any], summary_path: Path, paper_dir: Path) -> str:
    title = metadata.get("title") or "Untitled Paper"
    paper_url = metadata.get("paper_url") or ""
    paper_key = metadata["paper_key"]
    today = dt.date.today().isoformat()
    pdf_path = paper_dir / "source.pdf"
    txt_path = paper_dir / "source.txt"
    rel_registry = os.path.relpath(REGISTRY_PATH, summary_path.parent)
    rel_pdf = os.path.relpath(pdf_path, summary_path.parent)
    rel_txt = os.path.relpath(txt_path, summary_path.parent)

    lines = [
        f'<!-- paper_key: "{paper_key}" -->',
        f'<!-- paper_url: "{paper_url}" -->',
        f'<!-- generated_on: "{today}" -->',
        "",
        f"# Benchmark Summary for *{title}*",
        "",
        f"Source paper: [{paper_url}]({paper_url})" if paper_url else "Source paper:",
        "",
        "## Workflow Notes",
        "",
        f"- Initialized by `scripts/ehr_benchmark_pipeline.py` on `{today}`.",
        f"- Registry file: [`{rel_registry}`]({rel_registry})",
        f"- Cached PDF: [`{rel_pdf}`]({rel_pdf})",
        f"- Extracted text: [`{rel_txt}`]({rel_txt})",
        "- Record the exact search path used for this paper: paper body, appendix, supplement, cached source text, and official artifacts named by the paper.",
        "- Record normalization choices, paper/artifact naming discrepancies, and any gated-access limitations.",
        "- Fill benchmark sections below using the survey format.",
        "- Before syncing the registry, run:",
        f"  `python3 scripts/ehr_benchmark_pipeline.py audit-examples \"{summary_path}\"`",
        "- After the summary passes verification, run:",
        f"  `python3 scripts/ehr_benchmark_pipeline.py sync-registry \"{summary_path}\"`",
        "",
        "## Verifier Notes",
        "",
        "- Benchmark existence: ",
        "- Task mapping: ",
        "- Instruction fidelity: ",
        "- Example fidelity: ",
        "- Scoring fidelity: ",
        "- Judge prompt fidelity: ",
        "- Inference labeling: ",
        "",
        "## 1. [Benchmark Name]",
        "",
        "[Benchmark-level description]",
        "",
        "- **Language:** ",
        "- **Clinical Stage:** ",
        "- **Source Clinical Document Type:** ",
        "- **Clinical Specialty:** ",
        "- **Application Method:** ",
        "",
        "---",
        "",
        "## 1.1 Task: [Task Name]",
        "",
        "This task is to [task description].",
        "",
        "### Task type",
        "[Decision Making / Risk Prediction / Classification / Extraction / Generation / QA / etc.]",
        "",
        "```md",
        "### Instruction",
        "[Original or normalized instruction]",
        "### Input",
        "[Input description]",
        "### Output",
        "[Output description]",
        "```",
        "",
        "### Task example",
        "",
        "```md",
        "### Example Provenance",
        "[Paper / appendix / supplement / official dataset card / official repo / source benchmark paper]",
        "### Search Depth",
        "[Paper only / paper + supplement / paper + supplement + linked artifact / paper + linked artifact + source benchmark]",
        "### Example Type",
        "[Concrete dataset instance / prompt template / benchmark-family exemplar]",
        "### Source Dataset / Artifact",
        "[Exact dataset split, scenario file, appendix section, or official artifact that produced this example]",
        "### Task Construction",
        "[How the task is built from the source data, if stated]",
        "### Fidelity",
        "[Verbatim except line-wrap cleanup / lightly reformatted for readability / exact copy]",
        "### Example",
        "[Quoted task example or prompt template from the source]",
        "### Example Input",
        "[Concrete input / context / interaction trace]",
        "### Example Output",
        "[Concrete answer / label / SQL / action / target output]",
        "### Gold / Reference Answer",
        '[Gold label, target text, reference SQL, expected tool action, or "Not explicitly provided in the source."]',
        "```",
        "",
        "### Scoring standard",
        "",
        "```md",
        "### Scoring",
        "[Metric / rubric / exact-match / AUROC / F1 / human evaluation rule / etc.]",
        "### Evaluation Dimensions",
        '[List the dimensions, criteria, rubric axes, or write "Not explicitly provided in the paper."]',
        "### Judge Prompt",
        '[Full judge prompt if explicitly provided; otherwise write "The full judge prompt is not explicitly provided in the paper."]',
        "```",
        "",
    ]
    return "\n".join(lines)


def command_bootstrap(args: argparse.Namespace) -> int:
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)

    metadata = discover_metadata(args.url)
    if args.title:
        metadata["title"] = args.title
    if args.year:
        metadata["year"] = args.year

    fallback = metadata.get("arxiv_id") or Path(urllib.parse.urlparse(args.url).path).stem
    metadata["paper_key"] = build_paper_key(metadata.get("title"), metadata.get("year"), fallback)

    paper_dir = PAPERS_DIR / metadata["paper_key"]
    pdf_path = paper_dir / "source.pdf"
    txt_path = paper_dir / "source.txt"
    metadata_path = paper_dir / "metadata.json"

    summary_filename = f"{metadata['paper_key']}_benchmark_summary.md"
    summary_path = SUMMARIES_DIR / summary_filename

    paper_dir.mkdir(parents=True, exist_ok=True)

    pdf_url = metadata.get("pdf_url")
    if pdf_url:
        try:
            download_file(str(pdf_url), pdf_path, force=args.force)
            extract_pdf_text(pdf_path, txt_path, force=args.force)
        except Exception as exc:
            eprint(f"warning: failed to prepare PDF/text cache: {exc}")
    else:
        eprint("warning: no PDF URL discovered; summary skeleton will still be created")

    metadata_blob = {
        "paper_key": metadata["paper_key"],
        "title": metadata.get("title"),
        "year": metadata.get("year"),
        "paper_url": metadata.get("paper_url"),
        "pdf_url": pdf_url,
        "input_url": args.url,
        "summary_path": str(summary_path),
        "pdf_path": str(pdf_path) if pdf_path.exists() else None,
        "text_path": str(txt_path) if txt_path.exists() else None,
        "created_on": dt.datetime.now().isoformat(timespec="seconds"),
    }
    write_text(metadata_path, json.dumps(metadata_blob, ensure_ascii=False, indent=2) + "\n", force=True)

    skeleton = build_summary_skeleton(metadata, summary_path, paper_dir)
    write_text(summary_path, skeleton, force=args.force)

    print(f"PAPER_KEY={metadata['paper_key']}")
    print(f"SUMMARY_PATH={summary_path}")
    print(f"METADATA_PATH={metadata_path}")
    if pdf_path.exists():
        print(f"PDF_PATH={pdf_path}")
    if txt_path.exists():
        print(f"TEXT_PATH={txt_path}")
    return 0


def parse_summary_header(summary_text: str) -> dict[str, Any]:
    paper_key_match = re.search(r'<!--\s*paper_key:\s*"([^"]+)"\s*-->', summary_text)
    paper_url_match = re.search(r'<!--\s*paper_url:\s*"([^"]+)"\s*-->', summary_text)
    title_match = re.search(r"^# Benchmark Summary for \*(.+?)\*\s*$", summary_text, flags=re.MULTILINE)
    source_match = re.search(r"^Source paper:\s*\[[^\]]*\]\(([^)]+)\)", summary_text, flags=re.MULTILINE)

    header: dict[str, Any] = {
        "paper_key": paper_key_match.group(1) if paper_key_match else None,
        "paper_url": paper_url_match.group(1) if paper_url_match else None,
        "title": title_match.group(1).strip() if title_match else None,
    }
    if source_match:
        header["paper_url"] = source_match.group(1).strip()

    if header.get("paper_key"):
        metadata_path = PAPERS_DIR / header["paper_key"] / "metadata.json"
        if metadata_path.exists():
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            for key in ("title", "paper_url", "year"):
                if metadata.get(key):
                    header[key] = metadata[key]
    return header


def find_benchmark_headings(summary_lines: list[str]) -> list[dict[str, Any]]:
    headings: list[dict[str, Any]] = []
    for idx, line in enumerate(summary_lines):
        match = re.match(r"^## (\d+)\. (.+)$", line)
        if not match:
            continue
        major = match.group(1)
        name = match.group(2).strip()
        if name.startswith("Task:"):
            continue
        if name.endswith("Notes"):
            continue
        headings.append({"major": major, "name": name, "line_index": idx})
    return headings


def parse_task_types(summary_text: str, major: str) -> list[str]:
    pattern = re.compile(
        rf"^## {re.escape(major)}\.\d+ Task: .+?$"  # task heading
        rf"(.*?)"  # task body
        rf"(?=^## {re.escape(major)}\.\d+ (?:Task: |.+ Notes)|^## \d+\. |\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    task_types: list[str] = []
    for match in pattern.finditer(summary_text):
        section = match.group(1)
        type_match = re.search(r"^### Task type\s*$\n([^\n]+)", section, flags=re.MULTILINE)
        if type_match:
            task_type = type_match.group(1).strip()
            if task_type and task_type not in task_types:
                task_types.append(task_type)
    return task_types


def guess_source_system(section_text: str) -> str:
    guesses = [
        ("Stanford Medicine", "Stanford Medicine EHR"),
        ("MIMIC-IV", "MIMIC-IV"),
        ("MIMIC", "MIMIC"),
        ("eICU", "eICU"),
    ]
    for needle, value in guesses:
        if needle.lower() in section_text.lower():
            return value

    derived_match = re.search(r"derived from ([A-Za-z0-9\- /]+?)[\.,]", section_text, flags=re.IGNORECASE)
    if derived_match:
        return derived_match.group(1).strip()
    return ""


def normalize_task_families(task_types: list[str]) -> list[str]:
    normalized = []
    for item in task_types:
        value = item.strip().lower()
        if value and value not in normalized:
            normalized.append(value)
    return normalized


def summarize_benchmark_type(task_types: list[str]) -> str:
    normalized = normalize_task_families(task_types)
    if not normalized:
        return ""
    if len(normalized) == 1:
        return normalized[0]
    return "mixed: " + " + ".join(normalized)


def guess_role(section_text: str) -> str:
    lower = section_text.lower()
    if "out-of-distribution" in lower or "different healthcare system" in lower:
        return "out-of-distribution generalization benchmark"
    if "generalization" in lower:
        return "generalization benchmark"
    if "primary" in lower or "introduced by the paper" in lower or "introduced in the paper" in lower:
        return "primary benchmark"
    return "benchmark used in paper"


def build_registry_entries_from_summary(summary_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    summary_text = summary_path.read_text(encoding="utf-8")
    summary_lines = summary_text.splitlines()
    header = parse_summary_header(summary_text)
    headings = find_benchmark_headings(summary_lines)
    all_heading_indexes = [item["line_index"] for item in headings] + [len(summary_lines)]

    entries: list[dict[str, Any]] = []
    for idx, heading in enumerate(headings):
        start = heading["line_index"] + 1
        end = all_heading_indexes[idx + 1]
        section_text = "\n".join(summary_lines[start:end]).strip()
        task_types = parse_task_types(summary_text, heading["major"])

        source_paper = {
            "title": header.get("title") or summary_path.stem,
            "year": header.get("year") or extract_year_from_path(summary_path),
            "url": header.get("paper_url") or "",
            "role_in_paper": guess_role(section_text),
        }

        entry = {
            "canonical_name": heading["name"],
            "aliases": [],
            "benchmark_type": summarize_benchmark_type(task_types),
            "source_system": guess_source_system(section_text),
            "task_families": normalize_task_families(task_types),
            "source_papers": [source_paper],
            "notes": "",
        }
        entries.append(entry)
    return header, entries


def extract_year_from_path(summary_path: Path) -> int | None:
    match = re.search(r"\b(19|20)\d{2}\b", summary_path.stem)
    if match:
        return int(match.group(0))
    return None


def extract_summary_key(summary_path: Path) -> str:
    return re.sub(r"_benchmark_summary$", "", summary_path.stem)


def load_source_text_for_summary(summary_path: Path) -> tuple[Path, str] | tuple[None, str]:
    paper_key = extract_summary_key(summary_path)
    source_path = PAPERS_DIR / paper_key / "source.txt"
    if not source_path.exists():
        return None, ""
    return source_path, source_path.read_text(encoding="utf-8", errors="replace")


def collect_example_signals(source_text: str, limit: int = 8) -> list[tuple[int, str]]:
    patterns = [
        r"figure\s+\d+.*example",
        r"table\s+\d+.*example",
        r"case\s+\d+",
        r"example interaction",
        r"sample task",
        r"input example",
        r"evaluation examples",
        r"workflow example",
        r"illustrative example",
        r"sample question",
    ]
    matches: list[tuple[int, str]] = []
    seen: set[tuple[int, str]] = set()
    lines = source_text.splitlines()
    for lineno, line in enumerate(lines, start=1):
        compact = re.sub(r"\s+", " ", line).strip()
        if not compact:
            continue
        for pattern in patterns:
            if re.search(pattern, compact, flags=re.IGNORECASE):
                item = (lineno, compact[:220])
                if item not in seen:
                    matches.append(item)
                    seen.add(item)
                break
        if len(matches) >= limit:
            break
    return matches


def collect_urls(source_text: str, limit: int = 10) -> list[str]:
    urls = re.findall(r"https?://[^\s)>\]]+", source_text)
    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        cleaned = url.rstrip(".,;")
        if cleaned not in seen:
            deduped.append(cleaned)
            seen.add(cleaned)
        if len(deduped) >= limit:
            break
    return deduped


def command_audit_examples(args: argparse.Namespace) -> int:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.summary:
        summary_paths = [Path(args.summary).resolve()]
    else:
        summary_paths = sorted(SUMMARIES_DIR.glob("*_benchmark_summary.md"))

    lines = [
        "# Example Search Audit",
        "",
        f"Generated on: {dt.date.today().isoformat()}",
        "",
        "This report re-checks each collected summary for example-search depth using local paper text.",
        "",
    ]

    audited = 0
    for summary_path in summary_paths:
        if not summary_path.exists():
            eprint(f"warning: summary not found: {summary_path}")
            continue

        summary_text = summary_path.read_text(encoding="utf-8")
        no_example_count = summary_text.lower().count("no explicit task example")
        example_block_count = summary_text.count("### Example")
        source_path, source_text = load_source_text_for_summary(summary_path)
        signals = collect_example_signals(source_text)
        urls = collect_urls(source_text)

        lines.append(f"## {summary_path.name}")
        lines.append("")
        lines.append(f"- Summary path: `{summary_path}`")
        lines.append(f"- `No explicit task example` count: {no_example_count}")
        lines.append(f"- `### Example` block count: {example_block_count}")
        lines.append(f"- Source text available: {'yes' if source_path else 'no'}")
        if source_path:
            lines.append(f"- Source text path: `{source_path}`")

        if signals:
            lines.append("- Local example signals:")
            for lineno, signal in signals:
                lines.append(f"  - line {lineno}: {signal}")
        else:
            lines.append("- Local example signals: none detected in cached source text")

        if urls:
            lines.append("- Linked URLs detected in cached source text:")
            for url in urls:
                lines.append(f"  - {url}")
        else:
            lines.append("- Linked URLs detected in cached source text: none")

        lines.append("")
        audited += 1

    output_path = Path(args.output).resolve() if args.output else REPORTS_DIR / f"example_search_audit_{dt.date.today().isoformat()}.md"
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"AUDITED_SUMMARIES={audited}")
    print(f"REPORT_PATH={output_path}")
    return 0


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value == "[]":
        return []
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def _is_benchmark_entry(line: str) -> bool:
    """Return True if line looks like a top-level benchmark YAML list item."""
    return bool(re.match(r"^\s*-\s+canonical_name:", line))


def _detect_bench_indent(first_entry_line: str) -> int:
    """Return the indentation of the '-' marker for benchmark entries."""
    m = re.match(r"^(\s*)-\s", first_entry_line)
    return len(m.group(1)) if m else 0


def _peek_list_indent(lines: list[str], start_idx: int) -> int:
    """Look ahead from start_idx to find the indentation of the first nested '- ' item."""
    j = start_idx
    while j < len(lines):
        stripped = lines[j].lstrip()
        if stripped.startswith("- ") and ":" in stripped:
            return len(lines[j]) - len(lines[j].lstrip())
        if stripped and not stripped.startswith("- "):
            return len(lines[j]) - len(lines[j].lstrip())
        j += 1
    return -1


def _peek_subfield_indent(lines: list[str], start_idx: int, list_indent: int) -> int:
    """Look ahead to find the indentation of sub-fields within a list item."""
    j = start_idx
    saw_list_item = False
    while j < len(lines):
        line_indent = len(lines[j]) - len(lines[j].lstrip())
        stripped = lines[j].lstrip()
        if stripped.startswith("- ") and ":" in stripped:
            saw_list_item = True
            j += 1
            continue
        if saw_list_item and stripped and ":" in stripped and not stripped.startswith("- "):
            if line_indent > list_indent:
                return line_indent
            break
        if stripped and not stripped.startswith("- "):
            break
        j += 1
    return list_indent + 2


def parse_registry_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"last_updated": "", "benchmarks": []}

    lines = path.read_text(encoding="utf-8").splitlines()
    data: dict[str, Any] = {"last_updated": "", "benchmarks": []}
    i = 0

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("last_updated:"):
            data["last_updated"] = parse_scalar(line.split(":", 1)[1])
            i += 1
            continue
        if line.startswith("benchmarks:"):
            i += 1
            bench_indent = -1  # detected from first entry
            while i < len(lines):
                line = lines[i]
                if not line.strip():
                    i += 1
                    continue
                if bench_indent == -1 and _is_benchmark_entry(line):
                    bench_indent = _detect_bench_indent(line)
                if bench_indent == -1:
                    break
                if not _is_benchmark_entry(line):
                    break

                bench: dict[str, Any] = {}
                bench["canonical_name"] = parse_scalar(line.split(":", 1)[1])
                field_indent = bench_indent + 2
                i += 1
                while i < len(lines):
                    line = lines[i]
                    if not line.strip():
                        i += 1
                        continue
                    if _is_benchmark_entry(line):
                        break
                    line_indent = len(line) - len(line.lstrip())
                    if line_indent < field_indent:
                        break

                    stripped = line.strip()
                    if stripped.startswith("aliases:"):
                        value = stripped.split(":", 1)[1].strip()
                        if value == "[]":
                            bench["aliases"] = []
                            i += 1
                        else:
                            items = []
                            i += 1
                            list_indent = _peek_list_indent(lines, i)
                            while i < len(lines) and lines[i].startswith(" " * list_indent + "- "):
                                items.append(parse_scalar(lines[i].split("-", 1)[1]))
                                i += 1
                            bench["aliases"] = items
                        continue

                    if stripped.startswith("task_families:"):
                        items = []
                        i += 1
                        list_indent = _peek_list_indent(lines, i)
                        while i < len(lines) and lines[i].startswith(" " * list_indent + "- "):
                            items.append(parse_scalar(lines[i].split("-", 1)[1]))
                            i += 1
                        bench["task_families"] = items
                        continue

                    if stripped.startswith("source_papers:"):
                        papers = []
                        i += 1
                        list_indent = _peek_list_indent(lines, i)
                        subfield_indent = _peek_subfield_indent(lines, i, list_indent)
                        while i < len(lines) and lines[i].startswith(" " * list_indent + "- "):
                            paper: dict[str, Any] = {}
                            first_field = lines[i].strip()
                            if first_field.startswith("- "):
                                first_field = first_field[2:]
                            key, raw = first_field.split(":", 1)
                            paper[key.strip()] = parse_scalar(raw)
                            i += 1
                            while i < len(lines) and len(lines[i]) - len(lines[i].lstrip()) >= subfield_indent and lines[i].strip() and not lines[i].strip().startswith("- "):
                                sub = lines[i].strip()
                                if ":" in sub:
                                    sub_key, sub_raw = sub.split(":", 1)
                                    paper[sub_key.strip()] = parse_scalar(sub_raw)
                                i += 1
                            papers.append(paper)
                        bench["source_papers"] = papers
                        continue

                    if ":" in stripped:
                        key, raw = stripped.split(":", 1)
                        bench[key.strip()] = parse_scalar(raw)
                    i += 1
                data["benchmarks"].append(bench)
            continue
        i += 1

    return data


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def dump_registry_yaml(data: dict[str, Any]) -> str:
    lines = [f'last_updated: {yaml_quote(str(data.get("last_updated", "")))}', "benchmarks:"]
    for bench in data.get("benchmarks", []):
        lines.append(f'  - canonical_name: {yaml_quote(str(bench.get("canonical_name", "")))}')

        aliases = bench.get("aliases") or []
        if aliases:
            lines.append("    aliases:")
            for alias in aliases:
                lines.append(f"      - {yaml_quote(str(alias))}")
        else:
            lines.append("    aliases: []")

        lines.append(f'    benchmark_type: {yaml_quote(str(bench.get("benchmark_type", "")))}')
        lines.append(f'    source_system: {yaml_quote(str(bench.get("source_system", "")))}')

        task_families = bench.get("task_families") or []
        if task_families:
            lines.append("    task_families:")
            for item in task_families:
                lines.append(f"      - {yaml_quote(str(item))}")
        else:
            lines.append("    task_families: []")

        lines.append("    source_papers:")
        for paper in bench.get("source_papers", []):
            lines.append(f'      - title: {yaml_quote(str(paper.get("title", "")))}')
            year = paper.get("year")
            if isinstance(year, int):
                lines.append(f"        year: {year}")
            else:
                lines.append(f'        year: {yaml_quote(str(year or ""))}')
            lines.append(f'        url: {yaml_quote(str(paper.get("url", "")))}')
            lines.append(
                f'        role_in_paper: {yaml_quote(str(paper.get("role_in_paper", "")))}'
            )

        lines.append(f'    notes: {yaml_quote(str(bench.get("notes", "")))}')
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def merge_unique_strings(existing: list[str], new_items: list[str]) -> list[str]:
    values = list(existing)
    existing_lower = {item.lower(): item for item in existing}
    for item in new_items:
        key = item.lower()
        if key not in existing_lower:
            values.append(item)
            existing_lower[key] = item
    return values


def paper_identity(paper: dict[str, Any]) -> tuple[str, str]:
    return (str(paper.get("title", "")).strip().lower(), str(paper.get("url", "")).strip().lower())


def upsert_registry_entry(registry: dict[str, Any], new_entry: dict[str, Any]) -> None:
    target_name = new_entry["canonical_name"].strip().lower()
    for existing in registry.get("benchmarks", []):
        aliases = [str(alias).strip().lower() for alias in existing.get("aliases", [])]
        if existing.get("canonical_name", "").strip().lower() == target_name or target_name in aliases:
            existing["aliases"] = merge_unique_strings(existing.get("aliases", []), new_entry.get("aliases", []))
            if not existing.get("benchmark_type"):
                existing["benchmark_type"] = new_entry.get("benchmark_type", "")
            if not existing.get("source_system"):
                existing["source_system"] = new_entry.get("source_system", "")
            existing["task_families"] = merge_unique_strings(
                existing.get("task_families", []), new_entry.get("task_families", [])
            )

            existing_papers = existing.get("source_papers", [])
            existing_keys = {paper_identity(paper) for paper in existing_papers}
            for paper in new_entry.get("source_papers", []):
                if paper_identity(paper) not in existing_keys:
                    existing_papers.append(paper)
                    existing_keys.add(paper_identity(paper))
            existing["source_papers"] = existing_papers

            if not existing.get("notes") and new_entry.get("notes"):
                existing["notes"] = new_entry["notes"]
            return

    registry.setdefault("benchmarks", []).append(new_entry)


def command_sync_registry(args: argparse.Namespace) -> int:
    summary_path = Path(args.summary).resolve()
    if not summary_path.exists():
        raise SystemExit(f"summary file not found: {summary_path}")

    registry = parse_registry_yaml(REGISTRY_PATH)
    _, entries = build_registry_entries_from_summary(summary_path)
    if not entries:
        raise SystemExit("no benchmark headings found in summary; registry not updated")

    for entry in entries:
        upsert_registry_entry(registry, entry)

    registry["last_updated"] = dt.date.today().isoformat()
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(dump_registry_yaml(registry), encoding="utf-8")

    print(f"UPDATED_REGISTRY={REGISTRY_PATH}")
    print(f"SYNCED_BENCHMARKS={len(entries)}")
    for entry in entries:
        print(f"BENCHMARK={entry['canonical_name']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Semi-automatic EHR benchmark survey pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    bootstrap = subparsers.add_parser(
        "bootstrap",
        help="Download/cache a paper and create a standard summary skeleton",
    )
    bootstrap.add_argument("url", help="Paper URL, arXiv URL, or direct PDF URL")
    bootstrap.add_argument("--title", help="Override detected paper title")
    bootstrap.add_argument("--year", type=int, help="Override detected paper year")
    bootstrap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing summary and cached text",
    )
    bootstrap.set_defaults(func=command_bootstrap)

    sync = subparsers.add_parser(
        "sync-registry",
        help="Sync benchmark names from a completed summary into the registry",
    )
    sync.add_argument("summary", help="Path to a completed benchmark summary markdown file")
    sync.set_defaults(func=command_sync_registry)

    audit_examples = subparsers.add_parser(
        "audit-examples",
        help="Audit example-search coverage for one summary or all collected summaries",
    )
    audit_examples.add_argument(
        "summary",
        nargs="?",
        help="Optional path to one completed benchmark summary markdown file",
    )
    audit_examples.add_argument(
        "--output",
        help="Optional path for the markdown audit report",
    )
    audit_examples.set_defaults(func=command_audit_examples)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
