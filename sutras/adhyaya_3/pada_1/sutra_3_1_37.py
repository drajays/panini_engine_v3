"""
3.1.37  दयायासश्च  —  VIDHI
Kāśikā 3.1.37: "एतेभ्यश्च लिटि परत आम् प्रत्ययो भवति। दयाञ्चक्रे। पलायाञ्चक्रे। आसाञ्चक्रे।"
Ām goes before the liṭ placeholder (2.4.81 then luk's the liṭ); the anuprayoga is 3.1.40.

Pāṭha: ashtadhyayi.com data.txt row i=31037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_1.sutra_3_1_35 import am_site, insert_am

LISTED = frozenset({"daya~", "aya~", "Asa~"})   # the sūtra's own list (dhātupāṭha upadeśa)


def cond(state: State) -> bool:
    return am_site(state, LISTED) is not None


def act(state: State) -> State:
    li = am_site(state, LISTED)
    return state if li is None else insert_am(state, li)


SUTRA = SutraRecord(
    sutra_id              = "3.1.37",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "dayAyAsaSca",
    text_dev              = "दयायासश्च",
    samagra_slp1          = "dayAyAsaH ca liwi Am",
    samagra_dev           = "दयायासः च लिटि आम्",
    padaccheda_dev        = "दय-अय-आसः च",
    why_dev               = "दय-अय-आस्-धातोः लिटि आम् (आसाञ्चक्रे)।",
    anuvritti_from        = ('3.1.35',),
    cond                  = cond,
    act                   = act,
)
register_sutra(SUTRA)
