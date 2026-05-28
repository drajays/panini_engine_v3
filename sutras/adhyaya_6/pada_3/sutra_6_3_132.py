"""
6.3.132  ओषधेश्च विभक्तावप्रथमायाम्  —  VIDHI

Padaccheda: ओषधेः च विभक्तौ अ-प्रथमायाम्

ओषधेश्च विभक्तावप्रथमायाम् (6.3.132)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_132_ozaDeSca_132"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.132"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ozaDeSca viBaktAvapraTamAyAm",
    text_dev              = "ओषधेश्च विभक्तावप्रथमायाम्",
    padaccheda_dev        = "ओषधेः च विभक्तौ अ-प्रथमायाम्",
    why_dev               = "(सूत्रम् 6.3.132) ओषधेश्च विभक्तावप्रथमायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
