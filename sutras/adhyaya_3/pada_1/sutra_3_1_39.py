"""
3.1.39  भीह्रीभृहुवां श्लुवच्च  —  VIBHASHA

Kāśikā: "… एतेभ्यो लिटि परत आम् प्रत्ययो भवत्यन्यतरस्याम्, श्लाविव चास्मिन् कार्यं भवति। किं पुनस्तत्? द्वित्वमित्त्वं च। बिभयाञ्चकार, बिभाय। जिह्रयाञ्चकार, जिह्राय। बिभराञ्चकार, बभार। जुहवाञ्चकार, जुहाव॥"
Ām goes before the liṭ placeholder (3.1.35 insert_am); "as if before ślu" (ślāviva) is the atideśa: the dhātu takes the
``slu_replaced_sap`` marker that 6.1.10 (dvitva) and 7.4.76 (bhṛñām it) read -> bibhayāñcakāra, bibharāñcakāra.

Pāṭha: ashtadhyayi.com data.txt row i=31039 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_1.sutra_3_1_35 import am_site, insert_am

LISTED = frozenset({"YiBI", "hrI", "quBfY", "hu"})   # the sūtra's own list (dhātupāṭha upadeśa)


def cond(state: State) -> bool:
    return am_site(state, LISTED) is not None


def act(state: State) -> State:
    li = am_site(state, LISTED)
    if li is None:
        return state
    state.terms[li - 1].meta["slu_replaced_sap"] = True      # ślāviva: the ślu-kārya (dvitva, ittva) follows
    return insert_am(state, li)


SUTRA = SutraRecord(
    sutra_id              = "3.1.39",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "BIhrIBfhuvAM Sluvacca",
    text_dev              = "भीह्रीभृहुवां श्लुवच्च",
    samagra_slp1          = "BI-hrI-Bf-huvAm Sluvat ca liwi Am anyatarasyAm",
    samagra_dev           = "भी-ह्री-भृ-हुवाम् श्लुवत् च लिटि आम् अन्यतरस्याम्",
    padaccheda_dev        = "भी-ह्री-भृ-हुवाम् श्लु-वत् च",
    why_dev               = "भी-ह्री-भृ-हु-धातोः लिटि विकल्पेन आम्, श्लौ इव द्वित्वम् (बिभयाञ्चकार)।",
    anuvritti_from        = ('3.1.35',),
    vibhasha_default      = True,
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)
register_sutra(SUTRA)
