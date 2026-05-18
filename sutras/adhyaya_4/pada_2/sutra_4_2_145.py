"""
4.2.145  कृकणपर्णाद्भारद्वाजे  —  VIDHI

Padaccheda: कृकण-पर्णात् भारद्वाजे

कृकणपर्णाद्भारद्वाजे (4.2.145)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_145_kfkaRaparR_145"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_145_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfkaRaparRAdBAradvAje",
    text_dev              = "कृकणपर्णाद्भारद्वाजे",
    padaccheda_dev        = "कृकण-पर्णात् भारद्वाजे",
    why_dev               = "(सूत्रम् 4.2.145) कृकणपर्णाद्भारद्वाजे।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
