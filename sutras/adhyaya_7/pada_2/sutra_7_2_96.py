"""
7.2.96  त्वमावेकवचने / तवममौ ङसि  —  VIDHI

Padaccheda: त्व-मौ एकवचने / तव-ममौ ङसि

Two modes for asmad stem replacement in ekavacana context:

Mode A (general ekavacana: ṭā, ṅi, am, ṅasi/at): asm → ma
  arm flag "7_2_96_ma_arm":
  Replace [a,s,m] with [m,a] (SLP1: "ma")
  Result: stem = [m, a, a, d]

Mode B (ṅas genitive singular): asm → mama
  arm flag "7_2_96_mama_arm":
  Replace [a,s,m] with [m,a,m,a] (SLP1: "mama")
  Result: stem = [m, a, m, a, a, d]

त्वमौ एकवचने / तवममौ ङसि (7.2.96)
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target_ma(state: State):
    """Find stem for 'ma' replacement (general ekavacana)."""
    if not state.meta.get("7_2_96_ma_arm"):
        return None
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() != "asmad":
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_96_done" in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 3:
            continue
        if vs[0].slp1 != "a" or vs[1].slp1 != "s" or vs[2].slp1 != "m":
            continue
        return i
    return None


def _find_target_mama(state: State):
    """Find stem for 'mama' replacement (ṅas genitive singular)."""
    if not state.meta.get("7_2_96_mama_arm"):
        return None
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() != "asmad":
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_96_done" in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 3:
            continue
        if vs[0].slp1 != "a" or vs[1].slp1 != "s" or vs[2].slp1 != "m":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_target_ma(state) is not None or _find_target_mama(state) is not None


def act(state: State) -> State:
    # Mode B (mama) takes priority — check arm flags
    i_mama = _find_target_mama(state)
    if i_mama is not None:
        stem = state.terms[i_mama]
        replacement = parse_slp1_upadesha_sequence("mama")
        stem.varnas = replacement + list(stem.varnas[3:])
        # result: [m, a, m, a, a, d]
        stem.tags.add("7_2_96_done")
        state.samjna_registry["7_2_96_asm_to_mama"] = True
        return state

    i_ma = _find_target_ma(state)
    if i_ma is not None:
        stem = state.terms[i_ma]
        replacement = parse_slp1_upadesha_sequence("ma")
        stem.varnas = replacement + list(stem.varnas[3:])
        # result: [m, a, a, d]
        stem.tags.add("7_2_96_done")
        state.samjna_registry["7_2_96_asm_to_ma"] = True
        return state

    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tvamAvekavacane",
    text_dev              = "त्वमावेकवचने",
    padaccheda_dev        = "त्व-मौ एकवचने",
    why_dev               = "अस्मद्-शब्दस्य आदि-भागस्य [अ,स्,म्] स्थाने [म,अ] (एकवचने) "
                            "वा [म,म,अ] (ङसि) आदेशः (सूत्रम् ७.२.९६)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
