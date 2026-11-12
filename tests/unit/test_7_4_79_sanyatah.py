"""7.4.79 सन्यतः — abhyāsa a → i before san (Kāśikā: pipakṣati, tiṣṭhāsati; DB: vivadiṣate)."""
import sutras  # noqa: F401
from pipelines.tinanta import derive


def test_vivadizate():
    d = derive("vada~", "laT", "kartari", 3, 1, pada="atmane", san_recipe=True)
    assert d.flat_slp1() == "vivadizate"
    assert "7.4.79" in [s["sutra_id"] for s in d.trace if s.get("skip_reason") is None]
