"""Unit tests for ``pipelines/vepathuH_athuc_wuvepf_corrected_P002_A_demo.py`` (**P002-A**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.vepathuH_athuc_wuvepf_corrected_P002_A_demo import (
    derive_vepathuH_athuc_wuvepf_corrected_P002_A,
)


def test_P002_A_render_vepathuH():
    s = derive_vepathuH_athuc_wuvepf_corrected_P002_A()
    assert s.render() == "vepathuH"


def test_P002_A_spine_core_order():
    s = derive_vepathuH_athuc_wuvepf_corrected_P002_A()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.3.89" in ids
    assert "1.2.46" in ids
    assert "4.1.2" in ids
    assert "8.2.1" in ids
    assert ids.index("3.3.89") < ids.index("1.2.46") < ids.index("4.1.2")
