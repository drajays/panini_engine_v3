"""
bench/practice_key.py — which forms.db cells are safe to use as a practice answer key.
─────────────────────────────────────────────────────────────────────────────────────

A practice question that teaches a wrong form is worse than no question, so
``core/practice`` only asks cells where this engine's surface is among
Vidyut's forms for the same cell. Runs under the venv that has ``vidyut``:

    .venv/bin/python -m bench.practice_key

Writes ``bench/oracle/practice_verified.json``:
    {"generated_at": ..., "verified": [cell_key, ...], "disagree": {cell_key: [ours, vidyut]}}
The disagreements double as a bug list for the engine.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from bench.oracle_vidyut import _derive  # noqa: E402
from engine.form_index import iter_rows  # noqa: E402

OUT_PATH = _ROOT / "bench" / "oracle" / "practice_verified.json"
_LINGA = {"pulliṅga": "pum", "strīliṅga": "stri", "napuṃsaka": "napumsaka"}


def oracle_cell(row: dict) -> dict:
    f = row["features"]
    if row["kind"] == "subanta":
        return {"kind": "subanta", "stem": row["lemma"], "linga": _LINGA[f["linga"]],
                "vibhakti": f["vibhakti"], "vacana": f["vacana"]}
    gana = int(row["cell_key"].split("@")[1].split(".")[0])     # tinanta:BU@01.0001:laT:1:1
    return {"kind": "tinanta", "dhatu": row["lemma"], "gana": gana, "lakara": f["lakara"],
            "purusha": f["purusha"], "vacana": f["vacana"]}


def main() -> int:
    ours: dict[str, set[str]] = defaultdict(set)
    rows: dict[str, dict] = {}
    for row in iter_rows():
        ours[row["cell_key"]].add(row["surface_slp1"])
        rows[row["cell_key"]] = row
    verified, disagree, declined = [], {}, 0
    for key, row in rows.items():
        try:
            forms, _ = _derive(oracle_cell(row))
        except Exception:
            forms = ""
        if not forms:
            declined += 1
            continue
        theirs = set(forms.split("|"))
        if ours[key] <= theirs:
            verified.append(key)
        else:
            disagree[key] = [sorted(ours[key]), sorted(theirs)]
    OUT_PATH.write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "verified": sorted(verified), "disagree": disagree,
    }, ensure_ascii=False, indent=0) + "\n")
    print(f"[practice_key] {len(rows)} cells: {len(verified)} verified, "
          f"{len(disagree)} disagree, {declined} oracle-declined → {OUT_PATH.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
