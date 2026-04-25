#!/usr/bin/env python3
"""
regenerate_sig_artifacts — refresh the whole ``sig/`` tree from the live engine.

Runs ``tools.sig_benchmark`` with the **full** corpus set:

  * all gold JSONs under ``data/reference/`` (``sig_benchmark`` auto-discovers
    subanta *cells*, ``recipe`` drivers, and the *jayati* *steps* file)
  * ``coverage.json`` (registry coverage)
  * ``sig_manifest.json`` (what was run, when, artifact list)

Use in CI, after pulls, and before release:

    python3 -m tools.regenerate_sig_artifacts

Options are forwarded to ``sig_benchmark`` (e.g. ``--freeze`` only when intentionally
updating ``tests/regression/sig_applied_paths_baseline.json``).
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


def main(argv: list[str] | None = None) -> int:
    from tools import sig_benchmark

    a = list(argv) if argv is not None else sys.argv[1:]
    if "--out" not in a and "-o" not in a:
        a = ["--out", str(_ROOT / "sig"), *a]
    return sig_benchmark.main(a)


if __name__ == "__main__":
    raise SystemExit(main())
