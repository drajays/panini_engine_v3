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
Pāṭha: ashtadhyayi.com data.txt row i=72092 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from engine.pronoun_stem import PRONOUN_PREFIX, prefix_len, stem_key
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_2_92_arm"):
        return None
    for i, t in enumerate(state.terms):
        if stem_key(t) not in PRONOUN_PREFIX:
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_92_done" in t.tags:
            continue
        if not prefix_len(t):
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
    replacement = parse_slp1_upadesha_sequence({"asmad": "Ava", "yuzmad": "yuva"}[stem_key(stem)])
    stem.varnas = replacement + list(stem.varnas[prefix_len(stem):])
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
    samagra_slp1          = "aNgasya maparyantasya yuvAvO dvivacane viBaktO yuzmadasmadoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य मपर्यन्तस्य युवावौ द्विवचने विभक्तौ युष्मदस्मदोः",
    padaccheda_dev        = "युव-आवौ द्विवचने",
    why_dev               = "अस्मद्-शब्दस्य आदि-भागस्य [अ,स्,म्] स्थाने [आ,व,अ] आदेशः "
                            "द्विवचने (सूत्रम् ७.२.९२ युवावौ द्विवचने)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
