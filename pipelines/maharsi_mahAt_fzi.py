"""
pipelines/maharsi_mahAt_fzi.py — महर्षिः (mahat + fzi, prathamā-ekavacana) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/महर्षिः.md`.

Target SLP1: **maharziH** (महर्षिः).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_guna_prayoga_readiness,
    P00_attach_su_it_lopa,
    P00_tripadi_rutva_visarga,
)


def _build_state() -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mahat"),
        tags={"anga"},
        meta={"upadesha_slp1": "mahat"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("fzi"),
        tags={"anga"},
        meta={"upadesha_slp1": "fzi"},
    )
    s = State(terms=[left, right], meta={}, trace=[])
    return s


def _enter_tripadi_and_finish(state: State) -> State:
    from pipelines.subanta import _pada_merge

    s = state
    _pada_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


def derive_maharziH() -> State:
    s = _build_state()

    # Samāsa domain open (adhikāra) — for trace alignment.
    s = apply_rule("2.1.3", s)

    # Mark both members as samāsa-members so 1.2.46 can promote/merge.
    for t in s.terms:
        t.tags.add("samasa_member")

    # Prātipadika-saṃjñā for the samāsa community (1.2.46 will structurally merge).
    s = apply_rule("1.2.46", s)

    # 6.3.46 ān-ādeśa for mahat, then a+A → A (6.1.101)
    s.meta["6_3_46_An_mahat_arm"] = True
    s = apply_rule("1.1.52", s)
    s = apply_rule("6.3.46", s)
    s = apply_rule("6.1.101", s)

    # ā + ṛ → ar (6.1.87) + r-paratva (1.1.51)
    s = P00_guna_prayoga_readiness(s)
    s = apply_rule("6.1.87", s)
    s = apply_rule("1.1.51", s)

    # Promote to final prātipadika (so 4.1.2 can attach su), then Tripāḍī r/visarga.
    s.terms[0].tags.add("prātipadika")
    s.terms[0].tags.add("anga")
    s.meta["vibhakti_vacana"] = "1-1"
    s = P00_attach_su_it_lopa(s)
    s = _enter_tripadi_and_finish(s)
    return s


__all__ = ["derive_maharziH"]

