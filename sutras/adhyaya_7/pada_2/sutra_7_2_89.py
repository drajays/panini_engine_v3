"""
7.2.89  योऽचि  —  VIDHI

Padaccheda: यः अचि

For asmad stem, replace the final 'd' with 'y' (SLP1: "y") before a
vowel-initial suffix (os, i, ā in tṛtīyā/saptamī ekavacana).

योऽचि (7.2.89)

Engine implementation:
  cond:
    • arm flag "7_2_89_arm" set in meta
    • stem upadesha_slp1 == "asmad"
    • stem has "anga" tag and ends in 'd'
    • no "7_2_89_done" tag
  act:
    • replace final 'd' varna with 'y' (SLP1: "y")
    • add "7_2_89_done" tag to stem

Note: After this rule, the stem ends in 'y' followed by the suffix vowel,
giving the correct sandhi (e.g. ma+y + os → mayos, ma+y + i → mayi).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_2_89_arm"):
        return None
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() != "asmad":
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_89_done" in t.tags:
            continue
        if not t.varnas:
            continue
        if t.varnas[-1].slp1 != "d":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    stem = state.terms[i]
    # Replace final 'd' with 'y' (SLP1: "y")
    y_varna = parse_slp1_upadesha_sequence("y")
    stem.varnas[-1] = y_varna[0]
    stem.tags.add("7_2_89_done")
    state.samjna_registry["7_2_89_d_to_y"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yo'ci",
    text_dev              = "योऽचि",
    padaccheda_dev        = "यः अचि",
    why_dev               = "अस्मद्-शब्दस्य अन्त्य-दकारस्य स्थाने यकारः "
                            "अचि परे (सूत्रम् ७.२.८९ योऽचि)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
