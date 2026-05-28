"""
3.2.30  नाडीमुष्ट्योश्च  —  VIDHI

Padaccheda: नाडी-मुष्ट्योः च

krt-suffix rule: नाडीमुष्ट्योश्च (30)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_30_nAqImuzwyo_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_30_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAqImuzwyoSca",
    text_dev              = "नाडीमुष्ट्योश्च",
    padaccheda_dev        = "नाडी-मुष्ट्योः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [नाडीमुष्ट्योश्च] विहितः (३.२.30)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
