"""
T3 — P010 *āyacchate* (``A~N`` + ``yama~`` + laṭ) vs canonical ``derive``.
"""
from __future__ import annotations

from pipelines.Ayacchate_lat_yam_corrected_P010_demo import (
    derive_Ayacchate_lat_yam_corrected_P010,
)
from pipelines.tinanta import derive

_P010_SLP1 = "AyacCate"
# Joiner surface (prefix ``A~N`` residue); corrected-v2 JSON target ``आयच्छते`` is post-merge ideal.
_P010_DEV = "आँयच्छते"


def test_p010_demo_surface():
    s = derive_Ayacchate_lat_yam_corrected_P010()
    assert s.flat_slp1() == _P010_SLP1


def test_yama_Anga_canonical_lat_matches_p010():
    s = derive("yama~", "laT", "kartari", 3, 1, upasargas=["A~N"])
    assert s.flat_slp1() == _P010_SLP1
    assert s.flat_dev() == _P010_DEV
