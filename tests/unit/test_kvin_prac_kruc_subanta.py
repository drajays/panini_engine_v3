"""Kāśikā 3.2.59 kvin stems prāñc / kruñc: 8.2.23 drops the c, 8.2.62 makes the ñ a ṅ, 8.3.28 (optional) kuk — prāṅkṣu, kruṅkṣu."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def _forms(stem, vib, vac):
    return {b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, linga="pulliṅga"))}


def test_prac_kruc():
    assert {"prANkzu", "prANzu"} <= _forms("prAYc", 7, 3)
    assert "kruNkzu" in _forms("kruYc", 7, 3)
    assert "prAN" in _forms("prAYc", 1, 1) and "prANBiH" in _forms("prAYc", 3, 3)
    assert "dfk" in _forms("dfS", 1, 1)
