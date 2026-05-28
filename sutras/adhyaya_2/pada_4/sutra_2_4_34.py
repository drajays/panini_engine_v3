"""
2.4.34  द्वितीयाटौस्स्वेनः  —  VIDHI

Padaccheda: द्वितीया-टा-ओस्सु एनः

ena substitution in dvitiya, ta and os suffixes.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_34_dvitiya_ena"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(
        "dvandva_samasa" in t.tags or "samasa_member" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitIyAwOssvenaH",
    text_dev              = "द्वितीयाटौस्स्वेनः",
    padaccheda_dev        = "द्वितीया-टा-ओस्सु एनः",
    why_dev               = "द्वितीया-टा-ओस्सु एनः (२.४.३४)।",
    anuvritti_from        = ('2.4.32',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
