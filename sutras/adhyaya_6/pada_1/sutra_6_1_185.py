"""
6.1.185  तित्स्वरितम्  —  ANUVADA

**Pāṭha (cross-check: sutrANi.tsv):** *tit-svaritam* — an affix (pratyaya)
or nipāta bearing the indicatory letter **t** (*tit*) causes *svarita* accent
(*Ṛk-prātiśākhya* tier).

Engine (universal): fires on any ``Term`` that carries ``"tit"`` in its
``tags`` and has not yet been stamped ``tit_svarita_note``.  No hardcoded
upadeśa names or demo-context tags — the presence of the grammatical ``"tit"``
property is the sole trigger.

No *svara* columns on ``Varna`` rows (accent is *śruti*-metadata only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_tit_term(state: State):
    """First Term carrying the tit (indicatory t) property, not yet svarita-marked."""
    for t in state.terms:
        if "tit" not in t.tags:
            continue
        if t.meta.get("tit_svarita_note"):
            continue
        return t
    return None


def cond(state: State) -> bool:
    return _find_tit_term(state) is not None


def act(state: State) -> State:
    t = _find_tit_term(state)
    if t is None:
        return state
    t.meta["tit_svarita_note"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.185",
    sutra_type=SutraType.ANUVADA,
    text_slp1="titsvaritam",
    text_dev="तित्स्वरितम्",
    padaccheda_dev="तित्-स्वरितम्",
    why_dev="तित्-संज्ञकस्य प्रत्ययस्य / निपातस्य स्वरित-अनुवादः (यः «tit»-टैगयुतः पदः तस्य स्वरितः)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
