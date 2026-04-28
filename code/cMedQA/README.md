# cMedQA

- **Source**: HuggingFace `wangrongsheng/cMedQA-V2.0`
- **Config**: default
- **Split**: train
- **Examples collected**: 200

## Field Schema

```json
{
  "input": "str",
  "output": "str",
  "instruction": "str"
}
```

## Sample Examples

### Example 1

```json
{
  "input": "",
  "output": "你的症状好像还是感冒症状，可能出现发热，病毒合并细菌感染，可以去医院输液治疗或者口服抗病毒药物、抗生素，如果发热可以口服退热药物布洛芬治疗。",
  "instruction": "头痛恶心肌肉痛关节痛颈部淋巴结疼痛怎么回事啊"
}
```

### Example 2

```json
{
  "input": "",
  "output": "考虑是腹泻现象，容易诱发子宫收缩出现早产症状，可以在医生的指导下服用黄连素，思密达等治疗，同时注意多喝水，饮食要清淡，禁食生冷刺激食物。",
  "instruction": "我怀孕37周，肠子一直呼噜呼噜叫感觉像是在里面灌水，上厕所拉稀和喷水一样，一天上厕所5次，对孩子有啥影响，应该怎么办？"
}
```

### Example 3

```json
{
  "input": "",
  "output": "建议彩超检查右下肢动静脉情况，了解有无血管病变（如深静脉血栓及血管硬化堵塞等）",
  "instruction": "男，67岁，2天前突然出现右小腿（类似抽筋症状），现出现右小腿消肿，有指压痕，无，请问可能是什么疾病，该如何诊治"
}
```

### Example 4

```json
{
  "input": "",
  "output": "盆腔炎有急性与慢性之分。急性盆腔炎者发病急，病情较重，患者皆有不同程度的发冷、发烧和小腹痛。有时泌尿道也可出现受激惹或压迫症状，如尿痛、尿频、排尿困难等症。慢性盆腔炎常为急性盆腔炎未能彻底治疗，慢性盆腔炎病情常较顽固，多形成输卵管、卵巢粘连包块，且。与周围粘连，抗炎药物不易进入，因而，不容易彻底治愈。",
  "instruction": "怀孕前两个月照了CT和X光，来两次月经后怀孕了，怀孕期间有轻微盆腔积水吃了两瓶杏香兔耳片。请问这对孩子影响有多大"
}
```

### Example 5

```json
{
  "input": "",
  "output": "一般阴囊的潮湿可能和前列腺疾病肾虚是有一定的关系的，建议你还是积极做前列腺的检查确定具体的病情，注意对症治疗。因为肾虚造成的。可以服食桂附地黄丸调理。",
  "instruction": "阴囊湿冷阳痿早泻请问用点什么药"
}
```

## Data Files

- `raw/examples.json` — 200 records

## Reference

Zhang, S., et al. "On the Generation of Medical Question-Answer Pairs." AAAI Conference on Artificial Intelligence, 2018.
