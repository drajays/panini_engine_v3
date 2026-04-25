from __future__ import annotations

import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.krdanta import derive_krt, derive_pAcakaH


def test_pacaka_vrddhi_example():
    state = derive_pAcakaH()
    assert state.terms, "no output term"
    produced = slp1_to_devanagari(state.terms[0].varnas)
    assert produced == "पाचकः"


def test_pachak_md_step_sutras_appear_in_trace():
    """Extended recipe: saṃjñā/paribhāṣā → dhātu IT → 6.1.65 (no-op) → kṛt adhikāra → 3.4.67 → … → merge."""
    state = derive_krt("qupac~z", krt_upadesha_slp1="Nvul")
    path = [e.get("sutra_id") for e in state.trace if isinstance(e, dict)]
    for sid in (
        "1.1.1",
        "1.1.3",
        "1.1.7",
        "1.1.8",
        "1.1.9",
        "1.1.10",
        "1.1.11",
        "1.1.12",
        "1.1.13",
        "1.1.14",
        "1.1.100",
        "1.1.15",
        "1.1.16",
        "1.1.17",
        "1.1.18",
        "1.1.19",
        "1.1.20",
        "1.1.21",
        "1.1.46",
        "1.1.22",
        "1.1.23",
        "1.1.24",
        "1.1.50",
        "1.3.1",
        "1.3.9",
        "6.1.65",
        "3.1.1",
        "3.1.2",
        "3.1.3",
        "3.1.91",
        "3.4.67",
        "3.1.133",
        "1.3.7",
        "7.1.1",
        "1.4.13",
        "1.1.65",
        "6.4.1",
        "7.2.116",
        "7.2.115",
        "6.1.78",
        "1.2.45",
        "1.2.46",
        "__KRD_MERGE__",
    ):
        assert sid in path, f"missing trace step {sid!r} in {path}"
    assert state.flat_slp1() == "pAcaka"

