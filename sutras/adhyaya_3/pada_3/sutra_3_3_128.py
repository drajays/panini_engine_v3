"""
3.3.128  आतो युच्  —  VIDHI

Padaccheda: आतः युच्

krt-suffix rule: आतो युच्
Pāṭha: ashtadhyayi.com data.txt row i=33128 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return bhava_site(state, upapada_stems=frozenset({"Izat", "dus", "su"}), final=lambda f: f[-1:] == "A")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "yuc")


SUTRA = SutraRecord(
    sutra_id              = "3.3.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ato yuc",
    text_dev              = "आतो युच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH AtaH yuc kft kfcCra-akfcCra-arTezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आतः युच् कृत् कृच्छ्र-अकृच्छ्र-अर्थेषु",
    padaccheda_dev        = "आतः युच्",
    why_dev               = "धातोः प्रत्ययः (३.3.128)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of     = ("3.3.126",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
