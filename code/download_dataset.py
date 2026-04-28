#!/usr/bin/env python3
import json, os, sys, subprocess, argparse, io
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROXY = "socks5://127.0.0.1:20170"


def curl_json(url, timeout=30):
    result = subprocess.run(
        ["curl", "-x", PROXY, "-s", "--max-time", str(timeout), url],
        capture_output=True, text=True, timeout=timeout + 5,
    )
    if result.returncode == 0 and result.stdout.strip():
        return json.loads(result.stdout)
    return None


def fetch_rows(dataset_id, config, split, limit=500):
    all_rows = []
    offset = 0
    while offset < limit:
        url = (
            f"https://datasets-server.huggingface.co/rows?"
            f"dataset={dataset_id}&config={config}&split={split}"
            f"&offset={offset}&length=100"
        )
        data = curl_json(url)
        if not data:
            break
        for r in data.get("rows", []):
            all_rows.append(r["row"])
        if len(data.get("rows", [])) < 100:
            break
        offset += 100
    return all_rows


def save_json(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)


def write_readme(out_dir, benchmark_name, dataset_id, config, split, rows):
    readme = out_dir / "README.md"
    with open(readme, "w") as f:
        f.write(f"# {benchmark_name}\n\n")
        f.write(f"- **Source**: HuggingFace `{dataset_id}`\n")
        f.write(f"- **Config**: {config}\n")
        f.write(f"- **Split**: {split}\n")
        f.write(f"- **Examples collected**: {len(rows)}\n\n")
        if rows:
            fields = {k: type(v).__name__ for k, v in rows[0].items()}
            f.write("## Field Schema\n\n```json\n")
            f.write(json.dumps(fields, indent=2))
            f.write("\n```\n\n")
            f.write("## Sample Examples\n\n")
            for i in range(min(5, len(rows))):
                f.write(f"### Example {i+1}\n\n```json\n")
                ex = rows[i]
                simplified = {}
                for k, v in ex.items():
                    if isinstance(v, str) and len(v) > 500:
                        simplified[k] = v[:500] + "..."
                    elif isinstance(v, list) and len(v) > 3:
                        simplified[k] = v[:3]
                    else:
                        simplified[k] = v
                f.write(json.dumps(simplified, indent=2, ensure_ascii=False))
                f.write("\n```\n\n")
        f.write("## Data Files\n\n")
        f.write(f"- `raw/examples.json` — {len(rows)} records\n")
    print(f"  README: {readme}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_name")
    parser.add_argument("hf_dataset_id")
    parser.add_argument("--config", default="default")
    parser.add_argument("--split", default="train")
    parser.add_argument("--max-rows", type=int, default=500)
    args = parser.parse_args()

    out = ROOT / "code" / args.benchmark_name
    out.mkdir(parents=True, exist_ok=True)
    raw_dir = out / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    print(f"[{args.benchmark_name}] {args.hf_dataset_id} "
          f"config={args.config} split={args.split}")

    rows = fetch_rows(args.hf_dataset_id, args.config, args.split, args.max_rows)
    if not rows and args.config != "default":
        rows = fetch_rows(args.hf_dataset_id, "default", args.split, args.max_rows)

    if rows:
        save_json(rows, raw_dir / "examples.json")
        print(f"  Saved {len(rows)} examples")
    else:
        print(f"  WARNING: No data retrieved")

    write_readme(out, args.benchmark_name, args.hf_dataset_id,
                 args.config, args.split, rows)
    status = "OK" if rows else "FAIL"
    print(f"[{args.benchmark_name}] {status}: {len(rows)} examples")


if __name__ == "__main__":
    main()
