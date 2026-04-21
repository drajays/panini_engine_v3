from __future__ import annotations

import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.krdanta import derive_pAcakaH


def test_pacaka_vrddhi_example():
    state = derive_pAcakaH()
    assert state.terms, "no output term"
    produced = slp1_to_devanagari(state.terms[0].varnas)
    assert produced == "पाचकः"

