"""
3.2.130  इङ्धार्योः शत्रकृच्छ्रिणि  —  VIDHI

Padaccheda: इङ्-धार्य्योः (पञ्चम्यर्थे षष्ठी) शतृँ (लुप्तप्रथमान्तनिर्देशः) अकृच्छ्रिणि

krt-suffix rule: इङ्धार्योः शत्रकृच्छ्रिणि (130)
Pāṭha: ashtadhyayi.com data.txt row i=32130 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_3.pada_2.sutra_3_2_124 import participle_site, attach_participle, _atmanepada, SAnan_DHATUS  # noqa: F401


def _site(state: State):
    return participle_site(state, vivaksita(state, "kala", "vartamAna"), vivaksita(state, "akfcCra", "akfcCra"), dhatus=frozenset({"iN"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_participle(state, "Satf~")


SUTRA = SutraRecord(
    sutra_id              = "3.2.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iNDAryoH SatrakfcCriRi",
    text_dev              = "इङ्धार्योः शत्रकृच्छ्रिणि",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne iN-DAryyoH Satf akfcCriRi kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने इङ्-धार्य्योः शतृ अकृच्छ्रिणि कृत्",
    padaccheda_dev        = "इङ्-धार्य्योः (पञ्चम्यर्थे षष्ठी) शतृँ (लुप्तप्रथमान्तनिर्देशः) अकृच्छ्रिणि",
    why_dev               = "धातोः कृत्-प्रत्ययः [इङ्धार्योः शत्रकृच्छ्रिणि] विहितः (३.२.130)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
