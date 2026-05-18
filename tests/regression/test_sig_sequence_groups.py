"""
Regression locks for SIG-derived sūtra sequence groups.

These tests keep SIG as an audit oracle: pipelines do not read this baseline,
but path drift is caught when a live derivation stops traversing a locked
applied-only sūtra spine.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from engine.sig import extract_applied_path
from pipelines.subanta import derive

_ROOT = Path(__file__).resolve().parents[2]
_BASELINE_PATH = Path(__file__).parent / "sig_sequence_groups_baseline.json"


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _contains_contiguous_subsequence(path: list[str], sequence: list[str]) -> bool:
    if not sequence:
        return True
    width = len(sequence)
    return any(path[i : i + width] == sequence for i in range(0, len(path) - width + 1))


def _subanta_cases() -> list[dict[str, Any]]:
    baseline = _load_json(_BASELINE_PATH)
    files: list[str] = []
    for group in baseline.get("groups", []):
        applies_to = group.get("applies_to", {})
        if applies_to.get("kind") == "subanta_gold_manifest":
            files.extend(str(p) for p in applies_to.get("files", []))

    cases: list[dict[str, Any]] = []
    for rel in sorted(dict.fromkeys(files)):
        gold_path = _ROOT / rel
        gold = _load_json(gold_path)
        stem = gold["stem_slp1"]
        linga = gold.get("linga", "pulliṅga")
        for cell in sorted(gold.get("cells", {})):
            vibhakti, vacana = (int(part) for part in cell.split("-"))
            cases.append(
                {
                    "id": f"{gold_path.stem}:{cell}",
                    "stem": stem,
                    "linga": linga,
                    "vibhakti": vibhakti,
                    "vacana": vacana,
                }
            )
    return cases


_SUBANTA_CASES = _subanta_cases()


def test_sequence_group_baseline_is_not_empty():
    baseline = _load_json(_BASELINE_PATH)
    assert baseline["schema_version"] == 1
    assert baseline["groups"]
    for group in baseline["groups"]:
        assert group["layer"] == "applied_only"
        assert len(group["sequence"]) >= 3


@pytest.mark.parametrize("case", _SUBANTA_CASES, ids=[c["id"] for c in _SUBANTA_CASES])
def test_locked_subanta_sequence_groups_remain_contiguous(case: dict[str, Any]):
    baseline = _load_json(_BASELINE_PATH)
    state = derive(
        case["stem"],
        case["vibhakti"],
        case["vacana"],
        linga=case["linga"],
    )
    applied_path = extract_applied_path(state.trace)

    for group in baseline["groups"]:
        applies_to = group.get("applies_to", {})
        if applies_to.get("kind") != "subanta_gold_manifest":
            continue

        sequence = group["sequence"]
        assert _contains_contiguous_subsequence(applied_path, sequence), (
            f"SIG sequence group {group['id']!r} missing from {case['id']}.\n"
            f"Expected contiguous sequence: {sequence}\n"
            f"Current applied path: {applied_path}"
        )
