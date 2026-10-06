"""
3.2.131  द्विषोऽमित्रे  —  VIDHI

Padaccheda: द्विषः अमित्रे

krt-suffix rule: द्विषोऽमित्रे (131)
Pāṭha: ashtadhyayi.com data.txt row i=32131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_131_dvizomitr_131"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.131", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'dvizomitre',
    text_dev              = 'द्विषोऽमित्रे',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne dvizaH amitre kft Satf",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने द्विषः अमित्रे कृत् शतृ",
    padaccheda_dev        = "द्विषः अमित्रे",
    why_dev               = "धातोः कृत्-प्रत्ययः [द्विषोऽमित्रे] विहितः (३.२.131)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
