"""
5.3.114  आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्  —  VIDHI

Padaccheda: आयुध-जीवि-सङ्‍घात् ञ्यट् वाहीकेषु अ-ब्राह्मण-राजन्यात्

आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात् (5.3.114)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_114_AyuDajIvis_114"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_114_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AyuDajIvisaMGAYYyaqvAhIkezvabrAhmaRarAjanyAt",
    text_dev              = "आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्",
    padaccheda_dev        = "आयुध-जीवि-सङ्‍घात् ञ्यट् वाहीकेषु अ-ब्राह्मण-राजन्यात्",
    why_dev               = "(सूत्रम् 5.3.114) आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
