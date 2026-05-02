"""
2.4.40  लिट्यन्यतरस्याम्  —  VIDHI (narrow: *ad* → *ghas* in *liṭ*)

Teaching JSON **P034** (*jakṣatuḥ*): in *liṭ*, the root **ad** is replaced by **ghas**
(machine shape **Gas**).

Engine:
  - ``state.meta['lakara_liT']`` must already be True (**3.2.115**).
  - recipe arms via ``state.meta['P034_2_4_40_ad_to_gas_arm']``.
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
    if not state.meta.get("P034_2_4_40_ad_to_gas_arm"):
        return False
    if not state.meta.get("lakara_liT"):
        return False
    if _first_dhatu_index(state) is None:
        return False
    return _dhatu_flat(state) == "ad"


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
    state.meta.pop("P034_2_4_40_ad_to_gas_arm", None)
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
