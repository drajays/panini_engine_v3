"""
3.1.38  उषविदजागृभ्योऽन्यतरस्याम्  —  VIBHASHA
Kāśikā 3.1.38: उष, विद, जागृ → लिटि परतोऽन्यतरस्याम् आम् (ओषाञ्चकार, उवोष; विदाञ्चकार, विवेद; जागराञ्चकार, जजागार)
Ām goes before the liṭ placeholder (2.4.81 then luk's the liṭ); the anuprayoga is 3.1.40.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_1.sutra_3_1_35 import am_site, insert_am

LISTED = frozenset({"uza~", "vida~", "jAgf"})   # the sūtra's own list (dhātupāṭha upadeśa)


def cond(state: State) -> bool:
    return am_site(state, LISTED) is not None


def act(state: State) -> State:
    li = am_site(state, LISTED)
    if li is None:
        return state
    d = state.terms[li - 1]
    if (d.meta.get("upadesha_slp1") or "").strip() == "vida~":
        # ponytail: KV "विदेरदन्तत्वप्रतिज्ञानाद् आमि गुणो न भवति" is carried as a flag the ām path reads; SHORTCUT_LEDGER
        d.meta["adanta_pratijna_3_1_38"] = True
    return insert_am(state, li)


SUTRA = SutraRecord(
    sutra_id              = "3.1.38",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "uzavidajAgfByonyatarasyAm",
    text_dev              = "उषविदजागृभ्योऽन्यतरस्याम्",
    samagra_slp1          = "uza-vida-jAgfByaH anyatarasyAm liwi Am",
    samagra_dev           = "उष-विद-जागृभ्यः अन्यतरस्याम् लिटि आम्",
    padaccheda_dev        = "उष-विद-जागृभ्यः अन्यतरस्याम्",
    why_dev               = "उष-विद-जागृ-धातोः लिटि विकल्पेन आम्।",
    anuvritti_from        = ('3.1.35',),
    vibhasha_default      = True,
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)
register_sutra(SUTRA)
