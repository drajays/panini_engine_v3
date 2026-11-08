"""8.2.68 ahan: the pada ahan takes ru, not 8.2.7's n-lopa — ahaH, ahobhiḥ, ahobhyām (Kāśikā)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def f(v, n):
    return {b.surface_slp1 for b in explore(lambda: derive("ahan", v, n, linga="napuṃsaka")) if not any(c * 2 in b.surface_slp1 for c in "bynm")}      # the optional 8.4.46 doublings are not under test


def test_ahan():
    assert f(1, 1) == {"ahaH"} and f(3, 3) == {"ahoBiH"} and f(4, 2) == {"ahoByAm"} and f(3, 1) == {"ahnA"}
    assert derive("rAjan", 3, 3).flat_slp1() == "rAjaBiH"                         # other n-final stems keep 8.2.7
