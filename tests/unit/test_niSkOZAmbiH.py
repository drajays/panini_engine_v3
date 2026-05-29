"""Unit tests for ``pipelines/niSkOZAmbiH_prakriya_40_demo.py`` (``prakriya_40``)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.niSkOZAmbiH_prakriya_40_demo import derive_niSkOZAmbi_stem_prakriya_40


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_prakriya_40_tripadi_spine_json_vs_zAstra():
    """
    JSON lists **5.3.15** with ``source_fragment`` ``5|3|15`` — manuscript confusion with **8.3.15**
    (*खरवसानयोर्विसर्जनीयः*). The demo implements **8.3.15** + **8.3.41**.
    """
    s = derive_niSkOZAmbi_stem_prakriya_40()
    ids = _trace_ids(s)
    assert ids.index("8.2.1") < ids.index("8.3.15") < ids.index("8.3.41")
    assert s.flat_slp1().startswith("nizk")
    assert s.meta.get("prakriya_40_8_3_41_done") is True
