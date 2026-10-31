"""bhavya from adādi as (Scharf 2022 on Rajpopat): 2.4.52 asterbhūḥ is a viṣaya-saptamī (ārdhadhātuke) and every kṛtya is ārdhadhātuka
(3.4.114), so as → bhū stands before the kṛtya sūtras choose: 3.1.97 aco yat sees an ac-final dhātu, 3.1.124 ṇyat (ṛhalor) no longer does.
Kāśikā 2.4.52 bhavitā, bhavitavyam; 3.1.124 kāryam. Never *bhāvya* (ṇyat on the as-stage)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

AS, BHU = "Adadi_02_0060", "BvAdi_01_0001"
KRTYA = dict(krt="kftya")


def _forms(ref, **viv):
    return {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, "napuṃsaka", **viv))}


@pytest.mark.parametrize("ref", [AS, BHU])
def test_bhavya(ref):
    got = _forms(ref, **KRTYA)
    assert "Bavyam" in got and "BAvyam" not in got, sorted(got)


@pytest.mark.parametrize("want", ["Bavitavyam", "BavanIyam"])
def test_as_other_kftyas(want):
    assert want in _forms(AS, **KRTYA)


def test_as_kta():
    assert "BUtam" in _forms(AS, kala="BUta", artha="karman")
