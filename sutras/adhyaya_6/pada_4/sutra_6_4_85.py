"""
6.4.85  न भूसुधियोः  —  VIDHI

Padaccheda: न भू-सुधियोः

न भूसुधियोः (6.4.85)
Pāṭha: ashtadhyayi.com data.txt row i=64085 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, dhatu_aṅga, is_stem, n_vowels, samyoga_purva, vowel_initial
from phonology import mk

def _site(state: State):
    """न भूसुधियोः — no yaṇ (6.4.82 / 6.4.83) for the aṅga भू (svayambhū, with tadantavidhi) or सुधी: svayambhuvaḥ, sudhiyaḥ; वर्षाभू is 6.4.84's."""
    hit = anga_and_sup(state, "6.4.85")
    if hit is None:
        return None
    anga, sup = hit
    if is_stem(anga, "varzABU") or not vowel_initial(sup):
        return None
    return anga if is_stem(anga, "BU", "suDI", tadanta=True) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    state.blocked_sutras.update({"6.4.82", "6.4.83"})
    return state

SUTRA = SutraRecord(
    sutra_id              = "6.4.85",
    sutra_type            = SutraType.PRATISHEDHA,
    text_slp1             = "na BUsuDiyoH",
    text_dev              = "न भूसुधियोः",
    samagra_slp1          = "BUsuDiyoH aNgasya supi aci yaR na",
    samagra_dev           = "भूसुधियोः अङ्गस्य सुपि अचि यण् न",
    padaccheda_dev        = "न भू-सुधियोः",
    why_dev               = "(सूत्रम् 6.4.85) न भूसुधियोः।",
    anuvritti_from        = ('6.1.1',),
    blocks_sutra_ids      = ('6.4.82', '6.4.83'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
