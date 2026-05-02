"""
7.4.94  दीर्घो लघोः  —  VIDHI (narrow: P037 *abhyāsa-laghu*)

Teaching **P037** step 14: lengthen the *hrasva* onset of the *abhyāsa* after
**7.4.93** so ``i`` → ``ī`` (*ik* represented as ``I`` in SLP1).

Narrow: ``state.meta['P037_7_4_94_dirgha_arm']`` + first ``abhyasa`` with
leading ``i`` before ``w`` → ``I`` + ``w``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _abhyasa_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "abhyasa" in t.tags:
            return i
    return None


def _site(state: State) -> bool:
    if not state.meta.get("P037_7_4_94_dirgha_arm"):
        return False
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P037_7_4_94_done"):
        return False
    if len(t.varnas) != 2:
        return False
    return t.varnas[0].slp1 == "i" and t.varnas[1].slp1 == "w"


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    i = _abhyasa_index(state)
    assert i is not None
    t = state.terms[i]
    t.varnas[0] = mk("I")
    t.meta["P037_7_4_94_done"] = True
    state.meta.pop("P037_7_4_94_dirgha_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.94",
    sutra_type=SutraType.VIDHI,
    text_slp1="dIrgho laghoH",
    text_dev="दीर्घो लघोः",
    padaccheda_dev="दीर्घः / लघोः",
    why_dev="अभ्यास-laghu-वर्णस्य दीर्घः (प०३७: ``iw``→``Iw``)।",
    anuvritti_from=("7.4.93",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
