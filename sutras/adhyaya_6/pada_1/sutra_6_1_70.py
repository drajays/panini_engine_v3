"""
6.1.70  लोपो व्योर्वलि  —  VIDHI (narrow slice for P029; JSON mislabels as **6.1.66**)

Sources consulted:
- ashtadhyayi.com data.txt row i=601070
- Kāśikā: लोपो व्योर्वलि (यङ्-य्-लोपः वर-पूर्वम्)
- Cross-validation: tests/unit/test_yAyAvaraH_yang_varac.py (P029 arm),
  tests/unit/test_yAyAvar_yang_varac_purvavidhau_lesson.py (structural *varac*)

Authentic **6.1.66** in this repo is a different narrow rule (*apṛkta-hal* before *su*).

Glass-box for **P029** (*यायावर*): elide stem-final **y** (*vy*) when immediately
before **v** (start of *vara* after *it*-lopa), matching the teaching trace
“*yā+yā+ya+vara* → *yā+yā+vara*”.

Arms: ``state.meta['P029_6_1_70_vy_lopa_arm']``.

Structural: *aṅga* final ``y`` immediately before *varac* / ``vara`` (*yāyāvar*
lesson) — same *vyor vali* slice without an arm flag.

**P038** (*paceran*): ``state.meta['P038_6_1_70_y_before_r_arm']`` — elide final ``y``
on the *sīyuṭ* residue before *tiṅ* ``ran`` (``y`` + ``r`` …).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vareya_1_1_58 import (
    aca_sthanivat_blocks_yakaralopa,
    is_vyor_vali_following,
    vyor_vali_initial_of_following,
)


def _stem_index_p038(state: State) -> int | None:
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


def _varac_upadesha(term) -> bool:
    up = (term.meta.get("upadesha_slp1") or "").strip()
    return up in {"varac", "vara"} or ("krt" in term.tags and term.varnas and term.varnas[0].slp1 == "v")


def _stem_index_y_before_varac(state: State) -> int | None:
    """Final ``y`` on aṅga/dhātu before val (varac or vyor-initial): structural, no arm."""
    return _stem_index_y_before_v_krt(state, done_key="6_1_70_vy_lopa_done")


def _stem_index_y_before_v_krt(state: State, *, done_key: str) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" in t.tags:
            continue
        if "dhatu" not in t.tags or "anga" not in t.tags:
            continue
        if t.meta.get(done_key):
            continue
        if aca_sthanivat_blocks_yakaralopa(state, t):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "y":
            continue
        nxt = state.terms[i + 1]
        ini = vyor_vali_initial_of_following(nxt)
        if ini is not None and is_vyor_vali_following(ini):
            return i
        if _varac_upadesha(nxt):
            return i
    return None


def cond(state: State) -> bool:
    return (
        _stem_index_p038(state) is not None
        or _stem_index_y_before_varac(state) is not None
    )


def act(state: State) -> State:
    i = _stem_index_p038(state)
    if i is not None:
        t = state.terms[i]
        del t.varnas[-1]
        t.meta["P038_6_1_70_y_lopa_done"] = True
        return state
    i = _stem_index_y_before_varac(state)
    if i is None:
        return state
    t = state.terms[i]
    del t.varnas[-1]
    t.meta["6_1_70_vy_lopa_done"] = True
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
