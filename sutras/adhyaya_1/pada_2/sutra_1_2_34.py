"""
1.2.34  यज्ञकर्मण्यजपन्यूङ्खसामसु  —  VIDHI

Padaccheda: यज्ञकर्मणि · अजप · न्यूङ्ख · सामसु

In sacrificial contexts (yajnakarmani) with ajapa, nyunkha, and saman
the relevant forms are recognized as non-anudatta.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "1_2_34_yajna_karma"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["accent_kind"]         = "1.2.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajYakarmaRyajapanyUNKasAmasu",
    text_dev              = "यज्ञकर्मण्यजपन्यूङ्खसामसु",
    padaccheda_dev        = "यज्ञकर्मणि · अजप · न्यूङ्ख · सामसु",
    why_dev               = "यज्ञ-कर्मणि अजप-न्यूङ्ख-सामेषु अनुदात्तं विधीयते (१.२.३४)।",
    anuvritti_from        = ("1.2.33",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
