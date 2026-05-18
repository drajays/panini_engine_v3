"""
5.4.113  बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच्  —  VIDHI

Padaccheda: बहुव्रीहौ सक्थि-अक्ष्णोः स्वाङ्गात् षच्

बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच् (5.4.113)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_113_bahuvrIhO_113"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_113_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.113"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvrIhO sakTyakzRoH svANgAt zac",
    text_dev              = "बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच्",
    padaccheda_dev        = "बहुव्रीहौ सक्थि-अक्ष्णोः स्वाङ्गात् षच्",
    why_dev               = "(सूत्रम् 5.4.113) बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
