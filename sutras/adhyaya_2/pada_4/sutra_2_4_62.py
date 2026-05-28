"""
2.4.62  तद्राजस्य बहुषु तेनैवास्त्रियाम्  —  VIDHI

Padaccheda: तद्राजस्य बहुषु तेन एव अ-स्त्रियाम्

tadraaja suffix luk in plural non-feminine.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_62_tadraja_bahusu"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_62_yuna_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadrAjasya bahuzu tenEvAstriyAm",
    text_dev              = "तद्राजस्य बहुषु तेनैवास्त्रियाम्",
    padaccheda_dev        = "तद्राजस्य बहुषु तेन एव अ-स्त्रियाम्",
    why_dev               = "तद्राजस्य बहुषु तेन एव अ-स्त्रियाम् (२.४.६२)।",
    anuvritti_from        = ('2.4.58',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
