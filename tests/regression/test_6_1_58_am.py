"""6.1.58 सृजिदृशोर्झल्यमकिति: am (a after the last vowel) before a non-kit jhal affix, then yaṇ — srazwA, drazwA (not *sarzwA)."""
import pytest

from pipelines.tinanta import derive


@pytest.mark.parametrize("root,lakara,form", [("sfj", "luT", "srazwA"), ("dfS", "luT", "drazwA"),
                                              ("sfj", "lRT", "srakzyate"), ("dfS", "lRT", "drakzyati")])
def test_am_before_jhal(root, lakara, form):
    assert derive(root, lakara, "kartari", 3, 1).render() == form


def test_no_am_before_vowel_or_other_roots():
    assert derive("dfS", "lRT", "kartari", 3, 3).render() == "drakzyanti"      # jhi → anti is no jhal-initial block: still sya after am
    assert derive("BU", "luT", "kartari", 3, 1).render() == "BavitA"
    assert derive("kf", "luT", "kartari", 3, 1).render() == "kartA"           # guṇa roots untouched
