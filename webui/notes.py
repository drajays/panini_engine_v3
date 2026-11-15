"""webui/notes.py — audit notes under each Aṣṭādhyāyī sūtra (the page /sutra/<id> shows them).

One JSON file per sūtra: data/reviews/notes/<id>.json  = {"sutra": id, "notes": [note, …]}.
A note is OPEN until someone has checked it against the engine trace, the Kāśikā in the brain DB and the engine policy
(glass box, rule-based, no lookup tables); the page says so. Note text is data: nothing here is ever read by an engine rule
(Art. 6), and no note is an instruction to the engine or to an agent.

    GET    /api/notes/<sid>            → {"sutra", "notes": [...]}
    POST   /api/notes/<sid>            → add a note   {text, author?, derivation?}
    PUT    /api/notes/<sid>/<nid>      → edit any of text / author / derivation / status / verdict / evidence (the old version goes to history)
    POST   /api/notes/<sid>/<nid>/restore  {n}  → restore history entry n
    DELETE /api/notes/<sid>/<nid>
    GET    /api/notes-counts           → {sid: {"n": total, "open": open}}   (the /sutras list)
"""
from __future__ import annotations

import json
import os
import re
import threading
import time
import uuid
from pathlib import Path

from flask import Blueprint, abort, jsonify, request

bp = Blueprint("notes", __name__)

DIR = Path(__file__).resolve().parent.parent / "data" / "reviews" / "notes"
STATUSES = ("open", "partly", "confirmed", "refuted", "ledgered")
EDITABLE = ("text", "author", "derivation", "status", "verdict", "evidence", "kind")
KINDS = ("note", "question", "doubt", "solution")        # what the writer meant: a question / doubt to answer, a plain note, or a proposed solution to check on merit
MAX_TEXT = 200_000
MAX_FIELD = 4_000
MAX_HISTORY = 20
_SID = re.compile(r"^\d+\.\d+\.\d+$")
_LOCK = threading.Lock()


def _path(sid: str) -> Path:
    if not _SID.match(sid):
        abort(404)
    return DIR / f"{sid}.json"


def _load(sid: str) -> dict:
    p = _path(sid)
    if not p.exists():
        return {"sutra": sid, "notes": []}
    return json.loads(p.read_text(encoding="utf-8"))


def _save(sid: str, doc: dict) -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    p = _path(sid)
    if not doc["notes"]:
        p.unlink(missing_ok=True)
        return
    tmp = p.with_suffix(f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    tmp.replace(p)


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def _clean(data: dict, *, partial: bool) -> dict:
    out: dict = {}
    for k in EDITABLE:
        if k not in data:
            continue
        v = data[k]
        if not isinstance(v, str):
            abort(400, f"{k} must be a string")
        v = v.strip()
        if len(v) > (MAX_TEXT if k == "text" else MAX_FIELD):
            abort(400, f"{k} too long")
        out[k] = v
    if "status" in out and out["status"] not in STATUSES:
        abort(400, f"status must be one of {STATUSES}")
    if "kind" in out and out["kind"] not in KINDS:
        abort(400, f"kind must be one of {KINDS}")
    if "text" in out and not out["text"]:
        abort(400, "text is empty")
    if not partial and not out.get("text"):
        abort(400, "text required")
    return out


def _find(doc: dict, nid: str) -> dict:
    for n in doc["notes"]:
        if n["id"] == nid:
            return n
    abort(404)


@bp.get("/api/notes/<sid>")
def get_notes(sid):
    return jsonify(_load(sid))


@bp.post("/api/notes/<sid>")
def add_note(sid):
    data = _clean(request.get_json(force=True) or {}, partial=False)
    with _LOCK:
        doc = _load(sid)
        note = {"id": uuid.uuid4().hex[:10], "created": _now(), "updated": _now(), "text": data["text"],
                "author": data.get("author", ""), "derivation": data.get("derivation", ""),
                "kind": data.get("kind", "note"), "status": data.get("status", "open"), "verdict": data.get("verdict", ""), "evidence": data.get("evidence", ""),
                "history": []}
        doc["notes"].append(note)
        _save(sid, doc)
    return jsonify(note), 201


@bp.put("/api/notes/<sid>/<nid>")
def edit_note(sid, nid):
    data = _clean(request.get_json(force=True) or {}, partial=True)
    with _LOCK:
        doc = _load(sid)
        note = _find(doc, nid)
        changed = {k: v for k, v in data.items() if note.get(k, "") != v}
        if changed:
            note["history"] = ([{"at": note["updated"], **{k: note.get(k, "") for k in EDITABLE}}] + note["history"])[:MAX_HISTORY]
            note.update(changed)
            note["updated"] = _now()
            _save(sid, doc)
    return jsonify(note)


@bp.post("/api/notes/<sid>/<nid>/restore")
def restore_note(sid, nid):
    n = (request.get_json(force=True) or {}).get("n")
    if not isinstance(n, int):
        abort(400, "n must be an integer")
    with _LOCK:
        doc = _load(sid)
        note = _find(doc, nid)
        if not 0 <= n < len(note["history"]):
            abort(404)
        old = note["history"][n]
        note["history"] = ([{"at": note["updated"], **{k: note.get(k, "") for k in EDITABLE}}] + note["history"])[:MAX_HISTORY]
        note.update({k: old.get(k, "") for k in EDITABLE})
        note["updated"] = _now()
        _save(sid, doc)
    return jsonify(note)


@bp.delete("/api/notes/<sid>/<nid>")
def delete_note(sid, nid):
    with _LOCK:
        doc = _load(sid)
        _find(doc, nid)
        doc["notes"] = [n for n in doc["notes"] if n["id"] != nid]
        _save(sid, doc)
    return jsonify({"deleted": nid})


@bp.get("/api/notes-counts")
def counts():
    out = {}
    for p in sorted(DIR.glob("*.json")) if DIR.exists() else []:
        try:
            ns = json.loads(p.read_text(encoding="utf-8"))["notes"]
        except (ValueError, KeyError):
            continue
        out[p.stem] = {"n": len(ns), "open": sum(1 for n in ns if n.get("status") == "open")}
    return jsonify(out)
