"""Adhyāya 6 placeholders made real (6.1.59, 85, 133; 6.2.184; 6.3.2 – 138; 6.4.127 – 139): each on a hand-built tape, the Laghukaumudī / Kāśikā
examples from the DB, the vā ones down both readings. 6.1.134 (pādapūraṇa needs metre) is a strict xfail."""
import sqlite3
from contextlib import closing
from pathlib import Path

import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from engine.vikalpa import choose
from engine.vivaksha import set_vivaksha
from phonology import mk

DB = Path("/Users/dr.ajayshukla/data-master/ashtadhyayi-ai/db/ashtadhyayi.db")


def T(slp1, *tags, kind="prakriti", up=None, **meta):
    if up:
        meta["upadesha_slp1"] = up
    return Term(kind=kind, varnas=[mk(c) for c in slp1], tags=set(tags), meta=meta)


def SUP(slp1, vib, *tags, up=None):
    return T(slp1, "sup", "pratyaya", vib, *tags, kind="pratyaya", up=up)


def flat(s):
    return ["".join(v.slp1 for v in t.varnas) for t in s.terms]


def run(sid, terms, pick=None, adh=(), meta=None, **viv):
    s = State(terms=terms, meta=dict(meta or {}), trace=[])
    s.adhikara_stack = [{"id": a} for a in adh]
    if viv:
        set_vivaksha(s, **viv)
    if pick is None:
        return apply_rule(sid, s)
    with choose({sid: pick}):
        return apply_rule(sid, s)


BHA = ("6.4.1", "6.4.129")


# --- examples are the book's: the DB must carry them -------------------------------------------------------
EXAMPLES = [("6.1.59", "क्रष्टा"), ("6.1.85", "शिवेहि"), ("6.1.133", "उ॒त स्य"), ("6.2.184", "निरुदकम्"), ("6.3.2", "स्तोकान्मुक्तः"),
            ("6.3.9", "कण्ठेकालः"), ("6.3.14", "सरसिजम्"), ("6.3.34", "रूपवद्भार्यः"), ("6.3.47", "द्वादश"), ("6.3.48", "त्रयोदश"),
            ("6.3.73", "अब्राह्मणः"), ("6.3.74", "अनश्वः"), ("6.3.81", "सचक्रम्"), ("6.3.93", "सम्यङ्"), ("6.3.94", "तिर्यङ्"),
            ("6.3.95", "सध्र्यङ्"), ("6.3.128", "विश्वाराट्"), ("6.3.138", "प्राचः"), ("6.4.127", "अर्वन्तौ"), ("6.4.128", "मघवान्"),
            ("6.4.136", "दध्नि"), ("6.4.138", "दधीचः"), ("6.4.139", "उदीचः")]


@pytest.mark.skipif(not DB.exists(), reason="brain DB absent")
@pytest.mark.parametrize("sid,word", EXAMPLES)
def test_example_in_db(sid, word):
    with closing(sqlite3.connect(DB)) as db:
        texts = " ".join(r[0] for r in db.execute("select content from texts where sutra_id=? and source in ('laghukaumudi','kashika')", (sid,)))
        if word not in texts:      # the DB files a few LK passages under a neighbouring id: look in the next ids too
            texts = " ".join(r[0] for r in db.execute("select content from texts where sutra_id like ? and source in ('laghukaumudi','kashika')", (sid.rsplit(".", 1)[0] + ".%",)))
    assert word.replace("॒", "") in texts.replace("॒", "").replace("॑", ""), (sid, word)


# --- 6.1.59 --------------------------------------------------------------------------------------------------
def _dh(slp1, udatta=False):
    return T(slp1, "dhatu", "anga", udatta_dhatu=udatta)


@pytest.mark.parametrize("dh,want", [("kfz", "kfaz"), ("tfp", "tfap"), ("dfp", "dfap")])    # kraṣṭā, traptā, draptā
def test_6_1_59_am_vibhasha(dh, want):
    mk_ = lambda: [_dh(dh), T("tA", "pratyaya", kind="pratyaya")]
    assert flat(run("6.1.59", mk_(), pick=True))[0] == want
    assert flat(run("6.1.59", mk_(), pick=False))[0] == dh        # the other reading: karṣṭā


@pytest.mark.parametrize("terms", [
    [_dh("vfh", True), T("tA", "pratyaya", kind="pratyaya")],                                  # udātta: varḍhā
    [_dh("Bid"), T("tA", "pratyaya", kind="pratyaya")],                                        # not ṛdupadha
    [_dh("tfp"), T("tum", "pratyaya", "it:kit", kind="pratyaya")],                             # kit
    [_dh("tfp"), T("a", "pratyaya", kind="pratyaya")],                                         # not jhalādi
])
def test_6_1_59_not(terms):
    assert flat(run("6.1.59", terms, pick=True)) == flat(State(terms=terms))


# --- 6.1.85 --------------------------------------------------------------------------------------------------
def test_6_1_85_ekadesa_is_anta_and_adi():
    from sutras.adhyaya_6.pada_1 import sutra_6_1_85 as m
    s = State(terms=[T("Siva", "pada"), T("ihi", "pada")], meta={}, trace=[])
    assert not m._new_cond(s)
    s.terms[0].varnas[-1] = mk("e", "origin:6.1.87")
    assert m._new_cond(s)
    s = apply_rule("6.1.85", s)
    assert {"ekAdeSa_pUrvAnta", "ekAdeSa_parAdi"} <= s.terms[0].varnas[-1].tags and not m._new_cond(s)


def test_6_1_85_not_for_a_plain_sandhi():
    s = State(terms=[T("Siva", "pada"), T("ihi", "pada")], meta={}, trace=[])
    s.terms[0].varnas[-1] = mk("y", "origin:6.1.77")
    assert flat(apply_rule("6.1.85", s)) == flat(s) and not s.terms[0].varnas[-1].tags & {"ekAdeSa_antAdi"}


# --- 6.1.133 -------------------------------------------------------------------------------------------------
def test_6_1_133_su_of_sya_goes_in_the_veda():
    mk_ = lambda: [T("sya"), SUP("s", "vib_prathama", up="su~"), T("vAjI")]
    s = run("6.1.133", mk_(), pick=True, meta={"chandas": True})
    assert flat(s) == ["sya", "", "vAjI"]
    assert flat(run("6.1.133", mk_(), pick=False, meta={"chandas": True})) == ["sya", "s", "vAjI"]        # na ca bhavati


@pytest.mark.parametrize("meta,nxt", [({}, "vAjI"), ({"chandas": True}, "indra")])
def test_6_1_133_not(meta, nxt):
    s = run("6.1.133", [T("sya"), SUP("s", "vib_prathama"), T(nxt)], pick=True, meta=meta)
    assert flat(s)[1] == "s"


@pytest.mark.xfail(strict=True, reason="6.1.134 pādapūraṇa: whether the lopa fills the pāda needs the metre (pāda length), which no machinery has")
def test_6_1_134_sulopa_fills_the_pada():
    assert SUTRA_REGISTRY["6.1.134"].cond(State(terms=[T("sa"), SUP("s", "vib_prathama"), T("eza")], meta={"chandas": True})) and False


# --- 6.2.184 -------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("pu,ut", [("ni", "rudaka"), ("ni", "rupala"), ("ni", "rajina"), ("ud", "ajina")])
def test_6_2_184_antodatta(pu, ut):
    s = run("6.2.184", [T(pu, "samasa_purvapada"), T(ut)])
    assert "svara:antodAtta" in s.terms[-1].varnas[-1].tags


@pytest.mark.parametrize("pu,ut", [("ni", "kzepa"), ("ni", "rudakam")])
def test_6_2_184_not_outside_the_gana(pu, ut):
    s = run("6.2.184", [T(pu, "samasa_purvapada"), T(ut)])
    assert "svara:antodAtta" not in s.terms[-1].varnas[-1].tags


# --- the alug sūtras -----------------------------------------------------------------------------------------
def _alug_tape(pu, sup, vib, ut, *ptags):
    return [T(pu, "samasa_purvapada", *ptags), SUP(sup, vib), T(ut)]


@pytest.mark.parametrize("pu,ut", [("stoka", "mukta"), ("antika", "Agata"), ("dUra", "Agata"), ("kfcCra", "mukta"), ("aByASa", "Agata")])
def test_6_3_2(pu, ut):
    s = run("6.3.2", _alug_tape(pu, "At", "vib_panchami", ut))
    assert "alug" in s.terms[1].tags and flat(s)[1] == "At"


@pytest.mark.parametrize("pu,vib", [("go", "vib_panchami"), ("stoka", "vib_saptami"), ("stoka", "vib_shashthi")])
def test_6_3_2_not(pu, vib):
    assert "alug" not in run("6.3.2", _alug_tape(pu, "At", vib, "mukta")).terms[1].tags


@pytest.mark.parametrize("pu,ut", [("kaNWa", "kAla"), ("yuD", "sTira"), ("tvac", "sAra"), ("aranya", "tilaka"), ("vana", "kiMSuka")])
def test_6_3_9(pu, ut):
    s = run("6.3.9", _alug_tape(pu, "i", "vib_saptami", ut), arthaViSeSa="saMjYA")
    assert "alug" in s.terms[1].tags


@pytest.mark.parametrize("pu,viv", [("nadI", {"arthaViSeSa": "saMjYA"}), ("kaNWa", {}), ("Bumi", {"arthaViSeSa": "saMjYA"})])
def test_6_3_9_not(pu, viv):
    assert "alug" not in run("6.3.9", _alug_tape(pu, "i", "vib_saptami", "kAla"), **viv).terms[1].tags


def test_6_3_14_sarasija_both_readings():
    tape = lambda: [T("saras", "samasa_purvapada", "tatpurusha"), SUP("i", "vib_saptami"), T("jan", "dhatu"), T("qa", "krt", kind="pratyaya")]
    assert "alug" in run("6.3.14", tape(), pick=True).terms[1].tags
    assert "alug" not in run("6.3.14", tape(), pick=False).terms[1].tags          # saroja


def test_6_3_14_needs_a_krt_and_a_tatpurusha():
    assert "alug" not in run("6.3.14", [T("saras", "samasa_purvapada", "tatpurusha"), SUP("i", "vib_saptami"), T("kAla")], pick=True).terms[1].tags
    assert "alug" not in run("6.3.14", [T("saras", "samasa_purvapada"), SUP("i", "vib_saptami"), T("ja"), T("qa", "krt", kind="pratyaya")], pick=True).terms[1].tags


def test_alug_sup_is_not_lukked():
    s = run("6.3.2", _alug_tape("stoka", "At", "vib_panchami", "mukta"))
    s.meta.update({"luk_2_4_71_recipe": True, "pratipadika_avayava_ready": True})
    assert flat(apply_rule("2.4.71", s))[1] == "At"


# --- 6.3.34 --------------------------------------------------------------------------------------------------
def _pumvat(st, ut_tags=("strīliṅga",), pu="darSanIya", stem="A", extra=()):
    return [T(pu, "samasa_purvapada", "karmaDAraya", "lex:BAzitapuMska", *extra), T(stem, "stri_pratyaya", kind="pratyaya", up="wAp"), T("BAryA", *ut_tags)]


@pytest.mark.parametrize("pu,st", [("darSanIya", "A"), ("rUpavat", "I"), ("dIrGajaNGa", "A")])
def test_6_3_34(pu, st):
    s = run("6.3.34", _pumvat(st, pu=pu, stem=st))
    assert flat(s)[1] == "" and "puMvat" in s.terms[1].tags


@pytest.mark.parametrize("terms", [
    [T("KawvA", "samasa_purvapada", "karmaDAraya"), T("A", "stri_pratyaya", kind="pratyaya"), T("BAryA", "strīliṅga")],                    # not bhāṣitapuṃska
    [T("vAmorU", "samasa_purvapada", "karmaDAraya", "lex:BAzitapuMska"), T("U", "stri_pratyaya", kind="pratyaya", up="UN"), T("BAryA", "strīliṅga")],   # ūṅ
    [T("kalyARa", "samasa_purvapada", "karmaDAraya", "lex:BAzitapuMska"), T("I", "stri_pratyaya", kind="pratyaya"), T("pUraRI", "strīliṅga", "pUraRI")],
    [T("kalyARa", "samasa_purvapada", "karmaDAraya", "lex:BAzitapuMska"), T("I", "stri_pratyaya", kind="pratyaya"), T("priyA", "strīliṅga")],   # priyādi
])
def test_6_3_34_not(terms):
    assert "puMvat" not in run("6.3.34", terms).terms[1].tags


# --- 6.3.47 / 48 ---------------------------------------------------------------------------------------------
@pytest.mark.parametrize("pu,ut,want", [("dvi", "daSa", "dvA"), ("dvi", "viMSati", "dvA"), ("azwan", "daSa", "azwaA"), ("azwan", "triMSat", "azwaA")])
def test_6_3_47(pu, ut, want):
    assert flat(run("6.3.47", [T(pu, "samasa_purvapada"), T(ut, "saMKyA")]))[0] == want


@pytest.mark.parametrize("pu,ut,tags", [("dvi", "Sata", ()), ("dvi", "aSIti", ()), ("dvi", "daSa", ("bahuvrihi",)), ("paYcan", "daSa", ())])
def test_6_3_47_not(pu, ut, tags):
    assert flat(run("6.3.47", [T(pu, "samasa_purvapada", *tags), T(ut, "saMKyA")]))[0] == pu


@pytest.mark.parametrize("ut", ["daSa", "viMSati", "triMSat"])
def test_6_3_48(ut):
    assert flat(run("6.3.48", [T("tri", "samasa_purvapada"), T(ut, "saMKyA")]))[0] == "trayas"


def test_6_3_48_not():
    assert flat(run("6.3.48", [T("tri", "samasa_purvapada"), T("Sata", "saMKyA")]))[0] == "tri"
    assert flat(run("6.3.48", [T("tri", "samasa_purvapada"), T("mAtur")]))[0] == "tri"


# --- 6.3.73 / 74 ---------------------------------------------------------------------------------------------
@pytest.mark.parametrize("ut", ["brAhmaRa", "vfzala", "somapa", "aSva"])
def test_6_3_73(ut):
    s = run("6.3.73", [T("na", "samasa_purvapada", up="naY"), T(ut)])
    assert flat(s)[0] == "a"


def test_6_3_73_not():
    assert flat(run("6.3.73", [T("na", "samasa_purvapada", up="na"), T("brAhmaRa")]))[0] == "na"
    assert flat(run("6.3.73", [T("na", "samasa_purvapada", up="naY")]))[0] == "na"


@pytest.mark.parametrize("ut,want", [("aSva", "naSva"), ("aja", "naja")])
def test_6_3_74_after_6_3_73(ut, want):
    s = run("6.3.73", [T("na", "samasa_purvapada", up="naY"), T(ut)])
    s = apply_rule("6.3.74", s)
    assert flat(s) == ["a", want]


def test_6_3_74_needs_lopa_and_ajadi():
    assert flat(run("6.3.74", [T("na", "samasa_purvapada", up="naY"), T("aSva")]))[1] == "aSva"      # n not yet gone
    s = apply_rule("6.3.74", run("6.3.73", [T("na", "samasa_purvapada", up="naY"), T("brAhmaRa")]))
    assert flat(s)[1] == "brAhmaRa"


# --- 6.3.81 --------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("ut", ["cakra", "Dura", "hari"])
def test_6_3_81(ut):
    assert flat(run("6.3.81", [T("saha", "samasa_purvapada", "avyayibhava"), T(ut)]))[0] == "sa"


def test_6_3_81_not():
    assert flat(run("6.3.81", [T("saha", "samasa_purvapada", "avyayibhava"), T("pUrvAhRa", "lex:kAla")]))[0] == "saha"
    assert flat(run("6.3.81", [T("saha", "samasa_purvapada"), T("cakra")]))[0] == "saha"


# --- 6.3.93 – 95 ---------------------------------------------------------------------------------------------
def _anc(pu, d="aYc", pr="kvin"):
    return [T(pu, "upasarga", "samasa_purvapada"), T(d, "dhatu", up="aYcu~"), T("vi", "pratyaya", kind="pratyaya", up=pr)]


@pytest.mark.parametrize("sid,pu,want", [("6.3.93", "sam", "sami"), ("6.3.94", "tiras", "tiri"), ("6.3.95", "saha", "saDri")])
def test_anc_adesa(sid, pu, want):
    tape = _anc(pu)
    if sid == "6.3.94":                       # alope: the sup is there and the añcu is not bha (1.4.18)
        tape.append(T("s", "sup", "pratyaya", kind="pratyaya"))
    assert flat(run(sid, tape))[0] == want


@pytest.mark.parametrize("sid,pu", [("6.3.93", "sam"), ("6.3.94", "tiras"), ("6.3.95", "saha")])
def test_anc_not_without_kvin_or_anc(sid, pu):
    assert flat(run(sid, _anc(pu, pr="Gaw")))[0] == pu
    t = _anc(pu)
    t[1] = T("gam", "dhatu", up="gamx~")
    assert flat(run(sid, t))[0] == pu


def test_6_3_94_only_while_the_a_stands():
    assert flat(run("6.3.94", _anc("tirs")))[0] == "tirs"


# --- 6.3.128 -------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("ut,want", [("vasu", "viSvA"), ("rAw", "viSvA")])
def test_6_3_128(ut, want):
    assert flat(run("6.3.128", [T("viSva", "samasa_purvapada"), T(ut)]))[0] == want


@pytest.mark.parametrize("ut", ["rAj", "deva"])
def test_6_3_128_not(ut):
    assert flat(run("6.3.128", [T("viSva", "samasa_purvapada"), T(ut)]))[0] == "viSva"


# --- 6.3.138 -------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("pu,want", [("pra", "prA"), ("dadhi", "dadhI"), ("maDu", "maDU")])
def test_6_3_138(pu, want):
    assert flat(run("6.3.138", [T(pu), T("c", "dhatu", up="aYcu~")]))[0] == want


def test_6_3_138_not():
    assert flat(run("6.3.138", [T("ud"), T("c", "dhatu", up="aYcu~")]))[0] == "ud"              # not aṇ
    assert flat(run("6.3.138", [T("pra"), T("ac", "dhatu", up="aYcu~")]))[0] == "pra"          # the a is still there
    assert flat(run("6.3.138", [T("pra"), T("c", "dhatu", up="gamx~")]))[0] == "pra"


# --- 6.4.127 / 128 -------------------------------------------------------------------------------------------
def _arvan(stem, sup, *vtags, before=None):
    ts = [T(stem, "anga", "bha")] if False else [T(stem, "anga")]
    ts.append(SUP(sup, *vtags))
    return ([before] if before else []) + ts


@pytest.mark.parametrize("sup,vt", [("au", ("vib_prathama", "vac_dvi")), ("as", ("vib_prathama", "vac_bahu")), ("am", ("vib_dvitiya", "vac_eka")),
                                    ("As", ("vib_trtiya", "vac_eka"))])
def test_6_4_127(sup, vt):
    s = run("6.4.127", _arvan("arvan", sup, *vt), adh=("6.4.1",))
    assert flat(s)[0] == "arvat" and "origin_it:f" in s.terms[0].tags


def test_6_4_127_not_before_su_and_after_nan():
    assert flat(run("6.4.127", _arvan("arvan", "s", "vib_prathama", "vac_eka"), adh=("6.4.1",)))[0] == "arvan"           # arvā
    assert flat(run("6.4.127", _arvan("arvan", "au", "vib_prathama", "vac_dvi", before=T("a", up="naY")), adh=("6.4.1",)))[1] == "arvan"   # anarvāṇau
    assert flat(run("6.4.127", _arvan("arvan", "au", "vib_prathama", "vac_dvi")))[0] == "arvan"                               # no aṅga adhikāra


@pytest.mark.parametrize("sup,vt", [("s", ("vib_prathama", "vac_eka")), ("au", ("vib_prathama", "vac_dvi")), ("as", ("vib_prathama", "vac_bahu"))])
def test_6_4_128_both_readings(sup, vt):
    assert flat(run("6.4.128", _arvan("maGavan", sup, *vt), pick=True, adh=("6.4.1",)))[0] == "maGavat"             # maghavān, maghavantau
    assert flat(run("6.4.128", _arvan("maGavan", sup, *vt), pick=False, adh=("6.4.1",)))[0] == "maGavan"           # maghavā, maghavānau


# --- 6.4.136 -------------------------------------------------------------------------------------------------
def _ni(stem, up="Ni", i="i"):
    return [T(stem, "anga", "bha"), T(i, "sup", "pratyaya", kind="pratyaya", up=up)]


@pytest.mark.parametrize("stem,want", [("rAjan", "rAjn"), ("sAman", "sAmn"), ("dadan", "dadn")])
def test_6_4_136_both_readings(stem, want):
    assert flat(run("6.4.136", _ni(stem), pick=True, adh=BHA))[0] == want
    assert flat(run("6.4.136", _ni(stem), pick=False, adh=BHA))[0] == stem


def test_6_4_136_sI():
    assert flat(run("6.4.136", _ni("sAman", "SI", "I"), pick=True, adh=BHA))[0] == "sAmn"


def test_6_4_136_not():
    assert flat(run("6.4.136", _ni("karman"), pick=True, adh=BHA))[0] == "karman"              # 6.4.137
    assert flat(run("6.4.136", _ni("rAjan", "Bis", "Bis"), pick=True, adh=BHA))[0] == "rAjan"
    assert flat(run("6.4.136", _ni("rAjan"), pick=True))[0] == "rAjan"                          # no bha adhikāra


# --- 6.4.138 / 139 -------------------------------------------------------------------------------------------
def test_6_4_138():
    s = run("6.4.138", [T("dadhi"), T("ac", "dhatu", "bha", up="aYcu~"), SUP("as", "vib_dvitiya")], adh=BHA)
    assert flat(s)[1] == "c"


def test_6_4_138_not():
    assert flat(run("6.4.138", [T("dadhi"), T("aYc", "dhatu", "bha", up="aYcu~")], adh=BHA))[1] == "aYc"     # n not lost
    assert flat(run("6.4.138", [T("dadhi"), T("ac", "dhatu", up="aYcu~")], adh=BHA))[1] == "ac"             # not bha


def test_6_4_139_ud_ac():
    assert flat(run("6.4.139", [T("ud"), T("ac", "dhatu", "bha", up="aYcu~")], adh=BHA))[1] == "Ic"
    assert flat(run("6.4.139", [T("pra"), T("ac", "dhatu", "bha", up="aYcu~")], adh=BHA))[1] == "ac"
