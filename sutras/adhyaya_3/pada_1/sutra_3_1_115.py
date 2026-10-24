"""
3.1.115  भिद्योद्ध्यौ नदे  —  VIDHI

Padaccheda: भिद्य-उद्ध्यौ नदे

Krt suffix rule from dhatu: भिद्योद्ध्यौ नदे (115)
Pāṭha: ashtadhyayi.com data.txt row i=31115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem
from engine.vivaksha import vivaksita
from phonology import mk

def cond(state: State) -> bool:
    """bhid, ujjh → kyap for a river-bank scene (bhidyaḥ, uddhyaḥ); nipātana."""
    return kftya_open(state, "3.1.115") and vivaksita(state, "artha", "nada") and kftya_stem(state) in ("Bid", "ujJ")


def act(state: State) -> State:
    n = len(state.terms)
    state = kftya_attach(state, "3.1.115", "kyap")
    if len(state.terms) > n and "".join(v.slp1 for v in state.terms[n - 1].varnas[-2:]) == "jJ":
        state.terms[n - 1].varnas[-2:] = [mk("d"), mk("D")]         # ujjh → uddh (nipātana)
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BidyodDyO nade",
    text_dev              = "भिद्योद्ध्यौ नदे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH Bidya-udDyO nade kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः भिद्य-उद्ध्यौ नदे कृत् क्यप्",
    padaccheda_dev        = "भिद्य-उद्ध्यौ नदे",
    why_dev               = "धातोः [भिद्योद्ध्यौ नदे]-प्रत्ययः विहितः (३.१.115)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
