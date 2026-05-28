"""
3.2.37  उग्रम्पश्येरम्मदपाणिन्धमाश्च  —  VIDHI

Padaccheda: उग्रम्पश्य-इरम्मद-पाणिन्धमाः च

krt-suffix rule: उग्रम्पश्येरम्मदपाणिन्धमाश्च (37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_37_ugrampaSye_37"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ugrampaSyerammadapARinDamASca",
    text_dev              = "उग्रम्पश्येरम्मदपाणिन्धमाश्च",
    padaccheda_dev        = "उग्रम्पश्य-इरम्मद-पाणिन्धमाः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [उग्रम्पश्येरम्मदपाणिन्धमाश्च] विहितः (३.२.37)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
