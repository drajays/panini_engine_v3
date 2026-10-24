"""
3.3.10  तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्  —  VIDHI

Padaccheda: तुमुँन्-ण्वुलौ क्रियायाम् क्रिया-अर्थायाम्

krt-suffix rule: तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्
Pāṭha: ashtadhyayi.com data.txt row i=33010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, dhatu_ends_tape
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

def _site(state: State) -> bool:
    """तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम् — भविष्यति, for an action whose purpose is another action (भोक्तुं व्रजति / भोजको व्रजति)."""
    return vivaksita(state, "kala", "Bavizyat") and vivaksita(state, "kriyArTA", "kriyArTA") and dhatu_ends_tape(state)


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    return attach_krt(state, ("tumu~n", "Rvul")[policy_pick(state, "3.3.10", 2)])        # तुमुन् and ण्वुल् stand side by side


SUTRA = SutraRecord(
    sutra_id              = "3.3.10",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "tumunRvulO kriyAyAM kriyArTAyAm",
    text_dev              = "तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Bavizyati tumun-RvulO kriyAyAm kriyArTAyAm kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भविष्यति तुमुन्-ण्वुलौ क्रियायाम् क्रियार्थायाम् कृत्",
    padaccheda_dev        = "तुमुँन्-ण्वुलौ क्रियायाम् क्रिया-अर्थायाम्",
    why_dev               = "धातोः प्रत्ययः (३.3.10)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
