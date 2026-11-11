"""8.2.76 rvorupaDAyA dIrGa ikaH — a dhatu-derived pada ending in r/v lengthens its ik upadha (gIH, gIrByAm)."""
import pytest
from pipelines.subanta import derive


def _form(v, n):
    return "".join(x.slp1 for t in derive("gir", v, n, "strīliṅga").terms for x in t.varnas)


@pytest.mark.parametrize("v,n,want", [
    (1, 1, "gIH"), (8, 1, "gIH"), (3, 2, "gIrByAm"), (4, 3, "gIrByaH"),
    (1, 2, "girO"), (3, 1, "girA"), (6, 3, "girAm"),          # not pada-final before a vowel
])
def test_gir(v, n, want):
    assert _form(v, n) == want
