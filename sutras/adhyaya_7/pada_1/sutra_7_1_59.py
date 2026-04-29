"""
7.1.59  शे मुचादीनाम्  —  VIDHI (narrow demo)

Demo slice (मुञ्चति.md):
  When dhātu `muc` is followed by vikaraṇa `Sa`, insert nuṃ (`n`) after the
  last vowel of the dhātu (1.1.47 placement).

Engine:
  - recipe-armed by ``state.meta['7_1_59_num_arm']``.
  - performs the insertion directly on the dhātu term.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_dirgha, is_hrasva


def _is_ac(ch: str) -> bool:
    return bool(is_hrasva(ch) or is_dirgha(ch) or ch in {"e", "E", "o", "O"})


def _matches(state: State) -> bool:
    if not state.meta.get("7_1_59_num_arm"):
        return False
    if len(state.terms) < 2:
        return False
    dh = state.terms[0]
    sa = state.terms[1]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "muc":
        return False
    if (sa.meta.get("upadesha_slp1") or "").strip() != "Sa":
        return False
    if dh.meta.get("7_1_59_num_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    dh = state.terms[0]
    j = None
    for i in range(len(dh.varnas) - 1, -1, -1):
        if _is_ac(dh.varnas[i].slp1):
            j = i
            break
    if j is None:
        return state
    dh.varnas.insert(j + 1, mk("n"))
    dh.meta["7_1_59_num_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.59",
    sutra_type=SutraType.VIDHI,
    text_slp1="Se mucAdInAm (num)",
    text_dev="शे मुचादीनाम्",
    padaccheda_dev="शे / मुच-आदीनाम्",
    why_dev="श-विकरणे परे मुच्-आदीनां नुम्-आगमः (डेमो: मुञ्चति)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

