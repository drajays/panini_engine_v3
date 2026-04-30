"""
pipelines/prakriya_35_ordered_demo.py — ``prakriya_35`` (JSON ``ordered_sutra_sequence``).

From ``…/separated_prakriyas/prakriya_35_*.json``:

  ``ordered_sutra_sequence``: **6.1.66**, **1.3.1**, **3.1.62**

The commentary ``panini_engine_pipeline`` discusses **वाक्** *sup* apṛkta-hal-lopa under
**६.१.६८** *halṅyābhyo…* (not **६.१.६६**, which is a neighbour — noisy OCR between **६६**/**६८**).
This repo implements that prayoga via **6.1.68** as ``derive_prakriya_35_vAc_hal_aprkta_sup``.

Tracks:

  #. ``vAc`` + ``s`` *apṛkta*: **1.2.41** · **6.1.68** (stands in for JSON **6.1.66** slot).
  #. ``spfS`` dhātu: **1.3.1** · **3.1.62** (*acḥ karma-kartari* anchor).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_vAc_PR_nom_sg_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vAc")),
        tags={"anga", "prātipadika", "prakriya_35_vAc_sup_demo"},
        meta={"upadesha_slp1": "vAc"},
    )


def _mk_sup_s_pratyaya_after_it_lopa() -> Term:
    return Term(
        kind="pratyaya",
        varnas=[mk("s")],
        tags={"pratyaya", "sup"},
        meta={"upadesha_slp1": "s_sup_aprkta"},
    )


def derive_prakriya_35_vAc_hal_aprkta_sup() -> State:
    s = State(
        terms=[_mk_vAc_PR_nom_sg_demo(), _mk_sup_s_pratyaya_after_it_lopa()],
        meta={},
        trace=[],
    )
    s = apply_rule("1.2.41", s)
    s.meta["prakriya_35_vAc_sup_lopa_arm"] = True
    s = apply_rule("6.1.68", s)
    return s


def _mk_spfSa_dhatu_kvin_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("spfS")),
        tags={"dhatu", "upadesha", "prakriya_35_spfSa_kvin_demo"},
        meta={"upadesha_slp1": "spfS"},
    )


def derive_prakriya_35_spfSa_ac_karmakartari() -> State:
    s = State(terms=[_mk_spfSa_dhatu_kvin_demo()], meta={}, trace=[])

    s.meta["prakriya_35_1_3_1_arm"] = True
    s = apply_rule("1.3.1", s)

    s.meta["prakriya_35_3_1_62_arm"] = True
    s = apply_rule("3.1.62", s)
    return s


__all__ = [
    "derive_prakriya_35_vAc_hal_aprkta_sup",
    "derive_prakriya_35_spfSa_ac_karmakartari",
    "_mk_vAc_PR_nom_sg_demo",
    "_mk_sup_s_pratyaya_after_it_lopa",
    "_mk_spfSa_dhatu_kvin_demo",
]
