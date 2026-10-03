"""
6.1.94  एङि पररूपम्  —  VIDHI  (apavāda of 6.1.88 / 6.1.87)

अवर्णान्त उपसर्ग followed by an एङ्-आदि धातु: the अ/आ is replaced by the
following एङ् (pararūpa) — ``pra`` + ``ejate`` → ``prejate``, ``upa`` + ``ozati``
→ ``upozati``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State):
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if ("upasarga" in left.tags or left.kind == "upasarga") \
                and "dhatu" in right.tags \
                and left.varnas[-1].slp1 in ("a", "A") \
                and right.varnas[0].slp1 in ("e", "o"):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    del state.terms[i].varnas[-1]
    state.meta["__why_now_dev__"] = (
        "अवर्णान्त-उपसर्गात् एङ्-आदौ धातौ परे पररूपम्; यथा प्र+एजते → प्रेजते। (६.१.९४)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.94",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "eNi pararUpam",
    text_dev       = "एङि पररूपम्",
    padaccheda_dev = "एङि पररूपम्",
    why_dev        = "उपसर्गस्य अवर्णान्तस्य एङ्-आदौ धातौ परे पररूपम्।",
    apavada_of     = ("6.1.88",),
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
