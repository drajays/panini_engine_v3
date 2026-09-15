"""
6.2.165  संज्ञायां मित्राजिनयोः  —  VIDHI

Padaccheda: संज्ञायाम् मित्र-अजिनयोः

संज्ञायां मित्राजिनयोः (6.2.165)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_165_saMjYAyAM_165"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.165", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.165"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.165",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM mitrAjinayoH",
    text_dev              = "संज्ञायां मित्राजिनयोः",
    padaccheda_dev        = "संज्ञायाम् मित्र-अजिनयोः",
    why_dev               = "(सूत्रम् 6.2.165) संज्ञायां मित्राजिनयोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
