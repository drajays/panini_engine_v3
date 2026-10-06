"""
6.4.83  ओः सुपि  —  VIDHI

Padaccheda: ओः सुपि

ओः सुपि (6.4.83)
Pāṭha: ashtadhyayi.com data.txt row i=64083 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_83_oH_83"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.83", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "oH supi",
    text_dev              = "ओः सुपि",
    samagra_slp1          = "anekAcaH aNgasya asaMyogapUrvasya oH DAtoH supi aci yaR",
    samagra_dev           = "अनेकाचः अङ्गस्य असंयोगपूर्वस्य ओः धातोः सुपि अचि यण्",
    padaccheda_dev        = "ओः सुपि",
    why_dev               = "(सूत्रम् 6.4.83) ओः सुपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
