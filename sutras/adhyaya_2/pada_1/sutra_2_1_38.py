"""
2.1.38  अपेतापोढमुक्तपतितापत्रस्तैरल्पशः  —  VIDHI

Padaccheda: अपेत-अपोढ-मुक्त-पतित-अपत्रस्तैः अल्पशः

apeta, apoḍha, mukta, patita etc. (alpasas) with dvitiya form tatpurusha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_38_apeta_alpa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_38_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apetApoQamuktapatitApatrastEralpaSaH",
    text_dev              = "अपेतापोढमुक्तपतितापत्रस्तैरल्पशः",
    padaccheda_dev        = "अपेत-अपोढ-मुक्त-पतित-अपत्रस्तैः अल्पशः",
    why_dev               = "अपेत-अपोढ-आदिभिः अल्पशः द्वितीयान्तस्य सह तत्पुरुषः (२.१.३८)।",
    anuvritti_from        = ('2.1.22',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
