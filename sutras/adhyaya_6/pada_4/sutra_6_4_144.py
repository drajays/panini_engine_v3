"""
6.4.144  नस्तद्धिते  —  VIDHI (narrow)

**Pāṭha:** *nas taddhite* — *ṭi* portion of **-an** bases before *taddhita*.

Narrow v3 (``prakriya_18`` audit):
  • Fires only when ``state.meta['prakriya_18_6_4_144_attempt_arm']`` **and**
    **6.4.168** has **not** already registered ``6_4_168_yat_prakritibhava_sAman``
    (so the *sāmanyaḥ* recipe records **COND-FALSE** after **6.4.168** blocks
    *ṭi-lopa*).
  • ``act`` — narrow *lopa* of final ``n`` on ``sAman`` when unblocked (not used
    in the default ``sāmanyaḥ`` trace; kept for symmetry with **6.4.144** text).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _eligible(state: State) -> bool:
    if not state.meta.get("prakriya_18_6_4_144_attempt_arm"):
        return False
    if "6_4_168_yat_prakritibhava_sAman" in state.samjna_registry:
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if (t0.meta.get("upadesha_slp1") or "").strip() != "sAman":
        return False
    if not t0.varnas or t0.varnas[-1].slp1 != "n":
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    t0 = state.terms[0]
    if t0.varnas and t0.varnas[-1].slp1 == "n":
        t0.varnas.pop()
    state.meta["6_4_144_nas_taddhite_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.144",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "nas taddhite",
    text_dev       = "नस्तद्धिते",
    padaccheda_dev = "नः तद्धिते",
    why_dev        = "अन्-ान्ताद् यत्-परे टि-लोपः (प्रकृतिभावेन बाध्यते इति अङ्कनम्)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
