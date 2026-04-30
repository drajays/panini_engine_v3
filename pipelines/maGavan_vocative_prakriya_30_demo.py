"""
pipelines/maGavan_vocative_prakriya_30_demo.py — ``prakriya_30`` (*maghavan* vocative accent).

From ``…/separated_prakriyas/prakriya_30_*.json`` (``ordered_sutra_sequence`` includes **8.1.16**;
``panini_engine_pipeline`` rows: **2.3.48**, **8.1.16**/*padasya*, **8.1.18**, **8.1.19**).

Affixation (**4.1.2**), **2.3.47**/**2.3.49**, and **6.1.68** *su*-lopa are not in this narrow slice;
flat tape is ``maGavan`` (``upadesha_slp1``) throughout.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_maGavan_Amant_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("maGavan")),
        tags={"anga", "prātipadika", "sambuddhi_prayoga"},
        meta={"upadesha_slp1": "maGavan"},
    )


def derive_maGavan_vocative_prakriya_30() -> State:
    s = State(terms=[_mk_maGavan_Amant_demo()], meta={}, trace=[])

    s.meta["prakriya_30_2_3_48_arm"] = True
    s = apply_rule("2.3.48", s)

    s = apply_rule("8.1.16", s)
    s = apply_rule("8.1.18", s)

    s.meta["prakriya_30_8_1_19_arm"] = True
    s = apply_rule("8.1.19", s)
    return s


__all__ = ["derive_maGavan_vocative_prakriya_30", "_mk_maGavan_Amant_demo"]
