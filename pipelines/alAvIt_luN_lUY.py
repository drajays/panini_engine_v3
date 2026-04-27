"""
pipelines/alAvIt_luN_lUY.py — अलावीत् (lUY, luṅ, 3sg parasmaipada) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/अलावीत्.md`.

Target SLP1: **alAvIt** (अलावीत्).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_vrddhi_prayoga_readiness,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_it_halantyam_lopa_yathasankhyam,
    P00_dhatu_upadesha_it_lopa,
    P00_luN_lakara_cli_sic,
    P00_tip_to_t_aprkta,
)


def _build_lUY_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("lUY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "lUY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "parasmaipada"
    # Needed for iṭ-block plumbing (7.2.10) even if not invoked here.
    s.meta["ekac_dhatu"] = True
    s.meta["udatta_dhatu"] = True
    return s


def _enter_tripadi(state: State) -> State:
    from pipelines.subanta import _pada_merge

    s = state
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    return s


def derive_alAvIt() -> State:
    s = _build_lUY_state()

    # Dhātu saṃjñā + it/lopa (ञ्)
    s = P00_dhatu_upadesha_it_lopa(s)

    # Pratyaya adhikāra (3.1.91 + 3.1.1–3)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    # Lakāra + cli/sic + tip→t (canonical luṅ spine)
    s = P00_luN_lakara_cli_sic(s)
    s = P00_tip_to_t_aprkta(s)

    # aṭ augment (a + ...)
    s.meta["aT_agama_6_4_71"] = True
    s = apply_rule("6.4.71", s)

    # iṭ augment on sic (opt-in branch of 7.2.35)
    s.meta["7_2_35_allow_sic"] = True
    s.meta["luN_sic_ardhadhatuka"] = True
    s = apply_rule("7.2.35", s)

    # Īṭ augment between sic and apṛkta t
    s = apply_rule("7.3.96", s)

    # Vṛddhi of dhātu vowel ū → au (7.2.1), skipping aṭ-āgama's 'a'
    s = P00_vrddhi_prayoga_readiness(s)
    s = apply_rule("7.2.1", s)

    # au + i → āv + i (echoyavāyāvaḥ), before entering tripāḍī
    s = apply_rule("6.1.78", s)
    s = apply_rule("1.3.10", s)

    # Enter tripāḍī and delete sic 's' after iṭ (8.2.28)
    s = _enter_tripadi(s)
    s = apply_rule("8.2.28", s)

    return s


__all__ = ["derive_alAvIt"]

