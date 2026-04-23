"""
pipelines/devendra.py — guided derivation demos from `devendra.md`.

This pipeline is intentionally narrow: it demonstrates the canonical
examples from the notes:

- deva + indra  → devendraḥ
- sUrya + udaya → sUryodayaḥ
"""
from __future__ import annotations

from dataclasses import dataclass

import sutras  # noqa: F401  (fill registry)

from engine       import apply_rule
from engine.state import State, Term
from phonology    import mk
from phonology.varna import AC_DEV, HAL_DEV

from pipelines.subanta import derive_akarant_pullinga


def _varnas_from_slp1(slp1: str) -> list:
    varnas: list = []
    i = 0
    while i < len(slp1):
        ch = slp1[i]
        if ch in HAL_DEV or ch in AC_DEV:
            varnas.append(mk(ch))
        i += 1
    return varnas


def _structural_step(state: State, sid: str, label: str, why_dev: str) -> None:
    state.trace.append({
        "sutra_id"    : sid,
        "sutra_type"  : "STRUCTURAL",
        "type_label"  : label,
        "form_before" : state.flat_slp1(),
        "form_after"  : state.flat_slp1(),
        "why_dev"     : why_dev,
        "status"      : "APPLIED",
    })


def _merge_terms_as_pratipadika(state: State) -> None:
    if not state.terms:
        return
    all_varnas: list = []
    for t in state.terms:
        all_varnas.extend(t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": state.flat_slp1()},
    )
    state.terms = [merged]
    _structural_step(
        state,
        sid="__SAMASA_MERGE__",
        label="समास-एकीकरणम्",
        why_dev="दो पदों को एक प्रातिपदिक-आधार (अङ्ग) मानकर एक-Term में मर्ज किया।",
    )


@dataclass(frozen=True)
class DemoCase:
    first: str
    second: str
    expected_stem: str


DEVENDRA = DemoCase(first="deva", second="indra", expected_stem="devendra")
SURYODAYA = DemoCase(first="sUrya", second="udaya", expected_stem="sUryodaya")


def derive_demo(case: DemoCase) -> State:
    # Phase 0: initial two-term state.
    t1 = Term(kind="prakriti", varnas=_varnas_from_slp1(case.first), tags={"prātipadika"}, meta={})
    t2 = Term(kind="prakriti", varnas=_varnas_from_slp1(case.second), tags={"prātipadika"}, meta={})
    s = State(terms=[t1, t2])
    _structural_step(
        s,
        sid="__INPUT__",
        label="इनपुट",
        why_dev=f"प्रातिपदिक-द्वय: {case.first} + {case.second}",
    )

    # Phase 2 (from notes): guṇa sandhi must delegate selection to 1.1.50.
    s = apply_rule("1.1.2", s)    # guṇa-saṃjñā (availability)
    s = apply_rule("1.1.50", s)   # sthāne'ntaratamaḥ gate (provides guna map)
    s = apply_rule("6.1.87", s)   # āt guṇaḥ: a+i → e; a+u → o

    _merge_terms_as_pratipadika(s)

    # Phase 3-5: subanta (prathamā-ekavacana) + tripāḍī visarga.
    stem = s.render()
    # Re-run full subanta recipe on the compound stem (narrow demo).
    s2 = derive_akarant_pullinga(stem, vibhakti=1, vacana=1)
    # Stitch traces (keep s2 state object; prepend s trace for UI).
    s2.trace = s.trace + s2.trace
    return s2


def derive_devendraH() -> State:
    return derive_demo(DEVENDRA)


def derive_sUryodayaH() -> State:
    return derive_demo(SURYODAYA)

