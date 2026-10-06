"""
3.3.171  कृत्याश्च  —  VIDHI

Padaccheda: कृत्याः च

krt-suffix rule: कृत्याश्च
Pāṭha: ashtadhyayi.com data.txt row i=33171 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_171_kftyASca_171"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.171", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.171"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.171",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kftyASca",
    text_dev              = "कृत्याश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kftyAH ca kft AvaSyaka-ADamarRyayoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कृत्याः च कृत् आवश्यक-आधमर्ण्ययोः",
    padaccheda_dev        = "कृत्याः च",
    why_dev               = "धातोः प्रत्ययः (३.3.171)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
