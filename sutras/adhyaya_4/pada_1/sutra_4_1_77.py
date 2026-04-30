"""
4.1.77  यङश्चाप्  —  VIDHI (narrow: *yuvan* → strī-pratyaya *tip*)

Śāstra: within the *strī* domain (**4.1.3**), certain bases take specific
feminine suffixes.  This repository needs only a narrow slice to support
``split_prakriyas_11/P006.json``:

  yuvan + tip → yuvan + ti (after **1.3.3**/**1.3.9**) → yuvatiḥ (with other rules)

Engine (glass-box):
  - requires **4.1.3** on ``adhikara_stack`` and a primary *prātipadika* tagged
    ``strīliṅga`` (set by the recipe for this demo).
  - fires only when the base's ``meta['upadesha_slp1']`` is exactly ``'yuvan'``.
  - inserts a *pratyaya* ``Term`` with upadeśa ``tip`` (final ``p`` = *it* by
    **1.3.3**; lopa by **1.3.9**).

This is intentionally narrow (CONSTITUTION: avoid speculative bundles).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _in_stri_adhikara(state: State) -> bool:
    return any(e.get("id") == "4.1.3" for e in state.adhikara_stack)


def _target_base_index(state: State) -> int | None:
    if not _in_stri_adhikara(state):
        return None
    if any(t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "tip" for t in state.terms):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "prātipadika" not in t.tags or "anga" not in t.tags:
            continue
        if "strīliṅga" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "yuvan":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _target_base_index(state) is not None


def act(state: State) -> State:
    idx = _target_base_index(state)
    if idx is None:
        return state
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("tip"),
        tags={"pratyaya", "upadesha", "stri_pratyaya"},
        meta={"upadesha_slp1": "tip"},
    )
    state.terms.insert(idx + 1, pr)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.77",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "yaGaz cAp",
    text_dev       = "यङश्चाप्",
    padaccheda_dev = "यङः / च / आप्",
    why_dev        = "युवन्-प्रातिपदिकात् स्त्रियाम् ति(प्) प्रत्ययः (नर-नारी-निर्देशे; narrow demo)।",
    anuvritti_from = ("4.1.3",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

