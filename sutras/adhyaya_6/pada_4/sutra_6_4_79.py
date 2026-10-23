"""
6.4.79  स्त्रियाः  —  VIDHI

Padaccheda: स्त्रियाः

स्त्रियाः (6.4.79)
Pāṭha: ashtadhyayi.com data.txt row i=64079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, dhatu_aṅga, is_stem, n_vowels, samyoga_purva, vowel_initial
from phonology import mk

def _site(state: State):
    """स्त्रियाः — the word स्त्री (with tadantavidhi) before an ac-initial sup: iyaṅ. (6.4.80 lets am / śas keep ī: स्त्रीम्, स्त्रीः.)"""
    hit = anga_and_sup(state, "6.4.79")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "strI", tadanta=True) or anga.varnas[-1].slp1 != "I" or not vowel_initial(sup) or anga.meta.get("6_4_79_done") or anga.meta.get("6_4_80_kept"):
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1:] = [mk("i"), mk("y")]            # iyaṅ replaces the final ī (ṅit: only the last letter)
    anga.meta["6_4_79_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "6.4.79",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "striyAH",
    text_dev              = "स्त्रियाः",
    samagra_slp1          = "striyAH aNgasya aci iyaN",
    samagra_dev           = "स्त्रियाः अङ्गस्य अचि इयङ्",
    padaccheda_dev        = "स्त्रियाः",
    why_dev               = "(सूत्रम् 6.4.79) स्त्रियाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
