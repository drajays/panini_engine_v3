"""6.4.127 arvaNastrasAvanaYaH — arvan takes tf in place of n except before su (arvA, vocative arvan)."""
import pytest
from pipelines.subanta import derive


def _form(v, n):
    return "".join(x.slp1 for t in derive("arvan", v, n).terms for x in t.varnas)


@pytest.mark.parametrize("v,n,want", [
    (1, 1, "arvA"), (1, 2, "arvantO"), (1, 3, "arvantaH"), (2, 1, "arvantam"),
    (3, 1, "arvatA"), (3, 2, "arvadByAm"), (5, 1, "arvataH"), (7, 1, "arvati"), (7, 3, "arvatsu"),
    (8, 1, "arvan"),
])
def test_arvan(v, n, want):
    assert _form(v, n) == want
