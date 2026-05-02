"""
4.1.162  अपत्यं पौत्रप्रभृति गोत्रम्  —  SAMJNA (narrow: **P042**)

*Śāstra (laghu):* *apatya* in the *pautra-prabhṛti* sense with **yañ** is named
*gotra*.

Engine: ``state.meta['P042_4_1_162_arm']`` + ``P042_gArgya_stem`` tag on the stem
``Term`` before *jas* — registers ``samjna_registry['4.1.162_gotra_P042']``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("P042_4_1_162_arm"):
        return False
    return any("P042_gArgya_stem" in t.tags for t in state.terms)


def act(state: State) -> State:
    if not state.meta.get("P042_4_1_162_arm"):
        return state
    state.samjna_registry["4.1.162_gotra_P042"] = True
    state.meta.pop("P042_4_1_162_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.162",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "apatyaM pautraprabhfti gotram (narrow P042)",
    text_dev       = "अपत्यं पौत्रप्रभृति गोत्रम् — P042 संक्षेपः",
    padaccheda_dev = "अपत्यम् / पौत्रप्रभृति / गोत्रम्",
    why_dev        = "यञन्त-अपत्यं गोत्र-संज्ञकम् (४.१.१६२) — P042।",
    anuvritti_from = ("4.1.1",),
    cond           = cond,
    act            = act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
