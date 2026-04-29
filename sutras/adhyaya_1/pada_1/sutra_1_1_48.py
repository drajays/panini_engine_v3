"""
1.1.48  एच इग्घ्रस्वादेशे  —  PARIBHASHA (narrow demo)

Operational rules that require *hrasva* on an *एच्* vowel keep the output inside the
*इक्* domain by routing through ``phonology.ec_ig_hrasva`` (same bundle **6.4.92**
and **1.2.47** use); this sūtra remains the explicit *apply_rule("1.1.48")* hook
when a recipe injects the resolver via meta-arming.

Engine:
  - Arms via ``state.meta['1_1_48_ec_ig_hrasva_arm']``.
  - Target term: ``state.meta['1_1_48_target_term_index']`` (default ``0``).
  - Optional vowel row: ``state.meta['1_1_48_target_varna_index']`` (default: last).
"""
from __future__ import annotations

from typing import Optional, Tuple

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.ec_ig_hrasva import ec_ig_replacement_slp1


def _target_pair(state: State) -> Optional[Tuple[int, int]]:
    if not state.meta.get("1_1_48_ec_ig_hrasva_arm"):
        return None
    ti = state.meta.get("1_1_48_target_term_index", 0)
    if not isinstance(ti, int) or ti < 0 or ti >= len(state.terms):
        return None
    t = state.terms[ti]
    if "prātipadika" not in t.tags or "napuṃsaka" not in t.tags:
        return None
    if t.meta.get("1_1_48_done"):
        return None
    if not t.varnas:
        return None
    vi = state.meta.get("1_1_48_target_varna_index")
    if vi is None:
        vi = len(t.varnas) - 1
    if not isinstance(vi, int) or vi < 0 or vi >= len(t.varnas):
        return None
    ch = t.varnas[vi].slp1
    if ec_ig_replacement_slp1(ch) is None:
        return None
    return ti, vi


def cond(state: State) -> bool:
    return _target_pair(state) is not None


def act(state: State) -> State:
    hit = _target_pair(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    ch = t.varnas[vi].slp1
    rep = ec_ig_replacement_slp1(ch)
    if rep is None:
        return state
    t.varnas[vi] = mk(rep)
    t.meta["1_1_48_done"] = True
    state.paribhasha_gates["1.1.48_ec_ig_hrasva"] = True
    state.meta["1_1_48_ec_ig_hrasva_arm"] = False
    state.meta.pop("1_1_48_target_term_index", None)
    state.meta.pop("1_1_48_target_varna_index", None)
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.48",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="ec ig~ hrasvAdeSe",
    text_dev="एच इग्घ्रस्वादेशे",
    padaccheda_dev="एच् / इक् / ह्रस्व-आदेशे",
    why_dev=(
        "एच् के ह्रस्वादेशे इक् एव — अन्य विधि (६.४.९२, १.२.४७, …) यत्र एच्-ह्रस्वः "
        "तत्र एतत् कोर इन्जेक्शन् (`phonology.ec_ig_hrasva`)।"
    ),
    anuvritti_from=("1.1.47",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
