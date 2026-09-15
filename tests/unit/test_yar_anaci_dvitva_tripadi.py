"""
8.4.47 अनचि च + 8.4.46 अचो रहाभ्यां द्वे — lesson pipelines.
"""
from __future__ import annotations

import pytest

from pipelines.yar_anaci_dvitva_tripadi import (
    derive_apsarA_dvitva,
    derive_apsarA_prakrti,
    derive_dadDyatra_dvitva,
    derive_dadDyatra_prakrti,
    derive_kfznaH_dvitva,
    derive_kfznaH_prakrti,
    derive_kfzna_sya_dvitva_both,
    derive_kfzna_sya_dvitva_s_only,
    derive_kfzna_sya_dvitva_z_only,
    derive_kfzna_sya_prakrti,
    derive_matyatra_dvitva,
    derive_matyatra_prakrti,
    derive_rAmAt_dvitva,
    derive_rAmAt_prakrti,
    derive_sthAtA_dvitva,
    derive_sthAtA_prakrti,
    derive_sUry_prakrti,
    derive_sUry_y_dvitva,
    derive_vAlmIki_dvitva,
    derive_vAlmIki_prakrti,
)


def _statuses(trace, sutra_id: str) -> list[str]:
    return [e.get("status") for e in trace if e.get("sutra_id") == sutra_id]


@pytest.mark.parametrize(
    "derive_fn, gold",
    [
        (derive_kfznaH_dvitva, "kfzznaH"),
        (derive_matyatra_dvitva, "mattyatra"),
        (derive_rAmAt_dvitva, "rAmAtt"),
        (derive_sUry_y_dvitva, "sUryy"),
    ],
)
def test_yar_anaci_dvitva_lesson(derive_fn, gold: str) -> None:
    s = derive_fn()
    assert s.flat_slp1() == gold
    assert "APPLIED" in _statuses(s.trace, "8.4.47") or "APPLIED" in _statuses(s.trace, "8.4.46")


def test_kfznaH_prakrti_unchanged() -> None:
    assert derive_kfznaH_prakrti().flat_slp1() == "kfznaH"


def test_matyatra_single_gemination() -> None:
    assert derive_matyatra_prakrti().flat_slp1() == "matyatra"
    assert derive_matyatra_dvitva().flat_slp1() == "mattyatra"


def test_sUry_uses_8_4_46_not_8_4_47_on_r() -> None:
    s = derive_sUry_y_dvitva()
    assert s.flat_slp1() == "sUryy"
    assert "APPLIED" in _statuses(s.trace, "8.4.46")


def test_kfzna_sya_fourfold() -> None:
    assert derive_kfzna_sya_prakrti().flat_slp1() == "kfznasya"
    assert derive_kfzna_sya_dvitva_z_only().flat_slp1() == "kfzznasya"
    assert derive_kfzna_sya_dvitva_s_only().flat_slp1() == "kfznassya"
    assert derive_kfzna_sya_dvitva_both().flat_slp1() == "kfzznassya"


@pytest.mark.parametrize(
    "derive_fn, gold",
    [
        (derive_vAlmIki_dvitva, "vAlmmIki"),
        (derive_dadDyatra_dvitva, "dadDyyatra"),
        (derive_sthAtA_dvitva, "sTTAtA"),
        (derive_apsarA_dvitva, "apssarA"),
    ],
)
def test_kasika_vartika_dvitva_8_4_47(derive_fn, gold: str) -> None:
    s = derive_fn()
    assert s.flat_slp1() == gold
    assert "APPLIED" in _statuses(s.trace, "8.4.47")


def test_vartika_prakrti_unchanged() -> None:
    assert derive_vAlmIki_prakrti().flat_slp1() == "vAlmIki"
    assert derive_dadDyatra_prakrti().flat_slp1() == "dadDyatra"
    assert derive_sthAtA_prakrti().flat_slp1() == "sTAtA"
    assert derive_apsarA_prakrti().flat_slp1() == "apsarA"
