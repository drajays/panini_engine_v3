"""*śālā* + *tatra bhava* → *śālīya* (``pipelines/taddhita_salIya``)."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.taddhita_salIya import build_salIya_initial_state, derive_salIya


def test_build_initial_stem_only_vv_for_su():
    s = build_salIya_initial_state()
    assert len(s.terms) == 1
    assert s.meta.get("prakriya_sAlIya") is True
    assert s.meta.get("vibhakti_vacana") == "1-1"
    assert s.terms[0].meta.get("upadesha_slp1") == "SAlA"
    assert "prātipadika" not in s.terms[0].tags


def test_derive_salIya_surface_and_core_rules():
    s = derive_salIya()
    assert s.flat_slp1() == "SAlIya"
    steps = {step["sutra_id"]: step.get("status") for step in s.trace}
    # 4.1.3/4.1.4 are not scheduled: *śālā* is already ṭāp-anta in this recipe.
    # चरण २: **4.1.82** right after *sup* (**4.1.2**), then **4.1.83** + **4.3.53**
    tids = [x["sutra_id"] for x in s.trace]
    i2 = tids.index("4.1.2")
    i82, i83, i453 = tids.index("4.1.82"), tids.index("4.1.83"), tids.index("4.3.53")
    assert i2 < i82 < i83 < i453
    i423 = tids.index("1.4.23")
    i145 = tids.index("1.4.45")
    i236 = tids.index("2.3.36")
    i11 = tids.index("1.1.1")
    i173 = tids.index("1.1.73")
    i162 = tids.index("1.1.62")
    assert i453 < i423 < i145 < i236 < i11 < i173 < i162
    t311, t312, t313 = tids.index("3.1.1"), tids.index("3.1.2"), tids.index("3.1.3")
    t476, t292, t4114 = (
        tids.index("4.1.76"),
        tids.index("4.2.92"),
        tids.index("4.2.114"),
    )
    t1246 = tids.index("1.2.46")
    assert i162 < t311 < t312 < t313 < t476 < t292 < t4114 < t1246
    from engine.trace import TRACE_STATUSES_FIRED

    ids = [
        step["sutra_id"] for step in s.trace
        if step.get("status") in TRACE_STATUSES_FIRED
    ]
    for required in (
        "4.1.1",
        "1.2.45",
        "4.1.2",
        "4.1.82",
        "4.1.83",
        "4.3.53",
        "1.4.23",
        "1.4.45",
        "2.3.36",
        "1.1.1",
        "1.1.73",
        "1.1.62",
        "3.1.1",
        "3.1.2",
        "3.1.3",
        "4.1.76",
        "4.2.92",
        "4.2.114",
        "1.2.46",
        "2.4.71",
        "1.1.60",
        "1.1.61",
        "1.4.13",
        "6.4.1",
        "1.1.54",
        "7.1.2",
        "1.3.10",
        "1.4.18",
        "6.4.129",
        "1.1.52",
        "6.4.148",
    ):
        assert required in ids

    t71 = next(x for x in s.trace if x.get("sutra_id") == "4.2.71")
    t113 = next(x for x in s.trace if x.get("sutra_id") == "4.2.113")
    assert t71.get("status") == "SKIPPED"
    assert t113.get("status") == "SKIPPED"
    assert tids.index("4.2.114") < tids.index("4.2.71") < tids.index("4.2.113")
    assert tids.index("4.2.113") < tids.index("1.2.46")
    assert tids.index("2.4.71") < tids.index("1.1.60") < tids.index("1.1.61")


def test_derive_salIya_merge_optional():
    s = derive_salIya(pada_merge=True)
    assert len(s.terms) == 1
    assert "pada" in s.terms[0].tags
    assert s.flat_slp1() == "SAlIya"


def test_carana3_adhikaraNa_and_locative_note():
    from sutras.adhyaya_2.pada_3.sutra_2_3_36 import REGISTRY_KEY

    s = derive_salIya()
    assert "adhikaraṇa" in s.terms[0].tags
    assert s.samjna_registry.get(REGISTRY_KEY) == "SAlAyAm"


def test_carana4_vrddha_pada_and_TAp_anta():
    s = derive_salIya()
    st = s.terms[0]
    assert "TAp_anta" in st.tags
    assert "vṛddha" in st.tags
    assert s.samjna_registry.get("1.1.73_vrddham_term_indices") == frozenset({0})


def test_carana5_vrddhAc_cha_4_2_114():
    from sutras.adhyaya_4.pada_2.sutra_4_2_114 import SAMJNA_KEY

    s = derive_salIya()
    assert s.samjna_registry.get(SAMJNA_KEY) == frozenset({0})


def test_carana6_taddhite_pratyaya_4_1_76_cha():
    """
    4.1.76 (trace) + *taddhita* on *Cha* Term; *Cha* *vidhi* = **4.2.114**, not 4.2.71.
    """
    s = derive_salIya()
    tids = [x["sutra_id"] for x in s.trace]
    assert tids.index("4.1.76") < tids.index("4.2.114")
    prs = [t for t in s.terms if t.kind == "pratyaya" and "taddhita" in t.tags]
    assert len(prs) == 1
    assert prs[0].meta.get("upadesha_slp1_original") == "CaH"  # **7.1.2** *phadi* → *īya*


def test_carana7_1_2_46_kfttaddhita_samAsA_pratipadika_on_cha():
    """
    **1.2.46** *Case D* — *taddhite* *Cha* gets ``prātipadika`` before **2.4.71** *luk* and
    before **7.1.2** *phadi* (``C`` *it* lopa is in that chain *after* *prātipadika*).
    """
    s = derive_salIya()
    tids = [x["sutra_id"] for x in s.trace]
    assert tids.index("1.2.46") < tids.index("2.4.71") < tids.index("7.1.2")
    assert s.samjna_registry.get("1.2.46_sAlIya_avayava") is True
    pr = next(t for t in s.terms if t.kind == "pratyaya" and "taddhita" in t.tags)
    assert "prātipadika" in pr.tags


def test_carana8_2_4_71_supo_luk_internal_su_taddhita_stays():
    """
    **2.4.71** — *sup* ``Term`` (internal *sū* from **4.1.2** / *samarthā* **4.1.82**)
    elided; *aṅga* + *taddhite* *Cha* *īya* remain; ``meta['2_4_71_luk']`` set.
    """
    s = derive_salIya()
    assert s.meta.get("2_4_71_luk") is True
    from engine.lopa_ghost import term_is_sup_luk_ghost, term_sup_phonetically_live

    assert not any(term_sup_phonetically_live(t) for t in s.terms)
    assert any(term_is_sup_luk_ghost(t) for t in s.terms)
    tids = [x["sutra_id"] for x in s.trace]
    assert tids.index("1.2.46") < tids.index("2.4.71")
    assert "2.4.71" in {x["sutra_id"] for x in s.trace if x.get("status") in ("APPLIED", "AUDIT")}
    aMga = s.terms[0]
    tdd = next(t for t in s.terms if t.kind == "pratyaya" and "taddhita" in t.tags)
    assert "sup" not in tdd.tags
    assert aMga.meta.get("upadesha_slp1") == "SAlA"  # stem *śālā*; *sū* not a separate *rūpa* here


def test_carana9_ita_sikSA_engine_is_7_1_2_phadi_plus_1_3_10():
    """
    *Śikṣa* *it* 1.3.2…1.3.9: **7.1.2** *phadi* in v3 *pre-empts* a separate 1.3.7+1.3.9
    *lopa* on the same *C*; *trace* has 7.1.2 and 1.3.10, not 1.3.2–1.3.9.
    """
    s = derive_salIya()
    tids = [x["sutra_id"] for x in s.trace]
    assert tids.index("2.4.71") < tids.index("7.1.2")
    s71 = next(x for x in s.trace if x["sutra_id"] == "7.1.2")
    assert s71.get("status") == "APPLIED"
    assert s71.get("form_before", "").endswith("CaH")  # SAlA+CaH before *phadi* replacement
    assert s71.get("form_after", "").endswith("Iya")
    pr = next(t for t in s.terms if t.kind == "pratyaya" and "taddhita" in t.tags)
    assert pr.meta.get("7_1_2_phadi_done") is True
    for sid in (
        "1.3.2",
        "1.3.3",
        "1.3.4",
        "1.3.5",
        "1.3.6",
        "1.3.7",
        "1.3.8",
        "1.3.9",
    ):
        assert sid not in tids, f"expected no separate {sid} in śālīya *trace*"
    assert tids.index("1.3.10") == tids.index("7.1.2") + 1


def test_carana10_1_4_13_6_4_1_phadi_7_1_2_and_1_3_10():
    """
    *Aṅga* **1.4.13** (cf. *nimitta* *śālā* and *taddhite* *Cha*); **6.4.1**; **7.1.2** *C* → *Iya*;
    **1.3.10** *yathāsaṅkhyam* (4th to 4th).
    """
    s = derive_salIya()
    tids = [x["sutra_id"] for x in s.trace]
    st = s.trace[tids.index("1.4.13")]
    assert st.get("status") == "APPLIED"
    assert s.samjna_registry.get(("1.4.13_anga", 0)) == frozenset({"active"})
    aMga = s.terms[0]
    assert "anga" in aMga.tags
    assert tids.index("1.4.13") < tids.index("6.4.1") < tids.index("7.1.2") < tids.index("1.3.10")
    st71 = s.trace[tids.index("7.1.2")]
    assert st71.get("form_after", "").endswith("Iya")
    pr = next(t for t in s.terms if t.kind == "pratyaya" and "taddhita" in t.tags)
    assert pr.meta.get("upadesha_slp1") == "Iya"  # *C* (4th) *ādeśa* family


def test_carana11_bha_1_4_18_bhasya_6_4_129_6_4_148_anta_lopa():
    """
    **1.4.18** *bha* (after **7.1.2** *Iya*); *bhādhikāra* **6.4.129**; **6.4.148** *ā* *lopa*.
    """
    s = derive_salIya()
    tids = [x["sutra_id"] for x in s.trace]
    t18 = s.trace[tids.index("1.4.18")]
    assert t18.get("status") == "APPLIED"
    aMga = s.terms[0]
    assert "bha" in aMga.tags
    assert s.samjna_registry.get("1.4.18_bha_anga_indices") == frozenset({0})
    t129 = s.trace[tids.index("6.4.129")]
    assert t129.get("status") == "AUDIT"
    assert tids.index("1.4.18") < tids.index("6.4.129") < tids.index("6.4.148")
    st148 = s.trace[tids.index("6.4.148")]
    assert st148.get("status") == "APPLIED"
    assert s.flat_slp1() == "SAlIya"
    assert aMga.varnas[-1].slp1 == "l"  # *SAl*; final *A* loped


def test_carana12_flat_slp1_taddhitānta_and_pratipadika_parts():
    """
    चरण १२: *saṃhitā* ``SAlIya``; *dvy*-*avayava* still *taddhite*-*anta*; no second 1.2.46 in *trace*.
    """
    from engine.lopa_ghost import term_is_sup_luk_ghost

    s = derive_salIya()
    assert s.flat_slp1() == "SAlIya"
    tids = [x["sutra_id"] for x in s.trace]
    assert tids.index("1.2.46") < tids.index("6.4.148")
    assert tids.count("1.2.46") == 1
    a0 = s.terms[0]
    p1 = next(
        t
        for t in s.terms[1:]
        if "taddhita" in t.tags and not term_is_sup_luk_ghost(t)
    )
    assert "taddhitānta" in a0.tags and "taddhitānta" in p1.tags
    assert s.meta.get("taddhitānta_pada_slp1") == "SAlIya"
    assert "prātipadika" in a0.tags and "prātipadika" in p1.tags
