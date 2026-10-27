"""
3.2.131  द्विषोऽमित्रे  —  VIDHI

Padaccheda: द्विषः अमित्रे

krt-suffix rule: द्विषोऽमित्रे (131)
Pāṭha: ashtadhyayi.com data.txt row i=32131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_3.pada_2.sutra_3_2_124 import participle_site, attach_participle, _atmanepada, SAnan_DHATUS  # noqa: F401


def _site(state: State):
    return participle_site(state, vivaksita(state, "kala", "vartamAna"), vivaksita(state, "amitra", "amitra"), dhatus=frozenset({"dviza~"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_participle(state, "Satf~")


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
