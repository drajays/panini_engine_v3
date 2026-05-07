"""
4.3.92  शण्डिकादिभ्यो ञ्यः  —  VIDHI (narrow **corrected-v2 P004-B**)

*Śāstra:* from **śaṇḍikādi** stems in *tatra bhavaḥ*, the taddhita **ṇya** (*ñya*,
machine ``Yya``) is appended after the internal *śabda-linguistic* *su* host.

Engine: recipe arms ``corrected_v2_P004_B_4_3_92_arm`` + stem witness ``SaRqika``
(शण्डिक — explicit ``a`` after श्/ण्); inserts ``Yya`` after the live internal **su**.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM = "corrected_v2_P004_B_4_3_92_arm"
_STEM_UPA = "SaRqika"
_AFFIX_UPA = "Yya"


def _stem_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "anga" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != _STEM_UPA:
            continue
        return i
    return None


def _live_sup_after_stem(state: State, stem_i: int) -> int | None:
    j = stem_i + 1
    if j >= len(state.terms):
        return None
    pr = state.terms[j]
    if term_is_sup_luk_ghost(pr):
        return None
    if "sup" not in pr.tags:
        return None
    return j


def _has_Yya(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == _AFFIX_UPA for t in state.terms)


def cond(state: State) -> bool:
    if not state.meta.get(META_ARM):
        return False
    si = _stem_index(state)
    if si is None:
        return False
    if _live_sup_after_stem(state, si) is None:
        return False
    return not _has_Yya(state)


def act(state: State) -> State:
    if not cond(state):
        return state
    si = _stem_index(state)
    if si is None:
        return state
    sj = _live_sup_after_stem(state, si)
    if sj is None:
        return state
    affix = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(_AFFIX_UPA)),
        tags={"pratyaya", "upadesha", "taddhita"},
        meta={"upadesha_slp1": _AFFIX_UPA},
    )
    state.terms.insert(sj + 1, affix)
    state.meta.pop(META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="4.3.92",
    sutra_type=SutraType.VIDHI,
    text_slp1="SaRqikAdibhyaH YyaH",
    text_dev="शण्डिकादिभ्यो ञ्यः",
    padaccheda_dev="शण्डिकादिभ्यः / ञ्यः",
    why_dev="शण्डिकादि-प्रातिपदिकेभ्यः तत्रभव-अर्थे ञ्य-तद्धितः (प००४-ब आर्म्)।",
    anuvritti_from=("4.3.53",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
