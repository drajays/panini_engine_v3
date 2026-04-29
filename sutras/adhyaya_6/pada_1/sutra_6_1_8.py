"""
6.1.8  लिटि धातोरनभ्यासस्य  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  In liṭ, duplicate the primary dhātu to form a reduplication frame:
    [abhyāsa, dhātu, ...].

Engine:
  - recipe arms via ``state.meta['6_1_8_lit_dvitva_arm']``.
  - inserts an `abhyasa` Term as a copy of the dhātu term, immediately before it.
"""
from __future__ import annotations

from copy import deepcopy

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    if not state.meta.get("6_1_8_lit_dvitva_arm"):
        return False
    di = _first_dhatu_index(state)
    if di is None:
        return False
    # already has abhyāsa?
    if di > 0 and "abhyasa" in state.terms[di - 1].tags:
        return False
    return True


def act(state: State) -> State:
    di = _first_dhatu_index(state)
    if di is None:
        return state
    dh = state.terms[di]
    ab = Term(
        kind=dh.kind,
        varnas=[deepcopy(v) for v in dh.varnas],
        tags=set(dh.tags) | {"abhyasa"},
        meta=dict(dh.meta),
    )
    ab.tags.discard("dhatu")
    ab.meta["6_1_8_abhyasa"] = True
    state.terms.insert(di, ab)
    state.meta["6_1_8_lit_dvitva_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.8",
    sutra_type=SutraType.VIDHI,
    text_slp1="liTi DAtor anaByAsasya",
    text_dev="लिटि धातोरनभ्यासस्य",
    padaccheda_dev="लिटि / धातोः / अनभ्यासस्य",
    why_dev="लिटि धातोः द्वित्वं (अभ्यास-प्रकरणे) — विभिदतुः।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

