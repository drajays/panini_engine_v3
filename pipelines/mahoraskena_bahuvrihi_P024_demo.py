"""
pipelines/mahoraskena_bahuvrihi_P024_demo.py — P024 (महोरस्केन)

Target SLP1: ``mahoraskena`` — *mahat* + *uras* bahuvrīhi with **5.4.151** *kap*,
then **6.3.46** / **6.1.101** / **6.1.87** to ``mahoraska``, then standard *subanta*
*tṛtīyā-ekavacana* via ``derive_from_state`` (reuses ``pipelines/subanta`` spine).

JSON spine (compressed):
  **1.1.68** → **2.2.24** → **5.4.151** → **1.2.46** (structural samāsa merge) →
  **1.1.52** + **6.3.46** + **6.1.101** + guṇa readiness + **6.1.87** →
  ``derive_from_state(..., 3, 1)`` → **1.1.56** + **1.1.68** (siddhi frame).

Note: JSON’s **6.1.101** at *ā*+*u* is modeled here as **6.1.87** *ād guṇaḥ*
(``A`` + ``u`` → ``o``), after **6.3.46** + **6.1.101** fix *mahat* → *mahā* shape
(``a`` + ``A`` → ``A``) as in ``pipelines/maharsi_mahAt_fzi.py``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P00_guna_prayoga_readiness
from pipelines.subanta import derive_from_state


def derive_mahoraskena_bahuvrihi_P024() -> State:
    mahat = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("mahat")),
        tags={"anga", "samasa_member", "bahuvrIhi"},
        meta={"upadesha_slp1": "mahat"},
    )
    uras = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("uras")),
        tags={"anga", "samasa_member", "bahuvrIhi"},
        meta={"upadesha_slp1": "uras"},
    )
    s = State(terms=[mahat, uras], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)

    s.meta["P024_2_2_24_arm"] = True
    s = apply_rule("2.2.24", s)

    s.meta["P024_5_4_151_kap_arm"] = True
    s = apply_rule("5.4.151", s)

    s = apply_rule("1.2.46", s)

    s = apply_rule("1.1.52", s)
    s.meta["6_3_46_An_mahat_arm"] = True
    s = apply_rule("6.3.46", s)
    s = apply_rule("6.1.101", s)
    s = P00_guna_prayoga_readiness(s)
    s = apply_rule("6.1.87", s)

    s = derive_from_state(s, 3, 1)

    s = apply_rule("1.1.56", s)
    s.meta.pop("1_1_68_svadrupa_audit_done", None)
    s = apply_rule("1.1.68", s)
    return s


__all__ = ["derive_mahoraskena_bahuvrihi_P024"]
