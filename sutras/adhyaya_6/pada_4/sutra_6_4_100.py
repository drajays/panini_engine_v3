"""
6.4.100  घसिभसोर्हलि च  —  VIDHI (narrow: *ghas* *upadhā* *a*-*lopa*)

Teaching JSON **P033** step 7: before a following *hal*, *ghas* (**G**+**a**+**s**) loses
the penultimate short *a* (**a** between **G** and **s**).

Teaching JSON **P034** (*jakṣatuḥ*): same *upadhā*-*a*-*lopa* when **atus** (first
phoneme **a**, *ach*) follows — narrow **च**-clause demo arm (recipe-gated).

Narrow v3:
  • **P033**: ``state.meta['P033_6_4_100_gas_upadha_arm']`` + first ``dhatu`` ``Term``
    whose ``flat`` is exactly ``Gas``, and a following ``Term`` whose first *varṇa*
    is a *hal*.
  • **P034**: ``state.meta['P034_6_4_100_gas_upadha_atus_arm']`` + same ``Gas`` *dhātu*,
    following ``Term`` begins with **a** and is the *liṭ* *atus* slice (``lit_atus`` /
    ``upadesha_slp1 == 'atus'``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import HAL


def _gas_dhatu(state: State) -> tuple[int, int] | None:
    """Return (dhatu_idx, next_idx) if terms[dhatu] is Gas-dhātu and a right neighbour exists."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "Gas":
            continue
        if i + 1 >= len(state.terms):
            continue
        return (i, i + 1)
    return None


def _site_p033(state: State) -> bool:
    if not state.meta.get("P033_6_4_100_gas_upadha_arm"):
        return False
    hit = _gas_dhatu(state)
    if hit is None:
        return False
    di, ni = hit
    dh, nxt = state.terms[di], state.terms[ni]
    if dh.meta.get("P033_6_4_100_done"):
        return False
    if not nxt.varnas or nxt.varnas[0].slp1 not in HAL:
        return False
    return True


def _site_p034(state: State) -> bool:
    if not state.meta.get("P034_6_4_100_gas_upadha_atus_arm"):
        return False
    hit = _gas_dhatu(state)
    if hit is None:
        return False
    di, ni = hit
    dh, nxt = state.terms[di], state.terms[ni]
    if dh.meta.get("P034_6_4_100_done"):
        return False
    if not nxt.varnas or nxt.varnas[0].slp1 != "a":
        return False
    up = (nxt.meta.get("upadesha_slp1") or "").strip()
    if not (nxt.meta.get("lit_atus") is True or up == "atus"):
        return False
    return True


def _site(state: State) -> bool:
    return _site_p033(state) or _site_p034(state)


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    p033 = _site_p033(state)
    p034 = _site_p034(state)
    if not (p033 or p034):
        return state
    hit = _gas_dhatu(state)
    if hit is None:
        return state
    di, _ni = hit
    dh = state.terms[di]
    if len(dh.varnas) != 3:
        return state
    if dh.varnas[0].slp1 != "G" or dh.varnas[1].slp1 != "a" or dh.varnas[2].slp1 != "s":
        return state
    del dh.varnas[1]
    if p033:
        dh.meta["P033_6_4_100_done"] = True
        state.meta.pop("P033_6_4_100_gas_upadha_arm", None)
    else:
        dh.meta["P034_6_4_100_done"] = True
        state.meta.pop("P034_6_4_100_gas_upadha_atus_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.100",
    sutra_type=SutraType.VIDHI,
    text_slp1="Gasi-Bhasor hali ca",
    text_dev="घसिभसोर्हलि च",
    padaccheda_dev="घसेः-भसेः / हलि च",
    why_dev="घस्-उपधा-अकार-लोपः (हलि / अतुस्-परः) — प०३३–प०३४।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
