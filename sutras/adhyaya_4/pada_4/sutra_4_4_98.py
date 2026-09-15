"""
4.4.98  तत्र साधुः  —  VIDHI (narrow)

**Pāṭha:** *tatra sādhuḥ* — the **yat** *taddhita* after a locative *ṅi* in the
sense “skilled therein” (``prakriya_18`` / *sāmasu sādhuḥ* → *sāmanyaḥ*).

Narrow v3:
  • ``cond`` — ``state.meta['prakriya_18_4_4_98_arm']``; exactly two ``Term``s:
    *aṅga* ``sAman`` + ``Ni`` *sup* (``upadesha_slp1`` ``Ni``).
  • ``act`` — append ``yat`` *taddhita* ``Term`` (``y`` ``a`` ``t``); clear the arm.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 44098 · तत्र साधुः
              padaccheda: तत्र साधुः
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः | 44075: यत्
  Source #2 — Kāśikā 4.4.98 udāharaṇa:
                सामसु साधुः सामन्यः
                वेमन्यः
                कर्मण्यः
  Cross-check — surface pinned by: tests/unit/test_prakriya_sAmanyas_taddhita.py
  Reference record: sutra_ref_out/4_4_98.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _eligible(state: State) -> bool:
    if not state.meta.get("prakriya_18_4_4_98_arm"):
        return False
    if len(state.terms) != 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if "anga" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != "sAman":
        return False
    if "sup" not in t1.tags or "pratyaya" not in t1.tags:
        return False
    if (t1.meta.get("upadesha_slp1") or "").strip() != "Ni":
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    yat = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("yat")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "yat"},
    )
    state.terms.append(yat)
    state.meta.pop("prakriya_18_4_4_98_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.4.98",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tatra sAdhuH",
    text_dev       = "तत्र साधुः",
    padaccheda_dev = "तत्र साधुः",
    why_dev        = "तत्रार्थे साधौ यत्-प्रत्ययः (सामसु साधुः → सामन्यः)।",
    anuvritti_from = ("4.4.75",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
