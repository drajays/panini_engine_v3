import pytest

import sutras  # noqa: F401
from pipelines.tinanta import derive


@pytest.mark.parametrize("lk", ["liN", "luN", "laN", "xyz"])
def test_unknown_lakara_is_rejected_not_laT(lk):
    with pytest.raises(ValueError):
        derive("BU", lk, "kartari", 3, 1)


def test_known_lakara_still_derives():
    assert "".join(v.slp1 for t in derive("BU", "laG", "kartari", 3, 1).terms for v in t.varnas) == "aBavat"
