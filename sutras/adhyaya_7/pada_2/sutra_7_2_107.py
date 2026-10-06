"""
7.2.107  अदस औ सुलोपश्च  —  VIDHI

Padaccheda: अदसः औ (लुप्तप्रथमान्तनिर्देशः) सु-लोपः च

अदस औ सुलोपश्च (7.2.107)
Pāṭha: ashtadhyayi.com data.txt row i=72107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk

_GATE_KEY: str = "7_2_107_adasa_107"


def cond(state: State) -> bool:
    """अदस् + su (prathamā-ekavacana): s → au, su-lopa (then 7.2.106 d→s, 6.1.88 → असौ)."""
    if state.meta.get("adas_sau_au") or len(state.terms) < 2:
        return False
    if state.terms[0].meta.get("upadesha_slp1") != "adas":
        return False
    pr = state.terms[1]
    return "sup" in pr.tags and pr.meta.get("upadesha_slp1") == "s~"


def act(state: State) -> State:
    state.terms[1].varnas = [mk("O")]   # au replaces the su; the stem's final 'a' stays for 6.1.88
    state.meta["adas_sau_au"] = True
    state.meta["adas_stem"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.107",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "adasa O sulopaSca",
    text_dev              = "अदस औ सुलोपश्च",
    samagra_slp1          = "adasaH sO O sulopaH ca",
    samagra_dev           = "अदसः सौ औ सुलोपः च",
    padaccheda_dev        = "अदसः औ (लुप्तप्रथमान्तनिर्देशः) सु-लोपः च",
    why_dev               = "(सूत्रम् 7.2.107) अदस औ सुलोपश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
