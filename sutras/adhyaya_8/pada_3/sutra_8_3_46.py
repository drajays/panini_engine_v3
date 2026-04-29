"""
8.3.46  (narrow demo) — k+s → k+ṣ in desideratives.

The source JSON for *jighṛkṣati* references 8.3.46 as the ṣatva step on the `s`
of the san-pratyaya after `k` (from 8.2.41).  This repository already has a
general 8.3.59 ṣatva slice aimed at sup/pratyaya after vowels; that does not
cover this consonantal k+s locus.

So we provide a **recipe-armed** narrow slice:
  - after pada-merge, if the single term contains the sequence `k s`, replace
    that `s` by `S` (ष).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    if not state.tripadi_zone:
        return None
    if not state.meta.get("8_3_46_ksatva_arm"):
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("8_3_46_ksatva_done"):
        return None
    for i in range(1, len(t.varnas)):
        if t.varnas[i - 1].slp1 == "k" and t.varnas[i].slp1 == "s":
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("S")
    t.meta["8_3_46_ksatva_done"] = True
    state.meta["8_3_46_ksatva_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.46",
    sutra_type=SutraType.VIDHI,
    text_slp1="(narrow) k+s -> k+z (desiderative)",
    text_dev="(डेमो) क्स-प्रसङ्गे षत्वम्",
    padaccheda_dev="(डेमो) क् + स् → क् + ष्",
    why_dev="जिघृक्षति-प्रसङ्गे क्+स् → क्+ष् (डेमो-slice)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

