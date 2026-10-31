"""
3.1.8  सुप आत्मनः क्यच्  —  VIDHI

Padaccheda: सुप आत्मनः क्यच्

Krt suffix rule from dhatu: सुप आत्मनः क्यच् (8)
Pāṭha: ashtadhyayi.com data.txt row i=31008 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import term_sup_phonetically_live
from engine.state import State, Term
from engine.vivaksha import vivaksita
from phonology.varna import parse_slp1_upadesha_sequence

# SHORTCUT S101: "supaH" is read as "a sup stands last on the tape after a prātipadika"; "AtmanaH" and "karmaRaH" (the stem is the object of
# the speaker's own wish, and the sup is its dvitīyā) are the caller's vivakṣā `icCA`; samartha-vibhakti is not checked (S16)


def _site(state: State) -> bool:
    t = state.terms
    if len(t) < 2 or not vivaksita(state, "icCA", "icCA"):
        return False
    return (term_sup_phonetically_live(t[-1]) and t[-2].kind == "prakriti" and "prātipadika" in t[-2].tags
            and not any(x.meta.get("upadesha_slp1") == "kyac" for x in t))


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    state.terms.append(Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("kyac")),
                            tags={"pratyaya", "upadesha", "sanadi", "kyac"}, meta={"upadesha_slp1": "kyac"}))
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.8",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "supa AtmanaH kyac",
    text_dev              = "सुप आत्मनः क्यच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca supa AtmanaH kyac karmaRaH icCAyAM vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च सुप आत्मनः क्यच् कर्मणः इच्छायां वा",
    padaccheda_dev        = "सुप आत्मनः क्यच्",
    why_dev               = "धातोः [सुप आत्मनः क्यच्]-प्रत्ययः विहितः (३.१.8)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
