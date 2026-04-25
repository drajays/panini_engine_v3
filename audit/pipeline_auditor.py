"""
Static checks for pipeline / registry consistency.

Scans **only** ``.py`` files under selected subtrees.  Does not read
``data/**.json`` or other heavy assets (aligns with safe audit practice).
"""
from __future__ import annotations

import ast
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

# Keep in sync with ``tests/unit/test_prakriya_integrity._ENGINE_LITERAL_SUTRA_ID_ALLOW``.
_ENGINE_LITERAL_SUTRA_ID_ALLOW: dict[str, frozenset[str]] = {
    "executors/exec_vidhi.py": frozenset({"1.3.9"}),
    "stubs.py": frozenset({"0.0.0"}),
}

_SUTRA_ID_FULL = re.compile(r"^\d+\.\d+\.\d+$")

_SCAN_SUBDIRS: tuple[str, ...] = ("engine", "sutras", "pipelines", "core", "audit")


def _str_value(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if type(node).__name__ == "Str" and isinstance(getattr(node, "s", None), str):
        return node.s
    return None


def _iter_py_files(root: Path, subdirs: Iterable[str]) -> list[Path]:
    out: list[Path] = []
    for name in subdirs:
        d = root / name
        if not d.is_dir():
            continue
        for py in sorted(d.rglob("*.py")):
            p = str(py)
            if "__pycache__" in p or ".venv" in p or "venv" in p:
                continue
            out.append(py)
    return out


def _iter_engine_exact_sutra_id_literals(
    engine_dir: Path, repo_root: Path
) -> list[tuple[str, int, str, str]]:
    out: list[tuple[str, int, str, str]] = []
    for py in sorted(engine_dir.rglob("*.py")):
        if "__pycache__" in str(py):
            continue
        rel = py.relative_to(repo_root)
        try:
            sfx = str(py.relative_to(engine_dir))
        except ValueError:
            continue
        if sfx == "sutra_type.py":
            continue
        try:
            tree = ast.parse(py.read_text(encoding="utf-8"), filename=str(rel))
        except (OSError, SyntaxError):
            continue
        for n in ast.walk(tree):
            s = _str_value(n)
            if s and _SUTRA_ID_FULL.match(s):
                out.append((str(rel), n.lineno, s, sfx))
    return out


def _sutra_ids_from_sutra_files(sutras_dir: Path, repo_root: Path) -> list[str]:
    found: list[str] = []
    for py in sorted(sutras_dir.rglob("sutra_*.py")):
        if "__pycache__" in py.parts:
            continue
        rel = str(py.relative_to(repo_root))
        try:
            src = py.read_text(encoding="utf-8")
            tree = ast.parse(src, filename=rel)
        except (OSError, SyntaxError):
            continue
        for n in ast.walk(tree):
            if not isinstance(n, ast.Call):
                continue
            if not (isinstance(n.func, ast.Name) and n.func.id == "SutraRecord"):
                continue
            for kw in n.keywords:
                if kw.arg != "sutra_id":
                    continue
                v = _str_value(kw.value)
                if v and _SUTRA_ID_FULL.match(v):
                    found.append(v)
    return found


class PipelineAuditor:
    def __init__(self, project_root: str | Path) -> None:
        self.root = Path(project_root).resolve()

    def engine_disallowed_sutra_id_literals(self) -> list[str]:
        """Paths like ``engine/foo.py:12: '1.2.3'`` when not allowlisted."""
        hits: list[str] = []
        engine = self.root / "engine"
        for _rel, _ln, val, sfx in _iter_engine_exact_sutra_id_literals(
            engine, self.root
        ):
            allow = _ENGINE_LITERAL_SUTRA_ID_ALLOW.get(sfx)
            if allow and val in allow:
                continue
            hits.append(f"engine/{sfx}:{_ln}: {val!r}")
        return hits

    def duplicate_sutra_ids_in_sutra_files(self) -> list[str]:
        """Sūtra ids that appear in more than one ``SutraRecord(…, sutra_id=…)``."""
        sutras = self.root / "sutras"
        ids = _sutra_ids_from_sutra_files(sutras, self.root)
        return [k for k, c in Counter(ids).items() if c > 1]

    def py_file_count(self) -> int:
        return len(_iter_py_files(self.root, _SCAN_SUBDIRS))

    def run_smoke(self) -> dict:
        """
        Light-weight report (no JSON, no full-tree string matching).
        Import ``sutras`` before using :func:`registry_duplicate_check` if
        you need a populated ``SUTRA_REGISTRY``.
        """
        return {
            "project_root": str(self.root),
            "py_files_scanned_subtrees": self.py_file_count(),
            "engine_sutra_literal_violations": self.engine_disallowed_sutra_id_literals(),
            "duplicate_sutra_ids_ast": self.duplicate_sutra_ids_in_sutra_files(),
        }


def _render_markdown_report(report: dict) -> str:
    viol = report.get("engine_sutra_literal_violations") or []
    dup = report.get("duplicate_sutra_ids_ast") or []
    scanned = report.get("py_files_scanned_subtrees")
    root = report.get("project_root")

    lines: list[str] = []
    lines.append("# Pre-refactor audit (python-only)\n")
    lines.append(
        "This report is intentionally **python-only**: it scans AST and selected "
        "source subtrees and **does not** read `data/**` assets.\n"
    )
    lines.append(f"- **project_root**: `{root}`")
    lines.append(f"- **py_files_scanned_subtrees**: `{scanned}`")
    lines.append(f"- **duplicate_sutra_ids_ast**: `{len(dup)}`")
    lines.append(f"- **engine_sutra_literal_violations**: `{len(viol)}`\n")

    if dup:
        lines.append("## Duplicate sutra ids (AST)\n")
        for sid in sorted(dup)[:200]:
            lines.append(f"- `{sid}`")
        lines.append("")

    if viol:
        lines.append("## Disallowed bare sutra-id literals under `engine/`\n")
        for hit in viol[:400]:
            lines.append(f"- `{hit}`")
        lines.append("")

    if not dup and not viol:
        lines.append("## Result\n")
        lines.append("**CLEAN**: no duplicates detected by this audit.\n")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    root = Path(".").resolve()
    a = PipelineAuditor(root)
    report = a.run_smoke()
    md = _render_markdown_report(report)
    out = root / "docs" / "pre_refactor_audit.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(f"[audit] wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
