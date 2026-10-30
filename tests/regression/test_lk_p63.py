"""LK pāda 6.3: 6.3.66 (hrasva before a khit uttarapada), 6.3.90 / 6.3.91 (īś, kī, ā before vatu), 6.3.116 (dīrgha before nahi … kvip)."""
import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from engine.vikalpa import explore
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.krdanta import derive_krdanta
from pipelines.taddhita_loop import derive_taddhita
from sutras.adhyaya_6.pada_3 import sutra_6_3_116 as m116

PU = "pulliṅga"
VATU = [   # (stem, a form that must be among the readings): 5.2.39 – 40 with 6.3.90 / 6.3.91 / 7.1.2 on the stem and the gha
    ("yad", "yAvAn"), ("tad", "tAvAn"), ("etad", "etAvAn"), ("idam", "iyAn"), ("kim", "kiyAn"),
]
KHIT = [   # (upapada, linga, form): 6.3.66 shortens the long vowel, 6.3.67's mum stands after it
    ("kAlI", "strīliṅga", "kAlimmanyA"), ("hariRI", "strīliṅga", "hariRimmanyA"),
]


@pytest.mark.parametrize("stem,want", VATU)
def test_vatu(stem, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, PU, taddhitArtha="parimARa"))}
    assert want in got, sorted(got)


@pytest.mark.parametrize("up,linga,want", KHIT)
def test_hrasva_before_khit(up, linga, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta("mana~", 1, 1, linga, upapada=(up, "karman"), AtmamAna="AtmamAna"))}
    assert want in got, sorted(got)


def test_hrasva_not_for_an_avyaya():
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta("mana~", 1, 1, PU, upapada=("paRqita", "karman"), AtmamAna="AtmamAna"))}
    assert "paRqitammanyaH" in got, sorted(got)


def _term(slp1, kind="prakriti", tags=(), **meta):
    return Term(kind=kind, varnas=list(parse_slp1_upadesha_sequence(slp1)), tags=set(tags), meta=dict(meta))


def _flat(state):
    return "".join(v.slp1 for t in state.terms for v in t.varnas)


@pytest.mark.parametrize("dhatu,dh_slp1,upa,want", [("ruca~", "ruc", "ni", "nI"), ("vfzu~", "vfz", "pra", "prA"), ("Raha~", "Rah", "upa", "upA"), ("zaha~", "zah", "ati", "atI")])
def test_dirgha_before_kvip(dhatu, dh_slp1, upa, want):
    d = _term(dh_slp1, tags={"anga", "dhatu"}, upadesha_slp1=dhatu)
    kv = _term("kvip", kind="pratyaya", tags={"pratyaya", "krt"}, upadesha_slp1="kvip")
    s = State(terms=[_term(upa, tags={"upapada", "upasarga"}), d, kv])
    s.phase = "sandhi"
    assert SUTRA_REGISTRY["6.3.116"].cond(s)
    s = apply_rule("6.3.116", s)
    assert "".join(v.slp1 for v in s.terms[0].varnas) == want
    assert not m116._new_cond(s)      # once only (the legacy gate half is S24's)


def test_no_dirgha_without_kvip():
    d = _term("ruc", tags={"anga", "dhatu"}, upadesha_slp1="ruca~")
    s = State(terms=[_term("ni", tags={"upapada", "upasarga"}), d])
    s.phase = "sandhi"
    assert not m116._new_cond(s)
