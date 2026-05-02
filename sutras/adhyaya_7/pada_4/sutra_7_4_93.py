"""
7.4.93  सन्वल्लघुनि चङ्परेऽनग्लोपे  —  VIDHI (narrow: P037 *caṅ*-pare *abhyāsa*)

Teaching **P037** step 13: before the non-geminate *caṅ* context, the *laghu*
*abhyāsa* for *aṭ* is shaped like the *san* pattern — here modelled as initial
``a`` → ``i`` on the *abhyāsa* copy **aw** (``A`` → ``a`` already via **7.4.59**).

Narrow: ``state.meta['P037_7_4_93_sanvat_arm']`` + first ``abhyasa`` ``Term``
with varṇas ``a`` + ``w`` (*aṭ* segment) → ``i`` + ``w``.
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
    if not state.meta.get("P037_7_4_93_sanvat_arm"):
        return False
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P037_7_4_93_done"):
        return False
    if len(t.varnas) != 2:
        return False
    return t.varnas[0].slp1 == "a" and t.varnas[1].slp1 == "w"


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    i = _abhyasa_index(state)
    assert i is not None
    t = state.terms[i]
    t.varnas[0] = mk("i")
    t.meta["P037_7_4_93_done"] = True
    state.meta.pop("P037_7_4_93_sanvat_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.93",
    sutra_type=SutraType.VIDHI,
    text_slp1="sanvad laghuni caGpare'naglope",
    text_dev="सन्वल्लघुनि चङ्परेऽनग्लोपः",
    padaccheda_dev="सनिवत् लघुनि चङ्परि",
    why_dev="चङ्परे अभ्यास-laghu-संस्कारः (प०३७ *aṭ*: ``aw``→``iw``)।",
    anuvritti_from=("7.4.92",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
