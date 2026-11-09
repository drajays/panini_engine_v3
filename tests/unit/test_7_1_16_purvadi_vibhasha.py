"""7.1.16 pūrvādibhyo navabhyo vā (Kāśikā): pūrvāt / pūrvasmāt, pūrve / pūrvasmin; sarva keeps smāt/smin only (7.1.15)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def _f(stem, vib):
    return {b.surface_slp1 for b in explore(lambda: derive(stem, vib, 1, linga="pulliṅga"))}


def test_purvadi_optional():
    assert {"pUrvAt", "pUrvasmAt"} <= _f("pUrva", 5) and {"pUrve", "pUrvasmin"} <= _f("pUrva", 7)
    assert {"uttarAt", "uttarasmAt"} <= _f("uttara", 5)


def test_sarva_unchanged():
    assert "sarvAt" not in _f("sarva", 5) and "sarvasmin" in _f("sarva", 7)
