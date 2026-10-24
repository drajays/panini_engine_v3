"""
3.1.103  अर्यः स्वामिवैश्ययोः  —  VIDHI

Padaccheda: अर्यः स्वामि-वैश्ययोः

Krt suffix rule from dhatu: अर्यः स्वामिवैश्ययोः (103)
Pāṭha: ashtadhyayi.com data.txt row i=31103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem
from engine.vivaksha import vivaksita
from phonology import mk

def cond(state: State) -> bool:
    """ṛ → yat for a master or a merchant (aryaH svāmī / vaiśyaḥ); nipātana."""
    return kftya_open(state, "3.1.103") and vivaksita(state, "artha", "svAmivESya") and kftya_stem(state) == "f"


def act(state: State) -> State:
    return kftya_attach(state, "3.1.103", "yat")


SUTRA = SutraRecord(
    sutra_id              = "3.1.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aryaH svAmivESyayoH",
    text_dev              = "अर्यः स्वामिवैश्ययोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH aryaH svAmi-vESyayoH kft yat anupasarge",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः अर्यः स्वामि-वैश्ययोः कृत् यत् अनुपसर्गे",
    padaccheda_dev        = "अर्यः स्वामि-वैश्ययोः",
    why_dev               = "धातोः [अर्यः स्वामिवैश्ययोः]-प्रत्ययः विहितः (३.१.103)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
