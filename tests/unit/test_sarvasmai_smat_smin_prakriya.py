"""
*सर्वस्मै / सर्वस्मात् / सर्वस्मिन्* and parallel *viśva* (user ``सर्वस्मै and other.md``).

**7.1.14** *smai*; **7.1.15** *smAt* / *smin* on *adanta sarvanAma*; **7.1.12** *At* etc. is the
*ati-sAmAnya* for non-*sarva* (e.g. *rAma* paJcamI).
"""
from __future__ import annotations

import pytest
import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.sarva_subanta import derive_sarva_pulliṅga
from pipelines.subanta import derive


def _sutra_statuses(s, *ids: str) -> dict[str, str | None]:
    out: dict[str, str | None] = {i: None for i in ids}
    for e in s.trace:
        sid = e.get("sutra_id")
        if sid in out:
            out[str(sid)] = e.get("status")
    return out


def test_sarva_chaturthI_panchnamI_saptamI_eka_surfaces():
    s4 = derive_sarva_pulliṅga(4, 1)
    s5 = derive_sarva_pulliṅga(5, 1)
    s7 = derive_sarva_pulliṅga(7, 1)
    assert s4.flat_slp1() == "sarvasmE"
    assert s5.flat_slp1() == "sarvasmAt"
    assert s7.flat_slp1() == "sarvasmin"
    assert slp1_to_devanagari(s4.terms[0].varnas) == "सर्वस्मै"
    assert slp1_to_devanagari(s5.terms[0].varnas) == "सर्वस्मात्"
    assert slp1_to_devanagari(s7.terms[0].varnas) == "सर्वस्मिन्"


def test_viSva_chaturthI_panchnamI_saptamI_eka_parallel():
    s4 = derive("viSva", 4, 1, "pulliṅga")
    s5 = derive("viSva", 5, 1, "pulliṅga")
    s7 = derive("viSva", 7, 1, "pulliṅga")
    assert s4.flat_slp1() == "viSvasmE"
    assert s5.flat_slp1() == "viSvasmAt"
    assert s7.flat_slp1() == "viSvasmin"
    assert slp1_to_devanagari(s4.terms[0].varnas) == "विश्वस्मै"
    assert slp1_to_devanagari(s5.terms[0].varnas) == "विश्वस्मात्"
    assert slp1_to_devanagari(s7.terms[0].varnas) == "विश्वस्मिन्"


@pytest.mark.parametrize(
    "vibhakti,vacana,expect_714,expect_715,expect_712",
    [
        (4, 1, "APPLIED", "SKIPPED", "SKIPPED"),
        (5, 1, "SKIPPED", "APPLIED", "SKIPPED"),
        (7, 1, "SKIPPED", "APPLIED", "SKIPPED"),
    ],
)
def test_sarva_7_1_12_14_15_trace(
    vibhakti: int, vacana: int, expect_714: str, expect_715: str, expect_712: str
):
    s = derive_sarva_pulliṅga(vibhakti, vacana)
    st = _sutra_statuses(s, "7.1.12", "7.1.14", "7.1.15")
    assert st["7.1.14"] == expect_714, st
    assert st["7.1.15"] == expect_715, st
    assert st["7.1.12"] == expect_712, st


def test_rAma_panchnamI_7_1_12_not_7_1_15():
    s = derive("rAma", 5, 1, "puMliFga")
    assert s.flat_slp1() == "rAmAt"
    st = _sutra_statuses(s, "7.1.12", "7.1.14", "7.1.15")
    assert st["7.1.15"] == "SKIPPED"
    assert st["7.1.12"] == "APPLIED"
