"""
3.2.129  ताच्छील्यवयोवचनशक्तिषु चानश्  —  VIDHI

Padaccheda: ताच्छील्य-वयोवचन-शक्तिषु चानश्

krt-suffix rule: ताच्छील्यवयोवचनशक्तिषु चानश् (129)
Pāṭha: ashtadhyayi.com data.txt row i=32129 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_3.pada_2.sutra_3_2_124 import participle_site, attach_participle, _atmanepada, SAnan_DHATUS  # noqa: F401


def _site(state: State):
    return participle_site(state, vivaksita(state, "kala", "vartamAna"), vivaksita(state, "tAcCIlyAdi", "tAcCIlya") or vivaksita(state, "tAcCIlyAdi", "vayovacana") or vivaksita(state, "tAcCIlyAdi", "Sakti"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_participle(state, "cAnaS")


SUTRA = SutraRecord(
    sutra_id              = "3.2.129",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tAcCIlyavayovacanaSaktizu cAnaS",
    text_dev              = "ताच्छील्यवयोवचनशक्तिषु चानश्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne tAcCIlya-vayovacana-Saktizu cAnaS kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने ताच्छील्य-वयोवचन-शक्तिषु चानश् कृत्",
    padaccheda_dev        = "ताच्छील्य-वयोवचन-शक्तिषु चानश्",
    why_dev               = "धातोः कृत्-प्रत्ययः [ताच्छील्यवयोवचनशक्तिषु चानश्] विहितः (३.२.129)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
