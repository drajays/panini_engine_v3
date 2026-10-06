"""
3.1.93  कृदतिङ्  —  SAMJNA

Padaccheda: कृत् (प्रथमा-एकवचनम्) · अतिङ् (प्रथमा-एकवचनम्)

Krt suffix rule from dhatu: कृदतिङ् (93)
Pāṭha: ashtadhyayi.com data.txt row i=31093 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return "3_1_93_krdatinga" not in state.samjna_registry


def act(state: State) -> State:
    state.samjna_registry["3_1_93_krdatinga"] = True
    state.samjna_registry["krdatinga"]          = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.93",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "kfdatiN",
    text_dev              = "कृदतिङ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kft atiN tatra",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कृत् अतिङ् तत्र",
    padaccheda_dev        = "कृत् (प्रथमा-एकवचनम्) · अतिङ् (प्रथमा-एकवचनम्)",
    why_dev               = "कृत्-प्रत्ययः यदि अतिङ् तर्हि कृदतिङ्-संज्ञा (३.१.93)।",
    anuvritti_from        = ("3.1.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
