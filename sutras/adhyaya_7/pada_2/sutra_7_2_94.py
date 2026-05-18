"""
7.2.94  त्वाहौ सौ  —  VIDHI

Padaccheda: त्व-अहौ सौ

"tvā" and "aha" are the ādeśas of "tva" and "asma" respectively
before su (nom. sg.). For asmad stem: replace initial [a,s,m] with [a,h,a].

त्वाहौ सौ (7.2.94)

Engine implementation:
  cond — phonemic signals only (CONSTITUTION Art. 2):
    • stem upadesha_slp1 == "asmad"
    • stem varnas currently start with [a, s, m] (not yet replaced)
    • there exists a sup pratyaya (with '7_1_28_done' = am suffix present)
    • no "7_2_94_done" tag on stem
  act — replace first 3 varnas [a, s, m] of stem with [a, h, a]
        mark stem with "7_2_94_done"
        result: stem varnas = [a, h, a, a, d]
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    """
    Find stem idx where:
      - upadesha_slp1 == "asmad"
      - varnas start with [a, s, m]
      - no 7_2_94_done tag
      - a sup pratyaya follows

    Returns stem_idx or None.
    """
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() != "asmad":
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_94_done" in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 3:
            continue
        if vs[0].slp1 != "a" or vs[1].slp1 != "s" or vs[2].slp1 != "m":
            continue
        # Check there is a sup pratyaya following
        has_sup = any(
            "sup" in state.terms[j].tags
            for j in range(i + 1, len(state.terms))
        )
        if not has_sup:
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
    # Parse "aha" in SLP1: a, h (consonant with inherent a), a
    # parse_slp1_upadesha_sequence("aha") → [mk('a'), mk_inherent_a(), mk('a')]
    # i.e. 3 varnas: a(standalone) + h(consonant) + a(inherent after h)
    # But in SLP1 "aha": a=vowel, h=consonant, a=inherent-a after h
    replacement = parse_slp1_upadesha_sequence("aha")
    # replacement should be [Varna(a), Varna(h), Varna(a-inherent)]
    # Replace first 3 varnas with the replacement
    stem.varnas = replacement + list(stem.varnas[3:])
    stem.tags.add("7_2_94_done")
    state.samjna_registry["7_2_94_asm_to_ah"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tvAhO sO",
    text_dev              = "त्वाहौ सौ",
    padaccheda_dev        = "त्व-अहौ सौ",
    why_dev               = "अस्मद्-शब्दस्य आदि-भागस्य [अ,स्,म्] स्थाने [अ,ह,अ] आदेशः "
                            "सौ परे (सूत्रम् ७.२.९४ त्वाहौ सौ)।",
    anuvritti_from        = ("7.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
