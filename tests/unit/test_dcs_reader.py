"""
tests/unit/test_dcs_reader.py
─────────────────────────────

DCS (source #20) supplies a tagged hypothesis; the engine judges it. These tests
lock the CoNLL-U reader, the tag → engine-request mapping and the named
equivalences, and (when the snapshot is present) one Meghadūta sentence
through analysis-by-synthesis.
"""
from __future__ import annotations

import pytest

from tools import dcs_reader as d

# Meghadūta 1 (DCS sent_id 386937 / 386938), CC BY 4.0.
MEGH = """\
# text = kaścit kāntāvirahaguruṇā svādhikārāt pramattaḥ
# sent_id = 386937
1\tkaścit\tkaścit\tPRON\t_\tCase=Nom|Gender=Masc|Number=Sing\t_\t_\t_\tLemmaId=164309|Unsandhied=kaścid
2-4\tkāntāvirahaguruṇā\t_\t_\t_\t_\t_\t_\t_\t_
2\tkāntā\tkāntā\tNOUN\t_\tCase=Cpd\t_\t_\t_\tLemmaId=13608|Unsandhied=kāntā
4\tguruṇā\tguru\tADJ\t_\tCase=Ins|Gender=Masc|Number=Sing\t_\t_\t_\tLemmaId=124568|Unsandhied=guruṇā
7\tpramattaḥ\tpramad\tVERB\t_\tCase=Nom|Gender=Masc|Number=Sing|VerbForm=Part\t_\t_\t_\tLemmaId=162952
13\tbhartuḥ\tbhartṛ\tNOUN\t_\tCase=Gen|Gender=Masc|Number=Sing\t_\t_\t_\tLemmaId=49047|Unsandhied=bhartuḥ

# text = yakṣaścakre
# sent_id = 386938
1-2\tyakṣaścakre\t_\t_\t_\t_\t_\t_\t_\t_
1\tyakṣaḥ\tyakṣa\tNOUN\t_\tCase=Nom|Gender=Masc|Number=Sing\t_\t_\t_\tLemmaId=72794|Unsandhied=yakṣaḥ
2\tcakre\tkṛ\tVERB\t_\tTense=Past|Mood=Ind|Person=3|Number=Sing\t_\t_\t_\tLemmaId=156168|Unsandhied=cakre
"""


def test_parse_keeps_words_and_drops_multiword_ranges():
    s = d.parse(MEGH)
    assert [x["sent_id"] for x in s] == ["386937", "386938"]
    assert s[0]["text"].startswith("kaścit")
    assert [t["form"] for t in s[1]["tokens"]] == ["yakṣaḥ", "cakre"]


def test_classify_by_tag():
    toks = {t["form"]: t for x in d.parse(MEGH) for t in x["tokens"]}
    assert d.classify(toks["kāntā"]) == "samasa_member"
    assert d.classify(toks["pramattaḥ"]) == "krdanta"
    assert d.classify(toks["guruṇā"]) == "subanta"
    assert d.classify(toks["cakre"]) == "tinanta"


def test_subanta_request_and_untagged_linga_proposes_all_three():
    tok = {"lemma": "bhartṛ", "upos": "NOUN", "feats": {"Case": "Gen", "Gender": "Masc", "Number": "Sing"}, "misc": {}}
    (req,), why = d.subanta_requests(tok)
    assert why is None and (req["stem_slp1"], req["vibhakti"], req["vacana"], req["linga"]) == ("Bartf", 6, 1, "pulliṅga")
    reqs, _ = d.subanta_requests({"lemma": "tad", "upos": "PRON", "feats": {"Case": "Nom", "Number": "Sing"}, "misc": {}})
    assert {r["linga"] for r in reqs} == {"pulliṅga", "strīliṅga", "napuṃsaka"}


def test_dcs_lemma_conventions():
    pron = lambda lemma: d.subanta_requests({"lemma": lemma, "upos": "PRON", "misc": {},
                                             "feats": {"Case": "Acc", "Gender": "Masc", "Number": "Sing"}})
    assert pron("ka")[0][0]["stem_slp1"] == "kim"
    assert pron("mad")[0][0]["stem_slp1"] == "asmad"
    assert {(r["stem_slp1"], r.get("anvadesha")) for r in pron("enad")[0]} == {("etad", True), ("idam", True)}
    assert pron("kaścit") == ([], "kaścit = kim + particle (two padas)")


def test_split_preverbs_undoes_seam_sandhi():
    assert d.split_preverbs("samA") == ["sam", "A"]
    assert d.split_preverbs("vyA") == ["vi", "A"]
    assert d.split_preverbs("upA") == ["upa", "A"]
    assert d.split_preverbs("niH") == ["nis"]
    assert d.split_preverbs("ut") == ["ud"]
    assert d.split_preverbs("rASI") is None


def test_roots_after_preverb():
    assert d._roots("pramad", "pra") == ["mad"]
    assert "Ikz" in d._roots("prekz", "pra")        # 6.1.87
    assert "viS" in d._roots("nirviS", "niH")       # 8.2.66 seam
    assert "i" in d._roots("atI", "ati")            # 6.1.101


def test_nic_bases_undo_nic_changes():
    assert "dfS" in d._nic_bases("darSay")   # 7.3.86
    assert "vah" in d._nic_bases("vAhay")    # 7.2.116
    assert "kf" in d._nic_bases("kAray")     # 7.2.115
    assert "snA" in d._nic_bases("snapay")   # 7.3.36 + 6.4.92
    assert "gaRa" in d._nic_bases("gaRay")   # 6.4.48


def test_named_equivalences():
    assert d._match("kaScit", "kaScid") == "derived_8_4_56"
    assert d._match("saMdeSam", "sandeSam") == "derived_8_4_59"
    assert d._match("kAmAH", "kAmA") == "derived_8_3_22"
    assert d._match("rAmaH", "rAma") == "derived_8_3_22"
    assert d._match("rAmaH", "rAmo") is None


def test_dcs_codepoint_quirks():
    assert d.iast_to_slp1("k\uffb1p") == "kxp"
    assert d.iast_to_slp1("prak\uffde") == "prakF"


def test_attested_forms_prefer_padapatha_then_form():
    tok = {"form": "jalada", "misc": {"Unsandhied": "jaladaiḥ"}}
    assert d.attested_forms(tok) == ["jaladEH", "jalada"]


def test_last_word_of_a_multiword_token_is_checked_against_the_written_string():
    # MBh: guṇāṃstāta, DCS reconstructs the vocative as "tātaiḥ" in both FORM and Unsandhied
    s = d.parse("# sent_id = 1\n3-4\tguṇāṃstāta\t_\t_\t_\t_\t_\t_\t_\t_\n"
                "3\tguṇān\tguṇa\tNOUN\t_\tCase=Acc|Gender=Masc|Number=Plur\t_\t_\t_\tUnsandhied=guṇān\n"
                "4\ttātaiḥ\ttāta\tNOUN\t_\tCase=Voc|Gender=Masc|Number=Sing\t_\t_\t_\tUnsandhied=tātaiḥ\n")
    first, last = s[0]["tokens"]
    assert first["span_surface"] is None and last["span_surface"] == "guṇāṃstāta"
    assert d._match_any("tAta", ["tAtEH"], d.iast_to_slp1(last["span_surface"])) == "derived_surface"
    assert d._match_any("ta", ["tAtEH"], "guRAMstAta") is None


def test_lakara_candidates_for_past():
    assert d.LAKARAS[("Past", "Ind")] == ("liT", "luG")
    assert d.LAKARAS[("Impf", "Ind")] == ("laG",)


def test_coverage_every_samples_chapters(tmp_path, monkeypatch):
    files = []
    for i in range(4):
        f = tmp_path / f"c{i}.conllu"
        f.write_text(f"# sent_id = {i}\n1\tca\tca\tCONJ\t_\t_\t_\t_\t_\t_\n", encoding="utf-8")
        files.append(f)
    monkeypatch.setattr(d, "chapters", lambda text: files)
    assert d.coverage("x", every=2)["counts"] == {"avyaya": {"not_attempted": 2}}
    assert d.coverage("x")["counts"] == {"avyaya": {"not_attempted": 4}}


@pytest.mark.skipif(not d.available(), reason="DCS snapshot not fetched (python3 -m tools.fetch_dcs)")
def test_meghaduta_sentence_through_the_engine():
    toks = {t["form"]: t for x in d.parse(MEGH) for t in x["tokens"]}
    assert d.verify(toks["bhartuḥ"])["status"] == "derived"
    v = d.verify(toks["cakre"])
    assert v["status"] == "derived" and v["request"]["lakara"] == "liT"
