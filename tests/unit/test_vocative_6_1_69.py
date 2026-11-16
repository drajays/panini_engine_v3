"""Owner note 6.1.69 (2026-11-16): the vocative singular cases of the Kāśikā / textbook, surface only (path of neuter a-stems: S188)."""
import pytest
from pipelines.subanta import derive

CASES = [("muni", "pulliṅga", "मुने"), ("Denu", "pulliṅga", "धेनो"), ("bAla", "pulliṅga", "बाल"), ("mAlA", "strīliṅga", "माले"),
         ("nadI", "strīliṅga", "नदि"), ("vaDU", "strīliṅga", "वधु"), ("Pala", "napuṃsaka", "फल"), ("katara", "napuṃsaka", "कतरत्")]


@pytest.mark.parametrize("stem,linga,want", CASES)
def test_vocative_singular(stem, linga, want):
    assert derive(stem, 8, 1, linga).flat_dev() == want
