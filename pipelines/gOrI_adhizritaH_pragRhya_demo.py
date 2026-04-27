"""
pipelines/gOrI_adhizritaH_pragRhya_demo.py — *गौरी अधिश्रितः* & *मामकी इति* / *तनू इति*.

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/गौरी अधिश्रितः.md``.

Vedic **7.1.39** *sup* *luk* leaves *gau*…*ī*, *māmakī*, *tanū* looking like *prathamā* shapes while
the *artha* is *saptamī* (locative). **1.1.19** *Īdūtau ca saptamyarthe* extends *pragṛhya*;
with ``SAPTAMYARTHA_PRAGHYA_TAG_ARM_META`` the engine stamps ``pragrahya`` on *ī*/*ū*-final
*anga*/*prātipadika* **Term**s so **6.1.125** blocks **6.1.77** (*iko yaṇ aci*) before *ac*
(*adhiśritaḥ*, *iti*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_19 import SAPTAMYARTHA_PRAGHYA_TAG_ARM_META


def _bootstrap_1_1_11_and_1_1_19_registry(s: State) -> State:
    s = apply_rule("1.1.11", s)
    s = apply_rule("1.1.19", s)
    return s


def _stamp_saptamyartha_pragrahya_tags(s: State) -> State:
    s.meta[SAPTAMYARTHA_PRAGHYA_TAG_ARM_META] = True
    return apply_rule("1.1.19", s)


def _block_yan_after_pragrahya(s: State) -> State:
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.77", s)
    return s


def derive_gOrI_aDiSritaH_pragrahya() -> State:
    """*gau*…*ī* + *adhiśritaḥ* — no *ī*+*a*→*y* at the *pada* boundary."""
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("gOrI"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "gOrI"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("aDiSritaH"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "aDiSritaH"},
    )
    s = State(terms=[left, right], meta={}, trace=[])
    s = _bootstrap_1_1_11_and_1_1_19_registry(s)
    s = _stamp_saptamyartha_pragrahya_tags(s)
    return _block_yan_after_pragrahya(s)


def derive_mAmakI_iti_pragrahya() -> State:
    """*padapāṭha* slice: *māmakī* + *iti*."""
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mAmakI"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "mAmakI"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "iti"},
    )
    s = State(terms=[left, right], meta={}, trace=[])
    s = _bootstrap_1_1_11_and_1_1_19_registry(s)
    s = _stamp_saptamyartha_pragrahya_tags(s)
    return _block_yan_after_pragrahya(s)


def derive_tanU_iti_pragrahya() -> State:
    """*padapāṭha* slice: *tanū* + *iti*."""
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("tanU"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "tanU"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "iti"},
    )
    s = State(terms=[left, right], meta={}, trace=[])
    s = _bootstrap_1_1_11_and_1_1_19_registry(s)
    s = _stamp_saptamyartha_pragrahya_tags(s)
    return _block_yan_after_pragrahya(s)


__all__ = [
    "derive_gOrI_aDiSritaH_pragrahya",
    "derive_mAmakI_iti_pragrahya",
    "derive_tanU_iti_pragrahya",
]
