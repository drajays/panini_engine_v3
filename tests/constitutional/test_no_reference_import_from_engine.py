"""
tests/constitutional/test_no_reference_import_from_engine.py
─────────────────────────────────────────────────────────────

Constitution Article 6 (the firewall):

  engine / sutras / phonology / pipelines must NEVER reference the
  path 'data/reference' in any form.  Only tests and tools may
  consult data/reference.

We scan every source file in the protected directories for the
literal substring 'data/reference'.  If it appears, this test fails.
"""
from __future__ import annotations

import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]

PROTECTED_DIRS = (
    ROOT / "engine",
    ROOT / "sutras",
    ROOT / "phonology",
    ROOT / "pipelines",
)


def _iter_protected_files():
    for base in PROTECTED_DIRS:
        for p in base.rglob("*.py"):
            yield p


@pytest.mark.parametrize("src_path", list(_iter_protected_files()),
                         ids=lambda p: p.relative_to(ROOT).as_posix())
def test_no_reference_leak(src_path):
    text = src_path.read_text(encoding="utf-8")
    assert "data/reference" not in text, (
        f"{src_path}: imports/references 'data/reference'.  "
        "CONSTITUTION Article 6 forbids — only tests/ and tools/ may."
    )
