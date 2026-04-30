"""
pipelines/paYcAlAH_prakriya_45_demo.py — ``prakriya_45`` (**पञ्चालाः** *janapada*, spine fragment).

Source: ``…/separated_prakriyas/prakriya_45_2026-04-29_14_22_29.json``.

JSON ``ordered_sutra_sequence`` is empty (*scholarly_pass_confidence: low*). The commentary centres on
**1.2.51** (*लुपि युक्तवद् व्यक्तिवचने*) after **4.2.81** *जनपदे लुप्* style *luk* on *añ* — modelled only via
``meta['prakriya_45_janapade_luk_context_note']`` here.

Witness ``paYcAla`` stands in for the Phase-A stem before *janapada* *taddhita* + *luk* (full *prakriyā*
elsewhere).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_paYcAla_prakriya_45() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("paYcAla")),
        tags={"anga", "prātipadika", "prakriya_45_paYcAla_demo"},
        meta={"upadesha_slp1": "paYcAla"},
    )


def derive_paYcAlAH_prakriya_45() -> State:
    s = State(terms=[_witness_paYcAla_prakriya_45()], meta={}, trace=[])

    s.meta["prakriya_45_lupi_yuktavad_note"] = True
    s.meta["prakriya_45_janapade_luk_context_note"] = True
    s.meta["prakriya_45_1_2_51_arm"] = True
    s = apply_rule("1.2.51", s)
    return s


__all__ = ["derive_paYcAlAH_prakriya_45", "_witness_paYcAla_prakriya_45"]
