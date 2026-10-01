import pytest
from tools import samsaadhanii_reader as rd

pytestmark = pytest.mark.skipif(not rd.available(), reason="Saṃsādhanī snapshot absent")


def test_coverage_tallies_and_lists_gaps():
    u = rd.catalogue()[0]
    r = rd.coverage(u["id"], rd.chapters(u["id"])[0])
    n_gaps = r["counts"]["differs"] + r["counts"]["error"] + r["counts"]["unresolved"]
    assert len(r["gaps"]) == n_gaps
