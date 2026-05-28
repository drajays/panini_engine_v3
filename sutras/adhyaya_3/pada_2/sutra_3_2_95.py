"""
3.2.95  राजनि युधिकृञः  —  VIDHI

Padaccheda: राजनि युधि-कृञः

krt-suffix rule: राजनि युधिकृञः (95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_95_rAjani_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAjani yuDikfYaH",
    text_dev              = "राजनि युधिकृञः",
    padaccheda_dev        = "राजनि युधि-कृञः",
    why_dev               = "धातोः कृत्-प्रत्ययः [राजनि युधिकृञः] विहितः (३.२.95)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
