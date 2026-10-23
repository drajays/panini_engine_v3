"""
6.4.84  वर्षाभ्वश्च  —  VIDHI

Padaccheda: वर्षाभ्वः च

वर्षाभ्वश्च (6.4.84)
Pāṭha: ashtadhyayi.com data.txt row i=64084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, dhatu_aṅga, is_stem, n_vowels, samyoga_purva, vowel_initial
from phonology import mk

def _site(state: State):
    """वर्षाभ्वश्च — वर्षाभू takes yaṇ before an ac-initial sup (वर्षाभ्वः), the apavāda of 6.4.77's uvaṅ; the pratiṣedha 6.4.85 spares it."""
    hit = anga_and_sup(state, "6.4.84")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "varzABU") or anga.meta.get("6_4_84_yaN_done") or not vowel_initial(sup) or anga.varnas[-1].slp1 != "U":
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1] = mk("v")
    anga.meta["6_4_84_yaN_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "6.4.84",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "varzABvaSca",
    text_dev              = "वर्षाभ्वश्च",
    samagra_slp1          = "varzABvaH aNgasya aci supi yaRaH",
    samagra_dev           = "वर्षाभ्वः अङ्गस्य अचि सुपि यणः",
    padaccheda_dev        = "वर्षाभ्वः च",
    why_dev               = "(सूत्रम् 6.4.84) वर्षाभ्वश्च।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.1.77', '6.4.77'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
