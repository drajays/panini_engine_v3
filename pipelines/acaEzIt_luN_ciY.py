"""
pipelines/acaEzIt_luN_ciY.py — अचैषीत् (ciY, luṅ, 3sg parasmaipada) glass-box.

This is a one-form, rule-based pipeline matching the user's note
`/Users/dr.ajayshukla/Documents/my panini notes/अचैषीत्.md`.

Target SLP1: **acaEzIt** (अचैषीत्).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from phonology.pratyahara import is_ekac_upadesha

from core.canonical_pipelines import (
    P00_vrddhi_prayoga_readiness,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_dhatu_upadesha_it_lopa,
    P00_luN_lakara_cli_sic,
    P00_tip_to_t_aprkta,
)


def _build_ciY_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ciY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ciY", "karmakatva": "sakarmaka"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    # luṅ, parasmaipada, 1st person? actually 3sg: tip.
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "parasmaipada"
    return s


def _enter_tripadi_and_finish(state: State) -> State:
    from pipelines.subanta import _pada_merge
    s = state
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)  # satva in tripadi
    return s


def derive_acaEzIt() -> State:
    s = _build_ciY_state()

    # Dhātu it-prakaraṇa (as per note: 1.3.1 then it/lopa chain).
    s = P00_dhatu_upadesha_it_lopa(s)
    # Compute ekāc/udātta flags from the *current* dhātu tape (post-it-lopa), so
    # 7.2.10 can gate iṭ without hardcoded pipeline truth values.
    s.meta["ekac_dhatu"] = is_ekac_upadesha(s.flat_slp1())
    s.meta.setdefault("udatta_dhatu", False)

    # Pratyaya adhikāra (3.1.91 + 3.1.1–3)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    # Lakāra + cli/sic + tip→t (canonical luṅ spine)
    s = P00_luN_lakara_cli_sic(s)
    s = P00_tip_to_t_aprkta(s)

    # aṭ augment
    s = apply_rule("6.4.71", s)

    # Īṭ augment between sic and apṛkta t
    s = apply_rule("7.3.96", s)

    # Vṛddhi of dhātu vowel i→ai (7.2.1)
    s = P00_vrddhi_prayoga_readiness(s)
    s = apply_rule("7.2.1", s)

    # Enter tripadi and apply ṣatva (8.3.59)
    s = _enter_tripadi_and_finish(s)
    return s


__all__ = ["derive_acaEzIt"]

