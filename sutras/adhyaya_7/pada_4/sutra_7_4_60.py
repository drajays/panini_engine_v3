"""
7.4.60  हलादिः शेषः  —  VIDHI (narrow: abhyāsa keeps first hal+vowel)

Glass-box scope for `loluv`:
  For an abhyāsa term like lUy, keep only the first consonant + the following
  vowel (drop trailing y, etc.).

When ``Term.meta["7_4_60_first_hal_only"]`` is set (e.g. *mṛj* after *urat* +
*rapara*), keep **only** the first varṇa (initial *hal*), matching the *marīmṛj*
abhyāsa trim (``marj`` → ``m``).

**P030** (*vac*+*san*): when ``state.meta['P030_7_4_60_abhyasa_vowel_only_arm']``,
an *abhyāsa* shaped ``u``/``U`` + ``c`` keeps only the vowel — gate for **7.4.59**
*hrasva* (when ``U``) then **6.1.77** with the non-*abhyāsa* ``U``… *dhātu*.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State):
    if state.meta.get("P037_7_4_60_Iw_trim_arm"):
        for ti, t in enumerate(state.terms):
            if "abhyasa" not in t.tags:
                continue
            if t.meta.get("7_4_60_haladi_done"):
                continue
            if (
                len(t.varnas) == 2
                and t.varnas[0].slp1 == "I"
                and t.varnas[1].slp1 == "w"
            ):
                return ti
        return None
    if state.meta.get("P030_7_4_60_abhyasa_vowel_only_arm"):
        for ti, t in enumerate(state.terms):
            if "abhyasa" not in t.tags:
                continue
            if t.meta.get("7_4_60_haladi_done"):
                continue
            if (
                len(t.varnas) == 2
                and t.varnas[1].slp1 == "c"
                and t.varnas[0].slp1 in {"u", "U"}
            ):
                return ti
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_60_haladi_done"):
            continue
        if t.meta.get("7_4_60_first_hal_only"):
            if t.varnas:
                return ti
            continue
        if len(t.varnas) < 2:
            continue
        # Already exactly hal + vowel — no trim (avoids R1 no-op, e.g. *ci* abhyāsa).
        if len(t.varnas) == 2:
            continue
        # Keep first two varṇas (hal + vowel expected).
        return ti
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    if state.meta.get("P037_7_4_60_Iw_trim_arm"):
        for ti, t in enumerate(state.terms):
            if "abhyasa" not in t.tags or t.meta.get("7_4_60_haladi_done"):
                continue
            if (
                len(t.varnas) == 2
                and t.varnas[0].slp1 == "I"
                and t.varnas[1].slp1 == "w"
            ):
                t.varnas = [t.varnas[0]]
                t.meta["7_4_60_haladi_done"] = True
                state.meta.pop("P037_7_4_60_Iw_trim_arm", None)
                return state
    if state.meta.get("P030_7_4_60_abhyasa_vowel_only_arm"):
        for ti, t in enumerate(state.terms):
            if "abhyasa" not in t.tags or t.meta.get("7_4_60_haladi_done"):
                continue
            if (
                len(t.varnas) == 2
                and t.varnas[1].slp1 == "c"
                and t.varnas[0].slp1 in {"u", "U"}
            ):
                t.varnas = [t.varnas[0]]
                t.meta["7_4_60_haladi_done"] = True
                state.meta.pop("P030_7_4_60_abhyasa_vowel_only_arm", None)
                return state
    ti = _find(state)
    if ti is None:
        return state
    t = state.terms[ti]
    if t.meta.get("7_4_60_first_hal_only"):
        t.varnas = [t.varnas[0]]
        t.meta.pop("7_4_60_first_hal_only", None)
    else:
        t.varnas = t.varnas[:2]
    t.meta["7_4_60_haladi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.4.60",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "halAdi SezaH",
    text_dev       = "हलादिः शेषः",
    padaccheda_dev = "हलादिः / शेषः",
    why_dev        = (
        "अभ्यासे हलादिः एव शेषः (ग्लास-बॉक्स्: द्वित्व-प्रकरणे); प०३७ च ``Iw``→``I``।"
    ),
    anuvritti_from = ("6.1.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

