"""
3.2.51  कुमारशीर्षयोर्णिनिः  —  VIDHI

Padaccheda: कुमार-शीर्षयोः णिनिः

krt-suffix rule: कुमारशीर्षयोर्णिनिः (51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_51_kumAraSIrz_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_51_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kumAraSIrzayorRiniH",
    text_dev              = "कुमारशीर्षयोर्णिनिः",
    padaccheda_dev        = "कुमार-शीर्षयोः णिनिः",
    why_dev               = "धातोः कृत्-प्रत्ययः [कुमारशीर्षयोर्णिनिः] विहितः (३.२.51)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
