"""
3.3.57  ॠदोरप्  —  VIDHI

Padaccheda: ॠत्-ओः अप्

krt-suffix rule: ऋदोरप्
Pāṭha: ashtadhyayi.com data.txt row i=33057 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return bhava_site(state, vivaksita(state, "artha", "BAva"), final=lambda f: f[-1:] in ("f", "F", "u", "U"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "ap")


SUTRA = SutraRecord(
    sutra_id              = "3.3.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'Fdorap',
    text_dev              = 'ॠदोरप्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm FdoH ap kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् ॠदोः अप् कृत्",
    padaccheda_dev        = "ॠत्-ओः अप्",
    why_dev               = "धातोः प्रत्ययः (३.3.57)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of     = ("3.3.18",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
