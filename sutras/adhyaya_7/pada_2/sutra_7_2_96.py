"""
7.2.96  तवममौ ङसि  —  VIDHI

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
Pāṭha: ashtadhyayi.com data.txt row i=72096 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from engine.pronoun_stem import PRONOUN_PREFIX, prefix_len, stem_key
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target_ma(state: State):
    """Find stem for 'ma' replacement (general ekavacana)."""
    if not state.meta.get("7_2_96_ma_arm"):
        return None
    for i, t in enumerate(state.terms):
        if stem_key(t) not in PRONOUN_PREFIX:
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_96_done" in t.tags:
            continue
        if not prefix_len(t):
            continue
        return i
    return None


def _find_target_mama(state: State):
    """Find stem for 'mama' replacement (ṅas genitive singular)."""
    if not state.meta.get("7_2_96_mama_arm"):
        return None
    for i, t in enumerate(state.terms):
        if stem_key(t) not in PRONOUN_PREFIX:
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_96_done" in t.tags:
            continue
        if not prefix_len(t):
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
        replacement = parse_slp1_upadesha_sequence({"asmad": "mama", "yuzmad": "tava"}[stem_key(stem)])
        stem.varnas = replacement + list(stem.varnas[prefix_len(stem):])
        # result: [m, a, m, a, a, d]
        stem.tags.add("7_2_96_done")
        state.samjna_registry["7_2_96_asm_to_mama"] = True
        return state

    i_ma = _find_target_ma(state)
    if i_ma is not None:
        stem = state.terms[i_ma]
        replacement = parse_slp1_upadesha_sequence({"asmad": "ma", "yuzmad": "tva"}[stem_key(stem)])
        stem.varnas = replacement + list(stem.varnas[prefix_len(stem):])
        # result: [m, a, a, d]
        stem.tags.add("7_2_96_done")
        state.samjna_registry["7_2_96_asm_to_ma"] = True
        return state

    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'tavamamO Nasi',
    text_dev              = 'तवममौ ङसि',
    samagra_slp1          = "aNgasya maparyantasya tavamamO Nasi viBaktO yuzmadasmadoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य मपर्यन्तस्य तवममौ ङसि विभक्तौ युष्मदस्मदोः",
    padaccheda_dev        = "त्व-मौ एकवचने",
    why_dev               = "अस्मद्-शब्दस्य आदि-भागस्य [अ,स्,म्] स्थाने [म,अ] (एकवचने) "
                            "वा [म,म,अ] (ङसि) आदेशः (सूत्रम् ७.२.९६)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
