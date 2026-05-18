"""
5.4.107  अव्ययीभावे शरत्प्रभृतिभ्यः  —  VIDHI

Padaccheda: अव्ययीभावे शरत्-प्रभृतिभ्यः

अव्ययीभावे शरत्प्रभृतिभ्यः (5.4.107)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_107_avyayIBAve_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_107_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyayIBAve SaratpraBftiByaH",
    text_dev              = "अव्ययीभावे शरत्प्रभृतिभ्यः",
    padaccheda_dev        = "अव्ययीभावे शरत्-प्रभृतिभ्यः",
    why_dev               = "(सूत्रम् 5.4.107) अव्ययीभावे शरत्प्रभृतिभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
