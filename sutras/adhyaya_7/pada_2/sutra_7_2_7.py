"""
7.2.7  अतो हलादेर्लघोः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=702007
- Kāśikā: अतो हलादेः लघोः (विकल्पेन वृद्धिः)
- Cross-validation: tests/unit/test_avaDIt_luN_han.py (luṅ *iṭ*→*ī* on *sic*);
  tests/unit/test_avadhIt_han_lun_ekavacana.py (*a*-lopa + **1.1.57** block)

Two narrow engine slices:
  1. **P026** (*avaDIt*): lengthen *iṭ* ``i`` → ``I`` on *sic* when armed.
  2. **हन्-लुङ् lesson**: optional *ā* (*A*) on *aṅga* *a* before final *hal* — blocked
     after **6.4.48** + **1.1.57** (same gate as **7.2.116** *upadhā* block).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.nimitta_predicates import find_sic_term, has_it_agama
from phonology import HAL, mk

_GATE_1_1_57 = "1.1.57_aca_parasmin_purvavidhau"


def _anga_vrddhi_blocked(state: State, ang) -> bool:
    if state.paribhasha_gates.get(_GATE_1_1_57) is True:
        return True
    if ang.meta.get("6_4_48_a_lopa_done"):
        return True
    if ang.meta.get("upadha_blocked_para_nimitta"):
        return True
    return False


def _matches_sic_it(state: State) -> bool:
    if not state.meta.get("7_2_7_luN_it_vrddhi_arm"):
        return False
    pr = find_sic_term(state)
    if pr is None or not pr.varnas:
        return False
    if pr.meta.get("7_2_7_luN_it_vrddhi_done"):
        return False
    v0 = pr.varnas[0]
    return v0.slp1 == "i" and has_it_agama(v0)


def _find_anga_ato_halader(state: State) -> tuple[int, int] | None:
    """Optional *ā* on penultimate *a* before final *hal* on *aṅga*/*dhātu*."""
    if not state.meta.get("7_2_7_anga_vrddhi_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if "anga" not in t.tags and "dhatu" not in t.tags:
            continue
        if _anga_vrddhi_blocked(state, t):
            continue
        if t.meta.get("7_2_7_anga_vrddhi_done"):
            continue
        vs = t.varnas
        if len(vs) < 2 or vs[-1].slp1 not in HAL or vs[-2].slp1 != "a":
            continue
        return (ti, len(vs) - 2)
    return None


def cond(state: State) -> bool:
    return _matches_sic_it(state) or _find_anga_ato_halader(state) is not None


def act(state: State) -> State:
    hit = _find_anga_ato_halader(state)
    if hit is not None:
        ti, vi = hit
        t = state.terms[ti]
        t.varnas[vi] = mk("A")
        t.meta["7_2_7_anga_vrddhi_done"] = True
        state.meta.pop("7_2_7_anga_vrddhi_arm", None)
        return state
    if not _matches_sic_it(state):
        return state
    pr = find_sic_term(state)
    if pr is None:
        return state
    pr.varnas[0] = mk("I")
    pr.varnas[0].tags.add("it_agama")
    pr.meta["7_2_7_luN_it_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.7",
    sutra_type=SutraType.VIDHI,
    text_slp1="ato halAder laghoH",
    text_dev="अतो हलादेर्लघोः",
    padaccheda_dev="अतः / हलादेः / लघोः",
    why_dev="लुङ्-सिच्-पथे इट्-कार्यम् (इ→ई, P026); हलादेः पूर्वस्य अ-विकल्प-वृद्धिः (हन्-लुङ्)।",
    anuvritti_from=("7.2.6",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
