"""K5 — kṛts with an upapada (3.1.92 names it, 3.2.1 aṇ, 3.2.2 hve-ve-mā aṇ, 3.2.3 ā-final ka, 2.2.19 samāsa before any sup)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

CASES = [   # (upapada, dhātu id, form)
    ("kumBa", "qukfY", "kumBakAraH"),       # कुम्भकारः
    ("nagara", "qukfY", "nagarakAraH"),     # नगरकारः
    ("kARqa", "lUY", "kARqalAvaH"),         # काण्डलावः
    ("go", "qudAY", "godaH"),               # गोदः (3.2.3 ka, ā-lopa)
    ("kambala", "qudAY", "kambaladaH"),
    ("svarga", "hveY", "svargahvAyaH"),     # 3.2.2
    ("tantu", "veY", "tantuvAyaH"),
    ("DAnya", "mA", "DAnyamAyaH"),
]


@pytest.mark.parametrize("up,ref,want", CASES, ids=lambda c: None)
def test_upapada_krdanta(up, ref, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, "pulliṅga", upapada=(up, "karman")))}
    assert want in got, sorted(got)
