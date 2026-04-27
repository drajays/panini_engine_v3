"""
7.4.66  उरत्  —  VIDHI (narrow: abhyāsa-initial ṛ → ``a`` + *uRaṇ-rapara*)

Glass-box for *yaṅ*-reduplication where the abhyāsa still contains vocalic ṛ
(``f`` / ``F``): replace that ṛ with short ``a`` and arm **1.1.51** on the
abhyāsa *Term* (same mechanism as **6.1.87** / **7.2.114**).

Recipes must set ``state.meta["7_4_66_urat_abhyasa_arm"]`` before ``apply_rule``
so unrelated reduplication frames do not pick this up.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    if not state.meta.get("7_4_66_urat_abhyasa_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_66_urat_abhyasa_done"):
            continue
        for j, v in enumerate(t.varnas):
            if v.slp1 in {"f", "F"}:
                return ti, j
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j = hit
    t = state.terms[ti]
    t.varnas[j] = mk("A")
    t.meta["urN_rapara_pending"] = "r"
    t.meta["urN_rapara_after_index"] = j
    t.meta["7_4_66_urat_abhyasa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.4.66",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "urat",
    text_dev       = "उरत्",
    padaccheda_dev = "उरत्",
    why_dev        = "अभ्यासाद् ऋकारस्य अण्-देशः (रपरः १.१.५१) — यङ्-द्वित्व-प्रसङ्गे।",
    anuvritti_from = ("7.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
