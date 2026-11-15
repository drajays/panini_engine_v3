"""tools/impl_score.py — the per-sūtra implementation mark: every point comes from recorded evidence; the page shows it."""
from tools.impl_score import open_ledger_rows, score_all
from webui.app import app


def test_marks_follow_the_rubric():
    s = score_all()
    assert all(0 <= v["score"] <= 10 for v in s.values())
    assert all(v["score"] == 0 for v in s.values() if v["status"] == "placeholder")
    assert all(v["score"] <= 3 for v in s.values() if v["status"] == "gate_only")
    ten = [k for k, v in s.items() if v["score"] >= 10]
    assert all(s[k]["parts"] == {"A": 2.0, "B": 1.5 if s[k]["parts"]["B"] == 1.5 else 1.5, "C": 3.0, "D": 2.5, "E": 1.0} for k in ten)


def test_open_ledger_rows_cost_points():
    led = open_ledger_rows()
    s = score_all()
    assert "S174" in led["7.1.58"] and s["7.1.58"]["parts"]["D"] <= 1.5


def test_pages_show_the_mark():
    c = app.test_client()
    assert "implementation mark" in c.get("/sutra/6.1.77").get_data(as_text=True)
    assert c.get("/api/impl-score").get_json()["6.1.77"]["s"] >= 1
    assert 's-mark' in c.get("/sutras").get_data(as_text=True)
