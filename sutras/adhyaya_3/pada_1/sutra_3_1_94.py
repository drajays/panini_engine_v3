"""
3.1.94  वाऽसरूपोऽस्त्रियाम्  —  VIDHI

Padaccheda: वा असरूपः अ-स्त्रियाम्

Krt suffix rule from dhatu: वाऽसरूपोऽस्त्रियाम् (94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_94_vAsarUpost_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA'sarUpo'striyAm",
    text_dev              = "वाऽसरूपोऽस्त्रियाम्",
    padaccheda_dev        = "वा असरूपः अ-स्त्रियाम्",
    why_dev               = "धातोः [वाऽसरूपोऽस्त्रियाम्]-प्रत्ययः विहितः (३.१.94)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
