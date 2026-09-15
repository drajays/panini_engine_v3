"""
3.4.83  विदो लटो वा  —  VIDHI

Padaccheda: विदः लटः वा

krt-suffix rule: विदो लटो वा
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_83_vido_83"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.83", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vido lawo vA",
    text_dev              = "विदो लटो वा",
    padaccheda_dev        = "विदः लटः वा",
    why_dev               = "धातोः प्रत्ययः (३.4.83)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
