"""
6.1.96  उस्यपदान्तात्  —  VIDHI

Padaccheda: उसि अ-पदान्तात्

Before the vidhiliṅ 3pl suffix 'us' (from jus/us), the preceding 'a'/'ā'
(the vowel of the yāsuṭ-remnant 'yā' for consonant-final tanādi roots) drops,
leaving only the 'y'.

  tan + u (vikaraṇa) + yā + us  →  tan + u + y + us  →  tanuyuḥ

This is the apavāda to 6.1.87 (ādguṇaḥ: ā+u→o) for the 'yā+us' sequence
in vidhiliṅ 3pl derivation.

Engine scope: fires when a yasut_agama term ends in 'ā' (or 'A') and the
immediately following term starts with 'u' + 's' (= the 3pl liṅ suffix 'us').
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    """Return (yasut_idx, A_idx) if yā-term precedes us-term, else None."""
    for i, t in enumerate(state.terms):
        if "yasut_agama" not in t.tags:
            continue
        if not t.varnas:
            continue
        # Check last varna is 'A' (ā) or 'a'
        last = t.varnas[-1].slp1
        if last not in ("A", "a"):
            continue
        # Next term must start with 'u' (= the 'us' 3pl suffix)
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas:
            continue
        if nxt.varnas[0].slp1 != "u":
            continue
        if t.meta.get("6_1_96_done"):
            continue
        return (i, len(t.varnas) - 1)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    result = _find(state)
    if result is None:
        return state
    yasut_idx, a_idx = result
    t = state.terms[yasut_idx]
    # Drop the 'ā' (or 'a') — keep only the 'y' prefix
    t.varnas.pop(a_idx)
    t.meta["6_1_96_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "usyapadAntAt",
    text_dev              = "उस्यपदान्तात्",
    padaccheda_dev        = "उसि अ-पदान्तात्",
    why_dev               = (
        "विधिलिङि तृतीयपुरुष-बहुवचने (उस्-परे) यासुट्-अन्त्यस्य 'आ'-कारस्य लोपः — "
        "तनु-उ-या-उस् → तनु-उ-य्-उस् (तनुयुः)।"
    ),
    anuvritti_from        = ("6.1.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
