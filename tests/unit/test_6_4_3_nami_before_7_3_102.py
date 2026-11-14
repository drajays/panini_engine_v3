"""Kaumudi 6.4.3: nāmi dīrgha, not supi ca 7.3.102 (saṃnipāta-paribhāṣā), lengthens rāma before nām."""
import sutras  # noqa: F401
from tools.exercise_audit import run


def test_ramanam_by_6_4_3():
    branches, err = run(("subanta", "rAma", "pulliṅga", 6, 3))
    assert err is None
    seen = next(s for surf, s in branches if surf == "rAmARAm")
    assert "APPLIED" in seen["6.4.3"] and "APPLIED" not in seen.get("7.3.102", ())
