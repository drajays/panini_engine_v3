"""
8.2.35  आहस्थः  —  VIDHI

The ह् of आह् (the ब्रू-ādeśa of 3.4.84) becomes थ् before a थ-initial ending: आह + थल् → आथ्थ → आत्थ (8.4.55 खरि च).
(Before the vowel-initial अथुस् it stays: आहथुः.)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 8.2.35 (padaccheda: आहः थः)
  Source #2 — ashtadhyayi.com dhātu table, ब्रूञ् laṭ 2sg: आत्थ ; 2du: आहथुः

Engine: pre-merge (the root and the ending are still separate Terms, as for 8.2.32); reads the ``ah_adesha`` tag that
3.4.84 gave the root and the first letter of the following pratyaya.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "ah_adesha" not in t.tags or t.meta.get("8_2_35_done") or not t.varnas or t.varnas[-1].slp1 != "h":
            continue
        nxt = state.terms[i + 1]
        if "pratyaya" in nxt.tags and nxt.varnas and nxt.varnas[0].slp1 == "T":
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.varnas[-1] = mk("T")
        t.meta["8_2_35_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.35",
    sutra_type=SutraType.VIDHI,
    text_slp1="AhasTaH",
    text_dev="आहस्थः",
    padaccheda_dev="आहः थः",
    why_dev="आह् के ह् को थ्, थ-आदि प्रत्यय परे (आह + थल् → आथ्थ → आत्थ)।",
    anuvritti_from=("8.2.1",),
    apavada_of=("8.2.31",),   # आहः थः: the specific rule displaces हो ढः on this ह्
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
