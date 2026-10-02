"""
7.3.105  आङि चापः  —  VIDHI

Padaccheda: आङि च आपः

An āp-final aṅga (feminine ā-stem) takes e for its final ā before ṭā (āṅ): इदा/अन् + आ → अने + आ, whence
6.1.78 → अनया, एनया. (os is handled by the same sūtra in the tradition; the engine's existing os path is unchanged.)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 7.3.105 (padaccheda: आङि च आपः)
  Source #2 — ashtadhyayi.com śabda-prakriyā for इदम् strī 3-1: अन्+आ+आ [7.2.112] | अन्+ए+आ [7.3.105] | अनया [6.1.78]

Engine: reads Term tags and the sup's identity only (ṭā, by upadeśa) — the feminine ā-stem is the aṅga that 4.1.4 marked
``TAp_anta``; the sarvanāma ā-stem keeps ṭā because 7.1.12's strī branch stands down for it.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _site(state: State):
    if len(state.terms) < 2:
        return None
    anga, sup = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "TAp_anta" not in anga.tags or "sarvanama" not in anga.tags:
        return None
    if "sup" not in sup.tags or (sup.meta.get("upadesha_slp1") or "").strip() != "wA":
        return None
    if anga.meta.get("7_3_105_done") or not anga.varnas or anga.varnas[-1].slp1 != "A":
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    if anga is not None:
        anga.varnas[-1] = mk("e")
        anga.meta["7_3_105_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.105",
    sutra_type=SutraType.VIDHI,
    text_slp1="ANi cApaH",
    text_dev="आङि चापः",
    padaccheda_dev="आङि च आपः",
    why_dev="आप्-अन्त अङ्ग के अन्त्य आ को ए, आङ् (टा) परे — अनेया → अनया (६.१.७८)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
