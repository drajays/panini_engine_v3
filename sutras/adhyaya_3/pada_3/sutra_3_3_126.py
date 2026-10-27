"""
3.3.126  ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल्  —  VIDHI

Padaccheda: ईषत्-दुस्-सुषु कृच्छ्र-अकृच्छ्र-अर्थेषु खल्

krt-suffix rule: ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल्
Pāṭha: ashtadhyayi.com data.txt row i=33126 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return bhava_site(state, upapada_stems=frozenset({"Izat", "dus", "su"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "Kal")


SUTRA = SutraRecord(
    sutra_id              = "3.3.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "IzadduHsuzu kfcCrAkfcCrArTezu Kal",
    text_dev              = "ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Izat-dus-suzu kfcCra-akfcCra-arTezu Kal kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः ईषत्-दुस्-सुषु कृच्छ्र-अकृच्छ्र-अर्थेषु खल् कृत्",
    padaccheda_dev        = "ईषत्-दुस्-सुषु कृच्छ्र-अकृच्छ्र-अर्थेषु खल्",
    why_dev               = "धातोः प्रत्ययः (३.3.126)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
