"""
4.3.111  कर्मन्दकृशाश्वादिनिः  —  VIDHI

Padaccheda: कर्मन्द-कृशाश्वात् इनिः

कर्मन्दकृशाश्वादिनिः (4.3.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_111_karmandakf_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmandakfSASvAdiniH",
    text_dev              = "कर्मन्दकृशाश्वादिनिः",
    padaccheda_dev        = "कर्मन्द-कृशाश्वात् इनिः",
    why_dev               = "(सूत्रम् 4.3.111) कर्मन्दकृशाश्वादिनिः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
