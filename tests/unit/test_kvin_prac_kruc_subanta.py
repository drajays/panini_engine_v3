"""Kāśikā 3.2.59 kvin stems prāñc / kruñc: 8.2.23 drops the c, 8.2.62 makes the ñ a ṅ, 8.3.28 (optional) kuk — prāṅkṣu, kruṅkṣu."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def _forms(stem, vib, vac):
    return {b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, linga="pulliṅga"))}


def test_prac_kruc():
    # prAYc is a padas stem [pra][ac] (6.4.24 at the kit kvin): the weak/pada stem has no nasal — prAgBiH, prAkzu (the DB's ashtadhyayi.com
    # derivations: pra+ak+Bis > prAgBis; prAk+su > prAkzu); 7.1.70 gives the nasal back only before a sarvanāmasthāna: prAYcO, prAYcaH
    assert "prAkzu" in _forms("prAYc", 7, 3)
    assert "kruNkzu" in _forms("kruYc", 7, 3)
    assert "prAN" in _forms("prAYc", 1, 1) and "prAgBiH" in _forms("prAYc", 3, 3) and "prAYcO" in _forms("prAYc", 1, 2)
    assert "dfk" in _forms("dfS", 1, 1)
