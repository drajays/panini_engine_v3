"""Gold-bench clusters fixed together (ashtadhyayi.com tables, Vidyut-generated):

* 8.3.13 ढो ढे लोपः + 6.3.111 ढ्रलोपे दीर्घः + 6.3.112 सहिवहोरोत्  — लेढा, लीढ, वोढा
* 8.2.32 / 8.2.34 as apavādas of 8.2.31                         — दोग्धा, दोग्धि, नद्धा
* 6.1.73 छे च after aṭ and on the liṭ abhyāsa                     — अच्छषत्, चच्छाद
* 6.4.64 आतो लोप इटि च before 6.1.88 in liṭ ātmanepada           — ददे, तस्थे, जज्ञे
"""
from __future__ import annotations

import pytest

from pipelines.tinanta import derive

CASES = [
    (("lih", "luT", "kartari", 3, 1), {}, "लेढा"),
    (("lih", "laT", "kartari", 2, 3), {}, "लीढ"),
    (("vah", "luT", "kartari", 3, 1), {}, "वोढा"),
    (("02.0004", "luT", "kartari", 3, 1), {}, "दोग्धा"),
    (("02.0004", "laT", "kartari", 3, 1), {}, "दोग्धि"),
    (("02.0005", "luT", "karmani", 3, 1), {}, "देग्धा"),
    (("04.0062", "luT", "kartari", 3, 1), {}, "नद्धा"),
    (("01.1035", "laG", "kartari", 3, 1), {}, "अच्छषत्"),
    (("01.1035", "liT", "kartari", 3, 1), {}, "चच्छाष"),
    (("01.1035", "liT", "karmani", 3, 1), {}, "चच्छषे"),
    (("01.0925", "liT", "kartari", 3, 1), {}, "चच्छाद"),
    (("01.0925", "luG", "karmani", 3, 1), {}, "अच्छादि"),
    (("qudAY", "liT", "kartari", 3, 1), {"pada": "atmane"}, "ददे"),
    (("qudAY", "liT", "kartari", 3, 1), {}, "ददौ"),
    (("01.1077", "liT", "kartari", 3, 1), {"pada": "atmane"}, "तस्थे"),
    (("01.0923", "liT", "karmani", 3, 1), {}, "जज्ञे"),
]


@pytest.mark.parametrize("args,kw,gold", CASES, ids=[c[2] for c in CASES])
def test_surface(args, kw, gold):
    assert derive(*args, **kw).flat_dev() == gold


def test_dho_dhe_chain_is_traced():
    s = derive("vah", "luT", "kartari", 3, 1)
    applied = [e["sutra_id"] for e in s.trace if e["status"] == "APPLIED"]
    assert applied.index("8.4.41") < applied.index("8.3.13") < applied.index("6.3.112")
    assert "6.3.111" not in applied            # 6.3.112 is its apavāda
