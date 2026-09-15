"""
tests/constitutional/test_form_index_is_a_cache.py
──────────────────────────────────────────────────

Constitution **Article 17** — the form index is a cache, never a grammar.

Three properties, three tests: it is generated (a fresh build re-derives), it
is verifiable (a stored form the engine can no longer derive is a build
failure), and it is never consulted to derive (nothing in the engine's rule
path may import it).
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.form_index import DB_PATH, lookup, sample, stats
from tools.build_form_index import build, derive_cell

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "data" / "index" / "manifest.json"


GENERATION_SPINE = (
    "pipelines/subanta.py",
    "pipelines/tinanta.py",
    "pipelines/krdanta.py",
    "core/canonical_pipelines.py",
)


def _imports_index(path: Path) -> bool:
    import ast

    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(a.name.startswith("engine.form_index") for a in node.names):
                return True
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").startswith("engine.form_index"):
                return True
    return False


def test_no_sutra_and_no_generation_pipeline_imports_the_index():
    """Analysis may read the cache; the derivation path may not.

    ``pipelines/patha_pipeline.py`` is the analyser and is *allowed* to consult
    the index — that is what it is for. What must never happen is a sūtra, or
    the generation spine, deciding a form by lookup.
    """
    offenders = [
        path.relative_to(ROOT).as_posix()
        for path in [*(ROOT / "sutras").rglob("*.py"),
                     *(ROOT / rel for rel in GENERATION_SPINE)]
        if path.exists() and _imports_index(path)
    ]
    assert offenders == [], (
        "Art. 17: an engine that reads its own cache to produce a derivation "
        f"has become a lookup table — {offenders}"
    )


def test_deriving_a_form_never_loads_the_index():
    """The runtime proof: derive रामौ in a clean process and the module is absent."""
    import subprocess
    import sys

    code = (
        "import sutras\n"
        "from pipelines.subanta import derive\n"
        "derive('rAma', 1, 2)\n"
        "import sys; print('engine.form_index' in sys.modules)"
    )
    out = subprocess.run([sys.executable, "-c", code], cwd=ROOT,
                         capture_output=True, text=True, check=True)
    assert out.stdout.strip().endswith("False"), out.stdout


def test_a_fresh_build_derives_every_row_it_stores(tmp_path):
    """Generated, never authored: build a small index and re-derive all of it."""
    db = tmp_path / "forms.db"
    result = build(dhatu_limit=3, stem_limit=3, path=db)
    assert result["written"] > 0
    rows = sample(result["written"], db)
    for row in rows:
        surface = derive_cell({"kind": row["kind"], "lemma": row["lemma"],
                               "features": row["features"]}).flat_slp1()
        assert surface == row["surface_slp1"], row["cell_key"]


def test_manifest_is_committed_and_typed():
    assert MANIFEST.exists(), "run 'make index'"
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["forms"] > 40_000 and data["lemmas"] > 900
    assert len(data["fingerprint"]) == 50


@pytest.mark.skipif(not DB_PATH.exists(), reason="index not built here (make index)")
def test_built_index_matches_its_manifest():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert stats()["forms"] == data["forms"]
    for entry in data["fingerprint"][:10]:
        hits = lookup(entry["surface"])
        assert any(h["lemma"] == entry["lemma"] for h in hits), entry


@pytest.mark.skipif(not DB_PATH.exists(), reason="index not built here (make index)")
def test_lookup_returns_every_reading_not_one():
    """रामौ is prathamā, dvitīyā and sambodhana dual — ambiguity is the product."""
    readings = {h["features"]["vibhakti"] for h in lookup("rAmO") if h["kind"] == "subanta"}
    assert readings == {1, 2, 8}
