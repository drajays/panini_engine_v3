"""
3.2.179  भुवः संज्ञाऽन्तरयोः  —  VIDHI

Padaccheda: भुवः संज्ञा-अन्तरयोः

krt-suffix rule: भुवः संज्ञाऽन्तरयोः (179)
Pāṭha: ashtadhyayi.com data.txt row i=32179 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_179_BuvaH_179"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.179", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.179"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.179",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'BuvaH saMjYAntarayoH',
    text_dev              = 'भुवः संज्ञाऽन्तरयोः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne BuvaH saMjYA-antarayoH kft kvip",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने भुवः संज्ञा-अन्तरयोः कृत् क्विप्",
    padaccheda_dev        = "भुवः संज्ञा-अन्तरयोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [भुवः संज्ञाऽन्तरयोः] विहितः (३.२.179)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
