"""
6.1.70  लोपो व्योर्वलि  —  VIDHI (narrow slice for P029; JSON mislabels as **6.1.66**)

Authentic **6.1.66** in this repo is a different narrow rule (*apṛkta-hal* before *su*).

Glass-box for **P029** (*यायावर*): elide stem-final **y** (*vy*) when immediately
before **v** (start of *vara* after *it*-lopa), matching the teaching trace
“*yā+yā+ya+vara* → *yā+yā+vara*”.

Arms: ``state.meta['P029_6_1_70_vy_lopa_arm']``.

**P038** (*paceran*): ``state.meta['P038_6_1_70_y_before_r_arm']`` — elide final ``y``
on the *sīyuṭ* residue before *tiṅ* ``ran`` (``y`` + ``r`` …).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _stem_index_p038(state: State) -> int | None:
    if not state.meta.get("P038_6_1_70_y_before_r_arm"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "ling_sIyuw" not in t.tags:
            continue
        if t.meta.get("P038_6_1_70_y_lopa_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "y":
            continue
        nxt = state.terms[i + 1]
        if nxt.varnas and nxt.varnas[0].slp1 == "r":
            return i
    return None


def _stem_index_p029(state: State) -> int | None:
    if not state.meta.get("P029_6_1_70_vy_lopa_arm"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" in t.tags:
            continue
        if "dhatu" not in t.tags or "anga" not in t.tags:
            continue
        if t.meta.get("P029_6_1_70_vy_lopa_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "y":
            continue
        nxt = state.terms[i + 1]
        if nxt.varnas and nxt.varnas[0].slp1 == "v":
            return i
    return None


def cond(state: State) -> bool:
    return _stem_index_p038(state) is not None or _stem_index_p029(state) is not None


def act(state: State) -> State:
    i = _stem_index_p038(state)
    if i is not None:
        t = state.terms[i]
        del t.varnas[-1]
        t.meta["P038_6_1_70_y_lopa_done"] = True
        state.meta.pop("P038_6_1_70_y_before_r_arm", None)
        return state
    i = _stem_index_p029(state)
    if i is None:
        return state
    t = state.terms[i]
    del t.varnas[-1]
    t.meta["P029_6_1_70_vy_lopa_done"] = True
    state.meta.pop("P029_6_1_70_vy_lopa_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.70",
    sutra_type=SutraType.VIDHI,
    text_slp1="lopo vyor vali (P029 narrow)",
    text_dev="लोपो व्योर्वलि",
    padaccheda_dev="लोपः / व्योः / वलि",
    why_dev="यङ्-अन्त्य-य्-लोपः वर-पूर्वः (P029); य्-लोपः र्-पूर्वः (P038)।",
    anuvritti_from=("6.1.64",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
