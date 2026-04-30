"""
pipelines/godau_prakriya_46_demo.py — ``prakriya_46`` (**गोदौ ग्रामः** spine fragment).

Source: ``…/separated_prakriyas/prakriya_46_2026-04-29_14_22_39.json``.

JSON ``ordered_sutra_sequence`` is empty (*scholarly_pass_confidence: low*). The commentary centres on
**4.2.70** *adūrabhavaś ca* (*aṇ*), **4.2.82** *varaṇādibhyaś ca* (*luk* of that *aṇ* — ashtadhyayi-com
**i=42082**; OCR/vyākhyā sometimes mislabels this as “**4.2.81**”), then **1.2.51** *lupi yuktavad…*
(dual **गोदौ** retained after *luk*). **6.1.88** *vṛddhi* / full *sup* declension are out of scope here.

Witness ``goda`` stands in for the stem before *taddhita* + *luk* (full *prakriyā* elsewhere).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_goda_prakriya_46() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("goda")),
        tags={"anga", "prātipadika", "prakriya_46_godau_demo"},
        meta={"upadesha_slp1": "goda"},
    )


def derive_godau_prakriya_46() -> State:
    s = State(terms=[_witness_goda_prakriya_46()], meta={}, trace=[])

    s = apply_rule("4.1.76", s)

    s.meta["prakriya_46_adUrabhava_aR_note"] = True
    s.meta["prakriya_46_4_2_70_arm"] = True
    s = apply_rule("4.2.70", s)

    s.meta["prakriya_46_varaNAdi_luk_note"] = True
    s.meta["prakriya_46_4_2_82_arm"] = True
    s = apply_rule("4.2.82", s)

    s.meta["prakriya_46_lupi_yuktavad_note"] = True
    s.meta["prakriya_46_varaNAdi_luk_context_note"] = True
    s.meta["prakriya_46_1_2_51_arm"] = True
    s = apply_rule("1.2.51", s)
    return s


__all__ = ["derive_godau_prakriya_46", "_witness_goda_prakriya_46"]
