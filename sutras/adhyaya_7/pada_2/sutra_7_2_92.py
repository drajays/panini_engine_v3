"""
7.2.92  युवावौ द्विवचने  —  VIDHI

Padaccheda: युव-आवौ द्विवचने

In dvivacana context for yuzmad/asmad, replace the first three varnas
[a, s, m] of the asmad stem with [ā, v, a] (SLP1: "Ava").

युवावौ द्विवचने (7.2.92)

Engine implementation:
  cond:
    • arm flag "7_2_92_arm" set in meta
    • stem upadesha_slp1 == "asmad"
    • stem varnas start with [a, s, m]
    • no "7_2_92_done" tag
  act:
    • replace first 3 varnas [a,s,m] with parse("Ava") = [ā,v,a]
    • result: stem = [ā, v, a, a, d]
    • add "7_2_92_done" tag to stem
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_2_92_arm"):
        return None
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() != "asmad":
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_92_done" in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 3:
            continue
        if vs[0].slp1 != "a" or vs[1].slp1 != "s" or vs[2].slp1 != "m":
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
    # Replace [a,s,m] with [ā,v,a] (SLP1: "Ava")
    replacement = parse_slp1_upadesha_sequence("Ava")
    stem.varnas = replacement + list(stem.varnas[3:])
    # result: [ā, v, a, a, d]
    stem.tags.add("7_2_92_done")
    state.samjna_registry["7_2_92_asm_to_Ava"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yuvAvO dvivacane",
    text_dev              = "युवावौ द्विवचने",
    padaccheda_dev        = "युव-आवौ द्विवचने",
    why_dev               = "अस्मद्-शब्दस्य आदि-भागस्य [अ,स्,म्] स्थाने [आ,व,अ] आदेशः "
                            "द्विवचने (सूत्रम् ७.२.९२ युवावौ द्विवचने)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
