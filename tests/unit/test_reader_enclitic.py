import pytest

from tools import samsaadhanii_reader as rd
from tools import reader_enclitic as enc

pytestmark = pytest.mark.skipif(not rd.available(), reason="Saṃsādhanī snapshot absent")


def _gita(ch, sloka):
    u = next(x for x in rd.catalogue() if x["book"] == "श्रीमद्भगवद्गीता")
    return rd.verse(u["id"], ch, sloka)


def _word(v, dev):
    return [w for s in v["sentences"] for w in s["words"] if w["word_dev"] == dev]


def test_gita_2_7_me_and_te_are_derived_by_8_1_22_with_context():
    v = _gita("02", "007")
    for dev in ("मे", "ते"):
        (w,) = _word(v, dev)
        assert w["engine"]["status"] == "derived" and w["engine"]["produced_dev"] == dev
        assert w["engine"]["request"]["context"]["before"], "the pāda context travels with the request"


def test_full_form_where_adesha_expected_is_derived_with_a_note():
    v = _gita("02", "007")
    ws = _word(v, "त्वाम्")
    assert ws and all(w["engine"]["status"] == "derived" and w["engine"]["enclitic_note"] for w in ws)


def test_trace_request_replays_the_real_8_1_steps():
    (w,) = _word(_gita("02", "007"), "मे")
    s = rd.derive_request(w["engine"]["request"])
    fired = [r["sutra_id"] for r in s.trace if r.get("status") == "APPLIED"]
    assert s.flat_dev() == "मे" and "8.1.22" in fired


def test_unalignable_verse_gets_no_guess():
    assert enc.padas(["अ ब"], [{"anvaya_no": "1.1", "word_dev": "क", "sandhied_word": "क", "kind": "subanta"}]) is None
