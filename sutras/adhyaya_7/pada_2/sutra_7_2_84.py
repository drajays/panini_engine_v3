"""
7.2.84  अष्टन आ विभक्तौ  —  VIDHI

Padaccheda: अष्टनः आः विभक्तौ

अष्टन आ विभक्तौ (7.2.84)
Pāṭha: ashtadhyayi.com data.txt row i=72084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem
from engine.state import State
from phonology    import mk


def _site(state: State):
    """aṣṭan before a vibhakti (sup): its n becomes ā (aṣṭā-bhiḥ, aṣṭā-nām). Vikalpa (Kāśikā 7.2.84: aṣṭabhiḥ too)."""
    hit = anga_and_sup(state)      # no 6.4.1 gate: 6.4.8 is not gated either, and the luk / ādeśa must meet it as a rival (vipratiṣedha, para)
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "azwan") or anga.varnas[-1].slp1 != "n" or "luk_lopa" in sup.tags:
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1] = mk("A")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.84",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "azwana A viBaktO",
    text_dev              = "अष्टन आ विभक्तौ",
    samagra_slp1          = "azwanaH aNgasya viBaktO A",
    samagra_dev           = "अष्टनः अङ्गस्य विभक्तौ आ",
    padaccheda_dev        = "अष्टनः आः विभक्तौ",
    why_dev               = "(सूत्रम् 7.2.84) अष्टन आ विभक्तौ।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # aṣṭa- is the default reading; choose({"7.2.84": True}) / explore() give aṣṭā- (aṣṭau, aṣṭābhiḥ)
    vibhasha_scope        = cond,      # the question is asked only of an aṣṭan before a sup
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
