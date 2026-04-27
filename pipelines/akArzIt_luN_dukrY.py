"""
pipelines/akArzIt_luN_dukrY.py — अकार्षीत् (DukfY, luṅ, 3sg parasmaipada) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/अकार्षीत् .md`.

Target SLP1: **akArzIt** (अकार्षीत्).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_dhatu_upadesha_it_lopa,
    P00_luN_lakara_cli_sic,
    P00_tip_to_t_aprkta,
    P00_vrddhi_prayoga_readiness,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_upadesha_it_anunasik_hal_lopa,
)


def _build_dukrY_state() -> State:
    # Use a full upadeśa spelling so 1.3.5 (ṇi/ṭu/ḍu it) can see 'qu' (डु).
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("qukfY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "qukfY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "parasmaipada"
    # ekāc + anudātta for 7.2.10 iṭ-block (as per note).
    s.meta["ekac_dhatu"] = True
    s.meta["udatta_dhatu"] = False
    return s


def _enter_tripadi_and_satva(state: State) -> State:
    from pipelines.subanta import _pada_merge

    s = state
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)
    return s


def derive_akArzIt() -> State:
    s = _build_dukrY_state()

    # Dhātu it-prakaraṇa (note explicitly includes 1.3.5 for qu- marker).
    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.5", s)
    s = P00_upadesha_it_anunasik_hal_lopa(s)

    # Pratyaya adhikāra (3.1.91 + 3.1.1–3)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    # luṅ spine: luG + cli→sic + tip→t
    s = P00_luN_lakara_cli_sic(s)
    s = P00_tip_to_t_aprkta(s)

    # aṭ augment
    s.meta["aT_agama_6_4_71"] = True
    s = apply_rule("6.4.71", s)

    # iṭ attempt then block (7.2.10), per note.
    s.meta["7_2_35_allow_sic"] = True
    s.meta["luN_sic_ardhadhatuka"] = True
    s.meta["7_2_10_allow_sic"] = True
    s = apply_rule("7.2.10", s)
    s = apply_rule("7.2.35", s)  # should be blocked

    # vṛddhi on dhātu vowel (ṛ → A, then 1.1.51 appends r)
    s = P00_vrddhi_prayoga_readiness(s)
    s = apply_rule("7.2.1", s)
    s = apply_rule("1.1.51", s)

    # Īṭ augment before apṛkta t
    s = apply_rule("7.3.96", s)
    # i + I → I across sic-Īṭ boundary.
    s = apply_rule("6.1.101", s)

    # Tripāḍī: ṣatva (s → z) after Ī
    s = _enter_tripadi_and_satva(s)
    return s


__all__ = ["derive_akArzIt"]

