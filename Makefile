.PHONY: test check

test check:
	docker build -f docker/Dockerfile -t data-science-spark-tests .
	docker run --rm --network none --hostname localhost -e SPARK_LOCAL_IP=127.0.0.1 -v "$(CURDIR):/project:ro" -w /project data-science-spark-tests /opt/spark/bin/spark-submit --master 'local[2]' scripts/run_notebook.py
