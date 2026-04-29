"""
pipelines/uktaH_samprasaraNa_demo.py — 'उक्तः' (uktaH) prakriyā demo from `1145.md`.

Core spine (note):
  vac + kta
    1.1.26   (nisThA) — kta
    1.3.8/9  it-lopa: kta → ta (kit)
    6.1.15   samprasāraṇa trigger (vaci... kiti) — arms 1.1.45
    1.1.45   igyaṇaḥ samprasāraṇam: v → u
    6.1.108  pūrvarūpa: u + a → u
    8.2.1    Tripāḍī gate
    8.2.30   coḥ kuḥ: c → k before t

Then sup+visarga (minimal):
  4.1.2 (su) + 1.3.2/9 (su→s) + 1.2.41 (apṛkta) + 8.2.66 + 8.3.15 → uktaH
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from phonology import HAL
from pipelines.subanta import _pada_merge


def _structural_merge_to_pratipadika(state: State, *, upadesha_slp1: str) -> State:
    s = state
    all_varnas = []
    for t in s.terms:
        all_varnas.extend(v.clone() for v in t.varnas)
    # a-stem model: add inherent-a when consonant-final.
    if all_varnas and all_varnas[-1].slp1 in HAL:
        from phonology.varna import mk_inherent_a

        all_varnas.append(mk_inherent_a())
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": upadesha_slp1},
    )
    before = s.flat_slp1()
    s.terms = [merged]
    s.trace.append(
        {
            "sutra_id": "__UKTA_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "उक्त-मेलनम्",
            "form_before": before,
            "form_after": s.flat_slp1(),
            "why_dev": "धातु + क्त → प्रातिपदिकम् (संरचनात्मकं, न सूत्रम्)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_uktaH() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vac")),
        tags={"dhatu"},
        meta={"upadesha_slp1": "vac"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("kta")),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": "kta"},
    )
    s = State(terms=[dhatu, pr], meta={}, trace=[])

    s = apply_rule("1.1.26", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("6.1.15", s)
    s = apply_rule("1.1.45", s)
    s = apply_rule("6.1.108", s)

    # Now treat vac+ta as a prātipadika and attach su for uktaH.
    s = _structural_merge_to_pratipadika(s, upadesha_slp1="ukta")

    # Now attach su and finish with ru/visarga.
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta["linga"] = "pulliṅga"
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.2.41", s)
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.30", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_uktaH"]

