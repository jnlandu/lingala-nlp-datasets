# Lingala–French Proverbs

A collection of Lingala proverbs paired with their French translation and a plain-French explanation of their meaning. Useful for NLP research on Lingala, cultural/linguistic study, and as a small evaluation or few-shot prompting set distinct from literal sentence translation.

## Contents

| File | Description |
|---|---|
| `lin-fr-proverbs.tsv` | 500 Lingala proverbs with French translation and meaning, tab-separated |
| `code.py` | Script used to append new proverb entries to the TSV, deduplicating on the Lingala text |

## Format

UTF-8, tab-separated values (TSV) file with a header row:

```
prov lingala	French	signification
Mwana oyo aleli te, azwaka mabɛlɛ te.	L'enfant qui ne pleure pas ne reçoit pas le sein.	Si tu ne demandes rien, personne ne saura ce dont tu as besoin.
Loboko moko ekoki te kosukola elongi.	Une seule main ne peut pas bien laver le visage.	On a besoin des autres ; l'union fait la force.
```

| Column | Description |
|---|---|
| `prov lingala` | The proverb in Lingala |
| `French` | Literal/direct French translation of the proverb |
| `signification` | Plain-French explanation of the proverb's meaning/moral |

- 500 proverbs (501 lines including the header)
- No duplicate Lingala entries
- Proverbs are loosely grouped by theme (perseverance, family, wisdom, money, time, adaptability, etc.) in blocks of ten

## Usage

Load with pandas:

```python
import pandas as pd

df = pd.read_csv("lin-fr-proverbs.tsv", sep="\t")
```

Or with the Hugging Face `datasets` library:

```python
from datasets import load_dataset

ds = load_dataset("csv", data_files="lin-fr-proverbs.tsv", delimiter="\t")
```

## Updating the dataset

`code.py` loads the existing TSV, appends a hardcoded list of new `[lingala, french, signification]` rows, skips any whose Lingala text already exists in the file, and rewrites the TSV:

```bash
python3 code.py
```

To add more proverbs, extend the `new_rows` list in `code.py` and re-run it.

## Potential uses

- Few-shot prompts for LLM-based translation or cultural explanation tasks
- Evaluation set for idiomatic/non-literal translation (harder than literal sentence pairs)
- Bilingual educational material or flashcards
- Cultural NLP research (proverb interpretation, figurative language)

## Notes

- Entries are curated/compiled rather than sourced from an external corpus.
- Translation and interpretation quality has not been independently verified by native speakers.

## Citation

If you use this dataset, please cite:

```bibtex
@misc{mabiala2026linfrproverbs,
  author = {Mabiala, Jeremie},
  title  = {Lingala-French Proverbs: A Bilingual Proverb Dataset with Interpretations},
  year   = {2026},
  note   = {lin-fr-proverbs.tsv, 500 proverbs}
}
```

## License

This dataset is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

You are free to share and adapt this dataset for any purpose, even commercially, as long as you give appropriate credit (see [Citation](#citation)) and distribute any derivative works under the same license.
