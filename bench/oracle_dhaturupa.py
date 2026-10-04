"""
bench/oracle_dhaturupa.py — Vidyut's dhātu-rūpa tables and per-cell derivations, JSON in / JSON out.

Runs under the repo's ``.venv`` (the only interpreter with ``vidyut``); ``webui`` pipes requests here.
Never imported by the engine.

    {"op":"grid","upadesha":"BU","path_id":"01.0001","prayoga":"kartari","pada":null,"sanadi":null,"prefix":null,
     "lakaras":["Lat",...]}                       -> {"Lat":[[forms]*9 in prathama→uttama × eka→bahu order], ...}
    {"op":"cell", same + "lakara","purusha","vacana"} -> [{"text":..,"steps":[{"code","result"}]}]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from bench.oracle_vidyut import _GANA, _PURUSHA, _VACANA  # noqa: E402
from bench.practice_key import accented  # noqa: E402

LAKARAS = ["Lat", "Lit", "Lut", "Lrt", "Let", "Lot", "Lan", "VidhiLin", "AshirLin", "Lun", "Lrn"]


def _pada(q: dict, v_mod, lakara: str, purusha: int, vacana: int):
    from vidyut.prakriya import Dhatu, DhatuPada, Gana, Lakara, Pada, Prayoga, Purusha, Sanadi, Vacana
    d = Dhatu.mula(aupadeshika=accented(q["upadesha"], q["path_id"]),
                   gana=getattr(Gana, _GANA[int(q["path_id"].split(".")[0])]))
    if q.get("sanadi"):
        d = d.with_sanadi([getattr(Sanadi, q["sanadi"])])
    if q.get("prefix"):
        d = d.with_prefixes([q["prefix"]])
    kw = {"dhatu_pada": getattr(DhatuPada, q["pada"].capitalize() + "pada")} if q.get("pada") else {}
    return Pada.Tinanta(dhatu=d, prayoga=getattr(Prayoga, q["prayoga"].capitalize()),
                        lakara=getattr(Lakara, lakara), purusha=getattr(Purusha, _PURUSHA[purusha]),
                        vacana=getattr(Vacana, _VACANA[vacana]), **kw)


def _subanta(q: dict, vibhakti: int, vacana: int):
    from vidyut.prakriya import Linga, Pada, Pratipadika, Vacana, Vibhakti
    from bench.oracle_vidyut import _LINGA, _VIBHAKTI
    stem, linga = q["stem"], _LINGA[q["linga"]]
    nyap = linga == "Stri" and stem.endswith(("A", "I"))
    return Pada.Subanta(pratipadika=Pratipadika.nyap(stem) if nyap else Pratipadika.basic(stem),
                        linga=getattr(Linga, linga), vibhakti=getattr(Vibhakti, _VIBHAKTI[vibhakti]),
                        vacana=getattr(Vacana, _VACANA[vacana]))


def main() -> int:
    from vidyut.prakriya import Vyakarana
    v, q = Vyakarana(), json.load(sys.stdin)
    if q["op"] == "subgrid":                      # 8 vibhakti × 3 vacana, row-major
        out = []
        for vb in range(1, 9):
            for vc in (1, 2, 3):
                try:
                    out.append(sorted({p.text for p in v.derive(_subanta(q, vb, vc))}))
                except Exception:
                    out.append([])
    elif q["op"] == "subcell":
        try:
            out = [{"text": p.text, "steps": [{"code": s.code, "result": list(s.result)} for s in p.history]}
                   for p in v.derive(_subanta(q, q["vibhakti"], q["vacana"]))]
        except Exception as ex:
            out = {"error": f"{type(ex).__name__}: {ex}"[:200]}
    elif q["op"] == "grid":
        out = {}
        for la in q.get("lakaras") or LAKARAS:
            cells = []
            for pu in (3, 2, 1):
                for vc in (1, 2, 3):
                    try:
                        cells.append(sorted({p.text for p in v.derive(_pada(q, v, la, pu, vc))}))
                    except Exception:
                        cells.append([])
            out[la] = cells
    else:
        try:
            out = [{"text": p.text, "steps": [{"code": s.code, "result": list(s.result)} for s in p.history]}
                   for p in v.derive(_pada(q, v, q["lakara"], q["purusha"], q["vacana"]))]
        except Exception as ex:
            out = {"error": f"{type(ex).__name__}: {ex}"[:200]}
    json.dump(out, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
