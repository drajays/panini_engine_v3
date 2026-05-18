"""
2.3.16  नमःस्वस्तिस्वाहास्वधालंवषड्योगाच्च  —  VIDHI

Padaccheda: नमःस्वस्ति-स्वाहा-स्वधा-अलं-वषट्-योगात् च

namah svasti svaha svadha alam vashat combine with caturthy.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_16_namas_svaha"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_16_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "namaHsvastisvAhAsvaDAlaMvazaqyogAcca",
    text_dev              = "नमःस्वस्तिस्वाहास्वधालंवषड्योगाच्च",
    padaccheda_dev        = "नमःस्वस्ति-स्वाहा-स्वधा-अलं-वषट्-योगात् च",
    why_dev               = "नमः-स्वस्ति-स्वाहा-आदिभिः योगे चतुर्थी (२.३.१६)।",
    anuvritti_from        = ('2.3.13',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
