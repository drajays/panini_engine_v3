"""
1.1.45  इग्यणः सम्प्रसारणम्  —  PARIBHASHA

Operational role (v3.6, demo slice):
  - When a prior samprasāraṇa-trigger (e.g. 6.1.15) has marked a specific
    YAN-varṇa (y/v/r/l) on a dhātu Term, replace it by the corresponding IK
    vowel (i/u/f/x) by yathāsaṅkhya (1.3.10).

This file intentionally models the *deterministic mapping* described in the
note `1145.md`:
  y → i, v → u, r → f, l → x
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


META_TARGETS = "1_1_45_samprasaran_targets"

_MAP = {
    "y": "i",
    "v": "u",
    "r": "f",
    "l": "x",
}


def _targets(state: State):
    return state.meta.get(META_TARGETS) or []


def cond(state: State) -> bool:
    for ti, vi in _targets(state):
        if ti < 0 or ti >= len(state.terms):
            continue
        t = state.terms[ti]
        if vi < 0 or vi >= len(t.varnas):
            continue
        if t.varnas[vi].slp1 in _MAP:
            return True
    return False


def act(state: State) -> State:
    changed = False
    for ti, vi in list(_targets(state)):
        if ti < 0 or ti >= len(state.terms):
            continue
        t = state.terms[ti]
        if vi < 0 or vi >= len(t.varnas):
            continue
        src = t.varnas[vi].slp1
        dst = _MAP.get(src)
        if not dst:
            continue
        t.varnas[vi] = mk(dst)
        changed = True
    if changed:
        state.meta["1_1_45_samprasaran_done"] = True
    state.meta.pop(META_TARGETS, None)
    state.paribhasha_gates["1.1.45_igyana_samprasaranam"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.45",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="igyaNaH saMprasAraNam",
    text_dev="इग्यणः सम्प्रसारणम्",
    padaccheda_dev="इक्-यणः सम्प्रसारणम्",
    why_dev="यण्-वर्णस्य (य्/व्/र्/ल्) इक्-वर्णे (इ/उ/ऋ/ऌ) सम्प्रसारणम् — यथासंख्येन।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

__all__ = ["META_TARGETS", "SUTRA"]

