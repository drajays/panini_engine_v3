"""Gītā 15.3–4 yantra surfaces: अस्य, पदम्, तत्, अहम्."""
from __future__ import annotations

from pipelines.subanta import derive
from tools.samsaadhanii_tags import align_subanta_linga, parse_subanta_tag


def test_asya_idam_sasthi():
    s = derive("idam", 6, 1, linga="pulliṅga")
    assert s.flat_slp1() == "asya"
    ids = [x["sutra_id"] for x in s.trace if x.get("status") == "APPLIED"]
    assert "7.2.113" in ids and "7.1.12" in ids


def test_padam_napumsaka():
    s = derive("pada", 1, 1, linga="napuṃsaka")
    assert s.flat_slp1() == "padam"


def test_tat_tad_napumsaka():
    s = derive("tad", 1, 1, linga="napuṃsaka")
    assert s.flat_slp1() == "tat"


def test_aham_asmad_prathama():
    s = derive("asmad", 1, 1, linga="pulliṅga")
    assert s.flat_slp1() == "aham"


def test_adhyahrta_asmad_tag_parses():
    c = parse_subanta_tag("(अस्मद्{1;एक})")
    assert c.unresolved is None
    assert c.stem_slp1 == "asmad" and c.vibhakti == 1 and c.vacana == 1


def test_scl_linga_repair_padam_tat():
    p = align_subanta_linga(parse_subanta_tag("पद{पुं}{1;एक}"), "padam")
    assert p.linga == "napuṃsaka"
    t = align_subanta_linga(parse_subanta_tag("तद्{पुं}{1;एक}"), "tat")
    assert t.linga == "napuṃsaka"
