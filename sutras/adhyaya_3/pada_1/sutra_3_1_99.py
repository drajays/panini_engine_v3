"""
3.1.99  शकिसहोश्च  —  VIDHI

Padaccheda: शकि-सहोः च

Krt suffix rule from dhatu: शकिसहोश्च (99)
Pāṭha: ashtadhyayi.com data.txt row i=31099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem



def cond(state: State) -> bool:
    """śak, sah → yat (śakyam, sahyam)."""
    return kftya_open(state, "3.1.99") and kftya_stem(state) in ("Sak", "sah")


def act(state: State) -> State:
    return kftya_attach(state, "3.1.99", "yat")


SUTRA = SutraRecord(
    sutra_id              = "3.1.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SakisahoSca",
    text_dev              = "शकिसहोश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH Saki-sahoH ca kft yat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः शकि-सहोः च कृत् यत्",
    padaccheda_dev        = "शकि-सहोः च",
    why_dev               = "धातोः [शकिसहोश्च]-प्रत्ययः विहितः (३.१.99)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
