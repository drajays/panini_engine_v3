"""
7.4.83  दीर्घोऽकितः  —  VIDHI (narrow: *yaṅ* *abhyāsa* *dīrgha*, P029)

JSON **P029** step 8: after **7.4.59**, lengthen the *abhyāsa* *hrasva* back to
*dīrgha* in the *yaṅ*/*akit* frame (*ya* → *yā*).

Narrow v3: ``state.meta['P029_7_4_83_abhyasa_dirgha_arm']`` + ``abhyasa`` term
whose second varṇa is *hrasva* ``a`` after leading ``y`` → replace that ``a``
with ``A``.
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
    if not state.meta.get("P029_7_4_83_abhyasa_dirgha_arm"):
        return False
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P029_7_4_83_dirgha_done"):
        return False
    if len(t.varnas) < 3:
        return False
    if t.varnas[0].slp1 != "y":
        return False
    if t.varnas[1].slp1 != "a":
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    i = _abhyasa_index(state)
    assert i is not None
    t = state.terms[i]
    t.varnas[1] = mk("A")
    t.meta["P029_7_4_83_dirgha_done"] = True
    state.meta.pop("P029_7_4_83_abhyasa_dirgha_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.83",
    sutra_type=SutraType.VIDHI,
    text_slp1="dIrGo 'kitaH",
    text_dev="दीर्घोऽकितः",
    padaccheda_dev="दीर्घः / अकितः",
    why_dev="यङ्-प्रकरणे अभ्यासस्य दीर्घः (P029)।",
    anuvritti_from=("7.4.82",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
