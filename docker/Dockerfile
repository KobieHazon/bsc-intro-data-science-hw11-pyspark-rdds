FROM spark:3.5.7-python3
USER root
COPY --from=ghcr.io/astral-sh/uv:0.8.22 /uv /usr/local/bin/uv
RUN uv pip install --system "numpy==1.24.4" "pandas==2.0.3"
USER 185
