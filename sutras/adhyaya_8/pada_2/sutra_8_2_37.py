"""
8.2.37  एकाचो बशो भष् झषन्तस्य स्ध्वोः  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  For a one-vowel (ekāc) base ending in jhaṣ (`D`), when `s` follows, replace the
  initial `g` (baś) with `G` (bhaṣ) i.e. g → gh.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    for i in range(len(state.terms) - 1):
        t = state.terms[i]
        nxt = state.terms[i + 1]
        if "dhatu" not in t.tags and "anga" not in t.tags:
            continue
        if t.meta.get("8_2_37_bash_bhash_done"):
            continue
        if not t.varnas or not nxt.varnas:
            continue
        if not any(v.slp1 == "s" for v in nxt.varnas):
            continue
        # narrow: require ending in D and starting in g
        if t.varnas[-1].slp1 != "D":
            continue
        if t.varnas[0].slp1 != "g":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[0] = mk("G")
    t.meta["8_2_37_bash_bhash_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.37",
    sutra_type=SutraType.VIDHI,
    text_slp1="ekAco baSo Baz jhazantasya sDvoH (narrow)",
    text_dev="एकाचो बशो भष् झषन्तस्य स्ध्वोः",
    padaccheda_dev="एकाचः / बशः / भष् / झषन्तस्य / स्ध्वोः",
    why_dev="सकारपरे झषन्त-एकाच्-धातोः बश् → भष् (ग→घ) — जिघृक्षति।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

