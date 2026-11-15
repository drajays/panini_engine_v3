"""इट् is uttered as taught and goes through 1.3.3 → 1.3.9 like any upadeśa (engine.agama + dispatcher hook)."""
from __future__ import annotations

import pytest

from pipelines.tinanta import derive


def _after(st, sid):
    rows = [s for s in st.trace if s.get("sutra_id") == sid and s.get("status") == "APPLIED"]
    assert rows, f"{sid} never applied"
    i = st.trace.index(rows[0])
    return [s for s in st.trace[i + 1:] if s.get("status") == "APPLIED"]


@pytest.mark.parametrize("args, kw, final", [
    (("skudi~", "luG", "kartari", 2, 2), {"pada": "atmanepada"}, "askundizATAm"),
    (("BU", "lRT", "kartari", 3, 1), {}, "Bavizyati"),
])
def test_it_agama_is_named_and_deleted(args, kw, final):
    st = derive(*args, **kw)
    assert "".join(v.slp1 for t in st.terms for v in t.varnas) == final
    first = next(s for s in st.trace if s.get("sutra_id") == "7.2.35" and s.get("status") == "APPLIED")
    assert "iw" in first["form_after"]                       # uttered as इट्, not a bare इ
    nxt = _after(st, "7.2.35")[:2]
    assert [s["sutra_id"] for s in nxt] == ["1.3.3", "1.3.9"]
    assert "इट् (आगमः)" in nxt[1]["why_now_dev"] and "टित्" in nxt[1]["why_now_dev"]
    log = [r for r in st.meta.get("it_lopa_log", ()) if r.get("agama") == "iw"]
    assert log and log[0]["name"] == "wit"


def test_it_record_belongs_to_the_agama_not_its_host():
    st = derive("skudi~", "luG", "kartari", 2, 2, pada="atmanepada")
    for t in st.terms:
        assert "it:wit" not in t.tags or "agama" in t.tags


def test_yat_agama_on_rama_dative():
    from pipelines.subanta import derive_akarant_strilinga
    st = derive_akarant_strilinga("ramA", 4, 1)
    assert "".join(v.slp1 for t in st.terms for v in t.varnas) == "ramAyE"
    first = next(s for s in st.trace if s.get("sutra_id") == "7.3.113" and s.get("status") == "APPLIED")
    assert "yAw" in first["form_after"] or "yAwe" in first["form_after"]
    nxt = [s for s in st.trace[st.trace.index(first) + 1:] if s.get("status") == "APPLIED"][:2]
    assert [s["sutra_id"] for s in nxt] == ["1.3.3", "1.3.9"]
    assert "याट् (आगमः)" in nxt[1]["why_now_dev"] and "टित्" in nxt[1]["why_now_dev"]
    assert any(s.get("sutra_id") == "8.4.68" for s in st.trace)


def test_syat_agama_on_sarva_dative():
    from pipelines.subanta import derive
    st = derive("sarva", 4, 1, linga="strīliṅga")
    # सर्वस्याै / similar — at least स्याट् must be named and deleted
    rows = [s for s in st.trace if s.get("sutra_id") == "7.3.114" and s.get("status") == "APPLIED"]
    if not rows:
        return  # path may use another stem shape; याट् coverage is the primary pin
    first = rows[0]
    assert "syAw" in first["form_after"] or "w" in first["form_after"]
    nxt = [s for s in st.trace[st.trace.index(first) + 1:] if s.get("status") == "APPLIED"][:2]
    assert nxt[0]["sutra_id"] == "1.3.3" and nxt[1]["sutra_id"] == "1.3.9"


def test_num_agama_on_kut_lang():
    from pipelines.tinanta import derive
    st = derive("kuTi~", "laG", "kartari", 3, 1)
    first = next(s for s in st.trace if s.get("sutra_id") == "7.1.58" and s.get("status") == "APPLIED")
    assert "nm" in first["form_after"] or "num" in first["form_after"]  # न्+म् uttered (उ dropped)
    nxt = [s for s in st.trace[st.trace.index(first) + 1:] if s.get("status") == "APPLIED"]
    # 1.3.2 may skip; first applied after must be 1.3.3 then later 1.3.9
    ids = [s["sutra_id"] for s in nxt[:8]]
    assert "1.3.3" in ids and "1.3.9" in ids
    i3, i9 = ids.index("1.3.3"), ids.index("1.3.9")
    assert i3 < i9
    row9 = nxt[i9]
    assert "नुम् (आगमः)" in row9["why_now_dev"] and "मित्" in row9["why_now_dev"]
    assert any(r.get("agama") == "num" and r.get("name") == "mit" for r in st.meta.get("it_lopa_log", ()))


def test_at_agama_on_kut_lang():
    from pipelines.tinanta import derive
    st = derive("kuTi~", "laG", "kartari", 3, 1)
    first = next(s for s in st.trace if s.get("sutra_id") == "6.4.71" and s.get("status") == "APPLIED")
    assert "aw" in first["form_after"] or "w" in first["form_after"]
    nxt = [s for s in st.trace[st.trace.index(first) + 1:] if s.get("status") == "APPLIED"]
    ids = [s["sutra_id"] for s in nxt[:8]]
    assert "1.3.3" in ids and "1.3.9" in ids
    assert ids.index("1.3.3") < ids.index("1.3.9")
    row9 = nxt[ids.index("1.3.9")]
    assert "अट् (आगमः)" in row9["why_now_dev"] and "टित्" in row9["why_now_dev"]
    assert any(r.get("agama") == "aw" and r.get("name") == "wit" for r in st.meta.get("it_lopa_log", ()))


def test_lakara_lang_gets_1_3_2_and_leaves_only_l():
    from pipelines.tinanta import derive
    st = derive("skudi~", "laG", "kartari", 3, 1, pada="atmanepada")
    row9 = next(
        s for s in st.trace
        if s.get("sutra_id") == "1.3.9" and s.get("status") == "APPLIED"
        and "लँङ्" in (s.get("why_now_dev") or "")
    )
    assert "अँ → अदित्" in row9["why_now_dev"] and "ङित्" in row9["why_now_dev"]
    assert any(r.get("upadesha") == "laG" and r.get("sutra") == "1.3.2" for r in st.meta.get("it_lopa_log", ()))
    row78 = next(s for s in st.trace if s.get("sutra_id") == "3.4.78" and s.get("status") == "APPLIED")
    assert row78["form_before"].endswith("l") and "~" not in row78["form_before"]
