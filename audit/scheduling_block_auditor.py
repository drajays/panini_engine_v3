"""
Scheduling-block auditor — **read-only** AST pass.

Goal: find **contiguous** ``apply_rule("x.y.z", …)`` chains that appear in more
than one place (likely copy-paste scheduling), without touching engine state or
JSON.

**Not** what the draft did:
  • Do **not** treat every ``"4.2.114"`` string literal as a schedule step
    (docstrings, meta dicts, tests would explode false positives).
  • Do **not** use ``ast.walk`` for ordering (it is not source-order).
  • Do **not** emit ``O(n^2)`` *all* sub-windows of every function by default.

This implementation keys on **``apply_rule``** calls only (the CONSTITUTION
recipe port), with optional bounded windowing.
"""
from __future__ import annotations

import ast
import hashlib
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Iterator

SUTRA_ID_RE = re.compile(r"^\d+\.\d+\.\d+$")

# Directories to scan (python only).
SCAN_DIRS: tuple[str, ...] = ("pipelines", "core")

# Skip noisy / non-recipe trees.
SKIP_NAME_PREFIXES: tuple[str, ...] = ("test_",)
SKIP_BASENAMES: frozenset[str] = frozenset(
    {"__init__.py", "_template.py", "scheduling_block_auditor.py"}
)

MIN_BLOCK_LEN = 3
MAX_BLOCK_LEN = 24
MAX_WINDOWS_PER_FUNC = 400


@dataclass(frozen=True)
class _Occ:
    file: str
    func: str
    start_line: int
    end_line: int


@dataclass
class _DupGroup:
    sids: tuple[str, ...]
    fingerprint: str
    occurrences: list[_Occ] = field(default_factory=list)

    @property
    def span_files(self) -> int:
        return len({o.file for o in self.occurrences})


# ─────────────────────────────────────────────────────────────
# Public facade (used by constitutional tests)
# ─────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Occurrence:
    file: str
    func: str
    start_line: int
    end_line: int


@dataclass
class DuplicateGroup:
    fingerprint: str
    sids: list[str]
    occurrences: list[Occurrence] = field(default_factory=list)

    @property
    def length(self) -> int:
        return len(self.sids)


class SchedulingBlockAuditor:
    """
    Compatibility facade: the auditor is still AST-only and does not touch engine state.

    This wrapper matches the interface used by proposed constitutional tests:
      - ``scan()``
      - ``find_duplicates()``
      - ``files_scanned`` / ``errors``
    """

    def __init__(self, project_root: str | Path = ".") -> None:
        self.root = Path(project_root).resolve()
        self.files_scanned: list[str] = []
        self.errors: list[str] = []
        self._dups: list[DuplicateGroup] | None = None

    def scan(self) -> None:
        dups, errors, files = _run_audit_with_files(self.root)
        self._dups = dups
        self.errors = errors
        self.files_scanned = files

    def find_duplicates(self) -> list[DuplicateGroup]:
        if self._dups is None:
            self.scan()
        return list(self._dups or [])


def _str_arg0(call: ast.Call) -> str | None:
    if not call.args:
        return None
    a0 = call.args[0]
    if isinstance(a0, ast.Constant) and isinstance(a0.value, str):
        s = a0.value
        return s if SUTRA_ID_RE.match(s) else None
    return None


def _is_apply_rule_call(node: ast.AST) -> ast.Call | None:
    if not isinstance(node, ast.Call):
        return None
    f = node.func
    if isinstance(f, ast.Name) and f.id == "apply_rule":
        return node
    if isinstance(f, ast.Attribute) and f.attr == "apply_rule":
        return node
    return None


def _calls_in_stmt(stmt: ast.stmt) -> list[tuple[str, int]]:
    out: list[tuple[str, int]] = []
    if isinstance(stmt, ast.Assign):
        for t in stmt.targets:
            if isinstance(t, ast.Name) and isinstance(stmt.value, ast.Call):
                c = _is_apply_rule_call(stmt.value)
                if c:
                    sid = _str_arg0(c)
                    if sid:
                        out.append((sid, c.lineno))
    elif isinstance(stmt, ast.AnnAssign) and stmt.value and isinstance(stmt.value, ast.Call):
        c = _is_apply_rule_call(stmt.value)
        if c:
            sid = _str_arg0(c)
            if sid:
                out.append((sid, c.lineno))
    elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        c = _is_apply_rule_call(stmt.value)
        if c:
            sid = _str_arg0(c)
            if sid:
                out.append((sid, c.lineno))
    return out


def _collect_apply_rule_linear(stmts: list[ast.stmt]) -> list[tuple[str, int]]:
    """Best-effort **statement-order** collection (linear + shallow *if*)."""
    out: list[tuple[str, int]] = []
    for st in stmts:
        if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        if isinstance(st, ast.If):
            out.extend(_collect_apply_rule_linear(st.body))
            out.extend(_collect_apply_rule_linear(st.orelse))
            continue
        if isinstance(st, (ast.For, ast.While, ast.With, ast.Try)):
            inner: list[ast.stmt] = []
            if isinstance(st, ast.For):
                inner = st.body
            elif isinstance(st, ast.While):
                inner = st.body
            elif isinstance(st, ast.With):
                inner = st.body
            else:
                inner = st.body
            out.extend(_collect_apply_rule_linear(inner))
            continue
        out.extend(_calls_in_stmt(st))
    return out


def _function_defs(tree: ast.AST) -> Iterator[tuple[str, ast.FunctionDef | ast.AsyncFunctionDef]]:
    for n in tree.body:
        if isinstance(n, ast.FunctionDef | ast.AsyncFunctionDef):
            yield ("__module__", n)
        elif isinstance(n, ast.ClassDef):
            for m in n.body:
                if isinstance(m, ast.FunctionDef | ast.AsyncFunctionDef):
                    yield (f"{n.name}.{m.name}", m)


def _iter_windows(seq: list[str], lineno: list[int]) -> Iterator[tuple[tuple[str, ...], int, int]]:
    n = len(seq)
    if n < MIN_BLOCK_LEN:
        return
    emitted = 0
    for w in range(MIN_BLOCK_LEN, min(MAX_BLOCK_LEN, n) + 1):
        for i in range(0, n - w + 1):
            yield (tuple(seq[i : i + w]), lineno[i], lineno[i + w - 1])
            emitted += 1
            if emitted >= MAX_WINDOWS_PER_FUNC:
                return


def _scan_file(root: Path, path: Path) -> dict[tuple[str, ...], list[_Occ]]:
    rel = str(path.relative_to(root))
    hits: dict[tuple[str, ...], list[_Occ]] = defaultdict(list)
    try:
        src = path.read_text(encoding="utf-8")
        tree = ast.parse(src, filename=rel)
    except (OSError, SyntaxError, UnicodeDecodeError):
        return hits

    for func_label, fn in _function_defs(tree):
        seq_ln = _collect_apply_rule_linear(fn.body)
        if len(seq_ln) < MIN_BLOCK_LEN:
            continue
        sids = [s for s, _ in seq_ln]
        lnos = [ln for _, ln in seq_ln]
        for tup, a, b in _iter_windows(sids, lnos):
            hits[tup].append(_Occ(rel, func_label, a, b))
    return hits


def _merge_hits(
    per_file: Iterable[dict[tuple[str, ...], list[_Occ]]],
) -> dict[tuple[str, ...], list[_Occ]]:
    merged: dict[tuple[str, ...], list[_Occ]] = defaultdict(list)
    for h in per_file:
        for k, v in h.items():
            merged[k].extend(v)
    return merged


def _fingerprint(sids: tuple[str, ...]) -> str:
    return hashlib.md5("|".join(sids).encode(), usedforsecurity=False).hexdigest()[:12]


def run_audit(project_root: str | Path) -> tuple[list[_DupGroup], list[str]]:
    root = Path(project_root).resolve()
    errors: list[str] = []
    acc: dict[tuple[str, ...], list[_Occ]] = defaultdict(list)

    for dname in SCAN_DIRS:
        d = root / dname
        if not d.is_dir():
            errors.append(f"missing_dir:{dname}")
            continue
        for py in sorted(d.rglob("*.py")):
            p = str(py)
            if "__pycache__" in p or ".venv" in p or "venv" in p:
                continue
            if py.name in SKIP_BASENAMES:
                continue
            if any(py.name.startswith(pref) for pref in SKIP_NAME_PREFIXES):
                continue
            for k, v in _scan_file(root, py).items():
                acc[k].extend(v)

    dups: list[_DupGroup] = []
    for sids, occs in acc.items():
        if len(occs) < 2:
            continue
        if len({o.file for o in occs}) < 2:
            continue
        dups.append(
            _DupGroup(
                sids=sids,
                fingerprint=_fingerprint(sids),
                occurrences=sorted(occs, key=lambda o: (o.file, o.start_line)),
            )
        )
    dups.sort(key=lambda g: (-len(g.sids), -len(g.occurrences), g.fingerprint))
    return dups, errors


def _run_audit_with_files(project_root: Path) -> tuple[list[DuplicateGroup], list[str], list[str]]:
    """
    Same as ``run_audit`` but also returns list of python files that produced at least
    one ``apply_rule`` window (for scan-coverage assertions).
    """
    root = project_root
    errors: list[str] = []
    acc: dict[tuple[str, ...], list[_Occ]] = defaultdict(list)
    files_scanned: set[str] = set()

    for dname in SCAN_DIRS:
        d = root / dname
        if not d.is_dir():
            errors.append(f"missing_dir:{dname}")
            continue
        for py in sorted(d.rglob("*.py")):
            p = str(py)
            if "__pycache__" in p or ".venv" in p or "venv" in p:
                continue
            if py.name in SKIP_BASENAMES:
                continue
            if any(py.name.startswith(pref) for pref in SKIP_NAME_PREFIXES):
                continue
            rel = str(py.relative_to(root))
            file_hits = _scan_file(root, py)
            if file_hits:
                files_scanned.add(rel)
            for k, v in file_hits.items():
                acc[k].extend(v)

    groups: list[DuplicateGroup] = []
    for sids, occs in acc.items():
        if len(occs) < 2:
            continue
        if len({o.file for o in occs}) < 2:
            continue
        groups.append(
            DuplicateGroup(
                fingerprint=_fingerprint(sids),
                sids=list(sids),
                occurrences=[
                    Occurrence(o.file, o.func, o.start_line, o.end_line)
                    for o in sorted(occs, key=lambda x: (x.file, x.start_line))
                ],
            )
        )
    groups.sort(key=lambda g: (-g.length, -len(g.occurrences), g.fingerprint))
    return groups, errors, sorted(files_scanned)


def _render_md(
    dups: list[_DupGroup],
    errors: list[str],
    scanned_py: int,
) -> str:
    lines: list[str] = []
    lines.append("# Scheduling block audit (``apply_rule`` chains)\n")
    lines.append(
        "Read-only AST scan of **ordered** ``apply_rule(\"x.y.z\", …)`` calls.  "
        "Strings that are not the first argument to ``apply_rule`` are ignored.\n"
    )
    lines.append(f"- **scanned_py_files**: `{scanned_py}`")
    lines.append(f"- **duplicate_cross_file_groups**: `{len(dups)}`\n")

    if errors:
        lines.append("## Scan errors\n")
        for e in errors:
            lines.append(f"- `{e}`")
        lines.append("")

    if not dups:
        lines.append("## Result\n")
        lines.append("**CLEAN**: no duplicate contiguous ``apply_rule`` blocks "
                     f"(length ≥ {MIN_BLOCK_LEN}) found across multiple files.\n")
        return "\n".join(lines).rstrip() + "\n"

    lines.append("## Duplicate groups (longest first)\n")
    for i, g in enumerate(dups, 1):
        lines.append(f"### {i} — `{g.fingerprint}` ({len(g.sids)} sūtras)\n")
        lines.append("```")
        lines.append(" → ".join(g.sids))
        lines.append("```\n")
        lines.append("| File | Scope | Lines |")
        lines.append("|---|---|---|")
        for o in g.occurrences:
            lines.append(
                f"| `{o.file}` | `{o.func}` | {o.start_line}–{o.end_line} |"
            )
        lines.append("")
        lines.append(
            "**Note:** identical windows often mean “extract to "
            "``core.canonical_pipelines`` and call one helper”, not that the "
            "sūtras are duplicated in ``sutras/``.\n"
        )
    return "\n".join(lines).rstrip() + "\n"


def _count_py_files(root: Path) -> int:
    n = 0
    for dname in SCAN_DIRS:
        d = root / dname
        if not d.is_dir():
            continue
        for py in d.rglob("*.py"):
            if "__pycache__" in str(py):
                continue
            if py.name in SKIP_BASENAMES:
                continue
            if any(py.name.startswith(pref) for pref in SKIP_NAME_PREFIXES):
                continue
            n += 1
    return n


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    root = Path(argv[0]).resolve() if argv else Path(".").resolve()
    dups, errors = run_audit(root)
    out = root / "docs" / "scheduling_block_audit.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    scanned = _count_py_files(root)
    out.write_text(_render_md(dups, errors, scanned), encoding="utf-8")
    print(f"[scheduling_block_auditor] wrote {out} ({len(dups)} group(s))")
    return 0 if not dups else 1


if __name__ == "__main__":
    raise SystemExit(main())
