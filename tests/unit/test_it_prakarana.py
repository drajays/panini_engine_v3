"""
It-saṃjñā prakaraṇa **1.3.2**–**1.3.9** on single upadeśas, always run as the
full ordered sequence (``pipelines.it_prakarana.run_it_prakarana``).

Examples follow the Kāśikā udāharaṇa / pratyudāharaṇa of each sūtra and
N. Bodas, *इत्संज्ञाप्रकरणम्* (2015) — the flow-chart dhātu → pratyaya →
taddhita / vibhakti.  Each case pins the residue **and** the it-class names
1.3.9 records (kit, ṅit, ñīt, ḍvit, irit …), which later rules read.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401
from engine.it_samjna import (
    META_IT_LOPA_LOG,
    has_it,
    it_names,
    it_records,
)
from engine.state import State, Term
from pipelines.it_prakarana import IT_PRAKARANA_SEQUENCE, run_it_prakarana
from phonology.varna import parse_slp1_upadesha_sequence

_PRATYAYA = {"pratyaya", "upadesha"}


def _state(upadesha: str, kind: str, tags: set[str]) -> State:
    t = Term(
        kind=kind,
        varnas=list(parse_slp1_upadesha_sequence(upadesha)),
        tags=set(tags) | {"upadesha"},
        meta={"upadesha_slp1": upadesha},
    )
    return State(terms=[t], meta={}, trace=[])


def _run(upadesha: str, kind: str, tags: set[str]):
    s = run_it_prakarana(_state(upadesha, kind, tags))
    t = s.terms[0]
    return s, t, "".join(v.slp1 for v in t.varnas)


DHATU = ("prakriti", {"dhatu"})


@pytest.mark.parametrize(
    "upadesha, kind_tags, residue, names",
    [
        # 1.3.2 + 1.3.3 + 1.3.5 — dhātus (Bodas: डुपचँष्, णीञ्, गमॢँ, ओँप्यायीँ)
        ("qupaca~z", DHATU, "pac", {"qvit", "adit", "zit"}),
        ("YimidA~", DHATU, "mid", {"YIt", "Adit"}),
        ("wuo~Svi", DHATU, "Svi", {"wvit", "odit"}),
        ("qukfY", DHATU, "kf", {"qvit", "Yit"}),
        ("gamx~", DHATU, "gam", {"xdit"}),
        ("vadi~", DHATU, "vad", {"idit"}),
        ("BU", DHATU, "BU", set()),
        # vārttika इर इत्संज्ञा वाच्या — one irit, not i-dit + r-it
        ("Bidi~r", DHATU, "Bid", {"irit"}),
        # 1.3.6 pratyudāharaṇa: a dhātu's ष् is not it (षोडः)
        ("zaha~", DHATU, "zah", {"adit"}),
    ],
)
def test_dhatu_upadesha(upadesha, kind_tags, residue, names):
    _, t, got = _run(upadesha, *kind_tags)
    assert got == residue
    assert it_names(t) == names


@pytest.mark.parametrize(
    "upadesha, tags, residue, names",
    [
        # 1.3.8 लशक्वतद्धिते
        ("ktvA", {"krt"}, "tvA", {"kit"}),
        ("Sap", {"vikarana"}, "a", {"Sit", "pit"}),
        ("lyuw", {"krt"}, "yu", {"lit", "wit"}),
        ("NIz", {"stri_pratyaya"}, "I", {"Nit", "zit"}),
        ("GaY", {"krt"}, "a", {"Git", "Yit"}),
        # 1.3.7 चुटू
        ("Ric", {"nic"}, "i", {"Rit", "cit"}),
        ("Rvul", {"krt"}, "vu", {"Rit", "lit"}),
        ("ciR", {"vikarana"}, "i", {"cit", "Rit"}),
        # 1.3.6 षः प्रत्ययस्य
        ("zvun", {"krt"}, "vu", {"zit", "nit"}),
        # 1.3.3 alone
        ("tip", {"tin"}, "ti", {"pit"}),
        # 1.3.2 anunāsika u of सुँ is it; 1.3.9 elides the vowel (सुँ → स्)
        ("s~", {"sup"}, "s", {"udit"}),
    ],
)
def test_pratyaya_upadesha(upadesha, tags, residue, names):
    _, t, got = _run(upadesha, "pratyaya", _PRATYAYA | tags)
    assert got == residue
    assert it_names(t) == names


@pytest.mark.parametrize(
    "upadesha, tags, residue, names",
    [
        # 1.3.4 न विभक्तौ तुस्माः — tu-varga / s / m ending a vibhakti survive
        ("jas", {"sup"}, "as", {"jit"}),
        ("am", {"sup"}, "am", set()),
        ("tas", {"tin", "tin_adesha_3_4_78"}, "tas", set()),
        # … but not outside a vibhakti: तुमुँन्'s न्, श्नम्'s म् are halantyam
        ("tumu~n", {"krt"}, "tum", {"udit", "nit"}),
        ("Snam", {"vikarana"}, "na", {"Sit", "mit"}),
    ],
)
def test_vibhakti_tusma(upadesha, tags, residue, names):
    _, t, got = _run(upadesha, "pratyaya", _PRATYAYA | tags)
    assert got == residue
    assert it_names(t) == names


@pytest.mark.parametrize(
    "upadesha, residue, names",
    [
        # 1.3.8 is *a*taddhite: कन् keeps क्
        ("kan", "ka", {"nit"}),
        # 1.3.7 does apply to taddhitas: ञ्य (कौञ्जायन्यः)
        ("Yya", "ya", {"Yit"}),
        # sthānin of 7.1.2 / 7.3.50 stay: छ → ईय, ठक् → इक, ढक् → एय
        ("Ca", "Ca", set()),
        ("Wak", "Wa", {"kit"}),
        ("Qak", "Qa", {"kit"}),
        # 1.3.6 / 1.3.7 read the ādi only: इष्ठन्'s ष् / ठ् stay
        ("izWan", "izWa", {"nit"}),
    ],
)
def test_taddhita_upadesha(upadesha, residue, names):
    _, t, got = _run(upadesha, "pratyaya", _PRATYAYA | {"taddhita"})
    assert got == residue
    assert it_names(t) == names


def test_jhi_keeps_jh_for_7_1_3():
    _, t, got = _run("Ji", "pratyaya", _PRATYAYA | {"tin", "tin_adesha_3_4_78"})
    assert got == "Ji"
    assert it_names(t) == set()


def test_agama_is_not_a_pratyaya_for_1_3_8():
    # कुक् (8.3.28): only the final क् is halantyam; the initial क् is the augment.
    _, t, got = _run("kuk", "agama", {"agama"})
    assert got.startswith("k")


def test_full_sequence_runs_in_ashtadhyayi_order():
    s, _, _ = _run("qupaca~z", *DHATU)
    order = [e["sutra_id"] for e in s.trace if e.get("sutra_id") in IT_PRAKARANA_SEQUENCE]
    assert order == list(IT_PRAKARANA_SEQUENCE)


def test_residue_is_never_reanalysed():
    """गमॢँ → गम्: a second pass must not take म् as halantyam (no *ga*)."""
    s, t, got = _run("gamx~", *DHATU)
    assert got == "gam"
    s = run_it_prakarana(s)
    assert "".join(v.slp1 for v in s.terms[0].varnas) == "gam"
    kvasu = _state("kvasu~", "pratyaya", _PRATYAYA | {"krt"})
    kvasu = run_it_prakarana(run_it_prakarana(kvasu))
    assert "".join(v.slp1 for v in kvasu.terms[0].varnas) == "vas"
    assert it_names(kvasu.terms[0]) == {"kit", "udit"}


def test_records_carry_letter_sutra_position_and_name():
    s, t, _ = _run("qupaca~z", *DHATU)
    recs = {r["name"]: r for r in it_records(t)}
    assert recs["qvit"]["letters"] == "qu" and recs["qvit"]["sutra"] == "1.3.5"
    assert recs["qvit"]["position"] == "adi" and recs["qvit"]["name_dev"] == "ड्वित्"
    assert recs["zit"]["sutra"] == "1.3.3" and recs["zit"]["position"] == "antya"
    assert recs["adit"]["sutra"] == "1.3.2"
    assert {"it:qvit", "it:adit", "it:zit"} <= t.tags
    assert has_it(t, "zit") and not has_it(t, "kit")
    assert [r["name"] for r in s.meta[META_IT_LOPA_LOG]] == ["qvit", "adit", "zit"]
    why = next(e for e in s.trace if e.get("sutra_id") == "1.3.9")["why_now_dev"]
    assert "ड्वित्" in why and "षित्" in why


def test_purva_su_runs_full_it_prakarana_and_lops_anunasika_u():
    """पूर्व + सुँ: 1.3.2 names उँ as it; 1.3.2–1.3.8 then 1.3.9 elides it → पूर्वस् → पूर्वः."""
    from core.trace_view import slp1_str_to_dev
    from pipelines.subanta import derive

    s = derive("pUrva", 1, 1)
    assert s.flat_slp1() == "pUrvaH"
    it_ids = [e["sutra_id"] for e in s.trace if e.get("sutra_id") in IT_PRAKARANA_SEQUENCE]
    assert it_ids[:8] == list(IT_PRAKARANA_SEQUENCE)
    row_132 = next(
        e for e in s.trace
        if e.get("sutra_id") == "1.3.2" and e.get("status") == "APPLIED"
    )
    row_139 = next(
        e for e in s.trace
        if e.get("sutra_id") == "1.3.9" and e.get("status") == "APPLIED"
    )
    assert row_132["form_before"].endswith("su~")
    assert row_132["form_after"].endswith("su~")
    assert slp1_str_to_dev(row_132["form_before"]).endswith("सुँ")
    assert row_139["form_before"].endswith("su~")
    assert row_139["form_after"] == "pUrvas"
    assert slp1_str_to_dev(row_139["form_after"]) == "पूर्वस्"
