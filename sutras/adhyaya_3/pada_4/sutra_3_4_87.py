"""
3.4.87  सेर्ह्यपिच्च  —  VIDHI (narrow: *loṭ* *sip* → *hi*)

Teaching JSON **P031** step 5: in *loṭ*, *madhyamaika* *sip* is replaced by *hi*
(*apit*).

Narrow v3: ``state.meta['P031_3_4_87_sip_to_hi_arm']`` and a *tiṅ* ``Term`` whose
``upadesha_slp1`` is ``sip`` → rewrite to ``hi``, refresh ``tin_adesha_3_4_78``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find(state: State) -> int | None:
    if not state.meta.get("P031_3_4_87_sip_to_hi_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sip":
            continue
        if t.meta.get("P031_3_4_87_hi_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas = list(parse_slp1_upadesha_sequence("hi"))
    t.meta["upadesha_slp1"] = "hi"
    t.tags.add("tin_adesha_3_4_78")
    t.meta["P031_3_4_87_hi_done"] = True
    state.meta.pop("P031_3_4_87_sip_to_hi_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.87",
    sutra_type=SutraType.VIDHI,
    text_slp1="ser hyapic ca",
    text_dev="सेर्ह्यपिच्च",
    padaccheda_dev="सेः / हि / अपि / च",
    why_dev="लोटि सिप्-स्थाने हि-आदेशः — प०३१।",
    anuvritti_from=("3.4.86",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
