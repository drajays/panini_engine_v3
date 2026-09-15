"""
6.2.37  कार्तकौजपादयश्च  —  VIDHI

Padaccheda: कार्त्तकौजप-आदयः च

कार्तकौजपादयश्च (6.2.37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_37_kArtakOjap_37"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.37", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kArtakOjapAdayaSca",
    text_dev              = "कार्तकौजपादयश्च",
    padaccheda_dev        = "कार्त्तकौजप-आदयः च",
    why_dev               = "(सूत्रम् 6.2.37) कार्तकौजपादयश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
