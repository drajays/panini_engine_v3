"""
T3 — P010 *āyacchate* (``AN`` + ``yama~`` + laṭ) vs canonical ``derive``.
"""
from __future__ import annotations

from pipelines.tinanta import derive

_P010_SLP1 = "AyacCate"


def test_yama_Anga_canonical_lat_matches_p010():
    s = derive("yama~", "laT", "kartari", 3, 1, upasargas=["AN"])
    assert s.flat_slp1() == _P010_SLP1
