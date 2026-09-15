"""
8.4.46 अचो रहाभ्यां द्वे — VIDHI (र/ह परे यर्-द्वित्व)

Sources consulted:
- ashtadhyayi.com data.txt row i=84046
- Kāśikā: "सूर्य → सूर्य्य" (रेफात् परो यकारद्वित्वम्)
- Cross-validation: pipelines/yar_anaci_dvitva_tripadi.py — `derive_sUry_y_dvitva`

After *ac*, when *r* or *h* immediately follows and the next sound is a *yar* (*hal*
except *h*), optionally duplicate **that following *yar***, not the *r* / *h*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import HAL
from phonology.varna import AC_DEV

_AC = frozenset(AC_DEV.keys())
_YAR_HAL = HAL - frozenset({"h"})
_RAH = frozenset({"r", "h"})
_DVITVA_TAG = "yar_dvitva_8_4_46"


def _flat_varnas(state: State) -> list[tuple[int, int, str]]:
    out: list[tuple[int, int, str]] = []
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            out.append((ti, vi, v.slp1))
    return out


def _find_rah_yar_dvitva(state: State) -> tuple[int, int] | None:
    flat = _flat_varnas(state)
    n = len(flat)
    for i in range(n - 2):
        if flat[i][2] not in _AC:
            continue
        if flat[i + 1][2] not in _RAH:
            continue
        ti_y, vi_y, yar_slp = flat[i + 2]
        if yar_slp not in _YAR_HAL:
            continue
        v = state.terms[ti_y].varnas[vi_y]
        if _DVITVA_TAG in v.tags:
            continue
        return (ti_y, vi_y)
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find_rah_yar_dvitva(state) is not None


def act(state: State) -> State:
    hit = _find_rah_yar_dvitva(state)
    if hit is None:
        return state
    ti, vi = hit
    v = state.terms[ti].varnas[vi]
    dup = mk(v.slp1)
    dup.tags.update(v.tags)
    dup.tags.add(_DVITVA_TAG)
    v.tags.add(_DVITVA_TAG)
    state.terms[ti].varnas.insert(vi + 1, dup)
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.46",
    sutra_type=SutraType.VIDHI,
    text_slp1="aco rahAByAM dve",
    text_dev="अचो रहाभ्यां द्वे",
    padaccheda_dev="अचः र-हाभ्याम् द्वे",
    why_dev="अचः परस्मात् रेफ-हकारयोः परो यर्-वर्णस्य विकल्पेन द्वित्वम् (सूर्य्य)।",
    anuvritti_from=("8.2.108",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
