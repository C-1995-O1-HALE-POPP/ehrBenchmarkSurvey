# MedQA (USMLE)

- **Source**: HuggingFace `GBaker/MedQA-USMLE-4-options-hf`
- **Config**: train split
- **Total questions**: 10,178
- **Examples collected**: 25

## Data Format

Each question has a clinical vignette (`sent1`), four answer choices (`ending0`–`ending3`), and a `label` (0–3) indicating the correct answer.

## Data Files

- `raw/examples.json` — 25 records
- `raw/train_raw.json` — 10,178 records (not in repo)

## Sample Questions

### Question 1

> An 8-year-old African-American boy is brought to the emergency room with severe pain in both hands. His mother says that the patient had a fever with a cough a couple of days ago. Family history is positive for an uncle who died from a blood disease. A peripheral blood smear of this patient is shown in the image. Which of the following is the most likely mechanism for this patient’s disease?

- **A.** Frameshift mutation
- **B.** Mismatch repair
- **C.** Silent mutation
- **D.** Missense mutation **✓**

### Question 2

> An 11-year-old boy is brought to the emergency department by his parents with a 2-day history of fever, malaise, and productive cough. On presentation, he is found to be very weak and is having difficulty breathing. His past medical history is significant for multiple prior infections requiring hospitalization including otitis media, upper respiratory infections, pneumonia, and sinusitis. His family history is also significant for a maternal uncle who died of an infection as a child. Lab findings include decreased levels of IgG, IgM, IgA, and plasma cells with normal levels of CD4 positive cells. The protein that is most likely defective in this patient has which of the following functions?

- **A.** Actin polymerization
- **B.** Autoimmune regulation
- **C.** Lysosomal trafficking
- **D.** Protein phosphorylation **✓**

### Question 3

> A 37-year-old woman presents for prenatal counseling at 18 weeks gestation. The patient tells you that her sister recently had a child with Down's syndrome, and the patient would like prenatal screening for Down's in her current pregnancy.

Which of the following prenatal screening tests and results would raise concern for Down's syndrome?

- **A.** Increased AFP, normal HCG, normal unconjugated estriol
- **B.** Decreased AFP, increased HCG, decreased unconjugated estriol **✓**
- **C.** Normal AFP, increased HCG, decreased unconjugated estriol
- **D.** Normal AFP, decreased HCG, decreased unconjugated estriol

### Question 4

> A 59-year-old man comes to the physician for evaluation of a progressively enlarging, 8-mm skin lesion on the right shoulder that developed 1 month ago. The patient has a light-skinned complexion and has had several dysplastic nevi removed in the past. A photograph of the lesion is shown. The lesion is most likely derived from cells that are also the embryological origin of which of the following tumors?

- **A.** Neuroblastoma **✓**
- **B.** Medullary thyroid cancer
- **C.** Adrenal adenoma
- **D.** Basal cell carcinoma

### Question 5

> A 73-year-old man presents to the office, complaining of “weird blisters” on his right hand, which appeared 2 weeks ago. The patient says that he initially had a rash, which progressed to blisters. He denies any trauma or known contact with sick people. He is worried because he hasn’t been able to garden since the rash appeared, and he was planning on entering his roses into an annual competition this month. His vital signs are stable. On physical exam, the patient has multiple bullae accompanied by red, papular lesions on his right hand, which progress to his forearm. The right axillary lymph nodes are swollen and tender. What is the treatment for the most likely diagnosis of this patient?

- **A.** Potassium iodide solution
- **B.** Azithromycin
- **C.** Doxycycline
- **D.** Itraconazole **✓**

### Question 6

> A 27-year-old man presents to the clinic for his annual health check-up. He currently complains of fatigue for the past few months. He has no significant past medical history. He admits to being sexually active with men and also is an intravenous drug user. He has never received a hepatitis B vaccine. His blood pressure is 122/98 mm Hg, the respiratory rate is 16/min, the pulse is 68/min, and the temperature is 37.0°C (98.6°F). On physical examination, he appears fatigued and unkempt. His tongue and buccal mucosa appear moist and without ulcerations or lesions. There are no murmurs or gallops on cardiac auscultation. His lungs are clear bilaterally. No lesions are present on the surface of the skin nor skin discoloration. The physician proceeds to order a hepatitis B panel to assess the patient’s serologic status:
HBV DNA positive
HBsAg negative
HBeAg  negative
HBsAb negative
HBcAb positive
HBeAb negative
Which of the following disease states is the patient exhibiting?

- **A.** Acute infection
- **B.** Chronic infection
- **C.** Immune from vaccine
- **D.** Convalescent (window) period **✓**

### Question 7

> A 57-year-old man presents to the clinic for a chronic cough over the past 4 months. The patient reports a productive yellow/green cough that is worse at night. He denies any significant precipitating event prior to his symptoms. He denies fever, chest pain, palpitations, weight changes, or abdominal pain, but endorses some difficulty breathing that waxes and wanes. He denies alcohol usage but endorses a 35 pack-year smoking history. A physical examination demonstrates mild wheezes, bibasilar crackles, and mild clubbing of his fingertips. A pulmonary function test is subsequently ordered, and partial results are shown below:

Tidal volume: 500 mL
Residual volume: 1700 mL
Expiratory reserve volume: 1500 mL
Inspiratory reserve volume: 3000 mL

What is the functional residual capacity of this patient?

- **A.** 2000 mL
- **B.** 3200 mL **✓**
- **C.** 3500 mL
- **D.** 4500 mL

### Question 8

> A 33-year-old man presents to the emergency department complaining of weakness and fatigue. He states that his symptoms have worsened over the past day. He has a past medical history of IV drug abuse and alcoholism and he currently smells of alcohol. His temperature is 102°F (38.9°C), blood pressure is 111/68 mmHg, pulse is 110/min, respirations are 17/min, and oxygen saturation is 98% on room air. Physical exam is notable for focal tenderness over the lumbar spine. Initial lab values and blood cultures are drawn and are notable for leukocytosis and an elevated C-reactive protein (CRP). Which of the following is the best treatment for this patient?

- **A.** Ceftriaxone
- **B.** Ibuprofen and warm compresses
- **C.** Piperacillin-tazobactam
- **D.** Vancomycin **✓**

---

*8 of 25 examples shown. Full set in `raw/examples.json`.*

## Reference

Jin, D., et al. "What Disease Does This Patient Have? A Large-Scale Open Domain Question Answering Dataset from Medical Exams." *Applied Sciences*, 2021.
