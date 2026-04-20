"""
tests/constitutional/test_no_vibhakti_read_in_cond.py
───────────────────────────────────────────────────────

Constitution Article 2, rule (3): cond(state) may NEVER read
paradigm-coordinate keys from Term.meta.

We scan every sūtra source file for the literal offending strings
INSIDE any function whose name starts with 'cond'.  This is a static
scan — deliberately strict.

The ONE allowed exception is sutras/adhyaya_4/pada_1/sutra_4_1_2.py's
act() (not cond), because 4.1.2 is the designated sup-attacher and
is the only place where (vibhakti, vacana) enters the engine.  We
DO NOT exempt any cond() — not even 4.1.2's.
"""
from __future__ import annotations

import ast
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SUTRAS_DIR = ROOT / "sutras"

FORBIDDEN_META_KEYS = (
    "'vibhakti'", '"vibhakti"',
    "'vacana'",   '"vacana"',
    "'purusha'",  '"purusha"',
    "'lakara'",   '"lakara"',
    "'surface_gold'", '"surface_gold"',
)


def _iter_sutra_files():
    for p in SUTRAS_DIR.rglob("sutra_*.py"):
        yield p


def _source_of_function(tree: ast.AST, func_name: str, source: str) -> str | None:
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name == func_name:
                return ast.get_source_segment(source, node)
    return None


@pytest.mark.parametrize("sutra_path", list(_iter_sutra_files()),
                         ids=lambda p: p.relative_to(ROOT).as_posix())
def test_cond_does_not_read_forbidden_meta(sutra_path):
    source = sutra_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    cond_src = _source_of_function(tree, "cond", source)
    if cond_src is None:
        return  # sūtra has no cond (rare: NIPATANA stubs)
    for key in FORBIDDEN_META_KEYS:
        assert key not in cond_src, (
            f"{sutra_path}: cond() reads forbidden paradigm key {key}. "
            "CONSTITUTION Article 2 forbids (vibhakti/vacana/purusha/lakara) "
            "reads inside cond()."
        )
