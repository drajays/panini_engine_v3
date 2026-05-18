"""
2.4.26  परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः  —  VIDHI

Padaccheda: पर-वत् लिङ्गम् द्वन्द्व-तत्पुरुषयोः

dvandva and tatpurusha take gender of the latter member.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_26_paravat_linga"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_26_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paravalliNgaM dvandvatatpuruzayoH",
    text_dev              = "परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः",
    padaccheda_dev        = "पर-वत् लिङ्गम् द्वन्द्व-तत्पुरुषयोः",
    why_dev               = "द्वन्द्व-तत्पुरुषयोः पर-वत् लिङ्गम् (२.४.२६)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
