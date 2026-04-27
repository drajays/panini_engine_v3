"""
pipelines/devendra.py — guided derivation demos from `devendra.md`.

This pipeline is intentionally narrow: it demonstrates the canonical
examples from the notes:

- deva + indra  → devendraḥ
- sUrya + udaya → sUryodayaḥ
"""
from __future__ import annotations

import sutras  # noqa: F401  (fill registry)

from engine       import apply_rule
from engine.state import State, Term
from phonology    import mk
from phonology.varna import AC_DEV, HAL_DEV

from core.canonical_pipelines import (
    P00_guna_prayoga_readiness,
    P00_tripadi_rutva_visarga,
    sup_attach_it_chain,
)
from pipelines.subanta import _pada_merge


def _varnas_from_slp1(slp1: str) -> list:
    varnas: list = []
    i = 0
    while i < len(slp1):
        ch = slp1[i]
        if ch in HAL_DEV or ch in AC_DEV:
            varnas.append(mk(ch))
        i += 1
    return varnas


class DemoCase:
    def __init__(self, first: str, second: str, expected_stem: str):
        self.first = first
        self.second = second
        self.expected_stem = expected_stem


DEVENDRA = DemoCase(first="deva", second="indra", expected_stem="devendra")
SURYODAYA = DemoCase(first="sUrya", second="udaya", expected_stem="sUryodaya")


def derive_demo(case: DemoCase) -> State:
    # Phase 0: input as two samāsa-members with their internal sup markers
    # (as in devendra.md). These internal sups are deleted by 2.4.71.
    t1 = Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(case.first),
        tags={"samasa_member"},
        meta={"upadesha_slp1": case.first},
    )
    sup1 = Term(
        kind="pratyaya",
        varnas=[mk("A"), mk("m")],  # "Am" (demo internal sup marker)
        tags={"sup"},
        meta={"upadesha_slp1": "Am"},
    )
    t2 = Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(case.second),
        tags={"samasa_member"},
        meta={"upadesha_slp1": case.second},
    )
    sup2 = Term(
        kind="pratyaya",
        varnas=[mk("s"), mk("u")],  # "su~" simplified to "su" for demo
        tags={"sup"},
        meta={"upadesha_slp1": "su"},
    )
    s = State(terms=[t1, sup1, t2, sup2])

    # Phase 1: samāsa adhikāra metadata (glass-box scope marker).
    s = apply_rule("2.1.3", s)

    # Phase 1b: sup-lopa inside samāsa (removes internal sup terms).
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    # Phase 2: guṇa sandhi (a+i→e, a+u→o) with sthāne'ntaratamaḥ selection.
    s = P00_guna_prayoga_readiness(s)
    s = apply_rule("6.1.87", s)   # ād guṇaḥ

    # Phase 2b: prātipadika-saṃjñā for samāsa and structural merge into one aṅga.
    # *Prātipadika*: **1.2.45** (*avyutpanna*) then **1.2.46** (samāsa branch).
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.2.46", s)

    # Phase 3: subanta prathamā-ekavacana on the compound a-stem.
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("1.4.14", s)
    s = apply_rule("4.1.1",  s)
    s = apply_rule("1.1.2",  s)
    s = apply_rule("6.4.1",  s)
    s = sup_attach_it_chain(s)  # 4.1.2 + 1.3.2–1.3.10 (*it* prakaraṇa)
    s = apply_rule("7.3.102", s)  # a→A before consonant-initial sup

    # Phase 4: pada + tripāḍī visarga.
    _pada_merge(s)                # structural, but traced
    s = P00_tripadi_rutva_visarga(s)
    return s


def derive_devendraH() -> State:
    return derive_demo(DEVENDRA)


def derive_sUryodayaH() -> State:
    return derive_demo(SURYODAYA)

