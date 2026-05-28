"""
CONSTITUTIONAL TEST: No New Arm Gates in sūtra ``cond()``
=========================================================

Enforces **CONSTITUTION Article 13 §1** (hardened by AMENDMENT 14) on a
**strict-additive** basis.

Article 13 §1 forbids any file under ``sutras/`` whose ``cond()`` reads
``state.meta[K]`` (or ``state.meta.get(K, ...)``) where the string key ``K``:

  * ends in ``_arm``, **or**
  * matches the demo/prakriya regex ``(?i)(corrected_v[0-9]+|P[0-9]+(_|$))``.

These are "arm gates": ad-hoc recipe coordination switches that let a sūtra's
``cond`` fire because a *pipeline* flipped a flag, rather than because of a
genuine structural signal (tags / SAMJNA / registry / Term-local completion
flags — Articles 2, 7, 13).

The remaining live arm reads are **grandfathered technical debt**.  This test
pins the current count as a ceiling: a commit may **decrease** it (migration —
always allowed) but must never **increase** it.  Because the check is purely
additive, gradual cleanup is encouraged while regressions are blocked in CI.

Scope: only the body of the function literally named ``cond`` in each
``sutras/**/sutra_*.py`` file is analysed, matching the CONSTITUTION's wording
("its ``cond()`` reads ...").  String-literal keys only — a key supplied as a
module-level constant Name is not statically classifiable here and is governed
by the companion test ``test_no_demo_ids_in_sutra_arm_keys.py``.
"""
from __future__ import annotations

import ast
import re
import pathlib

# ── Arm-gate key classifiers (verbatim from CONSTITUTION Art. 13 §1) ──────────
_ARM_SUFFIX_RE = re.compile(r"_arm$")
_DEMO_RE = re.compile(r"(?i)(corrected_v[0-9]+|P[0-9]+(_|$))")

_SUTRAS_ROOT = pathlib.Path(__file__).resolve().parents[2] / "sutras"

# ── Strict-additive baseline ────────────────────────────────────────────────
# Number of arm-gate string-literal reads inside sūtra ``cond()`` bodies as of
# the P5/P6 audit.  This is a CEILING: migrations that remove an arm read must
# lower this number; commits may never raise it.
#   • measured 2026-05-28 after the P5 arm-flag clearance campaign.
ARM_GATE_BASELINE = 96


def _meta_key(node: ast.AST):
    """If ``node`` is ``state.meta[K]`` or ``state.meta.get(K, ...)`` with a
    string-literal ``K``, return ``(kind, K)``; else ``None``."""
    # state.meta[K]
    if isinstance(node, ast.Subscript):
        val = node.value
        if (
            isinstance(val, ast.Attribute)
            and val.attr == "meta"
            and isinstance(val.value, ast.Name)
            and val.value.id == "state"
        ):
            sl = node.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                return ("sub", sl.value)
    # state.meta.get(K, ...)
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Attribute) and f.attr == "get":
            base = f.value
            if (
                isinstance(base, ast.Attribute)
                and base.attr == "meta"
                and isinstance(base.value, ast.Name)
                and base.value.id == "state"
            ):
                if (
                    node.args
                    and isinstance(node.args[0], ast.Constant)
                    and isinstance(node.args[0].value, str)
                ):
                    return ("get", node.args[0].value)
    return None


def _is_arm_gate_key(key: str) -> bool:
    return bool(_ARM_SUFFIX_RE.search(key)) or bool(_DEMO_RE.search(key))


def _count_arm_reads_in_cond(tree: ast.Module) -> list[str]:
    """Return arm-gate keys read inside any function named ``cond`` in ``tree``."""
    hits: list[str] = []
    for fn in ast.walk(tree):
        if not (isinstance(fn, ast.FunctionDef) and fn.name == "cond"):
            continue
        for node in ast.walk(fn):
            mk = _meta_key(node)
            if mk is None:
                continue
            kind, key = mk
            if not _is_arm_gate_key(key):
                continue
            # Only count READS: a subscript in Load context, or any .get() call.
            if kind == "get":
                hits.append(key)
            elif kind == "sub" and isinstance(getattr(node, "ctx", None), ast.Load):
                hits.append(key)
    return hits


def _scan_all() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for path in sorted(_SUTRAS_ROOT.rglob("sutra_*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        hits = _count_arm_reads_in_cond(tree)
        if hits:
            out[str(path.relative_to(_SUTRAS_ROOT))] = hits
    return out


def test_arm_gates_in_cond_do_not_increase() -> None:
    """Strict-additive guard: the number of arm-gate reads in sūtra ``cond()``
    must never exceed the pinned baseline (CONSTITUTION Art. 13 §1)."""
    per_file = _scan_all()
    total = sum(len(v) for v in per_file.values())
    assert total <= ARM_GATE_BASELINE, (
        f"arm-gate reads inside sūtra cond() increased: got {total}, "
        f"baseline {ARM_GATE_BASELINE} (CONSTITUTION Art. 13 §1, strict-additive).\n"
        "A new sūtra cond() reads an '_arm' or demo-id (corrected_v*/P###_) "
        "state.meta key. Replace it with a structural signal — tags, a prior "
        "SAMJNA step, a registry entry, or a Term-local completion flag — or, "
        "if you intentionally REMOVED an arm read, lower ARM_GATE_BASELINE."
    )


def test_arm_gate_baseline_is_not_stale() -> None:
    """If cleanup has driven the count below the baseline, nudge the engineer to
    ratchet the baseline down (keeps the ceiling tight; never blocks a commit
    on its own beyond a clear instruction)."""
    per_file = _scan_all()
    total = sum(len(v) for v in per_file.values())
    assert total == ARM_GATE_BASELINE, (
        f"arm-gate reads in cond() = {total}, but ARM_GATE_BASELINE = "
        f"{ARM_GATE_BASELINE}. The count DECREASED (good — migration progress). "
        f"Lower ARM_GATE_BASELINE to {total} to keep the strict-additive ceiling "
        "tight (CONSTITUTION Art. 13 §1)."
    )
