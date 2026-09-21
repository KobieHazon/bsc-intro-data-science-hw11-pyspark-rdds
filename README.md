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

## Run

With Docker running:

```sh
make test
```

This runs every solution code cell in Spark 3.5.7, then executes 22 numerical cases for median, harmonic mean, and weighted harmonic mean across one- and two-partition RDDs. It also exercises answer export in a temporary directory without overwriting the submitted CSV. The test container has no external network access; building the image requires access to download dependencies.

Alternatively, with Spark 3.5.7, NumPy 1.24.4 and pandas 2.0.3 installed locally:

```sh
spark-submit --master 'local[2]' scripts/run_notebook.py
```
