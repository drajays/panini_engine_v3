"""
bench/oracle_vidyut.py — ask Vidyut for the same grid, write a CSV.

CONSTITUTION Art. 19: we do not grade our own homework. Vidyut
(github.com/ambuda-org/vidyut, MIT) is an independent implementation with
per-step sūtra citations, which makes it the one oracle whose disagreements
are diagnosable rather than merely annoying.

**This file is never imported by the engine.** It runs under its own
interpreter — the engine's environment does not carry vidyut, and must not::

    .venv/bin/python3 -m pip install vidyut
    PANINI_ORACLE_PYTHON=.venv/bin/python3 python3 -m bench.run --refresh-oracle

The product is ``bench/oracle/vidyut.csv`` (key, forms, sūtra path), committed
so the comparison reproduces without the oracle installed.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from bench.grids import all_cells  # noqa: E402

OUT_PATH = _ROOT / "bench" / "oracle" / "vidyut.csv"

_LINGA = {"pum": "Pum", "stri": "Stri", "napumsaka": "Napumsaka"}
_VIBHAKTI = {
    1: "Prathama", 2: "Dvitiya", 3: "Trtiya", 4: "Caturthi",
    5: "Panchami", 6: "Sasthi", 7: "Saptami", 8: "Sambodhana",
}
_VACANA = {1: "Eka", 2: "Dvi", 3: "Bahu"}
_PURUSHA = {1: "Uttama", 2: "Madhyama", 3: "Prathama"}   # Pāṇini's order
_GANA = {
    1: "Bhvadi", 2: "Adadi", 3: "Juhotyadi", 4: "Divadi", 5: "Svadi",
    6: "Tudadi", 7: "Rudhadi", 8: "Tanadi", 9: "Kryadi", 10: "Curadi",
}
_LAKARA = {"laT": "Lat", "laG": "Lan", "liT": "Lit", "lRT": "Lrt", "loT": "Lot"}


def _derive(cell: dict) -> tuple[str, str]:
    """(forms, sūtra path) from Vidyut, or ("", "") when it declines.

    Vidyut returns one prakriyā per branch — an ubhayapadī root gives both
    padas, a vibhāṣā gives both options — so the oracle records the whole set
    and agreement means *our form is among them*. Collapsing to the first
    result would manufacture disagreements out of optionality.
    """
    from vidyut.prakriya import (
        Dhatu, Gana, Lakara, Linga, Pada, Prayoga, Pratipadika,
        Purusha, Vacana, Vibhakti, Vyakarana,
    )

    v = Vyakarana()
    if cell["kind"] == "subanta":
        # An ā/ī-final feminine stem is *nyāp*-ending, and Vidyut needs to be
        # told: Pratipadika.basic("rADA") inflects it as a plain a-stem and
        # yields rADAH for षष्ठी where the āp-stem gives rADAyAH. That is a
        # question the grid must answer, not a disagreement about grammar.
        stem = cell["stem"]
        nyap = cell["linga"] == "stri" and stem.endswith(("A", "I"))
        args = Pada.Subanta(
            pratipadika=(Pratipadika.nyap(stem) if nyap
                         else Pratipadika.basic(stem)),
            linga=getattr(Linga, _LINGA[cell["linga"]]),
            vibhakti=getattr(Vibhakti, _VIBHAKTI[cell["vibhakti"]]),
            vacana=getattr(Vacana, _VACANA[cell["vacana"]]),
        )
    else:
        args = Pada.Tinanta(
            dhatu=Dhatu.mula(aupadeshika=cell["dhatu"],
                             gana=getattr(Gana, _GANA[cell["gana"]])),
            prayoga=Prayoga.Kartari,
            lakara=getattr(Lakara, _LAKARA[cell["lakara"]]),
            purusha=getattr(Purusha, _PURUSHA[cell["purusha"]]),
            vacana=getattr(Vacana, _VACANA[cell["vacana"]]),
        )
    results = v.derive(args)
    if not results:
        return "", ""
    forms = sorted({p.text for p in results})
    path = " ".join(step.code for step in results[0].history)
    return "|".join(forms), path


def main() -> int:
    rows = []
    declined = 0
    for cell in all_cells():
        try:
            form, path = _derive(cell)
        except Exception as ex:                      # the oracle's own gaps
            form, path = "", f"ERROR {type(ex).__name__}: {ex}"
        if not form:
            declined += 1
        rows.append({"key": cell["key"], "forms": form, "path": path})
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=["key", "forms", "path"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"[oracle_vidyut] {len(rows)} cells, {declined} declined → "
          f"{OUT_PATH.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
