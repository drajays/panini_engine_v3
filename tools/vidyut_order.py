"""tools/vidyut_order.py — Vidyut as VALIDATOR of sūtra order, never as authority (owner's rule, 2026-10-10).

We follow what the Aṣṭādhyāyī says, supported by Pushpa Dixit and the data; the loop's order is the glass box. Vidyut's sequence is
only a cross-check: every disagreement (a Vidyut sūtra we never fire, or a pair ordered a→b by Vidyut and b→a by us) is a *flag to
adjudicate*, not an error and not a thing to copy. Each flag gets a verdict in `data/inputs/vidyut_order_overrides.json`:
``ours`` (Pāṇini/Pushpa support our order — reason + authority recorded) or ``engine`` (we are wrong → fix) or stays open.
`--evidence` tallies the order in the brain's non-Vidyut derivations (ashtadhyayi.com subanta / sutrartha) as first evidence.

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


def evidence(pairs) -> dict:
    """For each (a,b): how many authentic (non-Vidyut) derivations in the brain order a<b vs b<a."""
    import sqlite3
    c = sqlite3.connect(f"file:{Path.home()}/data-master/ashtadhyayi-ai/db/ashtadhyayi.db?mode=ro", uri=True)
    seqs: dict[int, list[str]] = {}
    for d, st in c.execute("select s.deriv_id, s.sutras from steps s join derivations d on d.id=s.deriv_id "
                           "where d.source not like 'vidyut%' order by s.deriv_id, s.step_no"):
        seqs.setdefault(d, []).extend(x for x in str(st).replace(",", " ").split() if x.count(".") == 2)
    out = {}
    for a, b in pairs:
        ab = sum(1 for q in seqs.values() if a in q and b in q and q.index(a) < q.index(b))
        ba = sum(1 for q in seqs.values() if a in q and b in q and q.index(a) > q.index(b))
        out[f"{a}<{b}"] = {"vidyut_order_in_authentic": ab, "our_order_in_authentic": ba}
    return out


def sk_krama(pairs) -> dict:
    """Siddhānta-kaumudī order of the two sūtras (the tradition's own derivation order): +1 = a before b (Vidyut's order), -1 = b first."""
    import sqlite3
    c = sqlite3.connect(f"file:{Path.home()}/data-master/ashtadhyayi-ai/db/ashtadhyayi.db?mode=ro", uri=True)
    pos = lambda i: (c.execute("select sk_krama from sutras where id=?", (i,)).fetchone() or ("",))[0]
    out = {}
    for a, b in pairs:
        pa, pb = pos(a), pos(b)
        out[f"{a}<{b}"] = 0 if not (pa and pb) else (1 if int(pa) < int(pb) else -1)
    return out


def propose(e: dict) -> str:
    """Only a proposal from Pāṇinian-tradition evidence (authentic derivations + SK order). Confirmed by a card, never by this."""
    signs = {1 if e["vidyut_order_in_authentic"] > e["our_order_in_authentic"] else -1 if e["our_order_in_authentic"] > e["vidyut_order_in_authentic"] else 0,
             e["sk_krama"]} - {0}
    return "open" if len(signs) != 1 else ("engine" if signs == {1} else "ours")


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
    pairs = [tuple(k.split("<")) for k, _ in inv.most_common(40)]
    ev = evidence(pairs)
    sk = sk_krama(pairs)
    for k in ev:
        ev[k]["sk_krama"] = sk[k]
        ev[k]["proposed_verdict"] = propose(ev[k])
    return {"gana": gana, "cells": cells, "agree_with_vidyut": ok, "flagged_cells": bad[:50],
            "missing": miss.most_common(40), "inverted": inv.most_common(40), "authentic_evidence": ev}


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
