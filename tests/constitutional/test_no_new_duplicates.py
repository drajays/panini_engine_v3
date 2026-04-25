"""
CONSTITUTIONAL TEST: No New Duplicate Scheduling Blocks
=======================================================

This repo is mid-migration to canonical scheduling wrappers.
Until we reach zero duplicates, this test enforces **no regression**:

- the number of duplicate scheduling-block groups must not increase
  beyond a pinned baseline.

When we complete the collapse campaign, set the baseline to 0.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from audit.scheduling_block_auditor import SchedulingBlockAuditor


# Pinned after collapsing ``pipelines/subanta_trc`` preflight to P01.
# Update only when you intentionally collapse more blocks (should decrease).
MAX_DUPLICATE_GROUPS = 39


@pytest.fixture(scope="module")
def audit_result():
    auditor = SchedulingBlockAuditor(project_root=".")
    auditor.scan()
    return {
        "auditor": auditor,
        "duplicates": auditor.find_duplicates(),
    }


class TestNoNewDuplicates:
    def test_duplicate_groups_do_not_increase(self, audit_result) -> None:
        duplicates = audit_result["duplicates"]
        n = len(duplicates)
        assert n <= MAX_DUPLICATE_GROUPS, (
            f"duplicate scheduling-block groups increased: got {n}, "
            f"baseline {MAX_DUPLICATE_GROUPS}. "
            "Collapse more blocks (move scheduling into core.canonical_pipelines) "
            "or update baseline only after an intentional migration."
        )

    def test_all_blocks_in_scan_dirs(self, audit_result) -> None:
        auditor = audit_result["auditor"]
        assert not auditor.errors, "scan errors:\n" + "\n".join(auditor.errors)

    def test_scan_covers_pipelines_dir(self, audit_result) -> None:
        auditor = audit_result["auditor"]
        scanned = set(auditor.files_scanned)
        pipeline_files = list(Path("pipelines").glob("*.py"))
        if not pipeline_files:
            pytest.skip("no pipeline files found")
        assert any(p.as_posix() in scanned for p in pipeline_files), (
            "expected at least one pipelines/*.py to contribute apply_rule windows; "
            "if pipelines fully delegate, adjust SCAN_DIRS or this assertion."
        )


class TestCanonicalPipelinesIntact:
    def test_canonical_pipelines_importable(self) -> None:
        import core.canonical_pipelines as cp

        assert cp is not None

