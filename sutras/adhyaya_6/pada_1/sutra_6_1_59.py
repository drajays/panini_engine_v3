"""
6.1.59  अनुदात्तस्य चर्दुपधस्यान्यतरस्याम्  —  VIDHI

Padaccheda: अनुदात्तस्य च ऋत्-उपधस्य अन्यतरस्याम्

अनुदात्तस्य चर्दुपधस्यान्यतरस्याम् (6.1.59)
Pāṭha: ashtadhyayi.com data.txt row i=61059 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import JHAL


def _site(state: State):
    """अनुदात्तस्य ऋदुपधस्य (धातोः) झलादावकिति: an anudātta-upadeśa dhātu whose upadhā is ṛ, before a jhal-initial pratyaya that is not kit
    (tarpitā / traptā / tarptā, kraṣṭā / karṣṭā). The am (m-it, 1.1.47) stands after the last vowel of the aṅga, the ṛ."""
    for i in range(len(state.terms) - 1):
        d, p = state.terms[i], state.terms[i + 1]
        if "dhatu" not in d.tags or d.meta.get("udatta_dhatu") or d.meta.get("6_1_59_am_done") or len(d.varnas) < 2:
            continue
        if d.varnas[-2].slp1 != "f" or "pratyaya" not in (p.tags | {p.kind}) or not p.varnas or p.varnas[0].slp1 not in JHAL:
            continue
        if {"it:kit", "origin_it:k"} & p.tags:
            continue
        return d
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state)


def act(state: State) -> State:
    d = _site(state)
    d.varnas.insert(len(d.varnas) - 1, mk("a", "am_agama"))
    d.meta["6_1_59_am_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.59",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAttasya cardupaDasyAnyatarasyAm",
    text_dev              = "अनुदात्तस्य चर्दुपधस्यान्यतरस्याम्",
    samagra_slp1          = "anudAttasya ca ft-upaDasya anyatarasyAm upadeSe Jali am akiti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनुदात्तस्य च ऋत्-उपधस्य अन्यतरस्याम् उपदेशे झलि अम् अकिति",
    padaccheda_dev        = "अनुदात्तस्य च ऋत्-उपधस्य अन्यतरस्याम्",
    why_dev               = "अनुदात्तोपदेशस्य ऋदुपधस्य धातोः झलादौ अकिति प्रत्यये परे विकल्पेन अम्-आगमः — त्रप्ता, तर्प्ता; क्रष्टा, कर्ष्टा।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    vibhasha_scope        = _new_cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
