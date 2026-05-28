"""
3.3.72  ह्वः सम्प्रसारणं च न्यभ्युपविषु  —  VIDHI

Padaccheda: ह्वः सम्प्रसारणम् च नि-अभि-उप-विषु

krt-suffix rule: ह्वः सम्प्रसारणं च न्यभ्युपविषु
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_72_hvaH_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_72_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hvaH samprasAraRaM ca nyaByupavizu",
    text_dev              = "ह्वः सम्प्रसारणं च न्यभ्युपविषु",
    padaccheda_dev        = "ह्वः सम्प्रसारणम् च नि-अभि-उप-विषु",
    why_dev               = "धातोः प्रत्ययः (३.3.72)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
