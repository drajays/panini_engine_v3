"""
3.3.131  वर्तमानसामीप्ये वर्तमानवद्वा  —  VIDHI

Padaccheda: वर्तमान-सामीप्ये वर्तमान-वत् वा

krt-suffix rule: वर्तमानसामीप्ये वर्तमानवद्वा
Pāṭha: ashtadhyayi.com data.txt row i=33131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_131_vartamAnas_131"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.131", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.131",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = "vartamAnasAmIpye vartamAnavadvA",
    text_dev              = "वर्तमानसामीप्ये वर्तमानवद्वा",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAnasAmIpye vartamAnavat vA kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमानसामीप्ये वर्तमानवत् वा कृत्",
    padaccheda_dev        = "वर्तमान-सामीप्ये वर्तमान-वत् वा",
    why_dev               = "धातोः प्रत्ययः (३.3.131)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
