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


@pytest.mark.parametrize("stem,lg,vi,va,want", [("gomat", "pulliṅga", 1, 1, "गोमान्"), ("gomat", "pulliṅga", 1, 2, "गोमन्तौ"), ("kanIyas", "pulliṅga", 1, 2, "कनीयांसौ"),
                                                  ("kamitf", "pulliṅga", 1, 2, "कमितारौ"), ("pitf", "pulliṅga", 1, 2, "पितरौ"),
                                                  ("anyatarA", "strīliṅga", 4, 1, "अन्यतरस्यै"), ("sarvA", "strīliṅga", 6, 3, "सर्वासाम्"),
                                                  ("acCa", "pulliṅga", 1, 1, "अच्छः"), ("icCA", "strīliṅga", 1, 1, "इच्छा"), ("vAc", "strīliṅga", 7, 3, "वाक्षु")])
def test_stem_shape_flags_and_cC(stem, lg, vi, va, want):
    """ugit / tfc are inputs (here as the gold harness gives them); sarvādi feminines run from the a-stem; a stem-internal cC is not 8.2.30's c."""
    from bench.ashtadhyayi_gold import _origin_flags
    assert derive(stem, vi, va, linga=lg, **_origin_flags(stem)).flat_dev() == want
