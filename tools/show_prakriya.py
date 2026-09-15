"""
tools/show_prakriya.py — read a derivation the way a scholar would.

A small set of forms we are **certain** of, each with the warrant for that
certainty, printed step by step with the sūtra that did the work. Use it to
check the flow by eye:

    python3 -m tools.show_prakriya --list
    python3 -m tools.show_prakriya ramau
    python3 -m tools.show_prakriya ramau --all-steps     # include the vacuous rows
    python3 -m tools.show_prakriya --check               # every case, surfaces only

Certainty is not an opinion here. Each case says where it comes from: a cited
gold paradigm under ``data/reference/``, agreement with the Vidyut oracle in
``bench/oracle/vidyut.csv`` (Art. 19), or a repair made in this repository with
its own regression test. ``--check`` is the flow test: every expected surface
must still come out.
"""
from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

ORACLE = _ROOT / "bench" / "oracle" / "vidyut.csv"


@dataclass(frozen=True)
class Case:
    key: str
    expect_dev: str
    warrant: str
    kind: str
    args: tuple[Any, ...]

    @property
    def cell_key(self) -> str:
        if self.kind == "subanta":
            stem, vibhakti, vacana, linga = self.args
            short = {"pulliṅga": "pum", "strīliṅga": "stri", "napuṃsaka": "napumsaka"}[linga]
            return f"subanta:{stem}:{short}:{vibhakti}:{vacana}"
        dhatu, lakara, purusha, vacana = self.args
        return f"tinanta:{dhatu}:{lakara}:{purusha}:{vacana}"


CASES: tuple[Case, ...] = (
    Case("ramah",   "रामः",   "gold: rama_pullinga 1-1 · oracle agrees",
         "subanta", ("rAma", 1, 1, "pulliṅga")),
    Case("ramau",   "रामौ",   "oracle agrees, and by the same chain: 6.1.104 नादिचि → 6.1.88 वृद्धिः",
         "subanta", ("rAma", 1, 2, "pulliṅga")),
    Case("ramah_pl", "रामाः", "gold: rama_pullinga 1-3 · oracle agrees",
         "subanta", ("rAma", 1, 3, "pulliṅga")),
    Case("ramena",  "रामेण",  "gold: rama_pullinga 3-1 · oracle agrees (ṇatva by 8.4.2)",
         "subanta", ("rAma", 3, 1, "pulliṅga")),
    Case("ramasya", "रामस्य", "gold: rama_pullinga 6-1 · oracle agrees",
         "subanta", ("rAma", 6, 1, "pulliṅga")),
    Case("hari",    "हरी",    "gold: hari_pullinga 1-2 · oracle agrees (6.1.102 pūrvasavarṇa)",
         "subanta", ("hari", 1, 2, "pulliṅga")),
    Case("vayu",    "वायू",   "oracle agrees — u-stem dual, same pūrvasavarṇa",
         "subanta", ("vAyu", 1, 2, "pulliṅga")),
    Case("agni",    "अग्नी",  "oracle agrees — the tagging case behind 1.1.11",
         "subanta", ("agni", 1, 2, "pulliṅga")),
    Case("nadyau",  "नद्यौ",  "repaired 2026-09-15: pragṛhya belongs to the pada, so 6.1.77 applies "
                              "· test_6_1_104_nadici_ramau.py",
         "subanta", ("nadI", 1, 2, "strīliṅga")),
    Case("radhe",   "राधे",   "gold: rADA_strilinga 1-2 · oracle agrees (ā-stem dual)",
         "subanta", ("rADA", 1, 2, "strīliṅga")),
    Case("jnanam",  "ज्ञानम्", "gold: jnana_napumsaka 1-1 · oracle agrees",
         "subanta", ("jYAna", 1, 1, "napuṃsaka")),
    Case("bhavati", "भवति",   "gold: tinanta bhavati · oracle agrees",
         "tinanta", ("BU", "laT", 3, 1)),
    Case("bhavatah", "भवतः",  "oracle agrees — laṭ 3rd dual",
         "tinanta", ("BU", "laT", 3, 2)),
    Case("bhavanti", "भवन्ति", "oracle agrees — laṭ 3rd plural",
         "tinanta", ("BU", "laT", 3, 3)),
)


def derive(case: Case) -> Any:
    import sutras  # noqa: F401
    if case.kind == "subanta":
        from pipelines.subanta import derive as sub
        stem, vibhakti, vacana, linga = case.args
        return sub(stem, vibhakti, vacana, linga=linga)
    from pipelines.tinanta import derive as tin
    dhatu, lakara, purusha, vacana = case.args
    return tin(dhatu, lakara, "kartari", purusha, vacana)


def oracle_forms(cell_key: str) -> list[str]:
    if not ORACLE.exists():
        return []
    with ORACLE.open(encoding="utf-8") as fp:
        for row in csv.DictReader(fp):
            if row["key"] == cell_key:
                return [f for f in row["forms"].split("|") if f]
    return []


def show(case: Case, all_steps: bool) -> int:
    from core.trace_view import enrich_trace

    state = derive(case)
    got = state.flat_dev()
    print(f"\n  {case.key} — expecting {case.expect_dev}")
    print(f"  warrant: {case.warrant}")
    print(f"  {'─' * 74}")

    for n, step in enumerate(enrich_trace(state.trace), 1):
        changed = step.get("form_before") != step.get("form_after")
        if not (changed or all_steps):
            continue
        mark = "→" if changed else " "
        print(f"  {n:>3} {mark} {step.get('sutra_id',''):<9} {step.get('status',''):<16}"
              f" {step.get('form_before_dev','')} {'⇒' if changed else ' '} "
              f"{step.get('form_after_dev','')}")
        text = step.get("_sutra_text_dev") or ""
        if text:
            print(f"        {text}")
        if changed and step.get("_hint_hi"):
            print(f"        सङ्केतः {step['_hint_hi'][:88]}")

    theirs = oracle_forms(case.cell_key)
    verdict = "✓" if got == case.expect_dev else "✗"
    print(f"  {'─' * 74}")
    print(f"  {verdict} {got}   ({state.flat_slp1()})"
          + (f"   oracle: {'|'.join(theirs)}" if theirs else ""))
    return 0 if got == case.expect_dev else 1


def check() -> int:
    bad = 0
    for case in CASES:
        got = derive(case).flat_dev()
        ok = got == case.expect_dev
        bad += 0 if ok else 1
        print(f"  {'✓' if ok else '✗'} {case.key:<10} {got:<10}"
              + ("" if ok else f" expected {case.expect_dev}"))
    print(f"\n  {len(CASES) - bad}/{len(CASES)} certain prakriyās still derive")
    return 1 if bad else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Read a certain prakriyā, step by step.")
    ap.add_argument("case", nargs="?")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--all-steps", action="store_true", help="include vacuous rows")
    args = ap.parse_args(argv)

    if args.list:
        for case in CASES:
            print(f"  {case.key:<10} {case.expect_dev:<10} {case.warrant}")
        return 0
    if args.check or not args.case:
        return check()
    match = next((c for c in CASES if c.key == args.case), None)
    if match is None:
        print(f"no such case: {args.case}  (try --list)")
        return 2
    return show(match, args.all_steps)


if __name__ == "__main__":
    raise SystemExit(main())
