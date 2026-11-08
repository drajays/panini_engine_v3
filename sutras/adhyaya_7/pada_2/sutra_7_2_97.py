"""
7.2.97  त्वमावेकवचने  —  VIDHI

Padaccheda: त्व-मौ एकवचने

त्वमावेकवचने (7.2.97)
Pāṭha: ashtadhyayi.com data.txt row i=72097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.pronoun_stem import PRONOUN_PREFIX, prefix_len, stem_key
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target_ma(state: State):
    """Find stem for 'ma' replacement (general ekavacana)."""
    if not state.meta.get("7_2_97_ma_arm"):
        return None
    for i, t in enumerate(state.terms):
        if stem_key(t) not in PRONOUN_PREFIX:
            continue
        if "anga" not in t.tags:
            continue
        if "7_2_97_done" in t.tags:
            continue
        if not prefix_len(t):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_target_ma(state) is not None


def act(state: State) -> State:
    i_ma = _find_target_ma(state)
    if i_ma is not None:
        stem = state.terms[i_ma]
        replacement = parse_slp1_upadesha_sequence({"asmad": "ma", "yuzmad": "tva"}[stem_key(stem)])
        stem.varnas = replacement + list(stem.varnas[prefix_len(stem):])      # [m, a, a, d]
        stem.tags.add("7_2_97_done")
        state.samjna_registry["7_2_97_asm_to_ma"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.97",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "tvamAvekavacane",
    text_dev              = "त्वमावेकवचने",
    samagra_slp1          = "aNgasya maparyantasya tvamO ekavacane viBaktO yuzmadasmadoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य मपर्यन्तस्य त्वमौ एकवचने विभक्तौ युष्मदस्मदोः",
    padaccheda_dev        = "त्व-मौ एकवचने",
    why_dev               = "(सूत्रम् 7.2.97) त्वमावेकवचने।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
