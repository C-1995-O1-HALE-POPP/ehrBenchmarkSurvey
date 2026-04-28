# MedMCQA

- **Source**: HuggingFace `openlifescienceai/medmcqa`
- **Config**: default
- **Split**: train
- **Examples collected**: 300

## Field Schema

```json
{
  "id": "str",
  "question": "str",
  "opa": "str",
  "opb": "str",
  "opc": "str",
  "opd": "str",
  "cop": "int",
  "choice_type": "str",
  "exp": "str",
  "subject_name": "str",
  "topic_name": "str"
}
```

## Sample Examples

### Example 1

```json
{
  "id": "e9ad821a-c438-4965-9f77-760819dfa155",
  "question": "Chronic urethral obstruction due to benign prismatic hyperplasia can lead to the following change in kidney parenchyma",
  "opa": "Hyperplasia",
  "opb": "Hyperophy",
  "opc": "Atrophy",
  "opd": "Dyplasia",
  "cop": 2,
  "choice_type": "single",
  "exp": "Chronic urethral obstruction because of urinary calculi, prostatic hyperophy, tumors, normal pregnancy, tumors, uterine prolapse or functional disorders cause hydronephrosis which by definition is used to describe dilatation of renal pelvis and calculus associated with progressive atrophy of the kidney due to obstruction to the outflow of urine Refer Robbins 7yh/9,1012,9/e. P950",
  "subject_name": "Anatomy",
  "topic_name": "Urinary tract"
}
```

### Example 2

```json
{
  "id": "e3d3c4e1-4fb2-45e7-9f88-247cc8f373b3",
  "question": "Which vitamin is supplied from only animal source:",
  "opa": "Vitamin C",
  "opb": "Vitamin B7",
  "opc": "Vitamin B12",
  "opd": "Vitamin D",
  "cop": 2,
  "choice_type": "single",
  "exp": "Ans. (c) Vitamin B12 Ref: Harrison's 19th ed. P 640* Vitamin B12 (Cobalamin) is synthesized solely by microorganisms.* In humans, the only source for humans is food of animal origin, e.g., meat, fish, and dairy products.* Vegetables, fruits, and other foods of nonanimal origin doesn't contain Vitamin B12 .* Daily requirements of vitamin Bp is about 1-3 pg. Body stores are of the order of 2-3 mg, sufficient for 3-4 years if supplies are completely cut off.",
  "subject_name": "Biochemistry",
  "topic_name": "Vitamins and Minerals"
}
```

### Example 3

```json
{
  "id": "5c38bea6-787a-44a9-b2df-88f4218ab914",
  "question": "All of the following are surgical options for morbid obesity except -",
  "opa": "Adjustable gastric banding",
  "opb": "Biliopancreatic diversion",
  "opc": "Duodenal Switch",
  "opd": "Roux en Y Duodenal By pass",
  "cop": 3,
  "choice_type": "multi",
  "exp": "Ans. is 'd' i.e., Roux en Y Duodenal Bypass Bariatric surgical procedures include:a. Vertical banded gastroplastyb. Adjustable gastric bandingc. Roux-en Y gastric bypass (Not - Roux-en Y Duodenal Bypass)d. Biliopancreatic diversione. Duodenal switcho The surgical treatment of morbid obesity is known as bariatric surgery.o Morbid obesity is defined as body mass index of 35 kg/m2 or more with obesity related comorbidity, or BMI of 40 kg/m2 or greater without comorbidity.o Bariatric operations prod...",
  "subject_name": "Surgery",
  "topic_name": "Surgical Treatment Obesity"
}
```

### Example 4

```json
{
  "id": "cdeedb04-fbe9-432c-937c-d53ac24475de",
  "question": "Following endaerectomy on the right common carotid, a patient is found to be blind in the right eye. It is appears that a small thrombus embolized during surgery and lodged in the aery supplying the optic nerve. Which aery would be blocked?",
  "opa": "Central aery of the retina",
  "opb": "Infraorbital aery",
  "opc": "Lacrimal aery",
  "opd": "Nasociliary aretry",
  "cop": 0,
  "choice_type": "multi",
  "exp": "The central aery of the retina is a branch of the ophthalmic aery. It is the sole blood supply to the retina; it has no significant collateral circulation and blockage of this vessel leads to blindness. The branches of this aery are what you view during a fundoscopic exam. Note: The infraorbital aery is a branch of the maxillary aery. It comes through the infraorbital foramen, inferior to the eye. It supplies the maxillary sinus, the maxillary incisors, canine and premolar teeth, and the skin of...",
  "subject_name": "Ophthalmology",
  "topic_name": null
}
```

### Example 5

```json
{
  "id": "dc6794a3-b108-47c5-8b1b-3b4931577249",
  "question": "Growth hormone has its effect on growth through?",
  "opa": "Directly",
  "opb": "IG1-1",
  "opc": "Thyroxine",
  "opd": "Intranuclear receptors",
  "cop": 1,
  "choice_type": "single",
  "exp": "Ans. is 'b' i.e., IGI-1GH has two major functions :-i) Growth of skeletal system :- The growth is mediated by somatomedins (IGF). Increased deposition of cailage (including chondroitin sulfate) and bone with increased proliferation of chondrocytes and osteocytes.ii) Metabolic effects :- Most of the metabolic effects are due to direct action of GH. These include gluconeogenesis, decreased peripheral utilization of glucose (decreased uptake), lipolysis and anabolic effect on proteins.",
  "subject_name": "Physiology",
  "topic_name": null
}
```

## Data Files

- `raw/examples.json` — 300 records
