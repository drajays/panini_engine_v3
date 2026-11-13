"""3.1.28 गुपूधूपविच्छिपणिपनिभ्य आयः (sārvadhātuka: nitya) and 3.1.31 आयादय आर्धधातुके वा (ārdhadhātuka: optional).
Kāśikā: गोपायति। धूपायति। पणायति।; गोप्ता, गोपायिता।"""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def _all(dhatu, lakara):
    return {b.surface_slp1 for b in explore(lambda: derive(dhatu, lakara, "kartari", 3, 1))}


@pytest.mark.parametrize("dhatu,want", [
    ("01.0461", "gopAyati"),     # gupU
    ("01.0462", "DUpAyati"),     # DUpa
    ("01.0507", "paRAyati"),     # paRa: ātmanepadī root, but the āya-anta takes parasmaipada (Kāśikā 3.1.28)
])
def test_sarvadhatuka_nitya(dhatu, want):
    assert _all(dhatu, "laT") == {want}


def test_ardhadhatuka_vikalpa():
    got = _all("01.0461", "luT")
    assert {"gopitA", "gopAyitA"} <= got                      # Kāśikā 3.1.31
    assert "gopAyaitA" not in got


def test_aya_before_am_and_yasut():
    assert {"gopAyAYcakAra", "gopAyAmAsa"} <= _all("01.0461", "liT")          # 3.1.35: pratyayānta + ām
    assert {"gopAyyAt", "gupyAt"} <= _all("01.0461", "AsIrliG")
