"""
3.3.90  यजयाचयतविच्छप्रच्छरक्षो नङ्  —  VIDHI

Padaccheda: यज-याच-यत-विच्छ-प्रच्छ-रक्षः नङ्

krt-suffix rule: यजयाचयतविच्छप्रच्छरक्षो नङ्
Pāṭha: ashtadhyayi.com data.txt row i=33090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_90_yajayAcaya_90"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.90", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajayAcayatavicCapracCarakzo naN",
    text_dev              = "यजयाचयतविच्छप्रच्छरक्षो नङ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm yaja-yAca-yata-vicCa-pracCa-rakzaH naN kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् यज-याच-यत-विच्छ-प्रच्छ-रक्षः नङ् कृत्",
    padaccheda_dev        = "यज-याच-यत-विच्छ-प्रच्छ-रक्षः नङ्",
    why_dev               = "धातोः प्रत्ययः (३.3.90)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
