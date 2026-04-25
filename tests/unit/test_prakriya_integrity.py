"""
tests/unit/test_prakriya_integrity.py — *prakriyā* / engine integrity guardrails.

Complements ``test_prakriya_audit.py`` with framework-style checks: registry
uniqueness, structural gates vs recipe order, stable pipeline prefix, and
tight *sūtra* id usage under ``engine/`` (logic belongs in ``sutras/``).
"""
from __future__ import annotations

import ast
import re
from pathlib import Path

import pytest

import sutras  # noqa: F401
from engine.gates         import asiddha_violates, is_blocked, is_tripadi
from engine.registry      import SUTRA_REGISTRY, get_sutra
from engine.resolver      import CONFLICT_OVERRIDES, resolve
from engine.state         import State, Term
from engine.sutra_type    import SutraRecord, SutraType
from engine.trace         import extract_chronological_sutra_sequence

_REPO_ROOT = Path(__file__).resolve().parents[2]
_ENGINE_DIR = _REPO_ROOT / "engine"
_SUTRAS_DIR = _REPO_ROOT / "sutras"
_SUTRA_ID_FULLMATCH = re.compile(r"^\d+\.\d+\.\d+$")

# Stable prefix for ``derive(\"rAma\", 1, 1)`` (subanta canonical path).
# If preflight is intentionally reordered, update this tuple and the audit note.
EXPECTED_DERIVE_RAMA_1_1_CHRONO_PREFIX: tuple[str, ...] = (
    "1.4.14",
    "4.1.1",
    "1.1.1",
    "1.1.73",
    "1.1.2",
    "1.1.3",
    "1.1.7",
    "1.1.60",
    "1.1.61",
    "1.1.62",
    "1.1.63",
    "1.1.8",
)

# engine/*.py may contain a bare ``x.x.x`` string only in these allowlisted
# (path_suffix, {ids}) — everything else should live in ``sutras/`` or recipes.
_ENGINE_LITERAL_SUTRA_ID_ALLOW: dict[str, frozenset[str]] = {
    "executors/exec_vidhi.py"   : frozenset({"1.3.9"}),   # vacuous 1.3.9 hook
    "stubs.py"                 : frozenset({"0.0.0"}),   # stub pratiedha target
}


def _str_value(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if type(node).__name__ == "Str" and isinstance(getattr(node, "s", None), str):
        return node.s
    return None


def _sutra_ids_from_sutra_record_call(node: ast.Call) -> list[str]:
    out: list[str] = []
    if not (isinstance(node.func, ast.Name) and node.func.id == "SutraRecord"):
        return out
    for kw in node.keywords:
        if kw.arg == "sutra_id":
            v = _str_value(kw.value)
            if v and _SUTRA_ID_FULLMATCH.match(v):
                out.append(v)
    return out


def _collect_sutra_assignments_from_sutra_files() -> list[tuple[str, str, int]]:
    """(relative_path, sutra_id, lineno) for each SUTRA = SutraRecord(… sutra_id=…)."""
    found: list[tuple[str, str, int]] = []
    for py in sorted(_SUTRAS_DIR.rglob("sutra_*.py")):
        if "__pycache__" in py.parts:
            continue
        rel = str(py.relative_to(_REPO_ROOT))
        try:
            src = py.read_text(encoding="utf-8")
            tree = ast.parse(src, filename=rel)
        except SyntaxError as e:
            pytest.fail(f"SyntaxError in {rel}: {e}")
        for n in ast.walk(tree):
            if not isinstance(n, ast.Call):
                continue
            for sid in _sutra_ids_from_sutra_record_call(n):
                found.append((rel, sid, n.lineno))
    return found


def _iter_engine_exact_sutra_id_literals() -> list[tuple[str, int, str, str]]:
    """
    (relative_path, lineno, value, file_suffix) for exact ``d.d.d`` *str* constants.
    Excludes whole-file skip for ``sutra_type.py`` (class docs mention examples).
    """
    out: list[tuple[str, int, str, str]] = []
    for py in sorted(_ENGINE_DIR.rglob("*.py")):
        if "__pycache__" in py.parts:
            continue
        rel = py.relative_to(_REPO_ROOT)
        try:
            sfx = str(py.relative_to(_ENGINE_DIR))
        except ValueError:
            continue
        if sfx == "sutra_type.py":
            continue
        try:
            src = py.read_text(encoding="utf-8")
            tree = ast.parse(src, str(rel))
        except (OSError, SyntaxError):
            continue
        for n in ast.walk(tree):
            s = _str_value(n)
            if s and _SUTRA_ID_FULLMATCH.match(s):
                out.append((str(rel), n.lineno, s, sfx))
    return out


class TestPrakriyaIntegrity:
    def test_no_duplicate_sutra_definitions(self) -> None:
        """
        Registry keys are unique; ``sutras`` AST scan has no two files with the
        same ``sutra_id`` in ``SutraRecord`` (import would already have failed).
        """
        assert len(SUTRA_REGISTRY) == len(set(SUTRA_REGISTRY))
        from collections import Counter

        by_id: list[str] = [x[1] for x in _collect_sutra_assignments_from_sutra_files()]
        dupes = [k for k, c in Counter(by_id).items() if c > 1]
        assert not dupes, f"AST scan found multiple SutraRecord(s) for: {dupes[:20]}"

    def test_structural_blocking_enforcement(self) -> None:
        """
        Conflicts are not “first/last in list” — *tripāḍī* / *pratiṣedha* are prior
        gates; ``resolve`` uses specificity, then *Aṣṭādhyāyī* order, not ad-hoc
        *RHS wins*.
        """
        s = State(terms=[Term(kind="pada", varnas=[], tags=set(), meta={})])
        s.tripadi_zone = True
        assert asiddha_violates("1.1.1", s) is True
        assert asiddha_violates("8.2.7", s) is False
        assert is_tripadi("8.2.7")
        s2 = State(terms=[Term(kind="pada", varnas=[], tags=set(), meta={})])
        s2.blocked_sutras.add("1.1.1")
        assert is_blocked("1.1.1", s2)

        # resolve(): higher *specificity* wins; no silent “[0] wins”
        out = resolve(
            ["1.1.1", "1.1.2"],
            s,
            specificity={"1.1.1": lambda st: 0, "1.1.2": lambda st: 5},
        )
        assert out == "1.1.2", "expected specificity winner, not sequence order"
        # explicit override layer exists (structural, not string position)
        assert isinstance(CONFLICT_OVERRIDES, dict)

    @pytest.mark.parametrize(
        "label, run",
        [
            (
                "subanta_rAma_1_1",
                lambda: __import__("pipelines.subanta", fromlist=["derive"]).derive("rAma", 1, 1),  # noqa: PLC0415
            ),
        ],
    )
    def test_pipeline_standardization(
        self, label: str, run: "callable[[], object]",
    ) -> None:
        st = run()
        seq = extract_chronological_sutra_sequence(getattr(st, "trace", []))
        pfx = EXPECTED_DERIVE_RAMA_1_1_CHRONO_PREFIX
        for i, eid in enumerate(pfx):
            if i >= len(seq) or seq[i] != eid:
                raise AssertionError(
                    f"pipeline divergence for {label}: expected prefix {pfx!r} "
                    f"but got {seq[: len(pfx)]!r} (change EXPECTED_… in test if intentional)"
                )

    def test_ast_for_hardcoded_sutra_strings_in_engine(self) -> None:
        """
        No new bare *sūtra* id string constants under ``engine/`` (except
        allowlisted) — *vidhi* should come from ``sutras/`` and ``apply_rule``.
        """
        hits: list[str] = []
        for _rel, lineno, val, sfx in _iter_engine_exact_sutra_id_literals():
            allow = _ENGINE_LITERAL_SUTRA_ID_ALLOW.get(sfx)
            if allow and val in allow:
                continue
            hits.append(f"engine/{sfx}:{lineno}: {val!r}")
        assert not hits, f"Disallowed bare sūtra id literals in engine/:\n" + "\n".join(hits)
