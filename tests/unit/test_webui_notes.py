"""webui/notes.py — add, list, edit (with history + restore), status, delete; bad ids and bad status are refused; counts for /sutras."""
import pytest
from webui import notes as N
from webui.app import app


@pytest.fixture
def c(tmp_path, monkeypatch):
    monkeypatch.setattr(N, "DIR", tmp_path)
    app.config["TESTING"] = True
    return app.test_client()


def test_notes_roundtrip(c):
    a = c.post("/api/notes/7.4.61", json={"text": "audit one", "author": "me"}).get_json()
    b = c.post("/api/notes/7.4.61", json={"text": "audit two"}).get_json()
    assert [n["status"] for n in c.get("/api/notes/7.4.61").get_json()["notes"]] == ["open", "open"]
    e = c.put(f"/api/notes/7.4.61/{a['id']}", json={"text": "audit one, edited", "status": "partly", "verdict": "v"}).get_json()
    assert e["status"] == "partly" and e["history"][0]["text"] == "audit one"
    r = c.post(f"/api/notes/7.4.61/{a['id']}/restore", json={"n": 0}).get_json()
    assert r["text"] == "audit one" and r["status"] == "open" and len(r["history"]) == 2
    assert c.get("/api/notes-counts").get_json() == {"7.4.61": {"n": 2, "open": 2}}
    assert c.delete(f"/api/notes/7.4.61/{b['id']}").status_code == 200
    assert len(c.get("/api/notes/7.4.61").get_json()["notes"]) == 1


def test_notes_refuse_bad_input(c):
    assert c.get("/api/notes/abc").status_code == 404
    assert c.post("/api/notes/1.1.1", json={"text": ""}).status_code == 400
    n = c.post("/api/notes/1.1.1", json={"text": "t"}).get_json()
    assert c.put(f"/api/notes/1.1.1/{n['id']}", json={"status": "bogus"}).status_code == 400
    assert c.put("/api/notes/1.1.1/nope", json={"text": "x"}).status_code == 404


def test_sutra_page_has_notes_section(c):
    h = c.get("/sutra/7.4.61").get_data(as_text=True)
    assert 'id="sutra-notes"' in h and "notes.js" in h


def test_note_kind(c):
    n = c.post("/api/notes/4.1.2", json={"text": "why su?", "kind": "question", "derivation": "rAma 1-1 · step 37"}).get_json()
    assert n["kind"] == "question"
    assert c.post("/api/notes/4.1.2", json={"text": "x"}).get_json()["kind"] == "note"
    assert c.put(f"/api/notes/4.1.2/{n['id']}", json={"kind": "solution"}).get_json()["kind"] == "solution"
    assert c.put(f"/api/notes/4.1.2/{n['id']}", json={"kind": "nonsense"}).status_code == 400


def test_note_keeps_the_trace_it_was_seen_in(c):
    tr = "Derivation: rAma\n#1 1.2.45 [APPLIED] rAma → rAma\n#37 4.1.2 [APPLIED] rAma → rAmasup   ◀ NOTE HERE"
    n = c.post("/api/notes/4.1.2", json={"text": "why su?", "kind": "question", "trace": tr}).get_json()
    assert n["trace"] == tr
    assert c.get("/api/notes/4.1.2").get_json()["notes"][0]["trace"] == tr
    assert c.post("/api/notes/4.1.2", json={"text": "x", "trace": "y" * 400_001}).status_code == 400
