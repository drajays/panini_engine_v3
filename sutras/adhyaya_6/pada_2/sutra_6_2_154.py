"""
6.2.154  मिश्रं चानुपसर्गमसंधौ  —  VIDHI

Padaccheda: मिश्रम् च अनुपसर्गम् असन्धौ

मिश्रं चानुपसर्गमसंधौ (6.2.154)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_154_miSraM_154"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.154"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.154",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "miSraM cAnupasargamasaMDO",
    text_dev              = "मिश्रं चानुपसर्गमसंधौ",
    padaccheda_dev        = "मिश्रम् च अनुपसर्गम् असन्धौ",
    why_dev               = "(सूत्रम् 6.2.154) मिश्रं चानुपसर्गमसंधौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
