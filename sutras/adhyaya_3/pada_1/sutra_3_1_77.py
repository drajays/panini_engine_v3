"""
3.1.77  तुदादिभ्यः शः  —  VIDHI

  For tudādi (gaṇa 6) dhātu, use vikaraṇa `Sa` instead of `Sap`.

cond: dhātu.meta["gana"] == 6 AND no existing Śa term on tape.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _dhatu_gana(state: State) -> int | None:
    for t in state.terms:
        if "dhatu" in t.tags:
            g = t.meta.get("gana")
            return int(g) if g is not None else None
    return None


def _matches(state: State) -> bool:
    if _dhatu_gana(state) != 6:
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "Sa" for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    sa = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sa"),
        tags={"pratyaya", "vikarana", "upadesha"},
        meta={"upadesha_slp1": "Sa"},
    )
    state.terms.insert(1, sa)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.77",
    sutra_type=SutraType.VIDHI,
    text_slp1="tudAdibhyaH SaH",
    text_dev="तुदादिभ्यः शः",
    padaccheda_dev="तुदादिभ्यः शः",
    why_dev="तुदादि-गणेभ्यः धातुभ्यः श-विकरणः।",
    anuvritti_from=("3.1.67", "3.1.91"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

