"""
2.4.40  लिट्यन्यतरस्याम्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=20440
- Kāśikā: «लिटि अदः घसः अन्यतरस्याम्» (अद्भक्षणे → घस्)
- Cross-validation: tests/unit/test_tinanta_ad_lit_kartari.py

In *liṭ*, the root *ad* (to eat) is optionally replaced by *ghas* (tape: **Gas**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _dhatu_flat(state: State) -> str | None:
    i = _first_dhatu_index(state)
    if i is None:
        return None
    return "".join(v.slp1 for v in state.terms[i].varnas)


def _site(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    if _first_dhatu_index(state) is None:
        return False
    flat = _dhatu_flat(state)
    if flat == "ad":
        return True
    up = ""
    for t in state.terms:
        if "dhatu" in t.tags:
            up = (t.meta.get("upadesha_slp1") or "").strip().replace("~", "")
            break
    return up in {"ada", "ad", "ada~", "ad~"}


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    i = _first_dhatu_index(state)
    assert i is not None
    t = state.terms[i]
    t.varnas = list(parse_slp1_upadesha_sequence("Gas"))
    t.meta["upadesha_slp1"] = "Gas"
    state.meta["2_4_40_ad_to_gas"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.40",
    sutra_type=SutraType.VIDHI,
    text_slp1="liTy anyatarasyAm",
    text_dev="लिट्यन्यतरस्याम्",
    padaccheda_dev="लिटि / अन्यतरस्याम्",
    why_dev="लिटि अद्-धातोः घस्-आदेशः — प०३४ (*जक्षतुः*)।",
    anuvritti_from=("2.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
