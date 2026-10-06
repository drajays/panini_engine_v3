"""
3.2.77  स्थः क च  —  VIDHI

Padaccheda: स्थः क (लुप्तप्रथमान्तनिर्देशः) च

krt-suffix rule: स्थः क च (77)
Pāṭha: ashtadhyayi.com data.txt row i=32077 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_77_sTaH_77"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.77", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTaH ka ca",
    text_dev              = "स्थः क च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH sTaH ka ca kft supi upasarge api kvip",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः स्थः क च कृत् सुपि उपसर्गे अपि क्विप्",
    padaccheda_dev        = "स्थः क (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्थः क च] विहितः (३.२.77)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
