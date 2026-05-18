"""
2.3.73  चतुर्थी चाशिष्यायुष्यमद्रभद्रकुशलसुखार्थहितैः  —  VIDHI

Padaccheda: चतुर्थी च आशिषि आयुष्य-मद्र-भद्र-कुशल-सुख-अर्थहितैः

caturthy in blessings with ayusya, madra, bhadra etc.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_73_caturthy_asisi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_73_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "caturTI cASizyAyuzyamadraBadrakuSalasuKArTahitEH",
    text_dev              = "चतुर्थी चाशिष्यायुष्यमद्रभद्रकुशलसुखार्थहितैः",
    padaccheda_dev        = "चतुर्थी च आशिषि आयुष्य-मद्र-भद्र-कुशल-सुख-अर्थहितैः",
    why_dev               = "चतुर्थी च आशिषि आयुष्य-मद्र-भद्र-कुशल-सुख-अर्थहितैः (२.३.७३)।",
    anuvritti_from        = ('2.3.13',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
