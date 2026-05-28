"""
6.4.104  चिणो लुक्  —  VIDHI

Padaccheda: चिणः लुक्

चिणो लुक् (6.4.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_104_ciRo_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: ciṇ luk fires in karmani/bhāva context (dhātu tagged by pipeline)
    if any("bhava_karma_usage" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("6_4_104_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ciRo luk",
    text_dev              = "चिणो लुक्",
    padaccheda_dev        = "चिणः लुक्",
    why_dev               = "(सूत्रम् 6.4.104) चिणो लुक्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
