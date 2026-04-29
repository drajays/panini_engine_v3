"""
3.1.26  हेतुमति च  —  VIDHI

Glass-box demo slice (भीषयते .md):
  When the recipe arms causative formation, append the sanādi pratyaya ṇic.

Engine representation:
  - We model ṇic as a sanādi pratyaya whose surviving segment is `i`.
  - The full upadeśa identity is recorded as ``meta['upadesha_slp1'] = 'Ric'``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("3_1_26_nic_arm"):
        return False
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return False
    if any("nic" in t.tags for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    nic = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("i")),
        tags={"pratyaya", "upadesha", "sanadi", "nic"},
        meta={"upadesha_slp1": "Ric"},
    )
    state.terms.append(nic)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.26",
    sutra_type=SutraType.VIDHI,
    text_slp1="hetumati ca (Ric)",
    text_dev="हेतुमति च",
    padaccheda_dev="हेतुमति च",
    why_dev="हेतु-अर्थे (प्रेरणार्थके) धातोः परे णिच्-प्रत्ययः।",
    anuvritti_from=("3.1.23",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

