"""
3.1.111  ई च खनः  —  VIDHI

Padaccheda: ई (लुप्तप्रथमान्तनिर्देशः) च खनः

Krt suffix rule from dhatu: ई च खनः (111)
Pāṭha: ashtadhyayi.com data.txt row i=31111 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem
from phonology import mk

def cond(state: State) -> bool:
    """khan → kyap, with ī for the final n (khe-yam: kha-ī + ya, 6.1.87)."""
    return kftya_open(state, "3.1.111") and kftya_stem(state) == "Kan"


def act(state: State) -> State:
    n = len(state.terms)
    state = kftya_attach(state, "3.1.111", "kyap")
    if len(state.terms) > n:
        state.terms[n - 1].varnas[-1] = mk("I")          # ant-ādeśa (1.1.52)
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "I ca KanaH",
    text_dev              = "ई च खनः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH I ca KanaH kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः ई च खनः कृत् क्यप्",
    padaccheda_dev        = "ई (लुप्तप्रथमान्तनिर्देशः) च खनः",
    why_dev               = "धातोः [ई च खनः]-प्रत्ययः विहितः (३.१.111)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.97', '3.1.124'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
