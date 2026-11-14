"""Pada by upasarga + root, decided by the sūtras (engine/pada_ctx.py), not by a word recipe: 1.3.18 krī, 1.3.22 ṣṭhā (ātmanepada); 1.3.79 kṛ, 1.3.82 mṛṣ, 1.3.83/84 ram (parasmaipada)."""
import pytest

import sutras  # noqa: F401
from pipelines.tinanta import derive

CASES = [
    ("09.0001", ["pari"], "parikrIRIte", "1.3.18"), ("09.0001", ["vi"], "vikrIRIte", "1.3.18"), ("09.0001", ["aBi"], "aBikrIRAti", None),
    ("01.1077", ["sam"], "saMtizWate", "1.3.22"), ("01.1077", ["pra"], "pratizWate", "1.3.22"), ("01.1077", None, "tizWati", None),
    ("08.0010", ["anu"], "anukaroti", "1.3.79"), ("08.0010", ["parA"], "parAkaroti", "1.3.79"), ("08.0010", ["ud"], "utkurute", None),
    ("04.0060", ["pari"], "parimfzyati", "1.3.82"),
    ("01.0989", ["vi"], "viramati", "1.3.83"), ("01.0989", ["A"], "Aramati", "1.3.83"), ("01.0989", ["aBi"], "aBiramate", None),
    ("01.0989", ["upa"], "uparamati", "1.3.84"), ("01.0989", None, "ramate", None),
]


@pytest.mark.parametrize("dh,up,want,sid", CASES)
def test_pada_by_upasarga(dh, up, want, sid):
    s = derive(dh, "laT", "kartari", 3, 1, upasargas=up)
    assert s.flat_slp1() == want
    applied = {e["sutra_id"] for e in s.trace if e.get("status") == "APPLIED"}
    assert (sid in applied) if sid else not applied & {"1.3.18", "1.3.22", "1.3.79", "1.3.82", "1.3.83", "1.3.84"}
