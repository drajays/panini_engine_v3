"""
4.4.86  वशं गतः  —  VIDHI

Padaccheda: वशम् गतः

वशं गतः (4.4.86)
Pāṭha: ashtadhyayi.com data.txt row i=44086 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_86_vaSaM_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.86", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vaSaM gataH",
    text_dev              = "वशं गतः",
    samagra_slp1          = "tat vaSaM gataH iti samarTAnAm praTamAt paraH yat pratyayaH",
    samagra_dev           = "'तत् वशं गतः' (इति) समर्थानाम् प्रथमात् परः यत् प्रत्ययः",
    padaccheda_dev        = "वशम् गतः",
    why_dev               = "(सूत्रम् 4.4.86) वशं गतः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
