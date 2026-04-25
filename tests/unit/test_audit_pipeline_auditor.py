from __future__ import annotations

from pathlib import Path

import sutras  # noqa: F401

from audit.conflict_resolver import is_tripadi, resolve
from audit.pipeline_auditor import PipelineAuditor
from engine.state import State, Term


def test_pipeline_auditor_smoke() -> None:
    root = Path(__file__).resolve().parents[2]
    a = PipelineAuditor(root)
    r = a.run_smoke()
    assert "py_files_scanned_subtrees" in r
    assert r["duplicate_sutra_ids_ast"] == []
    assert a.engine_disallowed_sutra_id_literals() == []


def test_conflict_resolver_delegates_to_structural() -> None:
    s = State(terms=[Term(kind="pada", varnas=[], tags=set(), meta={})])
    s.tripadi_zone = True
    assert is_tripadi("8.2.7")
    w = resolve(
        ["1.1.1", "1.1.2"],
        s,
        specificity={"1.1.1": lambda st: 0, "1.1.2": lambda st: 1},
    )
    assert w == "1.1.2"
