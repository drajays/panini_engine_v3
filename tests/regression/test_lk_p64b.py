"""P4b — 6.4.115 – 6.4.169 placeholders made real: the verb ī/ā sūtras (115 – 118, 121, 124), the bha-aṅga sūtras (131, 132, 140, 150, 161)
and the prakṛtibhāva niṣedhas (163, 164, 167, 169). Each is run through apply_rule on a hand-built tape, as in test_sutra_6_4_bhAdhikAra_vidhis."""
import importlib

import pytest

import sutras  # noqa: F401
from engine import apply_rule, SUTRA_REGISTRY
from engine.state import State, Term
from engine.vikalpa import choose
from phonology import mk


def T(slp1, tags=(), kind="prakriti", **meta):
    return Term(kind=kind, varnas=[mk(c) for c in slp1], tags=set(tags), meta=dict(meta))


def flat(s, i=0):
    return "".join(v.slp1 for v in s.terms[i].varnas)


def run(sid, terms, adhikara=True):
    s = State(terms=terms)
    if adhikara:
        s.adhikara_stack.append({"id": "6.4.1", "scope_end": "7.4.97", "text_dev": "अङ्गस्य"})
        s.adhikara_stack.append({"id": "6.4.129", "scope_end": "6.4.175", "text_dev": "भस्य"})
    assert SUTRA_REGISTRY[sid].cond(s), sid
    with choose({sid: True}):                      # the vā sūtras: the reading in which the sūtra applies (the other reading leaves the tape alone)
        return apply_rule(sid, s)


def tin(up, first=None, extra=()):
    return T(first or up, {"pratyaya", "tin", "kngiti", *extra}, kind="pratyaya", upadesha_slp1=up)


DH = {"dhatu", "anga"}
AB = T("bi", {"abhyasa", "anga"})


def test_115_bhi_short_i():
    s = run("6.4.115", [AB, T("BI", DH), tin("tas")])
    assert flat(s, 1) == "Bi"


def test_116_jahati_short_i():
    s = run("6.4.116", [T("ja", {"abhyasa", "anga"}), T("hA", DH), tin("tas")])
    assert flat(s, 1) == "hi"


def test_117_jahati_long_i_before_hi():
    s = run("6.4.117", [T("ja", {"abhyasa", "anga"}), T("hA", DH), tin("hi", "hi")])
    assert flat(s, 1) == "hI"


def test_118_jahati_a_lopa_before_y():
    s = run("6.4.118", [T("ja", {"abhyasa", "anga"}), T("hA", DH), tin("yAs", "yAs")])
    assert flat(s, 1) == "h"


def test_121_thal_set_e_and_abhyasa_lopa():
    ab = T("pa", {"abhyasa", "anga"})
    it = T("iw", {"agama"}, kind="agama")
    it.varnas[0].tags.add("it_agama")
    th = T("Tal", {"pratyaya", "tin"}, kind="pratyaya", upadesha_slp1="Tal", source_lakara_upadesha="liT")
    th.varnas = [mk("i"), mk("T"), mk("a")]
    th.varnas[0].tags.add("it_agama")
    s = run("6.4.121", [ab, T("pac", DH), th])
    assert [flat(s, i) for i in range(len(s.terms))][0] == "pec"


def test_124_jar_bhram_tras_e():
    ab = T("Ba", {"abhyasa", "anga"})
    lit = Term(kind="pratyaya", varnas=[mk(c) for c in "atus"], tags={"pratyaya", "tin", "kngiti"},
               meta={"upadesha_slp1": "atus", "source_lakara_upadesha": "liT"})
    s = run("6.4.124", [ab, T("Bram", DH), lit])
    assert flat(s, 0) == "Brem"


def bha(slp1, *extra):
    return T(slp1, {"anga", "bha", "prātipadika", *extra})


SUP = T("as", {"pratyaya", "sup"}, kind="pratyaya", upadesha_slp1="Sas")


def test_131_vasu_samprasarana():
    s = run("6.4.131", [bha("vidvas", "origin_pratyaya:kvasu~"), SUP])
    assert flat(s) == "vidus"


def test_132_vah_uth():
    s = run("6.4.132", [bha("prazwavAh", "origin_dhatu:vah"), SUP])
    assert flat(s) == "prazwaUh"      # 6.1.89 then makes it प्रष्ठौह्


def test_140_dhatu_final_a_lopa_and_khatva_stays():
    s = run("6.4.140", [bha("kIlAlapA", "origin_dhatu:pA"), SUP])
    assert flat(s) == "kIlAlap"
    s2 = State(terms=[bha("KawvA"), SUP])
    s2.adhikara_stack += [{"id": "6.4.1", "scope_end": "7.4.97", "text_dev": "x"}, {"id": "6.4.129", "scope_end": "6.4.175", "text_dev": "x"}]
    assert importlib.import_module("sutras.adhyaya_6.pada_4.sutra_6_4_140")._find(s2) is None      # no origin_dhatu: खट्वा keeps its ā


def test_150_hal_ya_lopa_before_I():
    s = run("6.4.150", [bha("gArgya", "origin_pratyaya:yaY"), T("I", {"pratyaya"}, kind="pratyaya", upadesha_slp1="NIp")])
    assert flat(s) == "gArga"


def test_161_r_for_f():
    s = run("6.4.161", [T("pfT", {"anga"}), T("izW", {"pratyaya", "taddhita"}, kind="pratyaya", upadesha_slp1="izWan")])
    assert flat(s) == "praT"


def test_163_ekac_stays():
    t = T("srag", {"anga", "bha", "origin_pratyaya:vini"})
    s = run("6.4.163", [t, T("izW", {"pratyaya", "taddhita"}, kind="pratyaya", upadesha_slp1="izWan")])
    assert s.terms[0].meta.get("6_4_155_family_done") is True


ADH = [{"id": "6.4.1", "scope_end": "7.4.97", "text_dev": "x"}, {"id": "6.4.129", "scope_end": "6.4.175", "text_dev": "x"}]


def test_164_167_169_niShedha_set_the_guard_6_4_144_reads():
    cases = [("6.4.164", "daRqin", "aR", ()), ("6.4.167", "sAman", "aR", ()), ("6.4.169", "Atman", "Ka", ("origin_pratyaya:Ka",))]
    for sid, stem, up, extra in cases:
        taddh = T(up, {"pratyaya", "taddhita", *extra}, kind="pratyaya", upadesha_slp1=up)
        s = State(terms=[bha(stem), taddh])
        s.adhikara_stack += ADH
        assert SUTRA_REGISTRY[sid].cond(s), sid
        s = apply_rule(sid, s)
        assert s.terms[0].meta["6_4_144_ti_done"] is True
        assert importlib.import_module("sutras.adhyaya_6.pada_4.sutra_6_4_144")._in_site(s) is None      # 144 no longer offers this ṭi


def test_164_apatya_frame_does_not_bar():
    taddh = T("aR", {"pratyaya", "taddhita"}, kind="pratyaya", upadesha_slp1="aR")
    s = State(terms=[bha("daRqin"), taddh])
    s.adhikara_stack += ADH + [{"id": "4.1.92", "artha": "apatya", "scope_end": "4.1.175"}]
    assert importlib.import_module("sutras.adhyaya_6.pada_4.sutra_6_4_164")._find(s) is None      # an aṇ in the offspring sense: 6.4.144 may take the in


def test_115_vikalpa_other_reading_leaves_the_long_i():
    s = State(terms=[AB, T("BI", DH), tin("tas")])
    s.adhikara_stack += ADH
    with choose({"6.4.115": False}):
        s = apply_rule("6.4.115", s)
    assert flat(s, 1) == "BI"
