"""
7.2.88  प्रथमायाश्च द्विवचने भाषायाम्  —  VIDHI

Padaccheda: प्रथमायाः च द्विवचने भाषायाम्

For asmad stem, replace the final 'd' with long 'ā' (SLP1: "A") in
prathamā (nominative) dvivacana context in bhāṣā (spoken Sanskrit).

प्रथमायाश्च द्विवचने भाषायाम् (7.2.88)

Engine implementation:
  cond:
    • arm flag "7_2_88_arm" set in meta
    • stem upadesha_slp1 == "asmad"
    • stem has "anga" tag and ends in 'd'
    • no "7_2_88_done" tag
  act:
    • replace final 'd' varna with 'ā' (SLP1: "A")
    • add "7_2_88_done" tag to stem
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_2_88_arm"):
        return None
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() != "asmad":
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_88_done" in t.tags:
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
    # Replace final 'd' with long 'ā' (SLP1: "A")
    a_long = parse_slp1_upadesha_sequence("A")
    stem.varnas[-1] = a_long[0]
    stem.tags.add("7_2_88_done")
    state.samjna_registry["7_2_88_d_to_A"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praTamAyASca dvivacane BAzAyAm",
    text_dev              = "प्रथमायाश्च द्विवचने भाषायाम्",
    padaccheda_dev        = "प्रथमायाः च द्विवचने भाषायाम्",
    why_dev               = "अस्मद्-शब्दस्य अन्त्य-दकारस्य स्थाने दीर्घ-आकारः "
                            "प्रथमा-द्विवचने (सूत्रम् ७.२.८८ प्रथमायाश्च द्विवचने)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
