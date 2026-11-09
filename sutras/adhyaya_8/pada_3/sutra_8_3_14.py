"""
8.3.14  रो रि  —  VIDHI  (रः रि)

Padaccheda: रः रि (लोपः 8.3.13)
A r followed by a r is elided, whether the first r is pada-final or not: "पदस्य" is a viśeṣaṇa-ṣaṣṭhī (the r is part of a pada), so
the apadānta r goes too (examples: नीरक्तम्, दूरक्तम्, अग्नी रथः, इन्दू रथः, जर्गृधेरजर्घाः, पास्पर्धेरपास्पाः).
The surviving r is marked ``Qralopa_para`` — 6.3.111 lengthens the aṇ before it.
Pāṭha: ashtadhyayi.com data.txt row i=83014 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

MARK = "Qralopa_para"        # the same mark 8.3.13 leaves; 6.3.111 / 6.3.112 read it


def _site(state: State):
    if not state.tripadi_zone:
        return None
    cells = [(t, i) for t in state.terms for i in range(len(t.varnas))]
    for (t, i), (u, j) in zip(cells, cells[1:]):
        a, b = t.varnas[i], u.varnas[j]
        if a.slp1 == "r" and b.slp1 == "r" and "8_3_14_done" not in b.tags:
            return t, i, b
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        t, i, b = hit
        del t.varnas[i]
        b.tags.update({MARK, "8_3_14_done"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.3.14",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ro ri",
    text_dev       = "रो रि",
    samagra_slp1   = "padasya saMhitAyAm raH ri lopaH",
    samagra_dev    = "पदस्य संहितायाम् रः रि लोपः",
    padaccheda_dev = "रः रि",
    why_dev        = "रेफे परे रेफस्य लोपः (नीरक्तम्, अजर्घाः); पूर्वस्य अणो दीर्घः 6.3.111।",
    anuvritti_from = ("8.3.13",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
