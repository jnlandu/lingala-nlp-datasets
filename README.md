# Lingala Dataset

A collection of datasets for Lingala NLP: parallel sentence translations, proverbs and speech, intended for machine translation, language learning, and NLP research on Lingala, a Bantu language spoken by tens of millions of people across the Democratic Republic of the Congo, the Republic of the Congo, and neighboring regions.

## Datasets

| Directory | Description | Size |
|---|---|---|
| [`en-lin-parallel-corpus/`](en-lin-parallel-corpus/) | Parallel English–Lingala sentence pairs | 5,000 pairs |
| [`lin-fr-proverbs/`](lin-fr-proverbs/) | Lingala proverbs with French translation and meaning | 500 proverbs |
| [`lingala-stt/`](lingala-stt/) | Catalogue of Lingala broadcast news audio (Radio Okapi) for ASR, with the scraper; not yet transcribed | 31 bulletins, 5.6 h |


Each directory has its own README with format details, usage examples, and licensing.

## Repository structure

```
.
├── en-lin-parallel-corpus/
│   ├── kit5k_en_lin.tsv    # 5,000 English–Lingala sentence pairs
│   └── README.md
├── lin-fr-proverbs/
│   ├── lin-fr-proverbs.tsv # 500 Lingala proverbs with French translation and meaning
│   ├── code.py             # appends new proverb entries to the TSV
│   └── README.md
└── lingala-stt/
    ├── manifest.jsonl      # 31 Radio Okapi Lingala bulletins (5.6 h), audio not included
    ├── scripts/download_okapi.py
    ├── requirements.txt
    └── README.md
```

## Potential uses

- Training or fine-tuning English/French↔Lingala machine translation models
- Evaluation/benchmark sets for low-resource African language translation, including idiomatic/figurative language
- Few-shot prompting or instruction-tuning data for LLMs
- Bilingual dictionaries, phrase tables, and language-learning material
- Cultural and linguistic NLP research
- Building speech recognition data for Lingala

## License

Each dataset is licensed individually — see the README in its directory. Unless stated otherwise, datasets in this repository are licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

## Citation

See the README in each dataset directory for the citation specific to that dataset.
