"""
8.3.13  ढो ढे लोपः  —  VIDHI

Padaccheda: ढः ढे लोपः

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 83013 · ढो ढे लोपः
              padaccheda: ढः ढे लोपः
  Source #2 — Kāśikā 8.3.13 udāharaṇa:
                लीढम्, मीढम्, उपगूढम्
                "ष्टुत्वस्यात्र सिद्धत्वमाश्रयाद् द्रष्टव्यम्"
  Cross-check — ashtadhyayi.com gold लेढा / सोढा / वोढा (bench/ashtadhyayi_gold.py luṭ);
                tests/unit/test_dho_dhe_lopa_8_3_13.py

A ढ् immediately before another ढ् is elided. The second ढ् is usually the
product of 8.4.41 ष्टुना ष्टुः (लेढ्+धा → लेढ्+ढा); per the Kāśikā that ṣṭutva is
treated as siddha here, so the tripāḍī spine runs this after 8.4.41. The ढ्
that caused the lopa is marked ``Qralopa_para`` for 6.3.111 / 6.3.112.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

MARK = "Qralopa_para"


def _site(state: State):
    if not state.tripadi_zone:
        return None
    cells = [(t, i) for t in state.terms for i in range(len(t.varnas))]
    for (t, i), (u, j) in zip(cells, cells[1:]):
        if t.varnas[i].slp1 == "Q" and u.varnas[j].slp1 == "Q":
            return t, i, u.varnas[j]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        t, i, nxt = hit
        del t.varnas[i]
        nxt.tags.add(MARK)
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.3.13",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Qo Qe lopaH",
    text_dev       = "ढो ढे लोपः",
    padaccheda_dev = "ढः ढे लोपः",
    why_dev        = "ढकारे परे ढकारस्य लोपः — लेढ्+ढा → लेढा।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
