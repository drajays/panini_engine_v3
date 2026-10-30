"""P4a — 6.4.6 – 6.4.96 made real: nṛ ca, anunāsikasya kvijhaloḥ kṅiti, ūṭh (jvara …), rāllopaḥ, raṅjer nalopaḥ before ghañ, bhañjeś ca ciṇi,
viḍvanor anunāsikasyāt, ye vibhāṣā, tanoter yaki, bhrasjo ropadhayoḥ ram, ṇilopa before seṭ niṣṭhā, vā'nyasya saṃyogādeḥ, mayater id, chādeḥ ghe.
Each sūtra is checked on the tape it reads (an aṅga + the pratyaya that follows), the vā ones down both readings (engine.vikalpa.choose)."""
import pytest

import sutras  # noqa: F401
from engine import apply_rule
from engine.state import State, Term
from engine.vikalpa import choose
from engine.vivaksha import set_vivaksha
from phonology.varna import parse_slp1_upadesha_sequence


def T(slp1, tags=(), up=None, kind="pratyaya", **meta):
    return Term(kind=kind, varnas=list(parse_slp1_upadesha_sequence(slp1)), tags=set(tags), meta={"upadesha_slp1": up or slp1, **meta})


def D(slp1, up=None, **meta):
    return T(slp1, {"dhatu", "anga"}, up or slp1, kind="prakriti", **meta)


KIT = {"pratyaya", "ardhadhatuka", "kngiti"}


def run(sid, terms, vivaksha=None, pick=None):
    s = State(terms=terms, meta={}, trace=[])
    if vivaksha:
        set_vivaksha(s, **vivaksha)
    if pick is None:
        return apply_rule(sid, s)
    with choose({sid: pick}):
        return apply_rule(sid, s)


def surface(s, k=0):
    return "".join(v.slp1 for v in s.terms[k].varnas)


def test_6_4_6_nri_both_readings():
    def build():
        pr = T("nAm", {"sup"}, "Am")
        pr.varnas[0].tags.add("nut_agama_inserted")
        return [T("nf", {"anga"}, kind="prakriti"), pr]
    assert surface(run("6.4.6", build(), pick=True)) == "nF"
    assert surface(run("6.4.6", build(), pick=False)) == "nf"


@pytest.mark.parametrize("dh,up,extra,pr,want", [
    ("Sam", "Samu~", {}, T("ta", KIT, "kta"), "SAm"),                 # शान्तः
    ("Sam", "Samu~", {}, T("", {"pratyaya", "ardhadhatuka", "kngiti"}, "kvip"), "SAm"),     # प्रशान्
    ("tam", "tamu~", {}, T("tA", KIT, "kta"), "tAm"),
    ("gam", "gamx~", {"udatta_dhatu": False}, T("ta", KIT, "kta"), "gam"),    # 6.4.37 (para) takes the anudāttopadeśa nasal
    ("Sam", "Samu~", {}, T("tum", {"pratyaya", "ardhadhatuka"}, "tumun"), "Sam"),       # not a kṅit
])
def test_6_4_15(dh, up, extra, pr, want):
    s = run("6.4.15", [D(dh, up, **extra), pr])
    assert surface(s) == want


@pytest.mark.parametrize("dh,pr,want", [
    ("jvar", T("", KIT, "kvip"), "jUr"),
    ("tvar", T("ta", KIT, "kta"), "tUr"),
    ("sriv", T("ta", KIT, "kta"), "srU"),
    ("av", T("", KIT, "kvip"), "U"),
    ("mav", T("", KIT, "kvip"), "mU"),
    ("jvar", T("tum", {"pratyaya", "ardhadhatuka"}, "tumun"), "jvar"),
])
def test_6_4_20_uth(dh, pr, want):
    assert surface(run("6.4.20", [D(dh), pr])) == want


@pytest.mark.parametrize("dh,pr,want", [
    ("murC", T("", KIT, "kvip"), "mur"),
    ("tUrv", T("ta", KIT, "kta"), "tUr"),
    ("murC", T("tum", {"pratyaya", "ardhadhatuka"}, "tumun"), "murC"),
])
def test_6_4_21_ralopa(dh, pr, want):
    assert surface(run("6.4.21", [D(dh), pr])) == want


def test_6_4_27_raga():
    ghan = T("a", {"pratyaya", "ardhadhatuka", "krt"}, "GaY")
    assert surface(run("6.4.27", [D("raYj"), ghan], vivaksha={"artha": "BAva"})) == "raj"
    assert surface(run("6.4.27", [D("raYj"), ghan], vivaksha={"artha": "karaRa"})) == "raj"
    assert surface(run("6.4.27", [D("raYj"), ghan], vivaksha={"artha": "aDikaraRa"})) == "raYj"      # रङ्गः


def test_6_4_33_abhaji_both_readings():
    build = lambda: [D("BaYj"), T("i", {"pratyaya", "ardhadhatuka"}, "ciR")]
    assert surface(run("6.4.33", build(), pick=True)) == "Baj"
    assert surface(run("6.4.33", build(), pick=False)) == "BaYj"


@pytest.mark.parametrize("dh,up,pr,want", [
    ("jan", "jana~", T("", {"pratyaya"}, "viw"), "jaA"),           # गोजाः (the आ then merges by 6.1.101)
    ("Kan", "Kanu~", T("", {"pratyaya"}, "viw"), "KaA"),           # कूपखाः
    ("jan", "jana~", T("an", {"pratyaya"}, "vanip"), "jaA"),       # विजावा
    ("jan", "jana~", T("ta", KIT, "kta"), "jan"),
])
def test_6_4_41(dh, up, pr, want):
    assert surface(run("6.4.41", [D(dh, up), pr])) == want


@pytest.mark.parametrize("dh", ["jan", "san", "Kan"])
def test_6_4_43_both_readings(dh):
    build = lambda: [D(dh), T("ya", KIT, "yak")]
    assert surface(run("6.4.43", build(), pick=True)) == dh[:-1] + "A"      # जायते, सायते, खायते
    assert surface(run("6.4.43", build(), pick=False)) == dh                # जन्यते …


def test_6_4_44_tayate_both_readings():
    build = lambda: [D("tan", "tanu~", gana=8), T("ya", KIT, "yak")]
    assert surface(run("6.4.44", build(), pick=True)) == "taA"
    assert surface(run("6.4.44", build(), pick=False)) == "tan"
    assert surface(run("6.4.44", [D("tan", "tanu~", gana=10), T("ya", KIT, "yak")], pick=True)) == "tan"      # only the tanādi root


def test_6_4_47_bharsta_both_readings():
    build = lambda: [D("Brasj", "Brasja~"), T("tA", {"pratyaya", "ardhadhatuka"}, "tfc")]
    assert surface(run("6.4.47", build(), pick=True)) == "Barj"
    assert surface(run("6.4.47", build(), pick=False)) == "Brasj"
    assert surface(run("6.4.47", [D("Brasj", "Brasja~"), T("ta", KIT, "kta")], pick=True)) == "Brasj"      # before a kṅit the samprasāraṇa takes it


def test_6_4_52_nilopa_before_seT_nishtha():
    nic = T("i", {"pratyaya", "sanadi", "nic"}, "Nic")
    ta = T("ta", {"pratyaya", "ardhadhatuka", "kngiti", "nistha"}, "kta")
    ta.varnas.insert(0, parse_slp1_upadesha_sequence("i")[0])
    ta.varnas[0].tags.add("it_agama")
    s = run("6.4.52", [D("kAr"), nic, ta])
    assert surface(s, 1) == ""
    # no iṭ: no lopa
    s2 = run("6.4.52", [D("kAr"), T("i", {"pratyaya", "sanadi", "nic"}, "Nic"), T("ta", {"pratyaya", "ardhadhatuka", "kngiti", "nistha"}, "kta")])
    assert surface(s2, 1) == "i"


def test_6_4_68_gleyat_both_readings():
    build = lambda: [D("glA"), T("yAs", KIT | {"liN_ashir"}, "yAsuw")]
    assert surface(run("6.4.68", build(), pick=True)) == "gle"
    assert surface(run("6.4.68", build(), pick=False)) == "glA"
    assert surface(run("6.4.68", [D("sTA"), T("yAs", KIT, "yAsuw")], pick=True)) == "sTA"      # a ghu-mā-sthā root keeps ā (6.4.66)
    assert surface(run("6.4.68", [D("yA"), T("yAs", KIT, "yAsuw")], pick=True)) == "yA"        # not saṃyogādi


def test_6_4_70_apamitya_both_readings():
    build = lambda: [D("mA", "qumiY"), T("ya", {"pratyaya", "krt"}, "lyap")]
    assert surface(run("6.4.70", build(), pick=True)) == "mi"
    assert surface(run("6.4.70", build(), pick=False)) == "mA"


def test_6_4_96_chade_ghe():
    gha = T("a", {"pratyaya", "krt"}, "Ga")
    assert surface(run("6.4.96", [D("CAd"), gha])) == "Cad"          # उरश्छदः
    up1 = T("pra", {"upasarga"}, kind="prakriti")
    up2 = T("sam", {"upasarga"}, kind="prakriti")
    assert surface(run("6.4.96", [up1, D("CAd"), gha]), 1) == "Cad"
    assert surface(run("6.4.96", [up2, up1, D("CAd"), T("a", {"pratyaya", "krt"}, "Ga")]), 2) == "CAd"      # समुपच्छादः: after two upasargas it stays long


def test_6_4_49_yasya_halah():
    yan = T("ya", {"pratyaya", "sanadi"}, "yaN")
    ita = T("itA", {"pratyaya", "ardhadhatuka"}, "tfc")
    assert surface(run("6.4.49", [D("beBid"), yan, ita]), 1) == ""            # बेभिदिता
    assert surface(run("6.4.49", [D("lolU"), T("ya", {"pratyaya", "sanadi"}, "yaN"), T("itA", {"pratyaya", "ardhadhatuka"}, "tfc")]), 1) == "ya"   # हलः: not after a vowel (लोलूयिता)
    assert surface(run("6.4.49", [D("beBid"), T("ya", {"pratyaya", "sanadi"}, "yaN"), T("ta", {"pratyaya", "sarvadhatuka"}, "tip")]), 1) == "ya"   # only before an ārdhadhātuka


def test_6_4_50_kyasya_both_readings():
    build = lambda: [D("samiD"), T("ya", {"pratyaya", "sanadi"}, "kyac"), T("itA", {"pratyaya", "ardhadhatuka"}, "tfc")]
    assert surface(run("6.4.50", build(), pick=True), 1) == ""                 # समिधिता
    assert surface(run("6.4.50", build(), pick=False), 1) == "ya"              # समिध्यिता
    assert surface(run("6.4.50", [D("beBid"), T("ya", {"pratyaya", "sanadi"}, "yaN"), T("itA", {"pratyaya", "ardhadhatuka"}, "tfc")]), 1) == "ya"      # a plain ya is 6.4.49's
