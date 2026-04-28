# MedDialog

- **Source**: HuggingFace `petkopetkov/MedDialog`
- **Config**: default
- **Split**: train
- **Examples collected**: 200

## Field Schema

```json
{
  "description": "str",
  "utterances": "list"
}
```

## Sample Examples

### Example 1

```json
{
  "description": "throat a bit sore and want to get a good imune booster, especially in light of the virus. please advise. have not been in contact with nyone with the virus.",
  "utterances": [
    "patient: throat a bit sore and want to get a good imune booster, especially in light of the virus. please advise. have not been in contact with nyone with the virus.",
    "doctor: during this pandemic. throat pain can be from a strep throat infection (antibiotics needed), a cold or influenza or other virus, or from some other cause such as allergies or irritants. usually, a person sees the doctor (call first) if the sore throat is bothersome, recurrent, or doesn't go away quickly. covid-19 infections tend to have cough, whereas strep throat usually lacks cough but has more throat pain. (3/21/20)"
  ]
}
```

### Example 2

```json
{
  "description": "hey there i have had cold \"symptoms\" for over a week and had a low grade fever last week. for the past two days i have been feeling dizzy. should i contact my dr? should i see a dr",
  "utterances": [
    "patient: hey there i have had cold \"symptoms\" for over a week and had a low grade fever last week. for the past two days i have been feeling dizzy. should i contact my dr? should i see a dr",
    "doctor: yes. protection. it is not enough symptoms to say that you are a suspect case of covid19; but, independently of this, if you have been in contact with a case, or you present persistent cough (with or without sputum), shortness of breath, wheezing, or you have a chronic disease like diabetes, hypertension, low immune system or cancer, should ask for medical attention. and use all the protection measures."
  ]
}
```

### Example 3

```json
{
  "description": "i have a tight and painful chest with a dry cough, no fever and no headaches. could it possibly be coronavirus?",
  "utterances": [
    "patient: i have a tight and painful chest with a dry cough, no fever and no headaches. could it possibly be coronavirus?",
    "doctor: possible. top symptoms include fever, dry cough and sob. an obvious possibility. if so, your best step is to self-quarntine. remember at your age low risk of complication and typically will pass without issue. if worsening sob be seen. call your provider or check with local health department. these are healthtap guidelines:https://www.healthtap.com/blog/covid-19-care-guidelines/self-quarantine-guide."
  ]
}
```

### Example 4

```json
{
  "description": "what will happen after the incubation period for covid 19?",
  "utterances": [
    "patient: what will happen after the incubation period for covid 19?",
    "doctor: in brief: symptoms if you are infected, symptoms will emerge: tiredness, dry cough, fever worsening over 5-14 days. you will also become more infective so self-isolation and good hygiene are vital.only be concerned about covid-19 if: - you have been in contact with someone with a conformed diagnosis of covid-19 - you have visited a high risk area - symptoms worsen and include persistent fever and dry cough would you like to video or text chat with me?"
  ]
}
```

### Example 5

```json
{
  "description": "suggest treatment for pneumonia",
  "utterances": [
    "patient: just found out i was pregnant. yesterday diagnosed with pneumonia. i am a high risk pregnancy. fertility issues, pcos, weak cervix. delivered first daughter at 29 weeks, miscarried, and gave birth at 38 weeks to second daughter, but was on bedrest for weak cervix beginning at 5 months. i m a wreck. when i miscarried they said my progesterone level is low which caused me to miscarry, and gave me progesterone shots every week. can t see doctor for two days.",
    "doctor: thanks for your question on healthcare magic.i can understand your concern. pneumonia with pregnancy is always critical.antibiotics as early as possible is the treatment of choice for pneumonia. so better to immediately consult doctor and start antibiotics for pneumonia. drink plenty of fluids orally and keep yourself hydrated. with prompt and appropriate treatment, pneumonia can be cured easily. hope i have solved your query. i will be happy to help you further. wish you good health. thanks."
  ]
}
```

## Data Files

- `raw/examples.json` — 200 records

## Reference

Zeng, G., et al. "MedDialog: A Large-scale Medical Dialogue Dataset." Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2020.

Chen, S., et al. "MedDialog: Two Large-scale Medical Dialogue Datasets." arXiv:2004.03329, 2020.
