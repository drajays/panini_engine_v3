"""8.3.28 ṅṇoḥ kuk-ṭuk śari and 8.3.30 naś ca (dhuṭ): the optional augments (Kāśikā: प्राङ्क्षु / प्राङ्षु; प्रशान्त्सु / प्रशान्सु)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def _surfaces(stem, vib, vac):
    return {b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, linga="pulliṅga"))}


def test_8_3_28_kuk_after_nga_before_sar():
    got = _surfaces("prAN", 7, 3)
    assert {"prANkzu", "prANzu"} <= got


def test_8_3_30_dhut_after_n_before_s():
    got = _surfaces("praSAm", 7, 3)
    assert {"praSAntsu", "praSAnsu"} <= got
