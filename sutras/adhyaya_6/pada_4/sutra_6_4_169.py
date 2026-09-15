"""
6.4.169  आत्माध्वानौ खे  —  VIDHI

Padaccheda: आत्म-अध्वानौ खे

आत्माध्वानौ खे (6.4.169)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_169_AtmADvAnO_169"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.169", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.169"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.169",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmADvAnO Ke",
    text_dev              = "आत्माध्वानौ खे",
    padaccheda_dev        = "आत्म-अध्वानौ खे",
    why_dev               = "(सूत्रम् 6.4.169) आत्माध्वानौ खे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
