"""
6.4.113  ई हल्यघोः  —  VIDHI (narrow: corrected-v2 **P009** *śnā* residue)

*Śāstra (laghu):* long **ī** replaces **ā** of an *aghu* *aṅga* before a following
*hal*‑initial affix — modelled here for **SnA** → **nā** before **ta**.

Engine:
  • ``corrected_v2_P009_6_4_113_arm`` (**P009**),
  • ``corrected_v2_P012_6_4_113_arm`` (**P012**) —
``n`` + ``A`` + following ``ta`` → ``n`` + ``I``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_META_P009 = "corrected_v2_P009_6_4_113_arm"
_META_P012 = "corrected_v2_P012_6_4_113_arm"


def _hit(state: State) -> tuple[int, int] | None:
    """Return (term_idx, vowel_idx) of ``A`` in ``…n A`` before ``ta``."""
    if not (state.meta.get(_META_P009) or state.meta.get(_META_P012)):
        return None
    for i, t in enumerate(state.terms[:-1]):
        vs = t.varnas
        if len(vs) != 2:
            continue
        if vs[0].slp1 != "n" or vs[1].slp1 != "A":
            continue
        if "SnA_vikaraṇa" not in t.tags:
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas or nxt.varnas[0].slp1 != "t":
            continue
        return (i, 1)
    return None


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    h = _hit(state)
    if h is None:
        return state
    ti, vi = h
    state.terms[ti].varnas[vi] = mk("I")
    state.samjna_registry["6.4.113_snA_nA_to_nI"] = True
    state.meta.pop(_META_P009, None)
    state.meta.pop(_META_P012, None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.113",
    sutra_type=SutraType.VIDHI,
    text_slp1="I halyaghoH",
    text_dev="ई हल्यघोः",
    padaccheda_dev="ई / हलि / अघोः",
    why_dev="अघोः अङ्गस्य हलि परे आत् ईत्वम् — प००९ / प०१२ *श्ना*-शेषः।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
