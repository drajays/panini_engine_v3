"""
8.4.53  झलां जश् झशि  —  VIDHI (narrow demo)

Demo slice (रुणद्धि .md):
  When a jhal consonant (here: D = ध्) is immediately followed by a jhaś
  consonant (here: D from 8.2.40), change the first to its jaś counterpart
  (here: d).

So: ... D D ... → ... d D ...
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


_JHAL_TO_JAS = {
    "D": "d",  # dh -> d (for this demo)
}


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_4_53_jhalam_jash_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 in _JHAL_TO_JAS and vs[i + 1].slp1 == "D":
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk(_JHAL_TO_JAS[t.varnas[i].slp1])
    t.meta["8_4_53_jhalam_jash_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.53",
    sutra_type=SutraType.VIDHI,
    text_slp1="JhalAM jaS JhaSi",
    text_dev="झलां जश् झशि",
    padaccheda_dev="झलाम् / जश् / झशि",
    why_dev="झशि परे झल्-वर्णस्य जश्-आदेशः (डेमो: ध् → द्)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

