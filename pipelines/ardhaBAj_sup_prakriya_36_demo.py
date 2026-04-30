"""
pipelines/ardhaBAj_sup_prakriya_36_demo.py — ``prakriya_36`` (**अर्धभाज्** + *sup* *apṛkta* **स्**).

From ``…/separated_prakriyas/prakriya_36_*.json`` — ``ordered_sutra_sequence``: **6.1.66**;
``panini_engine_pipeline`` step 9 assigns **हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्** (**6.1.68**),
not **६.१.६६** (same noisy OCR class as ``prakriya_35``).

Narrow slice (glass-box): stem ``ardhaBAj`` + ``su``→``s`` with **1.2.41** *apṛkta*, then **6.1.68**
hal-lopa — matching **8–9** of the commentary table (full **ण्वि**, samāsa, **8.2.30** … omitted).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_ardhaBAj_prAtipadika_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("ardhaBAj")),
        tags={"anga", "prātipadika", "prakriya_36_ardhaBAj_demo"},
        meta={"upadesha_slp1": "ardhaBAj"},
    )


def _mk_sup_s_pratyaya_after_it_lopa() -> Term:
    return Term(
        kind="pratyaya",
        varnas=[mk("s")],
        tags={"pratyaya", "sup"},
        meta={"upadesha_slp1": "s_sup_aprkta"},
    )


def derive_ardhaBAj_sup_prakriya_36() -> State:
    s = State(
        terms=[_mk_ardhaBAj_prAtipadika_demo(), _mk_sup_s_pratyaya_after_it_lopa()],
        meta={},
        trace=[],
    )
    s = apply_rule("1.2.41", s)
    s.meta["prakriya_36_ardhaBAj_sup_lopa_arm"] = True
    s = apply_rule("6.1.68", s)
    return s


__all__ = [
    "derive_ardhaBAj_sup_prakriya_36",
    "_mk_ardhaBAj_prAtipadika_demo",
    "_mk_sup_s_pratyaya_after_it_lopa",
]
