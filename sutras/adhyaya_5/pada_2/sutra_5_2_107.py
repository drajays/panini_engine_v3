"""
5.2.107  ऊषसुषिमुष्कमधो रः  —  VIDHI

Padaccheda: ऊष-सुषि-मुष्क-मधः रः

ऊषसुषिमुष्कमधो रः (5.2.107)
Pāṭha: ashtadhyayi.com data.txt row i=52107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_107_Uzasuzimuz_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.107", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UzasuzimuzkamaDo raH",
    text_dev              = "ऊषसुषिमुष्कमधो रः",
    samagra_slp1          = "tat asya asmin astIti iti Uza-suzi-muzka-maDaH raH",
    samagra_dev           = "'तत् अस्य अस्मिन् अस्तीति' (इति) ऊष-सुषि-मुष्क-मधः रः",
    padaccheda_dev        = "ऊष-सुषि-मुष्क-मधः रः",
    why_dev               = "(सूत्रम् 5.2.107) ऊषसुषिमुष्कमधो रः।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
