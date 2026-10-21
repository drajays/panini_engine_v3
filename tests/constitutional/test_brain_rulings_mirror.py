"""The brain is the final reference (owner, 2026-10-21): every ruling the engine implements is recorded in
~/data-master/ashtadhyayi-ai/rulings first, and docs/SOURCE_CONFLICTS.md mirrors it. Skipped where the brain is absent."""
from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
BRAIN = Path(os.environ.get("PANINI_BRAIN", Path.home() / "data-master" / "ashtadhyayi-ai"))
pytestmark = pytest.mark.skipif(not (BRAIN / "rulings").is_dir(), reason="brain not present")


def _rulings() -> dict[str, dict]:
    return {r["id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in sorted((BRAIN / "rulings").glob("R-*.json")))}


def _mirror_headings() -> set[str]:
    return set(re.findall(r"^## (SC-[0-9T]+) ", (ROOT / "docs" / "SOURCE_CONFLICTS.md").read_text(encoding="utf-8"), re.M))


def test_every_source_conflict_is_a_brain_ruling_and_back():
    mirrored = {(r.get("engine") or {}).get("mirror") for r in _rulings().values()} - {None}
    assert _mirror_headings() == mirrored


def test_brain_rulings_validate():
    out = subprocess.run([str(BRAIN / "venv" / "bin" / "python"), str(BRAIN / "rulings" / "validate.py")],
                         capture_output=True, text=True, env={**os.environ, "PANINI_V3": str(ROOT)})
    assert out.returncode == 0, out.stdout


def test_engine_names_the_brain_commit_it_was_checked_against():
    pinned = json.loads((ROOT / "data" / "inputs" / "brain_version.json").read_text(encoding="utf-8"))["commit"]
    known = subprocess.run(["git", "-C", str(BRAIN), "cat-file", "-e", f"{pinned}^{{commit}}"], capture_output=True)
    assert known.returncode == 0, f"brain commit {pinned} unknown — pull the brain or re-pin data/inputs/brain_version.json"
