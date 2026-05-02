"""
6.1.8  लिटि धातोरनभ्यासस्य  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  In liṭ, duplicate the primary dhātu to form a reduplication frame:
    [abhyāsa, dhātu, …].

Teaching JSON **P036** (*nināya*): after **6.1.78** the tape is **nay** + augment **a**;
with **1.1.59** *sthānivat* the guṇa vowel **e** of **nī** is treated as present for
*abhyāsa*, so insert **ne** (not a copy of **nay**) before **nay** + **a**.

Engine:
  • default: ``state.meta['6_1_8_lit_dvitva_arm']`` — copy *dhātu*.
  • **P036**: ``state.meta['P036_6_1_8_lit_sthanivat_ne_arm']``.
"""
from __future__ import annotations

from copy import deepcopy

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _site_p036(state: State) -> bool:
    if not state.meta.get("P036_6_1_8_lit_sthanivat_ne_arm"):
        return False
    if not state.meta.get("lakara_liT"):
        return False
    di = _first_dhatu_index(state)
    if di is None or di + 1 >= len(state.terms):
        return False
    dh, nxt = state.terms[di], state.terms[di + 1]
    if dh.meta.get("P036_6_1_8_done"):
        return False
    if "".join(v.slp1 for v in dh.varnas) != "nay":
        return False
    if len(nxt.varnas) != 1 or nxt.varnas[0].slp1 != "a":
        return False
    if di > 0 and "abhyasa" in state.terms[di - 1].tags:
        return False
    return True


def cond(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    if _site_p036(state):
        return True
    if not state.meta.get("6_1_8_lit_dvitva_arm"):
        return False
    di = _first_dhatu_index(state)
    if di is None:
        return False
    if di > 0 and "abhyasa" in state.terms[di - 1].tags:
        return False
    return True


def act(state: State) -> State:
    if _site_p036(state):
        di = _first_dhatu_index(state)
        assert di is not None
        ab = Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("ne")),
            tags={"abhyasa", "anga"},
            meta={"P036_6_1_8_abhyasa_ne": True},
        )
        state.terms.insert(di, ab)
        state.terms[di + 1].meta["P036_6_1_8_done"] = True
        state.meta.pop("P036_6_1_8_lit_sthanivat_ne_arm", None)
        return state
    if not state.meta.get("6_1_8_lit_dvitva_arm"):
        return state
    di = _first_dhatu_index(state)
    if di is None:
        return state
    dh = state.terms[di]
    ab = Term(
        kind=dh.kind,
        varnas=[deepcopy(v) for v in dh.varnas],
        tags=set(dh.tags) | {"abhyasa"},
        meta=dict(dh.meta),
    )
    ab.tags.discard("dhatu")
    ab.meta["6_1_8_abhyasa"] = True
    state.terms.insert(di, ab)
    state.meta["6_1_8_lit_dvitva_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.8",
    sutra_type=SutraType.VIDHI,
    text_slp1="liTi DAtor anaByAsasya",
    text_dev="लिटि धातोरनभ्यासस्य",
    padaccheda_dev="लिटि / धातोः / अनभ्यासस्य",
    why_dev="लिटि धातोः द्वित्वम् (अभ्यास-प्रकरणे) — विभिदतुः / प०३६।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
