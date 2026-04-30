"""
pipelines/Amalakam_prakriya_44_demo.py — ``prakriya_44`` (**आमलकम्** spine fragment).

Source: ``…/separated_prakriyas/prakriya_44_2026-04-29_14_22_21.json``.

JSON ``ordered_sutra_sequence``: **4.3.132**, **1.2.46**, **7.1.24**.

On *ashtadhyayi-com*, **तस्य विकारः** is **4.3.134** (not **4.3.132**, which is *कौपिञ्जलहास्तिपदादण्*). This recipe
implements **4.3.134** + **1.2.46** + **7.1.24** as in the ``panini_engine_pipeline`` (*फलम्* from *आमलकी* tree).
**6.1.107** (*अमि पूर्वः*) follows **7.1.24** here so ``flat_slp1()`` is **Amalakam** (not in JSON’s three-id spine, but in the commentary table).

Witness ``Amalaka`` carries ``samasa_member`` only so **1.2.46** can register *prātipadika* on this glass-box tape;
full *ṣaṣṭī* + *aṇ* + *luk* chain lives elsewhere.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_Amalaka_prakriya_44() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("Amalaka")),
        tags={"anga", "prātipadika", "samasa_member", "prakriya_44_Amalakam_demo"},
        meta={"upadesha_slp1": "Amalaka"},
    )


def derive_Amalakam_prakriya_44() -> State:
    s = State(terms=[_witness_Amalaka_prakriya_44()], meta={}, trace=[])

    s = apply_rule("4.1.76", s)
    s.meta["prakriya_44_tasya_vikAra_note"] = True
    s.meta["prakriya_44_4_3_134_arm"] = True
    s = apply_rule("4.3.134", s)

    s = apply_rule("1.2.46", s)

    s.terms[0].tags.add("napuṃsaka")
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.24", s)
    s = apply_rule("6.1.107", s)
    return s


__all__ = ["derive_Amalakam_prakriya_44", "_witness_Amalaka_prakriya_44"]
