"""
2.3.17  मन्यकर्मण्यनादरे विभाषाऽप्राणिषु  —  VIDHI

Padaccheda: मन्य-कर्मणि अनादरे विभाषा अप्राणिषु

Optional tritiya with manya in disrespect context for non-beings.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_17_manya_anadare"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_17_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "manyakarmaRyanAdare viBAzA'prARizu",
    text_dev              = "मन्यकर्मण्यनादरे विभाषाऽप्राणिषु",
    padaccheda_dev        = "मन्य-कर्मणि अनादरे विभाषा अप्राणिषु",
    why_dev               = "मन्य-कर्मणि अनादरे अप्राणिषु विभाषा तृतीया (२.३.१७)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
