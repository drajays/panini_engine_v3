"""
tests/constitutional/test_no_kaumudi_leakage.py
────────────────────────────────────────────────

Constitution Article 3 — Aṣṭādhyāyī-kram is the ONLY permissible
rule ordering.  Siddhānta-Kaumudī headings, prakaraṇa labels, and
ordering annotations must NOT appear anywhere in the engine / sūtras
/ phonology / pipelines tree.

The forbidden substrings were the ones that leaked into v2 and
caused Kaumudī-first ordering to silently contaminate the resolver:

  • 'sk_kashika'
  • 'siddhanta_kaumudi' / 'Siddhanta-Kaumudi'
  • 'prakarana_order' / 'prakarana_index'
  • 'kashika_priority'
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

FORBIDDEN = (
    "sk_kashika",
    "siddhanta_kaumudi",
    "Siddhanta-Kaumudi",
    "Siddhānta-Kaumudī",
    "prakarana_order",
    "prakarana_index",
    "kashika_priority",
)


def _iter_protected_files():
    for base in PROTECTED_DIRS:
        for p in base.rglob("*.py"):
            yield p


@pytest.mark.parametrize("src_path", list(_iter_protected_files()),
                         ids=lambda p: p.relative_to(ROOT).as_posix())
def test_no_kaumudi_leakage(src_path):
    text = src_path.read_text(encoding="utf-8")
    for needle in FORBIDDEN:
        assert needle not in text, (
            f"{src_path}: contains forbidden Kaumudī marker {needle!r}. "
            "CONSTITUTION Article 3 forbids Kaumudī-flavoured ordering."
        )
