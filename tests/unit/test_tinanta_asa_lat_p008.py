"""
T3 — P008 *āste* (आसँ + laṭ ātmanepada 3 sg.) vs canonical ``derive``.
"""
from __future__ import annotations

from pipelines.tinanta import derive

_P008_SLP1 = "Aste"
_P008_DEV = "आस्ते"


def test_asa_canonical_lat_matches_p008():
    s = derive("Asa~", "laT", "kartari", 3, 1)
    assert s.flat_slp1() == _P008_SLP1
    assert s.flat_dev() == _P008_DEV
