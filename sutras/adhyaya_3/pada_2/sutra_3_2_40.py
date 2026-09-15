"""
3.2.40  वाचि यमो व्रते  —  VIDHI

Padaccheda: वाचि यमः व्रते

krt-suffix rule: वाचि यमो व्रते (40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_40_vAci_40"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.40", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAci yamo vrate",
    text_dev              = "वाचि यमो व्रते",
    padaccheda_dev        = "वाचि यमः व्रते",
    why_dev               = "धातोः कृत्-प्रत्ययः [वाचि यमो व्रते] विहितः (३.२.40)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
