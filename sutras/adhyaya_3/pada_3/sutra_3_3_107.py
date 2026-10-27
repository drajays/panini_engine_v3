"""
3.3.107  ण्यासश्रन्थो युच्  —  VIDHI

Padaccheda: णि-आस-श्रन्थः युच्

krt-suffix rule: ण्यासश्रन्थो युच्
Pāṭha: ashtadhyayi.com data.txt row i=33107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return bhava_site(state, vivaksita(state, "artha", "BAva"), vivaksita(state, "linga", "strI"), dhatus=frozenset({"Asa~", "SranTa~"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "yuc")


SUTRA = SutraRecord(
    sutra_id              = "3.3.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "RyAsaSranTo yuc",
    text_dev              = "ण्यासश्रन्थो युच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm Ri-Asa-SranTaH yuc kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् णि-आस-श्रन्थः युच् कृत्",
    padaccheda_dev        = "णि-आस-श्रन्थः युच्",
    why_dev               = "धातोः प्रत्ययः (३.3.107)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of     = ("3.3.103",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
