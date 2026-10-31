"""Petersen-style theorem check (SCHOLARS_FACTCHECK 6b; no optimality/NP claim): every pratyahara the
engine resolves = contiguous interval of the Sivasutra phoneme sequence from the start letter to
the it-marker that closes it (it-markers excluded), 1.1.71 adir antyena saheta."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from phonology import pratyahara as P
from phonology.pratyahara import build_pratyahara

MS = json.loads((Path(__file__).parents[2] / "data/inputs/maheshvara_sutras.json").read_text())
SEQ = [(ph, ms["index"]) for ms in MS for ph in ms["phonemes"]]       # phonemes only
ITS = [(ms["it"], ms["index"]) for ms in MS]
PH = [p for p, _ in SEQ]


def expected(start, it):
    """Independent reading: first phoneme `start`; closing it = first sutra (>= start's) whose it == `it`."""
    k = next(i for i, (p, _) in enumerate(SEQ) if p == start)
    end_ms = next(m for c, m in ITS if c == it and m >= SEQ[k][1])
    return frozenset(p for p, m in SEQ[k:] if m <= end_ms)


def test_json_matches_engine_table():
    from phonology.maheshvara import MAHESHVARA_SUTRAS
    assert [(m["phonemes"], m["it"]) for m in MS] == [(m["phonemes"], m["it"]) for m in MAHESHVARA_SUTRAS]


def test_every_resolvable_pair_is_the_contiguous_interval():
    n = 0
    for start in dict.fromkeys(PH):
        for it in dict.fromkeys(c for c, _ in ITS):
            try:
                got = build_pratyahara(start, it)
            except ValueError:
                continue
            assert got == expected(start, it), (start, it)
            n += 1
    assert n > 100


CONS = "hyvrlYmNRnJBGQDjbgqdKPCWTcwtkpSzs"
# Traditional pratyaharas (Laghukaumudi), SLP1 (aC in the brief = ac, it-markers lower/upper as in the table)
TRAD = {
    ("a", "c"): "aiufxeoEO",
    ("h", "l"): CONS,
    ("y", "R"): "yvrl",
    ("J", "S"): "JBGQDjbgqd",
    ("B", "S"): "BGQDjbgqd",
    ("a", "l"): "aiufxeoEO" + CONS,
    ("i", "k"): "iufx",
    ("e", "c"): "eoEO",
    ("a", "k"): "aiufx",
    ("y", "Y"): "yvrlYmNRnJB",
    ("J", "y"): "JBGQDjbgqdKPCWTcwtkp",
    ("K", "r"): "KPCWTcwtkpSzs",
    ("c", "r"): "cwtkpSzs",
    ("S", "r"): "Szs",
    ("S", "l"): "Szsh",
    # Doubly-used N (1.1.71 + tradition): the table names MS1's it "N" (data convention, colliding in
    # shape with the N phoneme but flagged as it) and MS6's "R"; so aN-first = (a,N), aN-wide/iN/yaN = ..R.
    ("a", "N"): "aiu",
    ("u", "N"): "u",
    ("a", "R"): "aiufxeoEOhyvrl",
    ("i", "R"): "iufxeoEOhyvrl",   # 8.3.57 iNkoh
    ("u", "k"): "ufx",
}


@pytest.mark.parametrize("pair", sorted(TRAD))
def test_traditional_pratyahara(pair):
    assert build_pratyahara(*pair) == frozenset(TRAD[pair])


def test_hal_includes_first_h_double_use():
    """h occurs in MS5 and MS14 (hal = h ... l-it of MS14): the set is all consonants."""
    assert build_pratyahara("h", "l") == frozenset(CONS)
    assert build_pratyahara("a", "l") == P.AC | P.HAL


def test_module_constants_agree_with_build():
    for const, pair in [(P.AC, ("a", "c")), (P.HAL, ("h", "l")), (P.IK, ("i", "k")), (P.EC, ("e", "c")),
                        (P.YAN, ("y", "R")), (P.JHAL, ("J", "l")), (P.KHAR, ("K", "r"))]:
        assert const == build_pratyahara(*pair)


def test_iN_is_the_laN_reading():
    assert P.IN == frozenset("iufxeoEOhyvrl")
