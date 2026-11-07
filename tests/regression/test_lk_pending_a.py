"""LK pending-structural batch A (ledger S114-S125): Laghukaumudi words put on the tape by the subanta pipeline's
build_initial_state, then each structural sutra is offered through engine.apply_rule and its registry/tag effect is asserted.
Sutras: 1.1.25 1.1.33 1.1.35 1.1.36 1.1.37 1.1.69 1.1.70 1.1.71 1.2.27 1.2.31 1.2.44 1.4.2 1.4.11 1.4.12 1.4.19 1.4.24
1.4.42 1.4.49 1.4.51 1.4.57 1.4.58 1.4.61 2.1.1 2.2.23 2.3.49 2.4.83."""
import pytest

import sutras  # noqa: F401
from engine import apply_rule
from engine.tape_init.sanadi import with_vivaksha
from pipelines.subanta import build_initial_state


def st(stem, *tags, viv=None, **meta):
    """The stem on the subanta tape; ``viv`` is the speaker's vivakṣā (engine/tape_init), the only way a sense reaches the tape."""
    s = build_initial_state(stem, 1, 1)
    s.terms[0].tags.add("prātipadika")
    s.terms[0].tags.update(tags)
    s.meta.update(meta)
    if viv:
        with_vivaksha(s, **viv)
    return s


def run(sid, s):
    return apply_rule(sid, s)


def reg(s, k):
    return s.samjna_registry.get(k)


# ── sarvanama / sankhya samjnas on a stem ─────────────────────────────────────
def test_1_1_25_kati_zat():
    s = st("kati")
    for sid in ("1.1.23", "1.1.24", "1.1.25"):
        s = run(sid, s)
    assert "zat_samjna" in s.terms[0].tags and reg(s, "zaW_qati") == frozenset({"kati"})
    assert "zat_samjna" not in run("1.1.25", st("rAma")).terms[0].tags      # not a kati-class stem


@pytest.mark.parametrize("stem", ["praTama", "carama", "alpa", "katipaya", "nema"])
def test_1_1_33_prathamadi(stem):
    assert "sarvanama" in run("1.1.33", st(stem)).terms[0].tags


def test_1_1_33_negative():
    assert "sarvanama" not in run("1.1.33", st("rAma")).terms[0].tags


def test_1_1_35_sva():
    assert "sarvanama" in run("1.1.35", st("sva")).terms[0].tags            # sva = the self's
    assert "sarvanama" not in run("1.1.35", st("sva", viv={"svaBeda": "jYAti"})).terms[0].tags   # sva = a kinsman
    assert "sarvanama" not in run("1.1.35", st("sva", viv={"svaBeda": "Dana"})).terms[0].tags    # sva = wealth


def test_1_1_36_antara():
    assert "sarvanama" in run("1.1.36", st("antara", viv={"antaraBeda": "bahiryoga"})).terms[0].tags        # antare grAmAH
    assert "sarvanama" in run("1.1.36", st("antara", viv={"antaraBeda": "upasaMvyAna"})).terms[0].tags      # antarah SATakah
    assert "sarvanama" not in run("1.1.36", st("antara")).terms[0].tags


def test_1_1_37_svaradi():
    assert "avyaya" in run("1.1.37", st("svar")).terms[0].tags                          # svar, svasti, ...
    assert "avyaya" not in run("1.1.37", st("rAma")).terms[0].tags


# ── paribhasha / samjna registrations (rule fires once, then is idempotent) ───
@pytest.mark.parametrize("sid,gate", [
    ("1.1.70", "1_1_70_tapara_tatkAlasya"),     # taparas tatkAlasya
    ("1.1.71", "1_1_71_Adir_antyena_sahetA"),   # Adir antyena sahetA (pratyahara)
    ("1.1.69", "1_1_69_aN_udit_savarNa"),       # aR udit savarnasya cApratyayaH
])
def test_gate_once(sid, gate):
    s = run(sid, st("rAma"))
    assert s.paribhasha_gates.get(gate) is True and reg(s, gate)


def test_1_1_69_an():
    assert reg(run("1.1.69", st("rAma")), "1_1_69_aN_udit_savarNa") == frozenset({"a", "i", "u"})


def test_1_2_27_matra():
    s = run("1.2.27", st("rAma"))
    assert "a" in reg(s, "hrasva") and "A" in reg(s, "dIrgha") and reg(s, "pluta") is True and "a" not in reg(s, "dIrgha")


def test_1_2_31_svarita():
    assert reg(run("1.2.31", st("rAma")), "svarita") == "samAhAraH"


def test_1_2_44_ekavibhakti():          # gate opens in the subanta scope only
    assert run("1.2.44", st("rAma")).paribhasha_gates.get("1_2_44_ekavibhakti_apUrvanipAte") is True


# ── 1.4 samjnas ───────────────────────────────────────────────────────────────
def test_1_4_2_vipratisedhe():
    s = run("1.4.2", st("rAma"))
    assert s.paribhasha_gates["1_4_2_vipratiSeDe"] is True and reg(s, "vipratiSeDe_param_kAryam") == frozenset({"para_wins"})


def test_1_4_11_samyoge_guru():
    assert reg(run("1.4.11", st("rAma")), "guru_saMYoge")


def test_1_4_12_dirgha_guru():
    assert "A" in reg(run("1.4.12", st("rAma")), "guru_dirgha")


def test_1_4_19_tasau():
    assert reg(run("1.4.19", st("Bagavat")), "tasau_matvArTe")


def test_1_4_24_apadana():             # grAmAd Agacchati: dhruvam apAye 'pAdAnam
    s = run("1.4.24", run("1.4.23", st("grAma", viv={"kArakaArTa": "apAya"})))
    assert "apAdAna" in s.terms[0].tags
    assert "apAdAna" not in run("1.4.24", st("grAma", viv={"kArakaArTa": "apAya"})).terms[0].tags   # no kAraka adhikara open


def test_1_4_42_karana():              # sAdhakatamaM karaNam: parazunA Cinatti
    s = run("1.4.42", st("parazu", viv={"kArakaArTa": "sADakatama"}))
    assert "karaRa" in s.terms[0].tags and reg(s, "karaRa") == "sADakatama"


def test_1_4_49_karman():              # kartur ipsitatamaM karma: odanaM pacati
    assert "karman" in run("1.4.49", st("odana", viv={"kArakaArTa": "Ipsitatama"})).terms[0].tags
    assert "karman" not in run("1.4.49", st("odana")).terms[0].tags


def test_1_4_51_akathita():            # akathitaM ca: gAM dogDi payaH
    assert "karman" in run("1.4.51", st("go", viv={"kArakaArTa": "akaTita"})).terms[0].tags


def test_1_4_57_ca_adi():
    assert "ca" in reg(run("1.4.57", st("ca")), "nipata_ca_adi")


def test_1_4_58_pra_adi():
    assert "pra" in reg(run("1.4.58", st("pra")), "upasarga_list")


def test_1_4_61_urya_adi():
    s = run("1.4.61", st("UrI"))
    assert "UrI" in reg(s, "gati_uryadiR") and "UrI" in reg(s, "gati_set")


# ── 2.x ───────────────────────────────────────────────────────────────────────
def test_2_1_1_samartha():
    assert run("2.1.1", st("rAjan")).paribhasha_gates["2.1.1_samartha_padavidhi"] is True


def test_2_2_23_bahuvrihi():           # prAptodaka: sesa = bahuvrihi
    assert run("2.2.23", st("prAptodaka", "bahuvrIhi")).meta["bahuvrihi_kind"] == "2.2.23"
    assert "bahuvrihi_kind" not in run("2.2.23", st("rAma")).meta


def test_2_3_49_sambuddhi():
    assert reg(run("2.3.49", st("rAma")), "sambuddhi") is True


def test_2_4_83_navyayibhava():        # upakumBam: am stays (no luk) -- the lup context is opened by the caller
    s = run("2.4.83", st("upakumBa", **{"2_4_83_lup_context": True}))
    assert s.meta["lup_kind"] == "2.4.83"
    assert "lup_kind" not in run("2.4.83", st("rAma")).meta


def test_derive_records_the_vivaksha():
    """The subanta pipeline takes the speaker's meaning and puts it on the tape (engine/tape_init); a value outside the closed schema is refused."""
    from pipelines.subanta import derive
    assert derive("grAma", 5, 1, "pulliṅga", kArakaArTa="apAya").vivaksha == {"kArakaArTa": "apAya"}
    with pytest.raises(ValueError):
        derive("grAma", 5, 1, "pulliṅga", kArakaArTa="no_such_role")
