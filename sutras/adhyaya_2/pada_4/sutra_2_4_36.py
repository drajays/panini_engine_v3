"""
2.4.36  अदो जग्धिर्ल्यप्ति किति  —  VIDHI

Padaccheda: अदः जग्धिः ल्यप् (लुप्तसप्तम्यन्तनिर्देशः) ति किति

adas root becomes jagdhi in lyap, ti, kit context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_36_adah_jagdhi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_36_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ado jagDirlyapti kiti",
    text_dev              = "अदो जग्धिर्ल्यप्ति किति",
    padaccheda_dev        = "अदः जग्धिः ल्यप् (लुप्तसप्तम्यन्तनिर्देशः) ति किति",
    why_dev               = "अदः जग्धिः ल्यप् ति किति (२.४.३६)।",
    anuvritti_from        = ('2.4.35',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
