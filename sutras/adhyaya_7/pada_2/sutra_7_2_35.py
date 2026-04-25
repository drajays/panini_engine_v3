"""
7.2.35  आर्धधातुकस्येड् वलादेः  —  VIDHI

Narrow v3: prepend **i** (iṭ āgama) on the **kṛt** ``Term`` so it stands
immediately before a following pratyaya that begins with a **velar-class**
(varga) obstruent — approximated as the first pratyaya letter in ``HAL`` but
not in ``YAN``.

Blocked by **7.2.10** via ``state.blocked_sutras`` for ekāc **anudātta** dhātus.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL, mk
from phonology.pratyahara import YAN


def _val_initial(pr_first: str) -> bool:
    if pr_first not in HAL:
        return False
    if pr_first in YAN:
        return False
    return True


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    d0 = state.terms[0]
    pr = state.terms[-1]
    if "dhatu" not in d0.tags or "krt" not in pr.tags:
        return False
    if "ardhadhatuka" not in pr.tags:
        return False
    if pr.meta.get("it_agama_7_2_35_done"):
        return False
    if not pr.varnas:
        return False
    return _val_initial(pr.varnas[0].slp1)


def act(state: State) -> State:
    pr = state.terms[-1]
    it_v = mk("i")
    it_v.tags.add("it_agama")
    pr.varnas.insert(0, it_v)
    pr.meta["it_agama_7_2_35_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.35",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ArDaDAtukasyeQ valAdeH",
    text_dev       = "आर्धधातुकस्येड् वलादेः",
    padaccheda_dev = "आर्धधातुकस्य इट् वलादेः",
    why_dev        = "आर्धधातुके परे वल्-प्रथमादौ इट्-आगमः (प्रतिषेधे न)।",
    anuvritti_from = ("7.2.34",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
