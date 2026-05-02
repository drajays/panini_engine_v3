"""
3.4.102  लिङः सीयुट्  —  VIDHI (narrow demo)

Demo slice (भित्सीष्ट / BitzIzwa):
  For āśīr-liṅ, insert the augment **sīyut** before the *tiṅ* ādeśa.

**P038** (*vidhi-liṅ*, *paceran*): when ``vidhi_liG`` is set, insert full ``sIyuw``
before the ``liG`` *lakāra* placeholder (then **3.4.78** replaces ``liG``).

Narrow v3 representation (*āśīr* path):
  We model the augment as surface ``sI`` (dropping ``y`` in this demo slice),
  because this repository currently does not carry an operational *vyor-lopa*
  rule in 6.1.x for that path. The key observable effect for downstream
  tripāḍī is: a long vowel ``I`` followed by ``s`` from suṭ (3.4.107).

Engine:
  - recipe arms via ``state.meta['3_4_102_sIyuw_arm']``.
  - inserts a pratyaya Term tagged ``ling_sIyuw`` immediately before the final
    *tiṅ* term (``ashir_liG``) **or** before ``liG`` (``vidhi_liG``).
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


def _find_liG_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "liG":
            continue
        if "lakAra_pratyaya_placeholder" not in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("3_4_102_sIyuw_arm"):
        return False
    if any("ling_sIyuw" in t.tags for t in state.terms):
        return False
    if state.meta.get("ashir_liG"):
        return _find_tin_index(state) is not None
    if state.meta.get("vidhi_liG"):
        return _find_liG_index(state) is not None
    return False


def act(state: State) -> State:
    if state.meta.get("ashir_liG"):
        idx = _find_tin_index(state)
        slp = "sI"
    elif state.meta.get("vidhi_liG"):
        idx = _find_liG_index(state)
        slp = "sIyuw"
    else:
        return state
    if idx is None:
        return state
    sI = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(slp),
        tags={"pratyaya", "ling_sIyuw"},
        meta={"upadesha_slp1": slp},
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
    why_dev="लिङि सीयुट्-आगमः — आशीर्लिङ् (भित्सीष्ट) अथवा विधि-लिङ् (P038)।",
    anuvritti_from=("3.4.77", "3.4.78"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

