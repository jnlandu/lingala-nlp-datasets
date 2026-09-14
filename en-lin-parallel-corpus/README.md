# Lingala Dataset

A parallel English–Lingala sentence pair dataset for machine translation, language learning, and NLP research on Lingala, a Bantu language spoken by tens of millions of people across the Democratic Republic of the Congo, the Republic of the Congo, and neighboring regions.

## Contents

| File | Description |
|---|---|
| `kit5k_en_lin.tsv` | 5,000 English–Lingala sentence pairs, tab-separated |

## Format

The file is a UTF-8, tab-separated values (TSV) file with a header row:

```
en	lin
Where were these photos taken?	Bakangaki bilili oyo wapi ?
Take one four times a day, after meals.	Kamataka yango moko mbala minei na mokolo, nsima ya koliya
```

| Column | Description |
|---|---|
| `en` | Source sentence in English |
| `lin` | Reference translation in Lingala |

- 5,070 sentence pairs (5,071 lines including the header)
- Every row has exactly two tab-separated fields; no missing translations
- 64 English source sentences appear more than once (e.g. common phrases translated in different contexts)
- Sentences range from short everyday phrases to longer, more literary sentences

## Usage

Load with pandas:

```python
import pandas as pd

df = pd.read_csv("kit5k_en_lin.tsv", sep="\t")
```

Or with the Hugging Face `datasets` library:

```python
from datasets import load_dataset

ds = load_dataset("csv", data_files="kit5k_en_lin.tsv", delimiter="\t")
```

## Potential uses

- Training or fine-tuning English↔Lingala machine translation models
- Evaluation/benchmark set for low-resource African language translation
- Building bilingual dictionaries or phrase tables
- Language learning applications and flashcard generation

## Notes

- No train/validation/test split is provided; split the data as needed for your use case.
- Translation quality has not been independently verified — review a sample before using for high-stakes applications.

## Data sources

Some of the Lingala translations in this dataset are derived from the upstream Gamayun dataset, distributed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The remaining sentence pairs were compiled/translated independently.

## Citation

If you use this dataset, please cite:

```bibtex
@misc{mabiala2026lingala,
  author = {Mabiala, Jeremie},
  title  = {Lingala Dataset: A Parallel English-Lingala Sentence Corpus},
  year   = {2026},
  note   = {kit5k\_en\_lin.tsv, 5,000 sentence pairs. Includes data from the Gamayun dataset (CC BY 4.0).}
}
```

Please also credit the upstream Gamayun dataset for the portion of translations sourced from it.

## License

This dataset is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

You are free to share and adapt this dataset for any purpose, even commercially, as long as you give appropriate credit (see [Citation](#citation)) and distribute any derivative works under the same license.

Portions of this dataset derive from the Gamayun dataset (CC BY 4.0); those portions remain subject to that license's attribution requirement.
