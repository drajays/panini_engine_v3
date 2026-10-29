"""
5.3.86  ह्रस्वे  —  VIDHI

Padaccheda: ह्रस्वे

ह्रस्वे (5.3.86)
Pāṭha: ashtadhyayi.com data.txt row i=53086 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_86_hrasve_86"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.86", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.86"
    return state


from engine.taddhita_attach import open_sense, open_default_frame


def _new_cond(state: State) -> bool:
    return open_sense(state, "5.3.86", "hrasva")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    return open_default_frame(state, "5.3.86", "hrasva", "5.3.70", "5.3.95")


SUTRA = SutraRecord(
    sutra_id              = "5.3.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hrasve",
    text_dev              = "ह्रस्वे",
    samagra_slp1          = "hrasve prAtipadikAt kaH",
    samagra_dev           = "ह्रस्वे प्रातिपदिकात् कः",
    padaccheda_dev        = "ह्रस्वे",
    why_dev               = "(सूत्रम् 5.3.86) ह्रस्वे।",
    anuvritti_from        = ('5.3.70',),
    also_vidhi     = True,          # the loop opens this sense-frame from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
