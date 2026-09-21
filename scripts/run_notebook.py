"""Execute the solution notebook and test its actual Spark RDD computations."""

from __future__ import annotations

import json
import math
import os
import statistics
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "solutions" / "HW11.ipynb"


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    completed = 0
    checked = 0
    original_cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="spark-homework-") as directory:
        try:
            os.chdir(directory)
            for index, cell in enumerate(notebook["cells"]):
                if cell["cell_type"] != "code":
                    continue
                source = "".join(cell["source"])
                if not source.strip():
                    continue
                print(f"Executing cell {index}", flush=True)
                exec(compile(source, f"{NOTEBOOK.name}:cell{index}", "exec"), namespace)
                completed += 1
                if "sc" in namespace:
                    namespace["sc"].setLogLevel("ERROR")

            sc = namespace["sc"]
            median_cases = [
                [9, 1, 5],
                [10, 2, 8, 4],
                [7],
                [3, 3, 9, 9],
                [-5, -1, 3, -2],
            ]
            for partitions in (1, 2):
                for values in median_cases:
                    actual = namespace["mystery"](sc.parallelize(values, partitions))
                    assert actual == statistics.median(values), (values, actual)
                    checked += 1
                for values in ([1, 2, 4], [3, 3, 3], [0.5, 1.5, 7.5]):
                    actual = namespace["a"](sc.parallelize(values, partitions))
                    assert math.isclose(
                        actual, statistics.harmonic_mean(values), rel_tol=1e-12
                    )
                    checked += 1
                for pairs in (
                    [(1, 1), (2, 2), (4, 1)],
                    [(3, 5), (3, 2)],
                    [(0.5, 3), (1.5, 1)],
                ):
                    expected = sum(weight for _, weight in pairs) / sum(
                        weight / value for value, weight in pairs
                    )
                    actual = namespace["b"](sc.parallelize(pairs, partitions))
                    assert math.isclose(actual, expected, rel_tol=1e-12), (
                        pairs,
                        actual,
                        expected,
                    )
                    checked += 1
            exported = next(Path(directory).glob("HW11_*.csv"))
            actual = namespace["pd"].read_csv(exported, index_col=0)
            assert actual.shape == (12, 1)
            assert actual.loc["Q10"].iloc[0] == "b"
            print(
                f"PASS: {completed} notebook code cells; {checked} numerical Spark cases; answer export"
            )
        finally:
            if "sc" in namespace:
                namespace["sc"].stop()
            os.chdir(original_cwd)


if __name__ == "__main__":
    main()
