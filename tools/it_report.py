"""
tools/it_report.py — which it-letters an upadeśa carries (1.3.2–1.3.9).

    python3 -m tools.it_report qukfY BvAdi_01_1140 gamx~     # dhātus (id or upadeśa)
    python3 -m tools.it_report --krt Kac Rvul GaY             # kṛt pratyayas
    python3 -m tools.it_report --taddhita cPaY Wak            # taddhita pratyayas
    python3 -m tools.it_report --sup jas Sas --tin Ji tip     # vibhaktis (1.3.4 applies)

Runs the full it-prakaraṇa on each upadeśa and prints, per it-letter, the sūtra
that named it and the Pāṇinian class name later rules read (kit, ṅit, ñīt, ṭvit …).
"""
from __future__ import annotations

import argparse
import sys

import sutras  # noqa: F401
from engine.it_samjna import it_records
from engine.state import State, Term
from phonology.joiner import slp1_to_devanagari
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.it_prakarana import run_it_prakarana

_KIND_TAGS = {
    "krt": {"krt"},
    "taddhita": {"taddhita"},
    "sup": {"sup"},
    "tin": {"tin", "tin_adesha_3_4_78"},
}


def _dhatu_state(ref: str) -> State:
    from pipelines.krdanta import build_dhatu_state

    return build_dhatu_state(ref)


def _pratyaya_state(upadesha: str, kind: str) -> State:
    t = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(upadesha)),
        tags={"pratyaya", "upadesha"} | _KIND_TAGS[kind],
        meta={"upadesha_slp1": upadesha},
    )
    return State(terms=[t], meta={}, trace=[])


def report(state: State, label: str) -> str:
    upadesha = (state.terms[0].meta.get("upadesha_slp1") or "").strip()
    state = run_it_prakarana(state)
    t = state.terms[0]
    residue = slp1_to_devanagari(t.varnas) or "∅"
    head = f"{label:9} {slp1_to_devanagari(parse_slp1_upadesha_sequence(upadesha))} ({upadesha}) → {residue}"
    rows = [
        f"    {r['letters_dev']:6} {r.get('sutra') or '—':16} {r.get('name_dev') or '—':10} "
        f"{r.get('name') or '—':8} {r['position']}"
        for r in it_records(t)
    ]
    return "\n".join([head] + (rows or ["    (no it-letters)"]))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dhatu", nargs="*", help="dhātupāṭha id or upadeśa (SLP1)")
    for kind in _KIND_TAGS:
        ap.add_argument(f"--{kind}", nargs="+", default=[], metavar="UPADESHA")
    args = ap.parse_args(argv)
    jobs = [("dhātu", ref, None) for ref in args.dhatu]
    for kind in _KIND_TAGS:
        jobs += [(kind, up, kind) for up in getattr(args, kind)]
    if not jobs:
        ap.print_help()
        return 1
    for label, ref, kind in jobs:
        try:
            st = _dhatu_state(ref) if kind is None else _pratyaya_state(ref, kind)
        except Exception as ex:  # unknown dhātu id / upadeśa
            print(f"{label:9} {ref}: {ex}")
            continue
        print(report(st, label))
    return 0


if __name__ == "__main__":
    sys.exit(main())
