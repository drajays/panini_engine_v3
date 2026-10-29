"""POST /v1/reviews with dry_run validates and echoes the record but writes nothing (so API tests leave no review file)."""
import pytest
from fastapi import HTTPException

from api import main as api


def test_dry_run_writes_nothing(tmp_path, monkeypatch):
    monkeypatch.setattr(api, "REVIEW_FILE", tmp_path / "corrections.jsonl")
    r = api.add_review(api.ReviewIn(target="t", note="n", dry_run=True))
    assert r["dry_run"] and r["target"] == "t" and not (tmp_path / "corrections.jsonl").exists()
    api.add_review(api.ReviewIn(target="t", note="n"))
    assert (tmp_path / "corrections.jsonl").exists()


def test_dry_run_still_validates(tmp_path, monkeypatch):
    monkeypatch.setattr(api, "REVIEW_FILE", tmp_path / "corrections.jsonl")
    with pytest.raises(HTTPException):
        api.add_review(api.ReviewIn(target="t", dry_run=True))
