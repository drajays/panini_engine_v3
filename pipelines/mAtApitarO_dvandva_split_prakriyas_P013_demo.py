"""
pipelines/mAtApitarO_dvandva_split_prakriyas_P013_demo.py — **P013** (**मातापितरौ**).

Source: ``…/my_scripts/final/split_prakriyas_11/P013.json``.

The JSON spine mixes ordering notes and placeholders; the operational goal is
the well-known dvandva output **mAtApitarO**.  This recipe keeps the process
rule-based by:
  - stamping dvandva intention (**2.2.29**) and ordering note (**2.2.34**) as
    narrow registry steps,
  - using a narrow special-base step (**6.3.25**) to form ``mAtApitar`` from
    ``mAtf`` + ``pitf``,
  - attaching nominative-dual ``O`` via **4.1.2**, and recording JSON's **6.1.93**
    placeholder as an anuvāda audit.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _member(stem: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(stem)),
        tags={"anga", "prātipadika", "samasa_member", "prakriya_P013_mAtApitarO_demo"},
        meta={"upadesha_slp1": stem},
    )


def derive_mAtApitarO_dvandva_split_prakriyas_P013() -> State:
    t1 = _member("mAtf")
    t2 = _member("pitf")
    s = State(terms=[t1, t2], meta={}, trace=[])

    s = apply_rule("2.1.3", s)
    s.meta["prakriya_P013_2_2_29_arm"] = True
    s = apply_rule("2.2.29", s)
    s.meta["prakriya_P013_2_2_34_arm"] = True
    s = apply_rule("2.2.34", s)

    s.meta["prakriya_P013_6_3_25_arm"] = True
    s = apply_rule("6.3.25", s)

    # Attach prathamā-dvivacana (O).
    s.meta["vibhakti_vacana"] = "1-2"
    s = apply_rule("4.1.2", s)

    # JSON placeholder (no mutation in this demo slice).
    s.meta["prakriya_P013_6_1_93_arm"] = True
    s = apply_rule("6.1.93", s)
    return s


__all__ = ["derive_mAtApitarO_dvandva_split_prakriyas_P013"]

