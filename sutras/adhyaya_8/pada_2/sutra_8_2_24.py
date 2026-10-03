"""
8.2.24  रात्सस्य  —  VIDHI

A pada-final *s* that follows *r* is deleted (a saṃyogānta lopa of 8.2.23's kind, but only for this cluster): पितुर् + स् → पितुर्,
which 8.3.15 then makes पितुः; मातुः, भ्रातुः, कर्तुः. (A final s after any other letter is handled by 8.2.66 — रामस् → रामः.)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 8.2.24 (padaccheda: रात् सस्य; anuvṛtti: संयोगान्तस्य लोपः 8.2.23, पदस्य)
  Source #2 — ashtadhyayi.com subanta table, ṛ-stems 5-1 / 6-1: पितुः, मातुः (the ṅasi/ṅas s after the r of ur)

Engine: reads the tape of the single merged pada: its last varṇa s with r immediately before it.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    vs = t.varnas
    if "pada" not in t.tags or t.meta.get("8_2_24_done") or len(vs) < 2:
        return None
    return t if vs[-1].slp1 == "s" and vs[-2].slp1 == "r" else None


def cond(state: State) -> bool:
    return state.tripadi_zone and _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        del t.varnas[-1]
        t.meta["8_2_24_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.24",
    sutra_type=SutraType.VIDHI,
    text_slp1="rAtsasya",
    text_dev="रात्सस्य",
    padaccheda_dev="रात् सस्य",
    why_dev="पदान्त रेफ के पश्चात् सकार का लोप (पितुर्स् → पितुर्, फिर ८.३.१५ से पितुः)।",
    anuvritti_from=("8.2.23",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
