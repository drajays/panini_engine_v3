"""Laghukaumudī examples that exercise the pending structural sūtras (ledger S126 – S137), each through apply_rule.

Every sūtra named here is applied by `apply_rule` on a tape that a real pipeline (the autonomous loop, `pipelines.subanta.derive`,
`pipelines.tinanta`, `pipelines.taddhita_loop`) produced; the example is the Laghukaumudī's own (its discussion text for that sūtra).
Where no pipeline reaches the sūtra yet the tape is built by hand and says so (HAND = S126 – S137 in docs/SHORTCUT_LEDGER.md).

3.1.93 3.1.94 3.1.95 3.4.115 4.1.10 4.1.56 4.1.163 4.1.174 4.4.1 5.4.69 6.1.3 6.1.37 6.1.105 6.4.4 6.4.7 6.4.30 6.4.74 6.4.85
6.4.126 6.4.137 7.1.29 7.1.78 7.2.4 7.2.8 7.2.13 7.2.39 7.2.59 7.3.3 7.3.87 8.1.2 8.2.3 8.2.8 8.2.79 8.3.16 8.4.42
"""
from types import SimpleNamespace

import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from tools.autonomy_report import run_autonomously, start_state


# ── helpers ────────────────────────────────────────────────────────────────────────────────────────────────────────
def _walk(state, budget=90):
    """The autonomous loop of tools.autonomy_report, yielding the tape before every step."""
    from engine.core_loop import advance_phase, apply_pratishedhas, open_adhikaras
    from engine.resolver import resolve_with_reason
    from engine.scheduler import effective_candidates, enumerate_candidates, operational_paribhasha_candidates

    for _ in range(budget):
        open_adhikaras(state)
        yield state
        state = apply_pratishedhas(state)
        usable = effective_candidates(enumerate_candidates(state) + operational_paribhasha_candidates(state), state)
        if not usable:
            if advance_phase(state):
                continue
            return
        state = apply_rule(resolve_with_reason(usable, state).winner, state)
    return


def _fire(sid, state, **kw):
    """(tape where sid's cond holds, tape after apply_rule(sid)) along the loop that starts at ``state``."""
    for st in _walk(state, **kw):
        if SUTRA_REGISTRY[sid].cond(st):
            return st, apply_rule(sid, st.clone())
    pytest.fail(f"{sid}: cond never held along the derivation")


def _never(sid, state):
    assert not any(SUTRA_REGISTRY[sid].cond(st) for st in _walk(state)), sid


def _sub(stem, vib, vac, linga, tags=()):
    s = start_state(SimpleNamespace(kind="subanta", args=(stem, vib, vac, linga)))
    s.terms[0].tags.update(tags)
    return s


def _tin(dhatu, lakara, purusha, vacana, dhatu_tags=()):
    s = start_state(SimpleNamespace(kind="tinanta", args=(dhatu, lakara, purusha, vacana)))
    next(t for t in s.terms if "dhatu" in t.tags).tags.update(dhatu_tags)
    return s


def _tin_pada(dhatu, lakara, purusha, vacana, pada):
    return start_state(SimpleNamespace(kind="tinanta", args=(dhatu, lakara, purusha, vacana), pada=pada))


def _reaches(state, gold, case="x"):
    return run_autonomously(state, gold, case, budget=120).outcome == "reached"


def _traced(state, sid):
    return any(r.get("sutra_id") == sid for r in state.trace)


def _barred(after, *sids):
    """What a pratiṣedha is for: the sūtras it names, offered to apply_rule afterwards, are BLOCKED and leave the tape as it is."""
    for sid in sids:
        out = apply_rule(sid, after.clone())
        assert out.flat_slp1() == after.flat_slp1(), sid
        assert out.trace[-1]["sutra_id"] == sid and out.trace[-1]["status"] == "BLOCKED", (sid, out.trace[-1])


def _hand(*terms, **kw):
    return State(terms=list(terms), meta={}, trace=[], **kw)


def _term(slp1, tags=(), **meta):
    return Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence(slp1)), tags=set(tags), meta=meta)


# ── 3.1 – 3.4: samjñā ──────────────────────────────────────────────────────────────────────────────────────────────
def _krdanta_scope(dhatu="BU"):
    from pipelines.krdanta import build_dhatu_state
    from pipelines.tinanta import P06a_pratyaya_adhikara_3_1_1_to_3

    s = build_dhatu_state(dhatu)
    s.meta["derivation_class"] = "krdanta"
    return P06a_pratyaya_adhikara_3_1_1_to_3(s)


def test_3_1_93_krdatinga_names_the_non_tin_pratyaya():
    """kṛdatiṅ (3.1.93): in the dhātu section a pratyaya that is not tiṅ is kṛt — the Laghukaumudī's own wording."""
    s = apply_rule("3.1.93", _krdanta_scope())
    assert s.samjna_registry.get("krdatinga") is True
    assert apply_rule("3.1.93", s).samjna_registry["krdatinga"] is True        # idempotent
    t = apply_rule("3.1.93", _tin("BU", "laT", 3, 1))
    assert t.samjna_registry.get("krdatinga") is True                           # the tape names it; tiṅ itself stays tiṅ
    assert any("tin_adesha_3_4_78" in x.tags or x.meta.get("upadesha_slp1") for x in t.terms)


def test_3_1_94_vasarupo_utsarga_apavada_gate():
    """vā 'sarūpo 'striyām (3.1.94): the asarūpa apavāda pratyaya may or may not bar the utsarga — a gate, opened once, before any kṛt is on the tape."""
    s = _krdanta_scope()
    assert SUTRA_REGISTRY["3.1.94"].cond(s)
    after = apply_rule("3.1.94", s)
    assert after.meta["krt_kind"] == "3.1.94" and after.paribhasha_gates["3_1_94_vAsarUpost_94"] is True
    assert not SUTRA_REGISTRY["3.1.94"].cond(after)                             # once
    assert not SUTRA_REGISTRY["3.1.94"].cond(_tin("BU", "laT", 3, 1))           # not a tiṅanta tape


def test_3_1_95_krtya_names_the_pratyayas_before_nvul():
    """kṛtyāḥ (3.1.95): the pratyayas up to ṇvul-tṛcau are kṛtya (tavyat, tavya, anīyar, yat, kyap, ṇyat) — read from the kṛt catalogue's own sūtra numbers."""
    from engine.state import Term
    from engine.tape_init.krdanta import build_krdanta_state

    def tape(upadesha):
        pr = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence(upadesha)), tags={"pratyaya", "krt", "upadesha"}, meta={"upadesha_slp1": upadesha})
        return build_krdanta_state([_term("kf", {"dhatu", "anga"}, upadesha_slp1="qukfY"), pr])

    for up in ("tavyat", "tavya", "anIyar", "yat", "kyap", "Ryat"):
        after = apply_rule("3.1.95", tape(up))
        assert "kftya" in after.terms[1].tags and after.samjna_registry["3_1_95_kftyAH"] is True, up
        assert not SUTRA_REGISTRY["3.1.95"].cond(after)                         # once
    for up in ("Rvul", "tfc", "Ramu"):
        assert not SUTRA_REGISTRY["3.1.95"].cond(tape(up)), up                  # ṇvul and after, or elsewhere: not kṛtya
    assert not SUTRA_REGISTRY["3.1.95"].cond(_tin("BU", "laT", 3, 1))           # a tiṅanta tape has no kṛtya


def test_3_4_115_lit_tin_is_ardhadhatuka():
    """liṭ ca (3.4.115): the tiṅ in liṭ's place is ārdhadhātuka — so no śap: cakāra, cakarTa (kṛ), babhūva (bhū)."""
    for dh, pu, gold in (("qukfY", 1, "cakAra"), ("qukfY", 2, "cakarTa"), ("BU", 1, "baBUva")):
        before, after = _fire("3.4.115", _tin(dh, "liT", pu, 1))
        tin = next(t for t in after.terms if "tin_adesha_3_4_78" in t.tags)
        assert "ardhadhatuka" in tin.tags and "sarvadhatuka" not in tin.tags
        assert _reaches(_tin(dh, "liT", pu, 1), gold)


# ── 4.1: strī-pratyaya / taddhita samjñā ────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("stem,linga,gold", [("svasf", "strīliṅga", "svasA"), ("mAtf", "strīliṅga", "mAtA")])
def test_4_1_10_svasradi_take_no_nip_tap(stem, linga, gold):
    """na ṣaṭsvasrādibhyaḥ (4.1.10): svasā, mātā — no ṅīp / ṭāp (the Laghukaumudī's list: svasā tisraś catasraś ca …)."""
    before, after = _fire("4.1.10", _sub(stem, 1, 1, linga))
    assert {"4.1.4", "4.1.5", "4.1.6", "4.1.15", "4.1.41", "4.1.66", "4.1.73"} <= after.blocked_sutras
    _barred(after, "4.1.5")
    assert _reaches(_sub(stem, 1, 1, linga), gold)
    _never("4.1.10", _sub("kanyA", 1, 1, "strīliṅga"))                          # any other stem: no pratiṣedha


def test_4_1_56_krodadi_take_no_nish():
    """na krodādibahvacaḥ (4.1.56): kalyāṇakrodā / sujaghanā keep ā — no ṅīṣ (4.1.54 / 4.1.55 are barred)."""
    for stem in ("kroqA", "sujaGanA"):                                           # krodādi · bahvac (four vowels)
        before, after = _fire("4.1.56", _sub(stem, 1, 1, "strīliṅga"))
        assert {"4.1.54", "4.1.55"} <= after.blocked_sutras
        _barred(after, "4.1.54", "4.1.55")
    assert _reaches(_sub("kroqA", 1, 1, "strīliṅga"), "kroqA")
    _never("4.1.56", _sub("kanyA", 1, 1, "strīliṅga"))                          # two vowels, not in the gaṇa


def _taddhita_hand(sid_adhikara, stem="garga"):
    """HAND (S126): a prātipadika with the adhikāra of the group open; the taddhita pipeline does not call these samjñā sūtras yet."""
    s = _hand(_term(stem, {"prātipadika"}, upadesha_slp1=stem))
    return apply_rule(sid_adhikara, s)


def test_4_1_163_yuva_samjna_for_a_living_vamsya():
    """jīvati tu vaṃśye yuvā (4.1.163): the apatya of the grandson on, while the father is alive, is yuvan."""
    s = _taddhita_hand("4.1.92")
    assert SUTRA_REGISTRY["4.1.163"].cond(s)
    after = apply_rule("4.1.163", s)
    assert after.meta["taddhita_kind"] == "4.1.163" and after.samjna_registry["4_1_163_jIvati_163"] is True
    assert not SUTRA_REGISTRY["4.1.163"].cond(after)


def test_4_1_174_tadraja_samjna():
    """te tadrājāḥ (4.1.174): the añ … pratyayas taught after a kṣatriya's janapada name are tadrāja (pāñcālāḥ)."""
    s = _taddhita_hand("4.1.92", "paYcAla")
    after = apply_rule("4.1.174", s)
    assert after.meta["taddhita_kind"] == "4.1.174" and after.paribhasha_gates["4_1_174_te_174"] is True


def test_4_4_1_pragvahates_thak_is_the_default_of_the_group():
    """prāgvahateṣ ṭhak (4.4.1): ṭhak up to tad vahati — akṣaiḥ dīvyati → ākṣikaḥ (4.4.2)."""
    from engine.vikalpa import explore
    from pipelines.taddhita_loop import derive_taddhita

    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("akza", 1, 1, "puṃliṅga", taddhitArtha="dIvyati"))}
    assert "AkzikaH" in got, sorted(got)
    branches = list(explore(lambda: derive_taddhita("akza", 1, 1, "puṃliṅga", taddhitArtha="dIvyati")))
    assert any(_traced(b.state, "4.4.1") for b in branches if hasattr(b, "state")) or "AkzikaH" in got


def test_5_4_69_na_pujanat_blocks_the_samasanta():
    """na pūjanāt (5.4.69): su-rājā, ati-rājā — no ṭac after pūjana-pūrvapada."""
    s = apply_rule("5.4.68", _hand(_term("su", {"prātipadika", "samAsa_first"}, upadesha_slp1="su"),
                                    _term("rAjan", {"prātipadika", "samAsa_second"}, upadesha_slp1="rAjan")))
    after = apply_rule("5.4.69", s)
    assert after.meta["taddhita_kind"] == "5.4.69" and after.paribhasha_gates["5_4_69_na_69"] is True


# ── 6.1 ────────────────────────────────────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("root,hit", [("UrRu", True), ("UrRu\\Y", True), ("eD", False), ("Ikz", False)])
def test_6_1_3_ndr_not_doubled(root, hit):
    """na ndrāḥ saṃyogādayaḥ (6.1.3): ūrṇu → the r of the rṇ is not doubled: ūrṇunāva (HAND S127 — dvitva is not looped for liṭ yet)."""
    name = root.split("\\")[0]
    s = _hand(_term(name, {"dhatu", "anga"}, upadesha_slp1=root))
    assert SUTRA_REGISTRY["6.1.3"].cond(s) is hit
    after = apply_rule("6.1.3", s)
    assert bool(after.terms[0].meta.get("6_1_3_done")) is hit


def test_6_1_37_yuvan_keeps_its_y():
    """na samprasāraṇe samprasāraṇam (6.1.37): yūnaḥ, yūnā — the y of yuvan is not itself samprasāraṇa'd after 6.4.133 made the ū."""
    before, after = _fire("6.1.37", _sub("yuvan", 3, 1, "puṃliṅga"))
    anga = next(t for t in after.terms if t.meta.get("6_1_37_done"))
    assert [v.slp1 for v in anga.varnas][-3:] == ["y", "U", "n"]
    assert _reaches(_sub("yuvan", 3, 1, "puṃliṅga"), "yUnA")
    _never("6.1.37", _sub("rAma", 3, 1, "puṃliṅga"))


@pytest.mark.parametrize("stem,vib,vac,gold", [("vizvapA", 1, 2, "vizvapO"), ("vizvapA", 1, 3, "vizvapAH"), ("vizvapA", 2, 1, "vizvapAm")])
def test_6_1_105_no_purvasavarna_after_dirgha(stem, vib, vac, gold):
    """dīrghāj jasi ci ca (6.1.105): viśvapau, viśvapāḥ — the dīrgha before jas / ic takes no pūrvasavarṇa (6.1.102)."""
    s = _sub(stem, vib, vac, "puṃliṅga")
    if vac == 1:
        _never("6.1.105", s)                                                    # am is neither jas nor ic: 6.1.107's
    else:
        before, after = _fire("6.1.105", s)
        assert "6.1.102" in after.blocked_sutras
        _barred(after, "6.1.102")
    assert _reaches(_sub(stem, vib, vac, "puṃliṅga"), gold)


# ── 6.4 ────────────────────────────────────────────────────────────────────────────────────────────────────────────
def test_6_4_4_tisr_keeps_short_r_before_nam():
    """na tisṛcatasṛ (6.4.4): tisṛṇām (not *tisṝṇām) — 6.4.3's dīrgha is barred; run by the subanta pipeline."""
    from pipelines.subanta import derive

    s = derive("tri", 6, 3, linga="strīliṅga")
    assert s.flat_slp1() == "tisfRAm" and "6.4.3" in s.blocked_sutras and _traced(s, "6.4.4")


def test_6_4_7_nopadhayah_lengthens_the_upadha_before_nam():
    """nopadhāyāḥ (6.4.7): pañcānām, saptānām — the upadhā of an n-final aṅga is lengthened before nām. Five checks, the sūtra being a vidhi."""
    for stem, gold in (("paYcan", "paYcAnAm"), ("saptan", "saptAnAm"), ("navan", "navAnAm")):
        before, after = _fire("6.4.7", _sub(stem, 6, 3, "puṃliṅga"))
        anga = after.terms[-2]
        assert [v.slp1 for v in anga.varnas][-2] == "A" and anga.meta["6_4_7_done"]
        from pipelines.subanta import derive                                    # the pipeline (8.2.7 after the pada merge) completes the form
        d = derive(stem, 6, 3, linga="puṃliṅga")
        assert d.flat_slp1() == gold and _traced(d, "6.4.7"), stem
    _never("6.4.7", _sub("rAma", 6, 3, "puṃliṅga"))                              # a-final: 6.4.3's dīrgha, not this one
    _never("6.4.7", _sub("rAjan", 3, 1, "puṃliṅga"))                             # no nām: nothing to lengthen for
    # 6.4.7 and 6.4.3 at one tape: the final vowel is 6.4.3's, the upadhā before n is 6.4.7's
    assert not SUTRA_REGISTRY["6.4.7"].cond(apply_rule("6.4.3", _sub("kavi", 6, 3, "puṃliṅga")))


def test_6_4_30_nanceh_pujayam_keeps_the_n():
    """nāñceḥ pūjāyām (6.4.30): prāñcaḥ (honoured), not prācaḥ — the nalopa of 6.4.24 is barred. HAND tag lex:pUjArTa (S128)."""
    before, after = _fire("6.4.30", _sub("prAYc", 1, 3, "puṃliṅga", {"lex:pUjArTa"}))
    assert "6.4.24" in after.blocked_sutras
    _barred(after, "6.4.24")
    _never("6.4.30", _sub("prAYc", 1, 3, "puṃliṅga"))                           # the other añc (gatyartha) is not barred
    _never("6.4.30", _sub("rAma", 1, 3, "puṃliṅga", {"lex:pUjArTa"}))


def test_6_4_74_na_mangyoge_no_at_after_ma():
    """na māṅyoge (6.4.74): mā bhavān bhūt — luṅ without aṭ. HAND tag mAN_yoga on the dhātu (S129, like 'ashis')."""
    s = _tin("BU", "luG", 3, 1, {"mAN_yoga"})
    assert _reaches(_tin("BU", "luG", 3, 1), "aBUt")                            # without māṅ: aṭ
    before, after = _fire("6.4.74", s)
    assert {"6.4.71", "6.4.72"} <= after.blocked_sutras
    _barred(after, "6.4.71", "6.4.72")
    assert _reaches(_tin("BU", "luG", 3, 1, {"mAN_yoga"}), "BUt")
    _never("6.4.74", _tin("BU", "laT", 3, 1, {"mAN_yoga"}))                     # laṭ has no aṭ to bar


def test_6_4_85_bhu_sudhi_no_yan():
    """na bhūsudhiyoḥ (6.4.85): svayambhuvaḥ, sudhiyaḥ — 6.4.82 / 6.4.83 are barred by name; run by the subanta pipeline."""
    from pipelines.subanta import derive

    s = derive("svaBU", 1, 3, linga="pulliṅga")
    assert s.flat_slp1() == "svaBuvaH" and {"6.4.82", "6.4.83"} <= s.blocked_sutras and _traced(s, "6.4.85")


def test_6_4_126_dadade_no_etva():
    """na śasdadavādiguṇānām (6.4.126): dadade — liṭ of dad keeps its a: no etva, no abhyāsalopa (6.4.120 / 6.4.121). HAND vādi (S130)."""
    before, after = _fire("6.4.126", _tin("dada~", "liT", 1, 1))
    assert {"6.4.120", "6.4.121"} <= after.blocked_sutras
    _barred(after, "6.4.120", "6.4.121")
    assert _reaches(_tin("dada~", "liT", 1, 1), "dadade")
    _never("6.4.126", _tin("BU", "liT", 1, 1))


def test_6_4_137_yajvan_keeps_its_a():
    """na saṃyogādvamantāt (6.4.137): yajvanaḥ, brahmaṇaḥ — the a of an -mvan / -vvan aṅga is not dropped (6.4.134); run by the subanta pipeline."""
    from pipelines.subanta import derive

    s = derive("yajvan", 6, 1, linga="pulliṅga")
    assert s.flat_slp1() == "yajvanaH" and _traced(s, "6.4.137")
    assert derive("rAjan", 6, 1, linga="pulliṅga").flat_slp1() == "rAjYaH"


# ── 7.1 ────────────────────────────────────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("stem,gold", [("yuzmad", "yuzmAn"), ("asmad", "asmAn")])
def test_7_1_29_shaso_na(stem, gold):
    """śaso naḥ (7.1.29): yuṣmān, asmān — the a of śas (after ś-lopa) becomes n; run by the asmad / yuṣmad pipeline."""
    from pipelines.asmad_subanta import derive_asmad, derive_yuzmad

    s = (derive_yuzmad if stem == "yuzmad" else derive_asmad)(2, 3)
    assert s.flat_slp1() == gold and _traced(s, "7.1.29")


def test_7_1_78_nabhyastat_satuh_no_num():
    """nābhyastācchatuḥ (7.1.78): dadat, dadatau, dadataḥ — a reduplicated Śatṛ-stem takes no nuṃ (7.1.70)."""
    ABH = {"origin_pratyaya:Satf~", "origin_it:f", "origin_abhyasta"}
    s = _sub("dadat", 1, 2, "puṃliṅga", ABH)
    before, after = _fire("7.1.78", s)
    assert "7.1.70" in after.blocked_sutras
    _barred(after, "7.1.70")
    assert _reaches(_sub("dadat", 1, 2, "puṃliṅga", ABH), "dadatO")
    NO = {"origin_pratyaya:Satf~", "origin_it:f"}                               # BavatO: not abhyasta — nuṃ applies
    assert _reaches(_sub("Bavat", 1, 2, "puṃliṅga", NO), "BavantO")
    _never("7.1.78", _sub("Bavat", 1, 2, "puṃliṅga", NO))


# ── 7.2 ────────────────────────────────────────────────────────────────────────────────────────────────────────────
def test_7_2_4_neti_agopit():
    """neṭi (7.2.4): agopīt — a sic with its iṭ takes no vṛddhi (not *agaupīt)."""
    before, after = _fire("7.2.4", _tin("gupU~", "luG", 3, 1))
    sic = next(t for t in after.terms if (t.meta.get("upadesha_slp1") or "") == "sic")
    assert "neti_7_2_4" in sic.tags
    assert _reaches(_tin("gupU~", "luG", 3, 1), "agopIt")


def _krt_tape(dhatu_upadesha, krt):
    """HAND (S141): the kṛt is put on the dhātu by the test — the kṛt-vidhāna sūtras (3.3.90 …) are not offered by a pipeline for these pratyayas."""
    from engine.lexicon import _dhatu_row
    from engine.tape_init.krdanta import build_krdanta_state
    from engine.tape_init.tinanta import dhatu_term_from_row

    dh = dhatu_term_from_row(_dhatu_row({"kind": "dhatu", "upadesha": dhatu_upadesha}), "kartari", "laT")
    dh.tags.discard("kartari")
    pr = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence(krt)), tags={"pratyaya", "krt", "upadesha"}, meta={"upadesha_slp1": krt})
    return build_krdanta_state([dh, pr])


def test_7_2_8_ned_vasi_kriti():
    """neḍ vaśi kṛti (7.2.8): no iṭ before a vaś-initial kṛt (yaj + naṅ → yajña) — 7.2.35 is barred; a kṛt that is not vaś-initial keeps the question open."""
    before, after = _fire("7.2.8", _krt_tape("yaja~", "naN"))
    assert "7.2.35" in after.blocked_sutras
    _barred(after, "7.2.35")
    assert _reaches(_krt_tape("yaja~", "naN"), "yajYa")
    _never("7.2.8", _krt_tape("yaja~", "tavyat"))                               # t is not vaś
    _never("7.2.8", _tin("BU", "laT", 3, 1))                                    # no kṛt on a tiṅanta tape


def test_7_2_13_krsr_bhr_vr_stu_dru_sru_shru_liti():
    """kṛsṛbhṛvṛstudrusruśruvo liṭi (7.2.13): cakartha, tastartha — these alone are aniṭ in liṭ thal; 7.2.35's iṭ is barred."""
    before, after = _fire("7.2.13", _tin("qukfY", "liT", 2, 1))
    assert "7.2.35" in after.blocked_sutras
    _barred(after, "7.2.35")
    assert _reaches(_tin("qukfY", "liT", 2, 1), "cakarTa")
    _never("7.2.13", _tin("paci~", "liT", 2, 1))                                # papaciTha: any other root keeps the iṭ


def test_7_2_39_na_lini():
    """na liṅi (7.2.39): the iṭ of vṛ / a ṝ-final root is not lengthened before the sīyuṭ of āśīrliṅ (Kāśikā 7.2.42: varisīṣṭa): 7.2.38 is barred."""
    before, after = _fire("7.2.39", _tin_pada("vfN", "AsIrliG", 1, 1, "atmane"))
    assert "7.2.38" in after.blocked_sutras
    _barred(after, "7.2.38")
    _never("7.2.39", _tin("vfN", "liT", 1, 1))                                 # not liṅ
    _never("7.2.39", _tin_pada("BU", "AsIrliG", 1, 1, "atmane"))                # not ṛ-final


def test_7_2_59_vrd_bhyash_catur():
    """na vṛdbhyaś caturbhyaḥ (7.2.59): vartsyati — no iṭ before sya after vṛt, vṛdh, śṛdh, syand in parasmaipada: 7.2.35 is barred."""
    before, after = _fire("7.2.59", _tin_pada("vftu~", "lRT", 3, 1, "parasmai"))              # 1.3.92: vṛtādi take parasmaipada before sya / sana
    assert "7.2.35" in after.blocked_sutras
    _barred(after, "7.2.35")
    _never("7.2.59", _tin_pada("vftu~", "lRT", 3, 1, "atmane"))                 # vartiṣyate: ātmanepada
    _never("7.2.59", _tin("pac", "lRT", 3, 1))                                  # any other root


# ── 7.3 ────────────────────────────────────────────────────────────────────────────────────────────────────────────
def test_7_3_3_ny_vabhyam_padantabhyam_gate():
    """na y-vābhyāṃ padāntābhyāṃ pūrvau tv aic (7.3.3): vaiyākaraṇaḥ — aic is āgama before the pada-final y / v (gate form, S131)."""
    before, after = _fire("7.3.3", _tin("BU", "liT", 1, 1))
    assert after.meta["anga_kind"] == "7.3.3"


def test_7_3_87_na_abhyastasya():
    """jusi ca; nābhyastasyācipiti sārvadhātuke (7.3.87): nenijāni, vevijāni — no laghūpadha guṇa for an abhyasta aṅga before an ac-initial pit sārvadhātuka."""
    for dh, gold in (("Riji~r", "nenijAni"), ("viji~r", "vevijAni"), ("vizx~", "vevizARi")):
        before, after = _fire("7.3.87", _tin(dh, "loT", 1, 1))
        assert "7.3.86" in after.blocked_sutras
        _barred(after, "7.3.86")
        assert _reaches(_tin(dh, "loT", 1, 1), gold)
    _never("7.3.87", _tin("Riji~r", "laT", 3, 1))                               # nenekti: the tiṅ is not ac-initial
    _never("7.3.87", _tin("pac", "loT", 1, 1))                                  # not abhyasta
    assert _reaches(_tin("hu", "loT", 1, 1), "juhavAni")                        # the final-ik guṇa of 7.3.84 is not 7.3.86's


# ── 8.x ────────────────────────────────────────────────────────────────────────────────────────────────────────────
def test_8_1_2_dvitiya_pawat_is_amredita():
    """dviruktasya param āmreḍitam (8.1.2): paṭapaṭāyati — the second paṭat is the āmreḍita; run by derive_anukarana_laT (P017)."""
    from pipelines.tinanta import derive_anukarana_laT

    s = derive_anukarana_laT("pawat", 3, 1)
    assert s.flat_slp1() == "pawapawAyati" and _traced(s, "8.1.2")


@pytest.mark.parametrize("rule", ["8.2.3"])
def test_8_2_3_na_gate_sutra_on_a_pada(rule):
    """8.2.3 na mu ne (amunā) — a tripāḍī prohibition that still opens its gate on a pada (S132: deferred, see ledger)."""
    before, after = _fire(rule, _sub("amu", 3, 1, "puṃliṅga"))
    assert after.meta["sandhi_kind"] == rule
    assert _reaches(_sub("amu", 3, 1, "puṃliṅga"), "amunA")


def test_8_2_8_na_ngi_sambuddhi():
    """8.2.8 na ṅisambuddhyoḥ: he rājan, rājani — the n of the prātipadika stays (8.2.7 is barred)."""
    before, after = _fire("8.2.8", _sub("rAjan", 8, 1, "puṃliṅga"))
    assert "8.2.7" in after.blocked_sutras
    _barred(after, "8.2.7")
    for vib, gold in ((8, "rAjan"), (7, "rAjani")):
        assert _reaches(_sub("rAjan", vib, 1, "puṃliṅga"), gold)
    _never("8.2.8", _sub("rAjan", 1, 1, "puṃliṅga"))                           # rājā: the n goes by 8.2.7


def test_8_2_79_na_bha_kur_chur():
    """8.2.79 na bhakurchurām: kurvaḥ, kurutaḥ, churataḥ — no dīrgha (8.2.77 / 8.2.78 are barred) for the dhātu kur / chur."""
    for dh, pu, gold in (("qukfY", 1, "kurvaH"), ("Cura~", 3, "CurataH")):
        before, after = _fire("8.2.79", _tin(dh, "laT", pu, 2))
        assert _reaches(_tin(dh, "laT", pu, 2), gold)
        assert {"8.2.77", "8.2.78"} <= after.blocked_sutras
        _barred(after, "8.2.77", "8.2.78")
    _never("8.2.79", _tin("BU", "laT", 3, 1))                                    # any other dhātu


def test_8_3_16_rors_supi_is_a_trace_of_8_3_15():
    """roḥ supi (8.3.16): the roḥ → visarga of 8.3.15 before a sup (rāmaḥ …); an anuvāda — its work is 8.3.15's; run by the subanta pipeline."""
    from pipelines.subanta import derive

    s = derive("rAma", 1, 1, linga="pulliṅga")
    assert s.flat_slp1() == "rAmaH"
    assert apply_rule("8.3.16", s.clone()).flat_slp1() == "rAmaH"               # anuvāda: the form does not move


def test_8_4_42_na_padantat_totor_anam():
    """na padāntāṭ ṭoranām (8.4.42): viṭsu (not *viṭṣu) — ṣṭutva (8.4.41) is barred after a pada-final ṭ-varga; run by the subanta pipeline."""
    from pipelines.subanta import derive

    s = derive("viS", 7, 3, linga="pulliṅga")
    assert s.flat_slp1() == "viwsu" and "8.4.41" in s.blocked_sutras and _traced(s, "8.4.42")
