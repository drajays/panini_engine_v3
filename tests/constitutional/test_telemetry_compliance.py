"""
tests/constitutional/test_telemetry_compliance.py
─────────────────────────────────────────────────

CONSTITUTION Article 11: SIG/telemetry and the single `apply_rule` port.

- ``notify_apply_rule_end`` / the ContextVar hook must be reachable from
  ``apply_rule`` (exercised with a test hook).
- Sūtra executors must be invoked only via ``apply_rule``; pipeline/sūtra
  code must not import ``engine.executors`` (static guard; complements the
  architectural rule against ad-hoc *State*/*Term* mutation).
"""
from __future__ import annotations

import pathlib
import re

import pytest
import sutras  # noqa: F401

from engine             import apply_rule
from engine.state       import State, Term
from engine.telemetry   import set_apply_rule_hook, reset_apply_rule_hook
from phonology          import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_14 as s1114

ROOT = pathlib.Path(__file__).resolve().parents[2]

_IMPORT_EXEC_LINE = re.compile(
    r"^\s*from\s+engine\.executors(?:\s+\w+)*\s+import\b",
    re.M,
)
_IMPORT_EXEC_PKG = re.compile(
    r"^\s*import\s+engine\.executors\b",
    re.M,
)


def _iter_guarded_source_files() -> list[pathlib.Path]:
    """
    All ``*.py`` that must not import ``engine.executors`` (except
    allowlisted dispatcher / executor package).
    """
    out: list[pathlib.Path] = []
    for base in (
        ROOT / "pipelines",
        ROOT / "sutras",
        ROOT / "phonology",
        ROOT / "engine",
    ):
        for p in base.rglob("*.py"):
            r = p.relative_to(ROOT)
            if r == pathlib.Path("engine/dispatcher.py"):
                continue
            if len(r.parts) >= 2 and r.parts[0] == "engine" and r.parts[1] == "executors":
                continue
            out.append(p)
    return out


def test_apply_rule_fires_telemetry_notify():
    events: list[tuple[object, str]] = []
    t = set_apply_rule_hook(
        lambda fr, to, st: events.append((fr, to))
    )
    try:
        s0 = State(terms=[Term(kind="prakriti", varnas=[mk("a")])])
        apply_rule("1.1.14", s0)
    finally:
        reset_apply_rule_hook(t)
    assert len(events) == 1
    assert events[0][1] == "1.1.14"


def test_samjna_hook_sees_sutra_ids():
    """``notify_apply_rule_end`` receives *to_sutra_id*; exercise twice (idempotent SAMJÑA)."""
    tids: list[str] = []
    tok = set_apply_rule_hook(lambda _f, to, _s: tids.append(to))
    try:
        s0 = State(terms=[Term(kind="prakriti", varnas=[mk("a")])])
        s1 = apply_rule("1.1.14", s0)
        s2 = apply_rule("1.1.14", s1)
        assert s1114.nipata_ekajang_samjna_is_registered(s2)
    finally:
        reset_apply_rule_hook(tok)
    assert tids == ["1.1.14", "1.1.14"]


@pytest.mark.parametrize("src", _iter_guarded_source_files(), ids=lambda p: p.relative_to(ROOT).as_posix())
def test_no_bypass_of_dispatcher_via_executors(src: pathlib.Path):
    text = src.read_text(encoding="utf-8")
    assert not _IMPORT_EXEC_LINE.search(
        text
    ), f"{src}: 'from engine.executors ...' bypasses apply_rule; CONSTITUTION Art. 11"
    assert not _IMPORT_EXEC_PKG.search(
        text
    ), f"{src}: 'import engine.executors' bypasses apply_rule; CONSTITUTION Art. 11"
