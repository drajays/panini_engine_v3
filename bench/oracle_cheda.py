"""
bench/oracle_cheda.py — Vidyut's Chedaka segmentation of sandhi-joined words, JSON in / JSON out.

    echo '["evABirakzati"]' | .venv/bin/python -m bench.oracle_cheda     # → [["eva", "aBirakzati"]]

Chedaka is statistical: a segmentation is a *proposal* (CONSTITUTION Art. 17). ``core/analyze``
accepts it only when every part is engine-derived and ``pipelines/pada_samhita`` re-joins the parts
into the written word. Data: ``$PANINI_VIDYUT_DATA`` or ``.venv/vidyut-data``. Never imported by the engine.
"""
from __future__ import annotations

import json
import sys

from bench.oracle_kosha import DATA


def main() -> int:
    from vidyut.cheda import Chedaka
    cheda = Chedaka(str(DATA))
    out = []
    for word in json.load(sys.stdin):
        try:
            out.append([t.text for t in cheda.run(word)])
        except Exception:                         # the oracle's own gaps
            out.append([])
    json.dump(out, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
