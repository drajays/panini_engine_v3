"""
tools/sutra_superset.py — the invariant: every sūtra Vidyut fires in a derivation, our engine fires too.

For each (dhātu, lakāra, prayoga, puruṣa, vacana) cell, Vidyut's step codes are compared with the sūtras
our engine applied. ``missing`` = Vidyut fired, we did not (a glass-box gap or a bug); ``extra`` = we fired and
Vidyut did not (fine: Pāṇinian rules Vidyut folds away). The goal is ``missing == ∅`` everywhere.

    .venv/bin/python -m tools.sutra_superset --roots 20 --lakara laT liT   # ranked missing-sūtra list

Runs under the venv that carries vidyut. Never imported by the engine.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

_V = {"laT": "Lat", "liT": "Lit", "luT": "Lut", "lRT": "Lrt", "loT": "Lot", "laG": "Lan",
      "liG": "VidhiLin", "AsIrliG": "AshirLin", "luG": "Lun", "lRG": "Lrn"}
_PUR = {3: "Prathama", 2: "Madhyama", 1: "Uttama"}
_VAC = {1: "Eka", 2: "Dvi", 3: "Bahu"}
_GANA = {1: "Bhvadi", 2: "Adadi", 3: "Juhotyadi", 4: "Divadi", 5: "Svadi",
         6: "Tudadi", 7: "Rudhadi", 8: "Tanadi", 9: "Kryadi", 10: "Curadi"}


# executed = the engine fired or recognised the rule (a saṃjñā DEFINED, a vacuous application); SKIPPED/BLOCKED did not
EXECUTED = {"APPLIED", "APPLIED_VACUOUS", "DEFINED", "VACUOUS", "AUDIT"}


def vidyut_codes(vy, row: dict, lakara: str, prayoga: str, purusha: int, vacana: int) -> list[set[str]]:
    """One set of sūtra codes per Vidyut derivation (a cell can have several)."""
    from vidyut.prakriya import Dhatu, Gana, Lakara, Pada, Prayoga, Purusha, Vacana
    from bench.practice_key import accented
    d = Dhatu.mula(aupadeshika=accented(row["upadesha_slp1"], row["dhatupatha_id"]),
                   gana=getattr(Gana, _GANA[int(row["dhatupatha_id"].split(".")[0])]))
    pada = Pada.Tinanta(dhatu=d, prayoga=getattr(Prayoga, prayoga.capitalize()), lakara=getattr(Lakara, _V[lakara]),
                        purusha=getattr(Purusha, _PUR[purusha]), vacana=getattr(Vacana, _VAC[vacana]))
    return [{s.code.split(":")[0] for s in p.history} for p in vy.derive(pada)]


def engine_codes(row: dict, lakara: str, prayoga: str, purusha: int, vacana: int):
    from pipelines.tinanta import derive
    st = derive(row.get("id") or row["upadesha_slp1"], lakara, prayoga, purusha, vacana)
    return st.flat_slp1(), {s["sutra_id"] for s in st.trace if s.get("status") in EXECUTED
                            and not str(s["sutra_id"]).startswith("__")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--roots", type=int, default=10)
    ap.add_argument("--lakara", nargs="+", default=["laT"])
    ap.add_argument("--prayoga", default="kartari")
    args = ap.parse_args()
    import sutras  # noqa: F401
    from pipelines.dhatupatha import _payload, _envelope
    from vidyut.prakriya import Vyakarana
    vy, rows = Vyakarana(), [e for e in _envelope(_payload())["entries"] if e.get("gana") == 1][: args.roots]
    miss, cells, clean = Counter(), 0, 0
    for row in rows:
        for la in args.lakara:
            for pu in (3, 2, 1):
                for vc in (1, 2, 3):
                    try:
                        surf, ours = engine_codes(row, la, args.prayoga, pu, vc)
                        theirs = vidyut_codes(vy, row, la, args.prayoga, pu, vc)
                    except Exception:
                        continue
                    if not theirs:
                        continue
                    cells += 1
                    best = min(theirs, key=lambda t: len(t - ours))          # the Vidyut branch we are closest to
                    gap = best - ours
                    clean += not gap
                    miss.update(gap)
    print(f"{cells} cells · {clean} with no Vidyut sūtra missing from the engine · {cells - clean} with gaps")
    for sid, n in miss.most_common(40):
        print(f"{n:5d}  {sid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
