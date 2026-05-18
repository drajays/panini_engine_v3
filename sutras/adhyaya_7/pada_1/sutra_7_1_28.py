"""
7.1.28  ङे प्रथमयोरम्  —  VIDHI

Padaccheda: ङे (लुप्तषष्ठ्यन्तनिर्देशः) प्रथमयोः अम्

For pronoun stems (asmad/yuzmad) in nominative singular context,
replace the sup pratyaya with 'am'.

ङे प्रथमयोरम् (7.1.28)

Engine implementation:
  cond — phonemic signals only (CONSTITUTION Art. 2):
    • stem upadesha_slp1 is "asmad" or "yuzmad" (sarvanama pronoun)
    • pratyaya has sup + upadesha tags and varnas are one of the
      eligible forms (after it-lopa):
        - starts with 's' (su → s after anunāsika-u lopa)
        - is exactly ['O'] (au dvivacana prathamā/dvitīyā)
        - starts with 'a','s' / is ['a','s'] (jas → as after j-it lopa)
        - is ['e'] (Ne → e after N-it lopa; dative ekavacana)
      The arm flag "7_1_28_au_arm" enables 'O' replacement.
      The arm flag "7_1_28_as_arm" enables 'as' replacement.
      The arm flag "7_1_28_e_arm"  enables 'e' replacement.
      No arm needed for 's' (original su path — default behaviour).
    • no "7_1_28_done" tag on the pratyaya
  act — replace pratyaya varnas with [a, m]; set upadesha_slp1 = "am"
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence

# Pronoun stems eligible for this substitution
_ELIGIBLE_STEMS = {"asmad", "yuzmad"}


def _find_target(state: State):
    """
    Find (stem_idx, pratyaya_idx) where:
      - stem has upadesha_slp1 in _ELIGIBLE_STEMS
      - pratyaya has sup + upadesha tags
      - pratyaya not yet replaced (no '7_1_28_done' tag)
      - pratyaya matches one of the eligible upadesha forms
        (considering arm flags for non-su paths)

    Returns (stem_idx, pratyaya_idx) or None.
    """
    stem_idx = None
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _ELIGIBLE_STEMS and "anga" in t.tags:
            stem_idx = i
            break
    if stem_idx is None:
        return None

    for j in range(stem_idx + 1, len(state.terms)):
        t = state.terms[j]
        if "sup" not in t.tags or "upadesha" not in t.tags:
            continue
        if "7_1_28_done" in t.tags:
            continue

        vs = t.varnas
        if not vs:
            continue

        # Original su path: pratyaya starts with 's' (su after anunāsika-u lopa)
        if vs[0].slp1 == "s":
            return (stem_idx, j)

        # au / auT dvivacana path (prathamā and dvitīyā dvivacana)
        # enabled by arm flag "7_1_28_au_arm"
        if state.meta.get("7_1_28_au_arm") and vs[0].slp1 == "O":
            return (stem_idx, j)

        # jas (→ as after j-it lopa) path for bahuvacana prathamā
        # enabled by arm flag "7_1_28_as_arm"
        if state.meta.get("7_1_28_as_arm"):
            upd = (t.meta.get("upadesha_slp1") or "").strip()
            if upd == "jas" and len(vs) == 2 and vs[0].slp1 == "a" and vs[1].slp1 == "s":
                return (stem_idx, j)

        # Ne / ṅe (→ e after N-it lopa) dative singular path
        # enabled by arm flag "7_1_28_e_arm"
        if state.meta.get("7_1_28_e_arm"):
            if len(vs) == 1 and vs[0].slp1 == "e":
                return (stem_idx, j)

    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    target = _find_target(state)
    if target is None:
        return state
    _stem_idx, pr_idx = target
    pr = state.terms[pr_idx]
    # Replace varnas with [a, m]
    pr.varnas = parse_slp1_upadesha_sequence("am")
    # Update upadesha_slp1 so 6.1.107 recognises the 'am' suffix
    pr.meta["upadesha_slp1"] = "am"
    # Mark done; keep structural tags
    pr.tags.add("7_1_28_done")
    # Ensure sup / vibhakti / sarvanamasthana tags are preserved
    pr.tags.add("sup")
    pr.tags.add("upadesha")
    pr.tags.discard("has_halant_it")   # no longer relevant after replacement
    state.samjna_registry["7_1_28_am_substitution"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ne praTamayoram",
    text_dev              = "ङे प्रथमयोरम्",
    padaccheda_dev        = "ङे (लुप्तषष्ठ्यन्तनिर्देशः) प्रथमयोः अम्",
    why_dev               = "अस्मद्/युष्मद्-शब्दयोः सुँ-प्रत्ययस्य स्थाने अम् आदेशः "
                            "(सूत्रम् ७.१.२८ ङे प्रथमयोरम्)।",
    anuvritti_from        = ("7.1.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
