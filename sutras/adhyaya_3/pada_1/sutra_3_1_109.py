"""
3.1.109  एतिस्तुशास्वृदृजुषः क्यप्  —  VIDHI

Padaccheda: एति-स्तु-शास्-वृ-दृ-जुषः क्यप्

Krt suffix rule from dhatu: एतिस्तुशस्वृदृजुषः क्यप् (109)
Pāṭha: ashtadhyayi.com data.txt row i=31109 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem

def cond(state: State) -> bool:
    """i, stu, śās, vṛ, juṣ → kyap (ityam, stutyam, śiṣyam, vṛtyam, juṣyam); the apavāda of yat (3.1.97) and ṇyat (3.1.124)."""
    return kftya_open(state, "3.1.109") and kftya_stem(state) in ("i", "stu", "zwu", "SAs", "vf", "juz")


def act(state: State) -> State:
    return kftya_attach(state, "3.1.109", "kyap")


SUTRA = SutraRecord(
    sutra_id              = "3.1.109",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'etistuSAsvfdfjuzaH kyap',
    text_dev              = 'एतिस्तुशास्वृदृजुषः क्यप्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH eti-stu-SAs-vf-df-juzaH kyap kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः एति-स्तु-शास्-वृ-दृ-जुषः क्यप् कृत्",
    padaccheda_dev        = "एति-स्तु-शास्-वृ-दृ-जुषः क्यप्",
    why_dev               = "धातोः [एतिस्तुशस्वृदृजुषः क्यप्]-प्रत्ययः विहितः (३.१.109)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.97', '3.1.124'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
