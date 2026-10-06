"""7.1.73 ikoci vibhaktau — nuṃ for a neuter ik-final aṅga before an ac-initial vibhakti (ashtadhyayi.com gold agrees)."""
import pytest

import sutras  # noqa: F401
from pipelines.subanta import derive

CASES = [("vAri", 1, 2, "वारिणी"), ("vAri", 1, 3, "वारीणि"), ("vAri", 3, 1, "वारिणा"), ("vAri", 4, 1, "वारिणे"), ("vAri", 5, 1, "वारिणः"),
         ("vAri", 6, 3, "वारीणाम्"), ("vAri", 7, 1, "वारिणि"), ("vAri", 2, 1, "वारि"),
         ("maDu", 1, 2, "मधुनी"), ("maDu", 4, 1, "मधुने"), ("maDu", 6, 2, "मधुनोः"), ("maDu", 7, 1, "मधुनि"), ("maDu", 6, 3, "मधूनाम्")]


@pytest.mark.parametrize("stem,vi,va,want", CASES)
def test_neuter_ik(stem, vi, va, want):
    assert derive(stem, vi, va, linga="napuṃsaka").flat_dev() == want
