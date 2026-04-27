"""
pipelines/marImfja_prathamA_mFjU.py — मरीमृजः (*mṛj* + *yaṅ* + *ac*, prathamā).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/मरीमृज.md``

Target SLP1: **marImfjaH** (मरीमृजः), agent noun “one who cleans repeatedly”.

Upadeśa uses ``mfjU~z`` (short ṛ ``f``) so the stem surfaces with ``mfj``, not ``mFj``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_bhuvadi_dhatu_it_anunasik_hal,
    P00_subanta_prathama_su_tripadi_visarga,
    P00_yang_ac_three_term_frame,
    P00_yang_adhikara_yaG_append_sanadi,
    P00_yang_dvitva_abhyasa_gate,
    P00_yang_luk_2_4_74_and_1_1_4,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mfjU~z"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "mfjU~z"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_marImfjaH() -> State:
    s = _build_state()

    s = P00_bhuvadi_dhatu_it_anunasik_hal(s)
    s = P00_yang_adhikara_yaG_append_sanadi(s)
    s = P00_yang_dvitva_abhyasa_gate(s)

    s.meta["7_4_66_urat_abhyasa_arm"] = True
    s = apply_rule("7.4.66", s)
    s = apply_rule("1.1.51", s)
    s.terms[0].meta["7_4_60_first_hal_only"] = True
    s = apply_rule("7.4.60", s)
    s.meta["7_4_90_rIk_arm"] = True
    s = apply_rule("7.4.90", s)

    s = P00_yang_ac_three_term_frame(s)
    s = P00_yang_luk_2_4_74_and_1_1_4(s)
    s = apply_rule("7.2.114", s)
    s = apply_rule("7.3.84", s)
    s = P00_subanta_prathama_su_tripadi_visarga(s)
    return s


__all__ = ["derive_marImfjaH"]
