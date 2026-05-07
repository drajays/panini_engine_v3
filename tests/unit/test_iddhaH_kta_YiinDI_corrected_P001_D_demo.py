"""Unit tests for ``pipelines/iddhaH_kta_YiinDI_corrected_P001_D_demo.py`` (**P001-D**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.iddhaH_kta_YiinDI_corrected_P001_D_demo import (
    derive_iddhaH_kta_YiinDI_corrected_P001_D,
)


def test_P001_D_render_iddhaH():
    s = derive_iddhaH_kta_YiinDI_corrected_P001_D()
    assert s.render() == "idDaH"


def test_P001_D_spine_pre_tripadi_cluster_then_subanta():
    s = derive_iddhaH_kta_YiinDI_corrected_P001_D()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "8.2.40" in ids
    assert "8.4.53" in ids
    assert "1.2.46" in ids
    assert ids.index("8.2.40") < ids.index("8.4.53") < ids.index("1.2.46")
    assert "4.1.2" in ids
    assert "8.2.1" in ids
    assert ids.index("8.4.53") < ids.index("4.1.2") < ids.index("8.2.1")
