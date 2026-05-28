"""
3.2.24  स्तम्बशकृतोरिन्  —  VIDHI

Padaccheda: स्तम्ब-शकृतोः इन्

krt-suffix rule: स्तम्बशकृतोरिन् (24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_24_stambaSakf_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_24_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stambaSakftorin",
    text_dev              = "स्तम्बशकृतोरिन्",
    padaccheda_dev        = "स्तम्ब-शकृतोः इन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्तम्बशकृतोरिन्] विहितः (३.२.24)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
