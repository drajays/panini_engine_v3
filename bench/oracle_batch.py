"""
bench/oracle_batch.py — Vidyut forms for a batch of cells, JSON in / JSON out.

The API runs in an interpreter without ``vidyut``; ``core/lab`` pipes a grid
here through the repo's ``.venv`` (which has it):

    echo '[{"kind":"tinanta","dhatu":"eDa~","path_id":"01.0002","lakara":"laT",
            "prayoga":"kartari","purusha":3,"vacana":1}]' | .venv/bin/python -m bench.oracle_batch

Each output item is the sorted list of Vidyut's forms (SLP1), [] if it declines.
Never imported by the engine.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from bench.oracle_vidyut import _GANA, _LINGA, _PURUSHA, _VACANA, _VIBHAKTI  # noqa: E402
from bench.practice_key import accented  # noqa: E402

_LAKARA = {"laT": "Lat", "liT": "Lit", "luT": "Lut", "lRT": "Lrt", "loT": "Lot",
           "laG": "Lan", "liG": "VidhiLin", "luG": "Lun", "lRG": "Lrn", "AsIrliG": "AshirLin"}


def forms(cell: dict, v) -> list[str]:
    from vidyut.prakriya import (Dhatu, Gana, Lakara, Linga, Pada, Prayoga, Pratipadika,
                                 Purusha, Vacana, Vibhakti)
    if cell["kind"] == "subanta":
        stem, linga = cell["stem"], _LINGA[cell["linga"]]
        nyap = linga == "Stri" and stem.endswith(("A", "I"))
        args = Pada.Subanta(pratipadika=Pratipadika.nyap(stem) if nyap else Pratipadika.basic(stem),
                            linga=getattr(Linga, linga), vibhakti=getattr(Vibhakti, _VIBHAKTI[cell["vibhakti"]]),
                            vacana=getattr(Vacana, _VACANA[cell["vacana"]]))
    else:
        args = Pada.Tinanta(
            dhatu=Dhatu.mula(aupadeshika=accented(cell["dhatu"], cell["path_id"]),
                             gana=getattr(Gana, _GANA[int(cell["path_id"].split(".")[0])])),
            prayoga=getattr(Prayoga, cell["prayoga"].capitalize()),
            lakara=getattr(Lakara, _LAKARA[cell["lakara"]]),
            purusha=getattr(Purusha, _PURUSHA[cell["purusha"]]),
            vacana=getattr(Vacana, _VACANA[cell["vacana"]]))
    return sorted({p.text for p in v.derive(args)})


def main() -> int:
    from vidyut.prakriya import Vyakarana
    v = Vyakarana()
    out = []
    for cell in json.load(sys.stdin):
        try:
            out.append(forms(cell, v))
        except Exception:                         # the oracle's own gaps
            out.append([])
    json.dump(out, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
