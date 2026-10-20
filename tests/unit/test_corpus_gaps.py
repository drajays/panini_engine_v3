"""tools/corpus_gaps — token-weighted statuses and gap clusters over a library (analysis stubbed)."""
from __future__ import annotations

import json

from tools import corpus_gaps as cg


def _lib(tmp_path):
    rows = [{"sanskrit_text": "रामः वनं गच्छति ।"}, {"sanskrit_text": "रामः भूत्वा ॥ १ ॥"}]
    (tmp_path / "w.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows), encoding="utf-8")
    return tmp_path


def _fake(words):
    table = {
        "रामः": {"status": "verified", "readings": []},
        "गच्छति": {"status": "verified", "readings": []},
        "वनं": {"status": "oracle_only", "readings": [{"status": "differs", "label_dev": "वन", "produced_dev": "वनम्",
                                                      "request": {"kind": "subanta", "vibhakti": 1}}]},
        "भूत्वा": {"status": "oracle_only", "readings": [{"status": "not_attempted", "label_dev": "कृदन्त", "request": None,
                                                         "note": "kṛdanta stem (BU + ktvA) — the kṛt spine is not yet an analysis target"}]},
    }
    return {"words": [{"word_dev": w, **table[w]} for w in words]}


def test_counts_skip_dandas_and_digits(tmp_path):
    freq, where = cg.counts(("w", "missing"), _lib(tmp_path))
    assert freq == {"रामः": 2, "वनं": 1, "गच्छति": 1, "भूत्वा": 1}
    assert where["रामः"] == {"w"}


def test_run_weights_by_tokens_and_clusters_gaps(tmp_path, monkeypatch):
    monkeypatch.setattr(cg, "analyze", _fake)
    rep = cg.run(("w",), None, _lib(tmp_path))
    assert rep["tokens_by_status"] == {"verified": 3, "oracle_only": 2}
    names = {c["cluster"] for c in rep["clusters"]}
    assert "subanta vibhakti 1: engine derives another form" in names
    assert "not attempted: the kṛt spine is not yet an analysis target" in names
    assert rep["oracle_only"][0]["engine"] == "वनम्"
