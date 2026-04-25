from __future__ import annotations

import pytest

import sutras  # noqa: F401

from core.transliterate import dev_to_slp1, slp1_to_dev, slp1_to_iast, validate_transliteration


def test_slp1_to_dev_salIyaH() -> None:
    assert slp1_to_dev("SAlIyaH") == "शालीयः"


def test_slp1_to_dev_not_naive_cluster_concat() -> None:
    dev = slp1_to_dev("SAlIyaH")
    assert "श्आ" not in dev


def test_dev_to_slp1_roundtrip_rough() -> None:
    assert dev_to_slp1("राम") == "rAma"


def test_validate_transliteration() -> None:
    validate_transliteration()


def test_slp1_to_iast_if_installed() -> None:
    indic = pytest.importorskip("indic_transliteration", reason="optional IAST")
    del indic
    out = slp1_to_iast("rAma")
    assert isinstance(out, str) and out
