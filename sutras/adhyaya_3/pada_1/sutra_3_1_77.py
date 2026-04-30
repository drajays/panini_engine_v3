"""
3.1.77  तुदादिभ्यः शः  —  VIDHI (narrow demo)

Demo slice (मुञ्चति.md):
  For tudādi dhātu `muc`, use vikaraṇa `Sa` (whose surface remainder is `a`)
  instead of `Sap`.

Engine:
  - recipe-armed: ``state.meta['3_1_77_sa_arm']``.
  - inserts a `Sa` vikaraṇa term immediately after the dhātu.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("3_1_77_sa_arm"):
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    # Narrow demo extension: allow additional tudādi witnesses when the recipe arms.
    if (dh.meta.get("upadesha_slp1") or "").strip() not in {"muc", "kF"}:
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
    why_dev="तुदादि-गणेभ्यः धातुभ्यः श-विकरणः (डेमो: मुच्)।",
    anuvritti_from=("3.1.67", "3.1.91"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

