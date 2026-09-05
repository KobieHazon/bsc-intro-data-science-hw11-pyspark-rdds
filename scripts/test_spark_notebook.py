#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "solutions" / "HW11.ipynb"


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    matching_cells = [
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
        and "def mystery(rdd):" in "".join(cell["source"])
    ]
    if len(matching_cells) != 1:
        raise SystemExit(f"expected one mystery cell, found {len(matching_cells)}")

    namespace: dict[str, object] = {}
    exec(compile(matching_cells[0], str(NOTEBOOK), "exec"), namespace)
    spark_context = namespace["sc"]
    mystery = namespace["mystery"]

    try:
        cases = [
            ([9, 1, 5], 5),
            ([10, 2, 8, 4], 6),
            ([7], 7),
            ([3, 3, 9, 9], 6),
        ]
        for values, expected in cases:
            actual = mystery(spark_context.parallelize(values, 2))
            if actual != expected:
                raise SystemExit(
                    f"median failed for {values}: expected {expected}, got {actual}"
                )
        print(f"validated {len(cases)} numeric Spark median case(s)")
    finally:
        spark_context.stop()


if __name__ == "__main__":
    main()
