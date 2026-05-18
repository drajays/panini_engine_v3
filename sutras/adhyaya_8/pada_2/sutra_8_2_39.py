"""
8.2.39  झलां जशोऽन्ते  —  VIDHI

Padaccheda: झलाम् जशः अन्ते

At pāda-end (avasāna), jhal consonants become jaś. For asmad pañcami eka,
the final 't' of "mat" (mad+at after 7.2.90) → 'd' (giving mad).

झलां जशोऽन्ते (8.2.39)

Engine implementation:
  cond:
    • arm flag "8_2_39_arm" set in meta
    • pada (merged term) ends in 't'
    • no "8_2_39_done" in term tags
  act:
    • replace final 't' with 'd'
    • add "8_2_39_done" to term tags
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("8_2_39_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "8_2_39_done" in t.tags:
            continue
        if not t.varnas:
            continue
        if t.varnas[-1].slp1 != "t":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    t = state.terms[i]
    d_varna = parse_slp1_upadesha_sequence("d")
    t.varnas[-1] = d_varna[0]
    t.tags.add("8_2_39_done")
    state.samjna_registry["8_2_39_t_to_d"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "JalAM jaSo'nte",
    text_dev              = "झलां जशोऽन्ते",
    padaccheda_dev        = "झलाम् जशः अन्ते",
    why_dev               = "पदान्ते झल्-व्यञ्जनस्य स्थाने जश्-व्यञ्जनः "
                            "(सूत्रम् ८.२.३९ झलां जशोऽन्ते) — त् → द्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
