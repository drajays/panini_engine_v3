"""
3.4.35  शुष्कचूर्णरूक्षेषु पिषः  —  VIDHI

Padaccheda: शुष्क-चूर्ण-रूक्षेषु पिषः

krt-suffix rule: शुष्कचूर्णरूक्षेषु पिषः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_35_SuzkacUrRa_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("3_4_35_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SuzkacUrRarUkzezu pizaH",
    text_dev              = "शुष्कचूर्णरूक्षेषु पिषः",
    padaccheda_dev        = "शुष्क-चूर्ण-रूक्षेषु पिषः",
    why_dev               = "धातोः प्रत्ययः (३.4.35)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
