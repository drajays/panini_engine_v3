"""
8.4.23  वमोर्वा  —  VIDHI

Padaccheda: व-मोः वा

वमोर्वा (8.4.23)
Pāṭha: ashtadhyayi.com data.txt row i=84023 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_23_vamorvA_23"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.23", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vamorvA",
    text_dev              = "वमोर्वा",
    samagra_slp1          = "razAByAm upasargAt hanteH atpUrvasya naH vamoH vA RaH",
    samagra_dev           = "रषाभ्याम्  उपसर्गात् हन्तेः अत्पूर्वस्य  नः वमोः वा णः",
    padaccheda_dev        = "व-मोः वा",
    why_dev               = "(सूत्रम् 8.4.23) वमोर्वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
