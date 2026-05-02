"""
3.2.91  अग्नौ चे  —  VIDHI (narrow: **P041** *agnicit* *upapada* frame)

*Śāstra (laghu):* in the *agni*-*upapada* context with *√ci* + *kvip* (*agnicid*),
**3.2.91** *agnau ce* is cited in the JSON spine as licensing the *kṛt* frame
(alongside **3.2.76** *kvip ca*).

Engine: recipe-only audit — no phoneme rewrite; registers
``samjna_registry['3.2.91_agnau_ce_P041']`` when ``state.meta['P041_3_2_91_arm']``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _witness(state: State) -> bool:
    if not state.meta.get("P041_3_2_91_arm"):
        return False
    has_agni = any((t.meta.get("upadesha_slp1") or "").strip() == "agni" for t in state.terms)
    has_ci = any(
        "dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "ci"
        for t in state.terms
    )
    has_kvip = any((t.meta.get("upadesha_slp1") or "").strip() == "kvip" for t in state.terms)
    return has_agni and has_ci and has_kvip


def cond(state: State) -> bool:
    return _witness(state)


def act(state: State) -> State:
    if not _witness(state):
        return state
    state.samjna_registry["3.2.91_agnau_ce_P041"] = True
    state.meta.pop("P041_3_2_91_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.91",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "agnO ce (narrow P041)",
    text_dev       = "अग्नौ चे — P041 संक्षेपः",
    padaccheda_dev = "अग्नौ / चे",
    why_dev        = "अग्नि-उपपद-प्रसङ्गे च-आर्थे क्विप्-उपसंहारः (३.२.९१) — P041।",
    anuvritti_from = ("3.2.84",),
    cond           = cond,
    act            = act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
