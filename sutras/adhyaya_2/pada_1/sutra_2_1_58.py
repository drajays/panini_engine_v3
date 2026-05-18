"""
2.1.58  पूर्वापरप्रथमचरमजघन्यसमानमध्यमध्यमवीराश्च  —  VIDHI

Padaccheda: पूर्व-अपर-प्रथम-चरम-जघन्य-समान-मध्य-मध्यम-वीराः च

purva, apara, prathama, carama etc. also form karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_58_purva_apara_carama"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_58_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvAparapraTamacaramajaGanyasamAnamaDyamaDyamavIrASca",
    text_dev              = "पूर्वापरप्रथमचरमजघन्यसमानमध्यमध्यमवीराश्च",
    padaccheda_dev        = "पूर्व-अपर-प्रथम-चरम-जघन्य-समान-मध्य-मध्यम-वीराः च",
    why_dev               = "पूर्व-अपर-प्रथम-चरम-आदयश्च कर्मधारये (२.१.५८)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
