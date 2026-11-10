"""7.1.78 नाभ्यस्ताच्छतुः bars nuṃ (7.1.70, 7.1.72) for an abhyasta Śatṛ stem; 7.1.79 वा नपुंसकस्य gives it back, optionally, in the neuter
(Kāśikā: dadanti / dadati; the abhyasta record comes from the real krt route: hu + Śatṛ → juhvat)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines import chain


def _forms(ref, vib, linga):
    st = chain.krt(ref, kala="vartamAna", samAnADikaraRa="apraTamA")
    return {b.surface_slp1 for b in explore(lambda: chain.sup(st, vib, 3, linga))}


def test_neuter_plural_both():
    f = _forms("03.0001", 1, "napuṃsaka")
    assert {"juhvanti", "juhvati"} <= f and not any("nn" in x for x in f)


def test_masculine_no_num():
    assert "juhvataH" in _forms("03.0001", 2, "pulliṅga")
