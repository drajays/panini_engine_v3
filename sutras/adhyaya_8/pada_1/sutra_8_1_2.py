"""
8.1.2  तस्य परमाम्रेडितम्  —  SAMJNA (narrow)

Teaching **corrected_prakriyas_v2** **P017**: the **second** of two identical
*anukaraṇa* **``pawat``** ``Term`` units before **``qAc``** (डाच्) receives the
*āmreḍita* stamp in ``meta`` (engine bookkeeping).

Engine:
  • ``state.meta['corrected_v2_P017_8_1_2_arm']`` (cleared in ``act``).
  • layout ``[pawat, pawat, qAc]``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

_META_ARM = "corrected_v2_P017_8_1_2_arm"
_META_STAMP = "AmreDita_8_1_2"


def _flat(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _site(state: State) -> bool:
    if len(state.terms) != 3:
        return False
    t0, t1, t2 = state.terms
    if _flat(t0) != "pawat" or _flat(t1) != "pawat":
        return False
    if (t2.meta.get("upadesha_slp1") or "").strip() != "qAc":
        return False
    if t1.meta.get(_META_STAMP):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.terms[1].meta[_META_STAMP] = True
    state.samjna_registry["8.1.2_P017_paramAmreDita_index"] = 1
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.2",
    sutra_type=SutraType.SAMJNA,
    text_slp1="tasya param AmreDitam",
    text_dev="तस्य परमाम्रेडितम्",
    padaccheda_dev="तस्य / परमाम्रेडितम्",
    why_dev="द्वितीय ``pawat`` आम्रेडित-स्मरणम् (P017)।",
    anuvritti_from=("8.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
