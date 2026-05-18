"""
2.1.62  वृन्दारकनागकुञ्जरैः पूज्यमानम्  —  VIDHI

Padaccheda: वृन्दारक-नाग-कुञ्जरैः पूज्यमानम्

vrndaaraka, naga, kunjara with pujyamana form karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_62_vrndarak_naga"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfndArakanAgakuYjarEH pUjyamAnam",
    text_dev              = "वृन्दारकनागकुञ्जरैः पूज्यमानम्",
    padaccheda_dev        = "वृन्दारक-नाग-कुञ्जरैः पूज्यमानम्",
    why_dev               = "वृन्दारक-नाग-कुञ्जरैः पूज्यमानं कर्मधारये (२.१.६२)।",
    anuvritti_from        = ('2.1.61',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
