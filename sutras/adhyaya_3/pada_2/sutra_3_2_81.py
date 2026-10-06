"""
3.2.81  बहुलमाभीक्ष्ण्ये  —  VIDHI

Padaccheda: बहुलम् आभीक्ष्ण्ये

krt-suffix rule: बहुलमाभीक्ष्ण्ये (81)
Pāṭha: ashtadhyayi.com data.txt row i=32081 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_81_bahulamABI_81"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.81", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulamABIkzRye",
    text_dev              = "बहुलमाभीक्ष्ण्ये",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH bahulam ABIkzRye kft supi RiniH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः बहुलम् आभीक्ष्ण्ये कृत् सुपि णिनिः",
    padaccheda_dev        = "बहुलम् आभीक्ष्ण्ये",
    why_dev               = "धातोः कृत्-प्रत्ययः [बहुलमाभीक्ष्ण्ये] विहितः (३.२.81)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
