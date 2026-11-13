"""strī pratyayas 4.1.16 yañaś ca, 4.1.20, 4.1.21, 4.1.44, 4.1.45, 4.1.48, 4.1.49, 4.1.63, 4.1.65, 4.1.68, 4.1.70: each a real sūtra on the tape (Kāśikā forms)."""
import pytest

import sutras  # noqa: F401
from engine import vikalpa
from pipelines import chain


def _strI(stem, tags=(), choose=None, **viv):
    with vikalpa.choose(choose or {}):
        u = chain.strI(chain.Stem(stem, frozenset(tags)), **viv)
    return u, set(u.trace[-1][1])


def test_4_1_16_gargI_not_gargyA():
    g = chain.taddhita(chain.Stem("garga"), taddhitArtha="apatya", apatyaBeda="gotra")     # 4.1.105 gargAdiByo yaY
    assert g.slp1 == "gArgya"
    u, fired = _strI("gArgya", {"origin_pratyaya:yaY", "origin_it:Y"})
    assert u.slp1 == "gArgI" and "4.1.16" in fired and "4.1.4" not in fired               # yaY: NIp, apavAda of wAp
    assert chain.sup(chain.strI(g), 1, 1).flat_slp1() == "gArgI"
    assert chain.sup(chain.strI(g), 1, 3).flat_slp1() == "gArgyaH"


@pytest.mark.parametrize("stem,tags,viv,sid,strI,nom", [
    ("kumAra", {"lex:prathamavayas"}, {}, "4.1.20", "kumArI", "kumArI"),
    ("paYcapUla", {"lex:dvigu"}, {}, "4.1.21", "paYcapUlI", "paYcapUlI"),
    ("gaRaka", {"lex:puMyoga"}, {}, "4.1.48", "gaRakI", "gaRakI"),
    ("kukkuwa", {"lex:jAti"}, {}, "4.1.63", "kukkuwI", "kukkuwI"),
    ("dAkzi", set(), {"jAtiBeda": "manuzyajAti"}, "4.1.65", "dAkzI", "dAkzI"),
    ("paNgu", set(), {}, "4.1.68", "paNgU", "paNgUH"),
    ("saMhitaUru", set(), {}, "4.1.70", "saMhitorU", "saMhitorUH"),
])
def test_strI_vidhi(stem, tags, viv, sid, strI, nom):
    u, fired = _strI(stem, tags, **viv)
    assert u.slp1 == strI and sid in fired
    assert chain.sup(u, 1, 1).flat_slp1() == nom


def test_4_1_20_needs_the_sense():
    u, fired = _strI("kumAra")
    assert "4.1.20" not in fired and u.slp1 == "kumArA"                                    # 4.1.4 wAp


@pytest.mark.parametrize("stem,tags,sid,vA", [("paTu", {"lex:guRavacana"}, "4.1.44", "paTvI"), ("bahu", set(), "4.1.45", "bahvI")])
def test_vibhasha_ngIz_both_readings(stem, tags, sid, vA):
    u, _ = _strI(stem, tags, choose={sid: False})
    assert u.slp1 == stem                                                                   # the vA not taken: the word stays as it is
    u, fired = _strI(stem, tags, choose={sid: True})
    assert u.slp1 == vA and sid in fired


def test_4_1_49_Anuk():
    u, fired = _strI("indra", {"lex:puMyoga"})
    assert u.slp1 == "indrAnI" and "4.1.49" in fired
    assert chain.sup(u, 3, 1).flat_slp1() == "indrARyA"                                    # 8.4.1 after the seam of Anuk
    assert _strI("hima", {"lex:puMyoga", "lex:mahattva"})[0].slp1 == "himAnI"
    assert _strI("hima", {"lex:puMyoga"})[0].slp1 != "himAnI"                               # himAraRyayor mahattve
