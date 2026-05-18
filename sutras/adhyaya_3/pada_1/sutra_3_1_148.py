"""
3.1.148  हश्च व्रीहिकालयोः  —  VIDHI

Padaccheda: हः च व्रीहि-कालयोः

Krt suffix rule from dhatu: हश्च व्रीहिकालयोः (148)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_148_haSca_148"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_148_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.148"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.148",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "haSca vrIhikAlayoH",
    text_dev              = "हश्च व्रीहिकालयोः",
    padaccheda_dev        = "हः च व्रीहि-कालयोः",
    why_dev               = "धातोः [हश्च व्रीहिकालयोः]-प्रत्ययः विहितः (३.१.148)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
