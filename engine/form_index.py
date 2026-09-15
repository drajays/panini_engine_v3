"""
engine/form_index.py — the generated-forms index (CONSTITUTION Art. 17).

Every form this engine can derive, stored once so that analysis can ask
*"what could this surface be?"* without a second grammar existing anywhere.

Three properties make it a cache rather than a rule base, and Art. 17 requires
all three:

1. **Generated, never authored.** Every row is written by
   ``tools/build_form_index.py`` from a derivation. No row is typed by hand.
   The table is the graph of the generation function restricted to the lexicon.
2. **Regenerated, and drift is a build failure.** ``--verify`` re-derives a
   sample and fails if any stored surface no longer matches.
3. **Never consulted to derive.** No sūtra and no generation pipeline may
   import this module, and deriving a form in a clean process must not load it
   — a constitutional test enforces both. The analyser *may* read it; that is
   what it is for. Lookup answers *what could this be*; only the engine
   answers *why is it this*.

A row stores the **cell key**, not the trace: the forward journey is
reproduced on demand by re-deriving, never cached as text.
"""
from __future__ import annotations

import json
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any, Iterable

_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = _ROOT / "data" / "index" / "forms.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS forms (
    surface_slp1 TEXT NOT NULL,
    surface_dev  TEXT NOT NULL,
    kind         TEXT NOT NULL,          -- subanta | tinanta
    lemma        TEXT NOT NULL,          -- prātipadika or dhātu upadeśa
    features     TEXT NOT NULL,          -- JSON: the paradigm coordinates
    cell_key     TEXT NOT NULL,          -- re-derives the forward journey
    branch       INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (cell_key, branch)
);
CREATE INDEX IF NOT EXISTS forms_by_surface ON forms (surface_slp1);
CREATE INDEX IF NOT EXISTS forms_by_lemma   ON forms (lemma);

CREATE TABLE IF NOT EXISTS gaps (
    cell_key TEXT PRIMARY KEY,
    kind     TEXT NOT NULL,
    lemma    TEXT NOT NULL,
    reason   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def connect(path: Path | None = None, *, write: bool = False) -> sqlite3.Connection:
    """Open the index. Callers must close: ``sqlite3``'s context manager ends
    the *transaction*, not the connection, and a leaked handle surfaces as a
    ResourceWarning against an unrelated test."""
    target = path or DB_PATH
    if write:
        target.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(target)
        conn.executescript(SCHEMA)
        return conn
    if not target.exists():
        raise FileNotFoundError(
            f"{target} not built — run 'python3 -m tools.build_form_index'"
        )
    conn = sqlite3.connect(f"file:{target}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def lookup(surface_slp1: str, path: Path | None = None) -> list[dict[str, Any]]:
    """Every lemma + feature set this engine derives to that surface.

    Many rows are the expected answer, not a defect: homonymy is real, and
    optional rules make generation one-to-many. Ranking them is the analyser's
    job (kāraka and agreement), not the index's.
    """
    with closing(connect(path)) as conn:
        rows = conn.execute(
            "SELECT surface_slp1, surface_dev, kind, lemma, features, cell_key, branch "
            "FROM forms WHERE surface_slp1 = ?",
            (surface_slp1,),
        ).fetchall()
    return [{**dict(row), "features": json.loads(row["features"])} for row in rows]


def stats(path: Path | None = None) -> dict[str, Any]:
    with closing(connect(path)) as conn:
        forms = conn.execute("SELECT COUNT(*) FROM forms").fetchone()[0]
        surfaces = conn.execute("SELECT COUNT(DISTINCT surface_slp1) FROM forms").fetchone()[0]
        lemmas = conn.execute("SELECT COUNT(DISTINCT lemma) FROM forms").fetchone()[0]
        gaps = conn.execute("SELECT COUNT(*) FROM gaps").fetchone()[0]
        meta = dict(conn.execute("SELECT key, value FROM meta").fetchall())
    return {
        "forms": forms,
        "distinct_surfaces": surfaces,
        "lemmas": lemmas,
        "gaps": gaps,
        "meta": meta,
    }


def sample(n: int, path: Path | None = None, *, seed: int = 0) -> list[dict[str, Any]]:
    """A deterministic sample of rows, for verification."""
    with closing(connect(path)) as conn:
        rows = conn.execute(
            "SELECT surface_slp1, kind, lemma, features, cell_key FROM forms "
            "ORDER BY substr(cell_key, ?) LIMIT ?",
            (1 + (seed % 3), n),
        ).fetchall()
    return [{**dict(row), "features": json.loads(row["features"])} for row in rows]


def iter_rows(path: Path | None = None) -> Iterable[dict[str, Any]]:
    with closing(connect(path)) as conn:
        for row in conn.execute(
            "SELECT surface_slp1, kind, lemma, features, cell_key FROM forms"
        ):
            yield {**dict(row), "features": json.loads(row["features"])}
