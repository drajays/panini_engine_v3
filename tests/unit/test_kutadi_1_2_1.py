"""1.2.1 गाङ्कुटादिभ्योऽञ्णिन्ङित् — a kuṭādi root's next pratyaya is ṅit (no guṇa)
unless it is ñit/ṇit. Gold: ashtadhyayi.com tables (कुट् 06.0093)."""
from __future__ import annotations

import pytest

from pipelines.tinanta import derive

CASES = [
    (("kuwa~", "luT", "kartari", 3, 1), "कुटिता"),
    (("kuwa~", "lRT", "kartari", 3, 1), "कुटिष्यति"),
    (("kuwa~", "luG", "kartari", 3, 1), "अकुटीत्"),
    (("kuwa~", "liT", "kartari", 2, 1), "चुकुटिथ"),     # thal: pit, not ṇit → ṅit
    (("kuwa~", "liT", "kartari", 3, 1), "चुकोट"),       # ṇal is ṇit → guṇa stays
    (("06.0093", "luG", "karmani", 3, 1), "अकोटि"),     # ciṇ is ṇit
    (("06.0093", "AsIrliG", "karmani", 3, 1), "कुटिषीष्ट"),
    (("BU", "luT", "kartari", 3, 1), "भविता"),           # not kuṭādi
]


@pytest.mark.parametrize("args,gold", CASES, ids=[c[1] for c in CASES])
def test_surface(args, gold):
    assert derive(*args).flat_dev() == gold


def test_atidesha_is_traced_before_guna():
    s = derive("kuwa~", "luT", "kartari", 3, 1)
    applied = [e["sutra_id"] for e in s.trace if e["status"] == "APPLIED"]
    assert "1.2.1" in applied and "7.3.84" not in applied
