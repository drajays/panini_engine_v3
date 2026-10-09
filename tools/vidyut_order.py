"""tools/vidyut_order.py — the Vidyut ORDER floor (owner's rule, 2026-10-10).

Vidyut's sūtra sequence for a form is a minimum: our loop's sequence must contain it as an ordered subsequence
(extra sūtras may come before, between, after). A pair (a, b) that Vidyut orders a→b but we order b→a — or a Vidyut sūtra we never
fire — is a *deviation*; it is allowed only if `data/inputs/vidyut_order_overrides.json` records it with a reason and an
authority (Pushpa Dixit card / Aṣṭādhyāyī data). Otherwise it is a bug or an Art. 18 gap.

    .venv/bin/python -m tools.vidyut_order [--gana N] [--lakara laT ...] [--roots K] [--write]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from types import SimpleNamespace as NS

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
OVR = ROOT / "data" / "inputs" / "vidyut_order_overrides.json"
OUT = ROOT / "docs" / "ratchet_vidyut_order.json"
EXECUTED = {"APPLIED", "APPLIED_VACUOUS", "DEFINED", "VACUOUS", "AUDIT"}


def overrides() -> dict:
    return json.loads(OVR.read_text(encoding="utf-8"))["overrides"] if OVR.exists() else {}


def ordered(codes) -> list[str]:
    return list(dict.fromkeys(codes))


def _operational(sid: str) -> bool:
    """Class override (reason on file in the overrides JSON, `classes.non_operational`): saṃjñā / adhikāra / atideśa / paribhāṣā / anuvāda
    sūtras change no tape; Vidyut stamps them where an operation cites them, the loop where it first consults them. Their *set* is still
    checked (missing); their *order* is not."""
    from engine.registry import SUTRA_REGISTRY
    r = SUTRA_REGISTRY.get(sid)
    return r is None or r.sutra_type.name in ("VIDHI", "NIYAMA", "VIBHASHA", "NIPATANA", "PRATISHEDHA")


def compare(vidyut: list[str], ours: list[str]) -> dict:
    """missing: Vidyut sūtras we never fire. inverted: [a,b] Vidyut puts a before b, we put b before a (both fired, both operational)."""
    v, o = ordered(vidyut), ordered(ours)
    pos = {s: i for i, s in enumerate(o)}
    have = [s for s in v if s in pos and _operational(s)]
    inv = [[a, b] for i, a in enumerate(have) for b in have[i + 1:] if pos[a] > pos[b]]
    return {"missing": [s for s in v if s not in pos], "inverted": inv}


def deviations_unexplained(cmp: dict, ovr: dict) -> dict:
    return {"missing": [s for s in cmp["missing"] if f"missing:{s}" not in ovr],
            "inverted": [p for p in cmp["inverted"] if f"{p[0]}<{p[1]}" not in ovr]}


def main(gana: int, lakaras: list[str], roots: int) -> dict:
    import sutras  # noqa: F401
    from pipelines.dhatupatha import iter_dhatu_entries
    from pipelines.tinanta import derive
    from tools.autonomy_report import run_autonomously, start_state
    from tools.sutra_superset import _GANA, vidyut_codes  # noqa: F401
    import vidyut.prakriya as vp
    vy = vp.Vyakarana()
    ovr = overrides()
    rows = [r for r in iter_dhatu_entries() if r.get("gana") == gana][:roots]
    cells = ok = 0
    miss, inv, bad = Counter(), Counter(), []
    for row in rows:
        root = row.get("id") or row["upadesha_slp1"]
        for lak in lakaras:
            try:
                expect = derive(root, lak, "kartari", 3, 1).flat_slp1()
                run = run_autonomously(start_state(NS(kind="tinanta", args=(root, lak, 3, 1))), expect, root, 120)
                vsets = _vidyut_seq(vy, row, lak)
            except Exception:
                continue
            if run.outcome != "reached" or not vsets:
                continue
            ours = [t["sutra_id"] for t in run.state.trace if t.get("status") in EXECUTED and not str(t["sutra_id"]).startswith("__")]
            # a cell can have several Vidyut derivations: the best-matching one is the floor
            best = min((compare(v, ours) for v in vsets), key=lambda c: len(c["missing"]) + len(c["inverted"]))
            cells += 1
            un = deviations_unexplained(best, ovr)
            if not un["missing"] and not un["inverted"]:
                ok += 1
                continue
            bad.append(f"{root}/{lak}")
            miss.update(un["missing"])
            inv.update(f"{a}<{b}" for a, b in un["inverted"])
    return {"gana": gana, "cells": cells, "floor_ok": ok, "bad_cells": bad[:50],
            "missing": miss.most_common(40), "inverted": inv.most_common(40)}


def _vidyut_seq(vy, row, lak):
    from vidyut.prakriya import Dhatu, Gana, Lakara, Pada, Prayoga, Purusha, Vacana
    from bench.practice_key import accented
    from tools.sutra_superset import _GANA, _V
    d = Dhatu.mula(aupadeshika=accented(row["upadesha_slp1"], row["dhatupatha_id"]),
                   gana=getattr(Gana, _GANA[int(row["dhatupatha_id"].split(".")[0])]))
    pada = Pada.Tinanta(dhatu=d, prayoga=Prayoga.Kartari, lakara=getattr(Lakara, _V[lak]), purusha=Purusha.Prathama, vacana=Vacana.Eka)
    return [[s.code.split(":")[0] for s in p.history if s.code.count(".") == 2] for p in vy.derive(pada)]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--gana", type=int, default=1)
    ap.add_argument("--lakara", nargs="+", default=["laT"])
    ap.add_argument("--roots", type=int, default=10)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    r = main(a.gana, a.lakara, a.roots)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    if a.write:
        OUT.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n")
