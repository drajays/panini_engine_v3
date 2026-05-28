"""
2.1.64  किं क्षेपे  —  VIDHI

Padaccheda: किम् क्षेपे

kim in ksepa context forms karmadharaya compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_64_kim_ksepe"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kiM kzepe",
    text_dev              = "किं क्षेपे",
    padaccheda_dev        = "किम् क्षेपे",
    why_dev               = "किम् क्षेपे कर्मधारये (२.१.६४)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
