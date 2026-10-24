"""
3.1.121  युग्यं च पत्रे  —  VIDHI

Padaccheda: युग्यम् च पत्रे

Krt suffix rule from dhatu: युग्यं च पत्त्रे (121)
Pāṭha: ashtadhyayi.com data.txt row i=31121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem
from engine.vivaksha import vivaksita
from phonology import mk

def cond(state: State) -> bool:
    """yuj → kyap with kutva for the vehicle (yugyaḥ); nipātana."""
    return kftya_open(state, "3.1.121") and vivaksita(state, "artha", "patra") and kftya_stem(state) == "yuj"


def act(state: State) -> State:
    n = len(state.terms)
    state = kftya_attach(state, "3.1.121", "kyap")
    if len(state.terms) > n:
        state.terms[n - 1].varnas[-1] = mk("g")
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'yugyaM ca patre',
    text_dev              = 'युग्यं च पत्रे',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH yugyam ca patre kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः युग्यम् च पत्रे कृत् क्यप्",
    padaccheda_dev        = "युग्यम् च पत्रे",
    why_dev               = "धातोः [युग्यं च पत्त्रे]-प्रत्ययः विहितः (३.१.121)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
