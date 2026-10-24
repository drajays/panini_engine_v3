"""
7.1.88  भस्य टेर्लोपः  —  VIDHI

Padaccheda: भस्य टेः लोपः

भस्य टेर्लोपः (7.1.88)
Pāṭha: ashtadhyayi.com data.txt row i=71088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import PATHIN_WORDS, anga_and_sup, is_stem
from engine.state import State

def _site(state: State):
    """भस्य टेर्लोपः — पथिन् / मथिन् / ऋभुक्षिन् as a bha (before an ac-initial sup that is not sarvanāmasthāna): the ṭi (the last vowel and what
    follows: -in) is dropped — पथः, पथा, मथे, ऋभुक्षः."""
    hit = anga_and_sup(state, "7.1.88")
    if hit is None:
        return None
    anga, _sup = hit
    if not is_stem(anga, *PATHIN_WORDS, tadanta=True) or "bha" not in anga.tags or anga.meta.get("7_1_88_done"):
        return None
    ix = [k for k, v in enumerate(anga.varnas) if v.slp1 in "aAiIuUfFxXeEoO"]
    return (anga, ix[-1]) if ix and anga.varnas[-1].slp1 == "n" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga, k = _site(state)
    del anga.varnas[k:]
    anga.meta["7_1_88_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.88",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "Basya werlopaH",
    text_dev              = "भस्य टेर्लोपः",
    samagra_slp1          = "paTi-maTi-fBukzAm Basya weH lopaH",
    samagra_dev           = "पथि-मथि-ऋभुक्षाम् भस्य टेः लोपः",
    padaccheda_dev        = "भस्य टेः लोपः",
    why_dev               = "(सूत्रम् 7.1.88) भस्य टेर्लोपः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
