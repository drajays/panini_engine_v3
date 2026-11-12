"""tools/exercise_audit: a kṛdanta example label becomes a call (meaning-chosen pratyaya, never named) and runs through derive_krdanta."""
import sutras  # noqa: F401
from tools.exercise_audit import _spec, attempt


def test_krdanta_label_runs():
    spec, exp, why = _spec("vidyut rA\\ (02.0052) +Ga Pum Prathama Eka → rAH", "vidyut", "krdanta", "", "")
    assert spec[:3] == ("krdanta", "02.0052", "Ga") and exp == "rAH", why
    r = attempt(spec, exp, "0.0.0", "VIDHI")
    assert r["observed"] == "rAH", r
