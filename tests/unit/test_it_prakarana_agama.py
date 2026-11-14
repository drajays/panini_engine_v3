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
