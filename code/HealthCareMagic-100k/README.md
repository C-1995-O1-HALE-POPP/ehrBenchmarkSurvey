# HealthCareMagic-100k

- **Source**: HuggingFace `wangrongsheng/HealthCareMagic-100k-en`
- **Config**: default
- **Split**: train
- **Examples collected**: 200

## Field Schema

```json
{
  "instruction": "str",
  "input": "str",
  "output": "str"
}
```

## Sample Examples

### Example 1

```json
{
  "instruction": "If you are a doctor, please answer the medical questions based on the patient's description.",
  "input": "I woke up this morning feeling the whole room is spinning when i was sitting down. I went to the bathroom walking unsteadily, as i tried to focus i feel nauseous. I try to vomit but it wont come out.. After taking panadol and sleep for few hours, i still feel the same.. By the way, if i lay down or sit down, my head do not spin, only when i want to move around then i feel the whole world is spinning.. And it is normal stomach discomfort at the same time? Earlier after i relieved myself, the spin...",
  "output": "Hi, Thank you for posting your query. The most likely cause for your symptoms is benign paroxysmal positional vertigo (BPPV), a type of peripheral vertigo. In this condition, the most common symptom is dizziness or giddiness, which is made worse with movements. Accompanying nausea and vomiting are common. The condition is due to problem in the ear, and improves in a few days on own. Betahistine tablets would help relieve your symptoms. Doing vestibular rehabilitation or adaptation exercises woul..."
}
```

### Example 2

```json
{
  "instruction": "If you are a doctor, please answer the medical questions based on the patient's description.",
  "input": "My baby has been pooing 5-6 times a day for a week. In the last few days it has increased to 7 and they are very watery with green stringy bits in them. He does not seem unwell i.e no temperature and still eating. He now has a very bad nappy rash from the pooing ...help!",
  "output": "Hi... Thank you for consulting in Chat Doctor. It seems your kid is having viral diarrhea. Once it starts it will take 5-7 days to completely get better. Unless the kids having low urine output or very dull or excessively sleepy or blood in motion or green bilious vomiting...you need not worry. There is no need to use antibiotics unless there is blood in the motion. Antibiotics might worsen if unnecessarily used causing antibiotic associated diarrhea. I suggest you use zinc supplements (Z&D Chat..."
}
```

### Example 3

```json
{
  "instruction": "If you are a doctor, please answer the medical questions based on the patient's description.",
  "input": "Hello, My husband is taking Oxycodone due to a broken leg/surgery. He has been taking this pain medication for one month. We are trying to conceive our second baby. Will this medication afect the fetus? Or the health of the baby? Or can it bring birth defects? Thank you.",
  "output": "Hello, and I hope I can help you today.First, there is no medication that can be taken by the father that has any way to get into your system or a baby if you conceive.  Medications can only affect a fetus if you take it while pregnant. The only issue is that certain medications may decrease a men sperm count and affect fertility, however pain medications like Oxycodone do not have this effect. So there is no reason for you to worry about conceiving while taking this medication.  The best way yo..."
}
```

### Example 4

```json
{
  "instruction": "If you are a doctor, please answer the medical questions based on the patient's description.",
  "input": "lump under left nipple and stomach pain (male) Hi,I have recently noticed a few weeks ago a lump under my nipple, it hurts to touch and is about the size of a quarter. Also I have bern experiencing stomach pains that prevent me from eating. I immediatly feel full and have extreme pain. Please help",
  "output": "HI. You have two different problems. The lump under the nipple should be removed, biopsied. This will help you to get rid of the disease, and you get a diagnosis. Second problem looks a bit serious one: Pain that prevents you from eating-immediate fullness, and extreme pain. I would advise such a patient to undergo the upper GI endoscopy asap. This can be an ulcer with a problem at the pylorus. The exact diagnosis is the most important to start the right therapy. Do not waste time in starting th..."
}
```

### Example 5

```json
{
  "instruction": "If you are a doctor, please answer the medical questions based on the patient's description.",
  "input": "I have a 5 month old baby who is very congested with a terrible cough. Its rattly/raspy and croupy sounding cough. She started choking on her coughs and the mucous that has come up. She also has a fever and runny nose. Should i take her to urgent care?",
  "output": "Thank you for using Chat Doctor. I would suggest that you see your doctor. Your baby maybe having bronchiolitis which is a lung infection common to your kids age. It is commonly caused by a virus. Albuterol via nebulization should be utilized in order to alleviate the wheezing and also help with the congestion. A decongestant can also be used for the colds. Also, it would also advise doing a chest X-ray in order to rule out other diseases (ex. pneumonia)sincerely, Mark RosarioGeneral pediatrics/..."
}
```

## Data Files

- `raw/examples.json` — 200 records

## Reference

Li, Y., et al. "ChatDoctor: A Medical Chat Model Fine-Tuned on LLaMA Using Medical Domain Knowledge." 2023.
