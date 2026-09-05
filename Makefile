check:
	python3 scripts/check_notebooks.py

test:
	spark-submit --master 'local[2]' scripts/test_spark_notebook.py
