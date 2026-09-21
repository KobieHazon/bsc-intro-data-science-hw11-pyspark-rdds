# BSc Intro Data Science - HW11 PySpark RDDs

- Course: BSc Computer Science.
- Available copy: 2019.
- Supplied exercise material is identified separately below.

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

## Dataset Notes

The original course folders for several data-science assignments contained the large `ebay_boys_girls_shirts` image dataset and tarball. Those files are not tracked in this repository. The recovered notebooks reference the course download URL and recreate the dataset folder when that URL is still available.

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
