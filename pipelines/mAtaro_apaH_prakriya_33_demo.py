"""
pipelines/mAtaro_apaH_prakriya_33_demo.py — ``prakriya_33`` (**१.२.४०** accent spine).

From ``…/separated_prakriyas/prakriya_33_*.json`` — ``ordered_sutra_sequence`` lists **1.2.40**
(OCR title **परि. उदात्तस्वरित…**). The corrected ``panini_engine_pipeline`` ties **1.2.40**
to the **मातरोऽपः** discussion: when **1.2.39** *ekaśruti* does not fully level the phrase,
**उदात्तस्वरितपरस्य सन्नतरः** licenses *sannatara* accent placement.

Full sandhi (**७.३.११०**, **८.२.६६**, **६.१.११३**, **६.१.८७**, **६.१.१०९**, **८.३.१५**) is out of
scope for this narrow slice — only **meta/tagged** preparation + **1.2.40**.

Flat tape (single-word orthographic demo): ``mAtaropaH`` (SLP1 without avagraha encoding).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_mAtaro_apaH_accent_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("mAtaropaH")),
        tags={"anga", "prātipadika", "prakriya_33_mAtaro_apaH_accent_demo"},
        meta={"upadesha_slp1": "mAtaropaH"},
    )


def derive_mAtaro_apaH_prakriya_33() -> State:
    s = State(terms=[_mk_mAtaro_apaH_accent_demo()], meta={}, trace=[])

    # Commentary: *ekaśruti* blocked across ``पृश्निमातरः`` … ``अपः`` boundary — narrow arm.
    s.meta["prakriya_33_ekazruti_na_upapatti_note"] = True

    s.meta["prakriya_33_1_2_40_arm"] = True
    s = apply_rule("1.2.40", s)
    return s


__all__ = ["derive_mAtaro_apaH_prakriya_33", "_mk_mAtaro_apaH_accent_demo"]
