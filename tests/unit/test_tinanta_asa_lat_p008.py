"""
T3 — P008 *āste* (आसँ + laṭ ātmanepada 3 sg.) vs canonical ``derive``.
"""
from __future__ import annotations

from pipelines.Aste_lat_Ada_corrected_P008_demo import derive_Aste_lat_Ada_corrected_P008
from pipelines.tinanta import derive

_P008_DEMO_SLP1 = "Aste"
_P008_DEMO_DEV = "आस्ते"


def test_p008_demo_surface():
    s = derive_Aste_lat_Ada_corrected_P008()
    assert s.flat_slp1() == _P008_DEMO_SLP1
    assert s.flat_dev() == _P008_DEMO_DEV


def test_asa_canonical_lat_matches_p008():
    s = derive("Asa~", "laT", "kartari", 3, 1)
    assert s.flat_slp1() == _P008_DEMO_SLP1
    assert s.flat_dev() == _P008_DEMO_DEV
