"""
7.1.23  स्वमोर्नपुंसकात्  —  VIDHI (narrow demo)

Demo slice (अतिरि कुलम्.md):
  For a napuṃsaka aṅga, drop the sup `su` (and `am`) by luk.

Engine:
  - applies when a napuṃsaka anga is followed by a sup pratyaya whose upadeśa
    is `s~` (su) or `am`.
  - performs luk by turning the sup Term into a zero-width ghost (varnas cleared,
    tag luk_lopa).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import LUK_LOPA_GHOST_TAG, term_is_sup_luk_ghost
from engine.state import State


_TARGETS = frozenset({"s~", "am"})


def _find(state: State):
    if len(state.terms) < 2:
        return None
    anga = state.terms[-2]
    pr = state.terms[-1]
    if "anga" not in anga.tags or "napuṃsaka" not in anga.tags:
        return None
    if "sup" not in pr.tags or term_is_sup_luk_ghost(pr):
        return None
    if (pr.meta.get("upadesha_slp1") or "").strip() not in _TARGETS:
        return None
    if pr.meta.get("7_1_23_luk_done"):
        return None
    return len(state.terms) - 1


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    pr = state.terms[i]
    pr.varnas.clear()
    pr.tags.add(LUK_LOPA_GHOST_TAG)
    pr.meta["7_1_23_luk_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.23",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="svamoH napuMsakAt",
    text_dev="स्वमोर्नपुंसकात्",
    padaccheda_dev="स्व-मोः / नपुंसकात्",
    why_dev="नपुंसक-अङ्गात् परयोः सु/अम्-प्रत्यययोः लुक्।",
    anuvritti_from=("7.1.20",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

