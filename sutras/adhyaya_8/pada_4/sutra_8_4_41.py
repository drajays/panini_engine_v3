"""
8.4.41  ष्टुना ष्टुः  —  VIDHI (narrow demo)

Demo slice:
  After ṣatva (8.3.59) yields a retroflex sibilant ``z`` (ष्), a following
  dental ``t`` becomes retroflex ``w`` (ट्).  This is the final step in
  *अध्यगीष्ट* (aDhyagIzwa).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    if not state.tripadi_zone:
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if "8_4_41_done" in t.meta:
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "z" and vs[i + 1].slp1 == "t":
            return i + 1
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("w")
    t.meta["8_4_41_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.41",
    sutra_type=SutraType.VIDHI,
    text_slp1="zwunA zwuH",
    text_dev="ष्टुना ष्टुः",
    padaccheda_dev="ष्टुना / ष्टुः",
    why_dev="ष्-समीपे तकारस्य टकारादेशः (त्रिपादी)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

