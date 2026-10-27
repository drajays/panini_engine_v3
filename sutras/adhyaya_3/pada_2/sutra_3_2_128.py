"""
3.2.128  पूङ्यजोः शानन्  —  VIDHI

Padaccheda: पूङ्-यजोः (पञ्चम्यर्थे षष्ठी) शानन्

krt-suffix rule: पूङ्यजोः शानन् (128)
Pāṭha: ashtadhyayi.com data.txt row i=32128 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_3.pada_2.sutra_3_2_124 import participle_site, attach_participle, _atmanepada, SAnan_DHATUS  # noqa: F401


def _site(state: State):
    return participle_site(state, vivaksita(state, "kala", "vartamAna"), dhatus=SAnan_DHATUS)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_participle(state, "SAnan")


SUTRA = SutraRecord(
    sutra_id              = "3.2.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUNyajoH SAnan",
    text_dev              = "पूङ्यजोः शानन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne pUNyajoH SAnan kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने पूङ्यजोः शानन् कृत्",
    padaccheda_dev        = "पूङ्-यजोः (पञ्चम्यर्थे षष्ठी) शानन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [पूङ्यजोः शानन्] विहितः (३.२.128)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
