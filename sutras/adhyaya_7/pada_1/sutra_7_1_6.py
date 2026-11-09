"""
7.1.6  शीङो रुट्  —  VIDHI

Padaccheda: शीङः रुट्

शीङो रुट् (7.1.6)
Pāṭha: ashtadhyayi.com data.txt row i=71006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_DONE = "7_1_6_rut_done"


def _target(state: State):
    """The a-initial tiṅ (jhi's ādeśa at-) after शीङ्: शे + रत् + ए → शेरते (Kāśikā 7.1.6)."""
    if len(state.terms) < 2:
        return None
    dhatu, affix = state.terms[-2], state.terms[-1]
    if "dhatu" not in dhatu.tags or (dhatu.meta.get("upadesha_slp1") or "").replace("~", "").strip() != "SIN":
        return None
    if "pratyaya" not in affix.tags or not affix.varnas or affix.varnas[0].slp1 != "a" or affix.meta.get(_DONE):
        return None
    return affix


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    affix = _target(state)
    affix.varnas.insert(0, parse_slp1_upadesha_sequence("r")[0])      # ṭit: the āgama stands before the at
    affix.meta[_DONE] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.6",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "SINo ruw",
    text_dev              = "शीङो रुट्",
    samagra_slp1          = "SINaH aNgAt JaH ataH rUw",
    samagra_dev           = "शीङः अङ्गात् झः अतः रूट्",
    padaccheda_dev        = "शीङः रुट्",
    why_dev               = "(सूत्रम् 7.1.6) शीङो रुट्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
