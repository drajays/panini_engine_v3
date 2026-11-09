"""
3.4.109  सिजभ्यस्तविदिभ्यश्च  —  VIDHI

Padaccheda: सिच्-अभ्यस्त-विदिभ्यः च

krt-suffix rule: सिजभ्यस्तविदिभ्यः च
Pāṭha: ashtadhyayi.com data.txt row i=34109 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_4.sutra_3_4_108 import _find_jhi_tin, act as _jus


def cond(state: State) -> bool:
    return _find_jhi_tin(state, "3.4.109") is not None


def act(state: State) -> State:
    return _jus(state, "3.4.109")


SUTRA = SutraRecord(
    sutra_id              = "3.4.109",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'sijaByastavidiByaSca',
    text_dev              = 'सिजभ्यस्तविदिभ्यश्च',
    samagra_slp1          = "sic-aByasta-vidiByaH NitaH JeH jus",
    samagra_dev           = "सिच्-अभ्यस्त-विदिभ्यः ङितः झेः जुस्",
    padaccheda_dev        = "सिच्-अभ्यस्त-विदिभ्यः च",
    why_dev               = "धातोः प्रत्ययः (३.4.109)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of            = ("7.1.3", "7.1.4"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
