"""
tests/constitutional/test_vidhi_cond_discipline.py — VIDHI false-positive ratchet.

Pins measured baselines from ``audit/cond_discipline_auditor.py`` on the
canonical BU dhātu probe.  Commits may **decrease** counts (migration progress)
but must not exceed the ceiling without lowering the baseline.
"""
from __future__ import annotations

import sutras  # noqa: F401

from audit.cond_discipline_auditor import (
    TINANTA_INIT_RAW_BASELINE,
    VIDHI_FP_FILTERED_BASELINE,
    VIDHI_FP_RAW_BASELINE,
    analyze_probe,
    bu_dhatu_probe,
    bu_tinanta_initialized,
)


def test_bu_probe_raw_vidhi_do_not_exceed_baseline() -> None:
    result = analyze_probe(bu_dhatu_probe(), "bu_dhatu")
    assert result.raw_vidhi <= VIDHI_FP_RAW_BASELINE, (
        f"BU probe raw VIDHI increased: {result.raw_vidhi} > baseline "
        f"{VIDHI_FP_RAW_BASELINE}. Tighten cond() or lower baseline after "
        "intentional migration."
    )


def test_bu_probe_filtered_vidhi_do_not_exceed_baseline() -> None:
    result = analyze_probe(bu_dhatu_probe(), "bu_dhatu")
    assert result.filtered_vidhi <= VIDHI_FP_FILTERED_BASELINE, (
        f"BU probe filtered VIDHI increased: {result.filtered_vidhi} > baseline "
        f"{VIDHI_FP_FILTERED_BASELINE}."
    )


def test_tinanta_init_probe_raw_vidhi_do_not_exceed_baseline() -> None:
    result = analyze_probe(bu_tinanta_initialized(), "bu_tinanta_init")
    assert result.raw_vidhi <= TINANTA_INIT_RAW_BASELINE, (
        f"tinanta-init raw VIDHI increased: {result.raw_vidhi} > baseline "
        f"{TINANTA_INIT_RAW_BASELINE}."
    )


def test_vidhi_baselines_track_improvement() -> None:
    """Nudge engineer to ratchet baselines down when counts drop."""
    result = analyze_probe(bu_dhatu_probe(), "bu_dhatu")
    if result.raw_vidhi < VIDHI_FP_RAW_BASELINE:
        assert False, (
            f"raw VIDHI = {result.raw_vidhi} < baseline {VIDHI_FP_RAW_BASELINE}. "
            f"Lower VIDHI_FP_RAW_BASELINE in audit/cond_discipline_auditor.py."
        )
    if result.filtered_vidhi < VIDHI_FP_FILTERED_BASELINE:
        assert False, (
            f"filtered VIDHI = {result.filtered_vidhi} < baseline "
            f"{VIDHI_FP_FILTERED_BASELINE}. Lower VIDHI_FP_FILTERED_BASELINE."
        )
    tin = analyze_probe(bu_tinanta_initialized(), "bu_tinanta_init")
    if tin.raw_vidhi < TINANTA_INIT_RAW_BASELINE:
        assert False, (
            f"tinanta-init raw = {tin.raw_vidhi} < baseline "
            f"{TINANTA_INIT_RAW_BASELINE}. Lower TINANTA_INIT_RAW_BASELINE."
        )
