"""
6.3.111  ढ्रलोपे पूर्वस्य दीर्घोऽणः  —  VIDHI

Padaccheda: ढ्-र-लोपे पूर्वस्य दीर्घः अणः

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 63111 · ढ्रलोपे पूर्वस्य दीर्घोऽणः
              padaccheda: ढ्रलोपे पूर्वस्य दीर्घः अणः
  Source #2 — Kāśikā 6.3.111 udāharaṇa:
                लीढम्, मीढम्, उपगूढम्, मूढः
  Cross-check — tests/unit/test_dho_dhe_lopa_8_3_13.py (लीढः); gold लेढा keeps ए
                (not an aṇ)

When a ढ् has been elided before ढ् (8.3.13), the aṇ vowel (अ इ उ) right before
the surviving ढ् is lengthened. The site is read from the ``Qralopa_para`` mark
8.3.13 leaves on that ढ्; this rule names the tripāḍī lopa as its own condition,
so it runs right after 8.3.13 in the spine. (र्-lopa of 8.3.14 is not yet marked.)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

MARK = "Qralopa_para"
_DIRGHA = {"a": "A", "i": "I", "u": "U"}


def _site(state: State):
    cells = [(t, i) for t in state.terms for i in range(len(t.varnas))]
    for (t, i), (u, j) in zip(cells, cells[1:]):
        nxt = u.varnas[j]
        if MARK in nxt.tags and "6_3_111_done" not in nxt.tags and t.varnas[i].slp1 in _DIRGHA:
            return t, i, nxt
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        t, i, nxt = hit
        old = t.varnas[i]
        t.varnas[i] = mk(_DIRGHA[old.slp1], *old.tags)
        nxt.tags.add("6_3_111_done")
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.3.111",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'Qralope pUrvasya dIrGoRaH',
    text_dev       = 'ढ्रलोपे पूर्वस्य दीर्घोऽणः',
    padaccheda_dev = "ढ्-र-लोपे पूर्वस्य दीर्घः अणः",
    why_dev        = "ढ्-लोपे सति पूर्वस्य अणः दीर्घः — लिढ्+ढ → लीढ।",
    anuvritti_from = ("6.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
