"""
5.4.57  अव्यक्तानुकरणाद्द्व्यजवरार्धादनितौ डाच्  —  VIDHI (narrow)

Teaching **corrected_prakriyas_v2** **P017** (*paṭapaṭāyati*): after *dvitva* of the
*avyakta-anukaraṇa* base **``pawat``** (two identical *prātipadika* ``Term`` units),
attach **डाच्** (machine **``qAc``**) before *it*-prakaraṇa.

Engine:
  • ``state.meta['corrected_v2_P017_5_4_57_arm']`` (cleared in ``act``).
  • expects **two** adjacent **``pawat``** stems with **``prātipadika``** and **``anga``**.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_META_ARM = "corrected_v2_P017_5_4_57_arm"


def _flat(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _site(state: State) -> bool:
    if not state.meta.get(_META_ARM):
        return False
    if len(state.terms) != 2:
        return False
    a, b = state.terms[0], state.terms[1]
    if _flat(a) != "pawat" or _flat(b) != "pawat":
        return False
    if "prātipadika" not in a.tags or "prātipadika" not in b.tags:
        return False
    if "anga" not in a.tags or "anga" not in b.tags:
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    q = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("qAc")),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "qAc"},
    )
    q.tags.add("dit_pratyaya")
    state.terms.append(q)
    state.meta.pop(_META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="5.4.57",
    sutra_type=SutraType.VIDHI,
    text_slp1="avyaktAnukaraRAd dvyajarArdhAd anitO qAc",
    text_dev="अव्यक्तानुकरणाद्द्व्यजवरार्धादनितौ डाच्",
    padaccheda_dev="अव्यक्त-अनुकरणात् / द्व्यज्-अवरार्धात् / अनितौ / डाच्",
    why_dev="अव्यक्तानुकरण-``pawat``-द्वित्वे परे ``qAc`` (डाच्) — P017।",
    anuvritti_from=("5.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
