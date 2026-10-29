"""
5.3.74  कुत्सिते  —  VIDHI

Padaccheda: कुत्सिते

कुत्सिते (5.3.74)
Pāṭha: ashtadhyayi.com data.txt row i=53074 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_74_kutsite_74"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.74", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.74"
    return state


from engine.taddhita_attach import open_sense, open_default_frame


def _new_cond(state: State) -> bool:
    return open_sense(state, "5.3.74", "kutsita")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    return open_default_frame(state, "5.3.74", "kutsita", "5.3.70", "5.3.95")


SUTRA = SutraRecord(
    sutra_id              = "5.3.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kutsite",
    text_dev              = "कुत्सिते",
    samagra_slp1          = "kutsite prAtipadikAt tiNaH ca kaH",
    samagra_dev           = "कुत्सिते प्रातिपदिकात् तिङः च कः",
    padaccheda_dev        = "कुत्सिते",
    why_dev               = "(सूत्रम् 5.3.74) कुत्सिते।",
    anuvritti_from        = ('5.3.70',),
    also_vidhi     = True,          # the loop opens this sense-frame from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
