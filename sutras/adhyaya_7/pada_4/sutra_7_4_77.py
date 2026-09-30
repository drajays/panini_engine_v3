"""
7.4.77  अर्तिपिपर्त्योश्च  —  VIDHI (apavāda of 7.4.66 उरत्, in श्लौ)

Padaccheda: अर्ति-पिपर्त्योः च

Extends **7.4.76**'s इत्-आदेश to ऋ (अर्ति) and पॄ/पृ (पिपर्ति): their गण-3
*abhyāsa* ऋ/ॠ becomes इ too — इयर्ति (नोट: अच्-आदि ऋ की अभ्यास-उवङ्/इयङ्
सन्धि अभी general नहीं है, केवल इत्व यहाँ), पिपर्ति, पिपृतः/पिपूर्तः.

Engine: same mechanism as **7.4.76**, root-scoped to ``f`` (ऋ) / ``pF``
(पॄ) / ``pf`` (पृ) after *it*-lopa.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 74077 · अर्तिपिपर्त्योश्च
              padaccheda: अर्ति-पिपर्त्योः च
              anuvṛtti:   74076: इत् | 74075: श्लौ | 74058: अभ्यासस्य
  Source #2 — Kāśikā 7.4.77 udāharaṇa:
                इयर्ति
                पिपर्ति
  Reference record: sutra_ref_out/7_4_77.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_TARGET_ROOTS = {"f", "pF", "pf"}


def _root_varnas(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _find(state: State):
    dhatu = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dhatu is None or _root_varnas(dhatu) not in _TARGET_ROOTS:
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
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
    state.terms[ti].varnas[j] = mk("i")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.77",
    sutra_type            = SutraType.VIDHI,
    text_slp1              = "artipipartyoSca",
    text_dev               = "अर्तिपिपर्त्योश्च",
    padaccheda_dev         = "अर्ति-पिपर्त्योः च",
    why_dev                = "ऋतेः पॄतेश्च अभ्यासस्य ऋकारस्य इत्-आदेशः श्लौ (इयर्ति, पिपर्ति) — ७.४.७६ भृञामित्-अनुवृत्तिः।",
    anuvritti_from         = ("7.4.76", "7.4.75", "7.4.58"),
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
