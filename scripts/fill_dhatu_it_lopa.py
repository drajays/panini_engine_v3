"""
Fill the two derived root fields of ``data/inputs/dhatupatha_upadesha.json`` (AMENDMENT 20 §7). Idempotent.

    python3 scripts/fill_dhatu_it_lopa.py

* ``raw_dhatu_after_it_lopa_slp1/_dev`` — exactly what the name says: the engine's own it-prakaraṇa
  (1.3.2–1.3.9 sūtra files) run on ``upadesha_slp1``. Nothing after 1.3.9 (no num, ṣatva, ṇatva …).
* ``citation_dhatu_slp1/_dev`` — the traditional citation root (``mula_dhatu_dev``: नन्द्, निन्द्, पञ्च्, स्तु …),
  the form people type and dictionaries list. Lookups use this.

Run after editing the dhātupāṭha; ``tests/unit/test_dhatu_root_fields.py`` fails if they drift.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
PATH = ROOT / "data/inputs/dhatupatha_upadesha.json"


def it_lopa_residue(entry_id: str) -> str:
    import sutras  # noqa: F401  (registers 1.3.2–1.3.9)
    from pipelines.it_prakarana import run_it_prakarana
    from pipelines.krdanta import build_dhatu_state

    return run_it_prakarana(build_dhatu_state(entry_id)).flat_slp1()


def main() -> None:
    from phonology.joiner import slp1_to_devanagari
    from phonology.tokenizer import devanagari_to_slp1_flat
    from phonology.varna import parse_slp1_upadesha_sequence

    data = json.loads(PATH.read_text(encoding="utf-8"))
    changed = 0
    for i, e in enumerate(data["entries"]):
        raw = it_lopa_residue(e["id"])
        new = {
            "raw_dhatu_after_it_lopa_dev": slp1_to_devanagari(parse_slp1_upadesha_sequence(raw)),
            "raw_dhatu_after_it_lopa_slp1": raw,
            "citation_dhatu_dev": e["mula_dhatu_dev"],
            "citation_dhatu_slp1": devanagari_to_slp1_flat(e["mula_dhatu_dev"]),
        }
        if any(e.get(k) != v for k, v in new.items()):
            changed += 1
        out = {}
        for k, v in e.items():  # keep key order; citation_* right after raw_*
            if k in new:
                continue
            out[k] = v
            if k == "mula_dhatu_dev":
                out.update(new)
        data["entries"][i] = out
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(data['entries'])} dhātus, {changed} updated")


if __name__ == "__main__":
    main()
