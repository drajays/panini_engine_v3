"""
3.4.110  आतः  —  VIDHI

Padaccheda: आतः

krt-suffix rule: आतः
Pāṭha: ashtadhyayi.com data.txt row i=34110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_4.sutra_3_4_108 import _find_jhi_tin, act as _jus


def cond(state: State) -> bool:
    return _find_jhi_tin(state, "3.4.110") is not None


def act(state: State) -> State:
    return _jus(state, "3.4.110")


SUTRA = SutraRecord(
    sutra_id              = "3.4.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtaH",
    text_dev              = "आतः",
    samagra_slp1          = "AtaH sicaH lugantAt NitaH JeH jus",
    samagra_dev           = "आतः सिचः (लुगन्तात्) ङितः झेः जुस्",
    padaccheda_dev        = "आतः",
    why_dev               = "धातोः प्रत्ययः (३.4.110)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of            = ("7.1.3", "7.1.4"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
