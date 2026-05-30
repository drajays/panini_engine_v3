"""
pipelines/avadhIt_han_lun_ekavacana_lesson.py — अवधीत् (*han* → *vadh*, luṅ 1sg para).

Prakriyā (per user spine):
  हन् + लुङ् → **2.4.43** वध → च्लि/सिच् → **6.4.71** अट् → **3.4.78** तिप् → **7.2.35** इट् →
  **6.4.48** अतो लोपः + **1.1.57** (लुप्त-अ स्थानिवत् → **7.2.3**/**7.2.7** न) →
  **3.4.100** → **7.3.96** ईट् → **8.2.28** सिज्लोप → **6.1.101** सवर्ण-दीर्घ।

Target SLP1: **avadhIt** (अवधीत्).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_luN_lakara_cli_sic,
    P00_parasmai_tin_adesha,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_hal_it_lopa,
    P00_luG_dhatu_it_context,
    P00_luN_han_sic_6_4_48,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _build_han_luG_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("han"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "han", "karmakatva": "sakarmaka"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "parasmaipada"
    return s


def _enter_tripadi(state: State) -> State:
    from pipelines.subanta import _pada_merge

    s = state
    _pada_merge(s)
    return apply_rule("8.2.1", s)


def derive_avadhIt_han_lun_ekavacana_lesson() -> State:
    s = _build_han_luG_state()

    s = P00_luG_dhatu_it_context(s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s = P00_luN_lakara_cli_sic(s)

    s.meta["2_4_43_han_vadh_luG_arm"] = True
    s = apply_rule("2.4.43", s)
    s.terms[0].tags.discard("upadesha")

    s = apply_rule("6.4.71", s)

    s = P00_parasmai_tin_adesha(s, "tip")
    s = P00_hal_it_lopa(s)

    s.meta["3_4_114_luN_sic_samjna_arm"] = True
    s.meta["7_2_35_allow_sic"] = True
    s.meta["luN_sic_ardhadhatuka"] = True
    s.meta["han_6_4_48_arm"] = True
    s = P00_luN_han_sic_6_4_48(s)
    s.meta.pop("7_2_35_allow_sic", None)
    s.meta.pop("luN_sic_ardhadhatuka", None)

    s = apply_rule("7.2.3", s)
    s.meta["7_2_7_anga_vrddhi_arm"] = True
    s = apply_rule("7.2.7", s)

    s = apply_rule("3.4.100", s)
    s = apply_rule("1.2.41", s)

    s = apply_rule("7.3.96", s)

    s = _enter_tripadi(s)
    s = apply_rule("8.2.28", s)
    s = apply_rule("6.1.101", s)
    return s


__all__ = ["derive_avadhIt_han_lun_ekavacana_lesson"]
