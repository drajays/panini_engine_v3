"""
Constitutional test: no direct '.varnas =' assignments in pipeline files
outside of a function named 'act'.

Scans the main pipeline files (tinanta.py, subanta.py, asmad_subanta.py)
for '.varnas =' outside an 'act' function. This catches Article 11 violations
(direct varnas mutation bypassing apply_rule).

Additional pipeline files will be added as they are refactored.
"""
from __future__ import annotations

import re
import pathlib
import ast
import pytest

_VARNAS_ASSIGN = re.compile(r'\.varnas\s*=')

_PIPELINES_ROOT = pathlib.Path(__file__).parent.parent.parent / "pipelines"

# Pipeline files that must be Article-11 clean (no .varnas = outside act).
_CLEAN_PIPELINE_FILES: list[str] = [
    "tinanta.py",
    "asmad_subanta.py",
]


def _collect_files():
    return [_PIPELINES_ROOT / f for f in _CLEAN_PIPELINE_FILES]


def _line_is_inside_act_function(source: str, lineno: int) -> bool:
    """Return True if the 1-based lineno is inside a function def named 'act'."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name != "act":
            continue
        start = node.lineno
        end = getattr(node, "end_lineno", None)
        if end is None:
            continue
        if start <= lineno <= end:
            return True
    return False


@pytest.mark.parametrize(
    "pipeline_file",
    _collect_files(),
    ids=lambda p: p.name,
)
def test_no_varnas_direct_write_outside_act(pipeline_file: pathlib.Path) -> None:
    """Main pipeline files must not assign .varnas directly outside an 'act' function."""
    source = pipeline_file.read_text(encoding="utf-8")
    lines = source.splitlines()
    violations: list[str] = []
    for lineno, line in enumerate(lines, 1):
        if not _VARNAS_ASSIGN.search(line):
            continue
        if _line_is_inside_act_function(source, lineno):
            continue
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        violations.append(f"  line {lineno}: {stripped}")
    if violations:
        msg = (
            f"{pipeline_file.name} "
            f"contains direct '.varnas =' outside an 'act' function:\n"
            + "\n".join(violations)
        )
        pytest.fail(msg)
