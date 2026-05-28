"""
8.1.20  युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ  —  VIDHI

Padaccheda: युष्मद्-अस्मदोः षष्ठी-चतुर्थी-द्वितीया-स्थयोः वाम्-नावौ

युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ (8.1.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_20_yuzmadasma_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_20_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yuzmadasmadoH zazWIcaturTIdvitIyAsTayorvAnnAvO",
    text_dev              = "युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ",
    padaccheda_dev        = "युष्मद्-अस्मदोः षष्ठी-चतुर्थी-द्वितीया-स्थयोः वाम्-नावौ",
    why_dev               = "(सूत्रम् 8.1.20) युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
