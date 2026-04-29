"""
3.4.102  लिङः सीयुट्  —  VIDHI (narrow demo)

Demo slice (भित्सीष्ट / BitzIzwa):
  For āśīr-liṅ, insert the augment **sīyut** before the *tiṅ* ādeśa.

Narrow v3 representation:
  We model the augment as surface ``sI`` (dropping ``y`` in this demo slice),
  because this repository currently does not carry an operational *vyor-lopa*
  rule in 6.1.x for this path. The key observable effect for downstream
  tripāḍī is: a long vowel ``I`` followed by ``s`` from suṭ (3.4.107).

Engine:
  - recipe arms via ``state.meta['3_4_102_sIyuw_arm']``.
  - inserts a pratyaya Term tagged ``ling_sIyuw`` immediately before the final
    *tiṅ* term.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_tin_index(state: State) -> int | None:
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" in t.tags:
            return i
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG"}:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("3_4_102_sIyuw_arm"):
        return False
    if not state.meta.get("ashir_liG"):
        return False
    # avoid duplicates
    if any("ling_sIyuw" in t.tags for t in state.terms):
        return False
    return _find_tin_index(state) is not None


def act(state: State) -> State:
    idx = _find_tin_index(state)
    if idx is None:
        return state
    sI = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("sI"),
        tags={"pratyaya", "ling_sIyuw"},
        meta={"upadesha_slp1": "sI"},
    )
    state.terms.insert(idx, sI)
    state.meta["3_4_102_sIyuw_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.102",
    sutra_type=SutraType.VIDHI,
    text_slp1="liGaH sIyuw",
    text_dev="लिङः सीयुट्",
    padaccheda_dev="लिङः / सीयुट्",
    why_dev="आशीर्लिङि तिङ्-आदेशस्य पुरः सीयुट्-आगमः (डेमो: भित्सीष्ट)।",
    anuvritti_from=("3.4.77", "3.4.78"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

