"""
3.1.116  पुष्यसिद्ध्यौ नक्षत्रे  —  VIDHI

Padaccheda: पुष्य-सिद्ध्यौ नक्षत्रे

Krt suffix rule from dhatu: पुष्यसिद्ध्यौ नक्षत्रे (116)
Pāṭha: ashtadhyayi.com data.txt row i=31116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem
from engine.vivaksha import vivaksita
from phonology import mk

def cond(state: State) -> bool:
    """puṣ, sidh → kyap for the nakṣatra (puṣyaḥ, siddhyaḥ); nipātana."""
    return kftya_open(state, "3.1.116") and vivaksita(state, "artha", "nakzatra") and kftya_stem(state) in ("puz", "siD", "ziD")


def act(state: State) -> State:
    n = len(state.terms)
    state = kftya_attach(state, "3.1.116", "kyap")
    if len(state.terms) > n and state.terms[n - 1].varnas[-1].slp1 == "D":
        state.terms[n - 1].varnas[-1:] = [mk("d"), mk("D")]         # sidh → siddh (nipātana)
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puzyasidDyO nakzatre",
    text_dev              = "पुष्यसिद्ध्यौ नक्षत्रे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH puzya-sidDyO nakzatre kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः पुष्य-सिद्ध्यौ नक्षत्रे कृत् क्यप्",
    padaccheda_dev        = "पुष्य-सिद्ध्यौ नक्षत्रे",
    why_dev               = "धातोः [पुष्यसिद्ध्यौ नक्षत्रे]-प्रत्ययः विहितः (३.१.116)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
