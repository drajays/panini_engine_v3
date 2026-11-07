"""
6.4.30  नाञ्चेः पूजायाम्  —  VIDHI

Padaccheda: न अञ्चेः पूजायाम्

नाञ्चेः पूजायाम् (6.4.30)
Pāṭha: ashtadhyayi.com data.txt row i=64030 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, stem_of
from engine.state import State


def _site(state: State):
    """नाञ्चेः पूजायाम् — the aṅga अञ्चु in the sense of honouring (प्राञ्च्, प्रत्यञ्च् …): the nalopa of the upadhā n (6.4.24) does not happen: प्राञ्चः, प्राङ्. The
    sense is a lexical fact of the stem (``lex:pUjArTa``, S22), as añc (gatipūjanayoḥ) has two senses."""
    hit = anga_and_sup(state, "6.4.30")
    if hit is None or "6.4.24" in state.blocked_sutras:
        return None
    anga, _ = hit
    return anga if "lex:pUjArTa" in anga.tags and stem_of(anga).endswith("Yc") else None


# SHORTCUT S128: see docs/SHORTCUT_LEDGER.md
def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    state.blocked_sutras.add("6.4.24")
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.30",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nAYceH pUjAyAm",
    text_dev              = "नाञ्चेः पूजायाम्",
    samagra_slp1          = "pUjAyAmaYceH aNgasya upaDAyAH nalopaH na",
    samagra_dev           = "पूजायामञ्चेः अङ्गस्य  उपधायाः नलोपः न",
    padaccheda_dev        = "न अञ्चेः पूजायाम्",
    why_dev               = "नाञ्चेः पूजायाम् — पूजार्थस्य अञ्चतेः अङ्गस्य उपधायाः नलोपः (६.४.२४) न (प्राञ्चः)।",
    anuvritti_from        = ('6.1.1',),
    blocks_sutra_ids      = ('6.4.24',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
