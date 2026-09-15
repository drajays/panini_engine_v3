"""
3.2.188  मतिबुद्धिपूजार्थेभ्यश्च  —  VIDHI

Padaccheda: मति-बुद्धि-पूजा-अर्थेभ्यः च

krt-suffix rule: मतिबुद्धिपूजार्थेभ्यश्च (188)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_188_matibudDip_188"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.188", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.188"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.188",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "matibudDipUjArTeByaSca",
    text_dev              = "मतिबुद्धिपूजार्थेभ्यश्च",
    padaccheda_dev        = "मति-बुद्धि-पूजा-अर्थेभ्यः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [मतिबुद्धिपूजार्थेभ्यश्च] विहितः (३.२.188)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
