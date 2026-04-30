"""
3.4.101  तस्थस्थमिपां तांतंतामः  —  VIDHI (narrow: *tas* → *tām* in *laṅ*)

**Padaccheda (teaching):** *tasthasthamipām* (the tiṅ items *tas*, *thas*, *tha*, *mip*)
→ *tāṃtaṃtāmaḥ* (*tām*, *tām*, *ta*, *mi*) in the *lakāra*s listed in the full sūtra.

**Engine (narrow v3):** after **3.4.78** has replaced *lac* by *tas*, and the recipe has
``state.meta['lakara'] == 'laG'``, rewrite the *tas* pratyaya tape to **tAm** (SLP1).

Broader *thas* / *tha* / *mip* and other *lakāra*s are intentionally out of scope until
their demo recipes need them (CONSTITUTION — no speculative bundles).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_tas_index(state: State) -> int | None:
    if (state.meta.get("lakara") or "").strip() != "laG":
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "tas":
            continue
        if t.meta.get("3_4_101_tastha_done"):
            continue
        if "".join(v.slp1 for v in t.varnas) == "tas":
            return i
    return None


def cond(state: State) -> bool:
    return _find_tas_index(state) is not None


def act(state: State) -> State:
    idx = _find_tas_index(state)
    if idx is None:
        return state
    t = state.terms[idx]
    t.varnas = list(parse_slp1_upadesha_sequence("tAm"))
    t.meta["upadesha_slp1"] = "tAm"
    t.meta["3_4_101_tastha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.101",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tasthasthamipAM tAMtaMtAmaH",
    text_dev       = "तस्थस्थमिपां तांतंतामः",
    padaccheda_dev = "तस्थस्थमिपाम् / तांतंतामः",
    why_dev        = "लङादौ तस्-आदेशस्य स्थाने ताम् (द्विवचन-प्रथम-परस्मैपद) ।",
    anuvritti_from = ("3.4.78",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
