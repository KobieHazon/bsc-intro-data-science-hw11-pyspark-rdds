# BSc Intro Data Science - HW11 PySpark RDDs

- Course: BSc Computer Science.

## Contents

Big-data computing coursework using PySpark RDD transformations and answer extraction.

## Files

Template or reference material:

- `assignment/HW11-SOL.ipynb`

My solution notebooks:

- `solutions/HW11.ipynb`

My submitted answers:

- `results/hw11_answers.csv`

## Tech Stack

- Python notebooks.
- Main Python packages: pandas, pyspark, notebook.
- Jupyter-compatible local review flow.

## Notes

- Full rerun requires a local Spark-compatible Python environment.

## Validate

```bash
python3 scripts/check_notebooks.py
```

This check verifies that notebooks parse as JSON and that the removed student identifier does not remain in tracked text files.

With Spark available, run the numeric median regression cases with:

```bash
make test
```
