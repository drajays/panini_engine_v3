"""
pipelines/paYcendra_prakriya_42_demo.py — ``prakriya_42`` (**पञ्चेन्द्रः** spine fragment).

Source: ``…/separated_prakriyas/prakriya_42_2026-04-29_14_22_07.json``.

JSON ``ordered_sutra_sequence``: **2.1.50**, **4.1.88**.

In **ashtadhyayi-com** machine indexing, **तद्धितार्थोत्तरपदसमाहारे च** is **2.1.51**, while **2.1.50** is *दिक्संख्ये संज्ञायाम्*
(a different rule). The ``panini_engine_pipeline`` commentary corresponds to **2.1.51** + **4.1.88**;
this recipe implements **2.1.51** (not **2.1.50**) and **4.1.88**.

Spine (glass-box stamps):
  **2.1.3** → **2.1.51** → **4.1.76** → **4.1.88**.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_paYcendra_prakriya_42() -> Term:
    """Abstract stem witness after internal समास/*sandhi* stages (full *niṣpatti* elsewhere)."""
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("paYcendra")),
        tags={"anga", "prātipadika", "prakriya_42_paYcendra_demo"},
        meta={"upadesha_slp1": "paYcendra"},
    )


def derive_paYcendra_prakriya_42() -> State:
    s = State(terms=[_witness_paYcendra_prakriya_42()], meta={}, trace=[])

    s = apply_rule("2.1.3", s)
    s.meta["prakriya_42_taddhitartha_samAhAra_note"] = True
    s.meta["prakriya_42_2_1_51_arm"] = True
    s = apply_rule("2.1.51", s)

    s = apply_rule("4.1.76", s)
    s.meta["prakriya_42_dvigu_anapatye_note"] = True
    s.meta["prakriya_42_4_1_88_arm"] = True
    s = apply_rule("4.1.88", s)
    return s


__all__ = ["derive_paYcendra_prakriya_42", "_witness_paYcendra_prakriya_42"]
