"""
tools/sutra_lint.py — the edit-time gate for Articles 2, 13, 15 and 16.
──────────────────────────────────────────────────────────────────────

Seven checks. Each names a failure that has already cost real time in this
repository, and each can fail — advice is not a check.

  RATCHETED (a violation is an error; the count may only fall)
    arm-in-cond          Art. 13 §1 — `cond()` gated on a `_arm` meta flag
                         instead of the linguistic environment
    coordinate-in-cond   Art. 2 §2c — `cond()` reading vibhakti / vacana /
                         puruṣa / lakāra, the paradigm coordinates it is
                         supposed to be blind to

    nisedha-as-vidhi     a sūtra whose padaccheda contains the standalone
                         word न — a निषेध — typed VIDHI and declaring no
                         blocks. 6.1.104 नादिचि was exactly this, and रामौ
                         derived for the wrong reason until it was fixed
                         (Art. 15). 87 more are like it today.

  ERRORS (never acceptable)
    inert-pratisedha     a प्रतिषेध whose declared target is never actually
                         BLOCKED anywhere in the suite — a निषेध that cannot
                         say no is dead code (Art. 15)

  REPORTS (the worklist; they do not fail the build)
    uncited-mover        moves the tape, no Art. 14 citation (Art. 16 §3)
    untested-mover       moves the tape, no test names it (Art. 16 §4)
    placeholder-gloss    why_dev is still the scaffolding string

Usage::

    python3 -m tools.sutra_lint                 # human report, exit 1 on errors
    python3 -m tools.sutra_lint --json
    python3 -m tools.sutra_lint --freeze        # accept current ratchet counts
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

BASELINE_PATH = _ROOT / "sig" / "sutra_lint_baseline.json"
SUITE_SIG_PATH = _ROOT / "sig" / "suite_sig.json"

ARM_RE = re.compile(r"""["'][\w.]*_arm["']|_arm\b""")
COORDINATE_RE = re.compile(r"""meta(?:\.get\(|\[)\s*["'](vibhakti|vacana|purusha|lakara)""")
PLACEHOLDER_RE = re.compile(r"\(सूत्रम्\s")
# A निषेध carries न as its own *word*. The surface may hide it — नादिचि is
# न + आदिचि — so the test is on the padaccheda, never on the sandhi'd text.
PADA_SEP_RE = re.compile(r"[·\s।,]+")


def _padaccheda(sutra_id: str, rec: Any) -> str:
    text = (getattr(rec, "padaccheda_dev", "") or "").strip()
    if text:
        return text
    path = _ROOT / "sutra_ref_out" / (sutra_id.replace(".", "_") + ".json")
    if not path.exists():
        return ""
    record = json.loads(path.read_text(encoding="utf-8"))
    return (((record.get("text") or {}).get("padaccheda") or {}).get("dev") or "").strip()


def _is_nisedha(sutra_id: str, rec: Any) -> bool:
    return "न" in [t for t in PADA_SEP_RE.split(_padaccheda(sutra_id, rec)) if t]


def _sutra_files() -> list[Path]:
    return sorted((_ROOT / "sutras").rglob("sutra_*.py"))


def _sutra_id(path: Path) -> str:
    return path.stem.replace("sutra_", "").replace("_", ".")


def _cond_source(tree: ast.Module) -> str:
    """Source of `cond` and every helper it calls at module level, roughly."""
    chunks = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and (
            node.name == "cond" or node.name.startswith("_")
        ):
            chunks.append(ast.unparse(node))
    return "\n".join(chunks)


def scan_files() -> dict[str, dict[str, Any]]:
    """Static facts per sūtra file."""
    out: dict[str, dict[str, Any]] = {}
    for path in _sutra_files():
        text = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        cond_src = _cond_source(tree)
        out[_sutra_id(path)] = {
            "path": path.relative_to(_ROOT).as_posix(),
            "arm_in_cond": bool(ARM_RE.search(cond_src)),
            "coordinate_in_cond": bool(COORDINATE_RE.search(cond_src)),
            "placeholder_gloss": bool(PLACEHOLDER_RE.search(text)),
        }
    return out


def lint() -> dict[str, Any]:
    import sutras  # noqa: F401 — fills SUTRA_REGISTRY
    from engine import SUTRA_REGISTRY
    from engine.coverage import honest_coverage, load_ledger

    static = scan_files()
    report = honest_coverage(SUTRA_REGISTRY)
    ledger = load_ledger() or {}
    moved = set(ledger.get("moved", ()))
    suite_sig = (
        json.loads(SUITE_SIG_PATH.read_text(encoding="utf-8"))
        if SUITE_SIG_PATH.exists() else {"nodes": {}}
    )
    ever_blocked = {
        sid for sid, node in suite_sig.get("nodes", {}).items()
        if node.get("status", {}).get("BLOCKED")
    }

    findings: dict[str, list[str]] = {
        "arm-in-cond": [],
        "coordinate-in-cond": [],
        "nisedha-as-vidhi": [],
        "inert-pratisedha": [],
        "uncited-mover": [],
        "untested-mover": [],
        "placeholder-gloss": [],
    }

    for sid, facts in static.items():
        if facts["arm_in_cond"]:
            findings["arm-in-cond"].append(sid)
        if facts["coordinate_in_cond"]:
            findings["coordinate-in-cond"].append(sid)
        if facts["placeholder_gloss"]:
            findings["placeholder-gloss"].append(sid)

    for sid, rec in SUTRA_REGISTRY.items():
        text_dev = (getattr(rec, "text_dev", "") or "").strip()
        blocks = tuple(getattr(rec, "blocks_sutra_ids", ()) or ())
        type_name = rec.sutra_type.name
        if type_name == "VIDHI" and not blocks and _is_nisedha(sid, rec):
            findings["nisedha-as-vidhi"].append(f"{sid} {text_dev}")
        if type_name == "PRATISHEDHA" and blocks:
            if not any(b in ever_blocked for b in blocks):
                findings["inert-pratisedha"].append(f"{sid} → {','.join(blocks)}")

    uncited = set(report["moving_but_uncited"])
    findings["uncited-mover"] = [sid for sid in sorted(moved) if sid in uncited]
    findings["untested-mover"] = [
        sid for sid in sorted(moved)
        if sid in SUTRA_REGISTRY and not _has_test(sid)
    ]

    return {"findings": findings, "coverage": {
        "registered": report["registered"],
        "implemented": report["implemented"],
    }}


def _has_test(sutra_id: str) -> bool:
    from engine.coverage import _test_mentions

    return _test_mentions().get(sutra_id, 0) > 0


RATCHETED = ("arm-in-cond", "coordinate-in-cond", "nisedha-as-vidhi")
ERRORS = ("inert-pratisedha",)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Constitutional lint for sūtra files.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--freeze", action="store_true",
                    help="accept the current ratchet counts as the new baseline")
    args = ap.parse_args(argv)

    result = lint()
    findings = result["findings"]
    baseline = (
        json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        if BASELINE_PATH.exists() else {}
    )

    if args.freeze:
        BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
        BASELINE_PATH.write_text(
            json.dumps({k: len(findings[k]) for k in RATCHETED}, indent=2) + "\n",
            encoding="utf-8",
        )
        print("frozen:", {k: len(findings[k]) for k in RATCHETED})
        return 0

    if args.json:
        print(json.dumps({**result, "baseline": baseline}, ensure_ascii=False, indent=2))
        return _exit_code(findings, baseline)

    print("sūtra lint — CONSTITUTION Art. 2 · 13 · 15 · 16\n")
    for name in RATCHETED:
        n, was = len(findings[name]), baseline.get(name)
        verdict = "" if was is None else (
            "  ✗ RISEN" if n > was else f"  (baseline {was})"
        )
        print(f"  {name:<20} {n:>5}{verdict}")
        for sid in findings[name][:5]:
            print(f"      {sid}")
    for name in ERRORS:
        print(f"  {name:<20} {len(findings[name]):>5}" + ("  ✗" if findings[name] else ""))
        for item in findings[name][:5]:
            print(f"      {item}")
    print("\n  reports (worklist, not failures)")
    for name in ("uncited-mover", "untested-mover", "placeholder-gloss"):
        print(f"  {name:<20} {len(findings[name]):>5}")
        for item in findings[name][:3]:
            print(f"      {item}")
    cov = result["coverage"]
    print(f"\n  implemented {cov['implemented']} / registered {cov['registered']} (Art. 16)")
    return _exit_code(findings, baseline)


def _exit_code(findings: dict[str, list[str]], baseline: dict[str, int]) -> int:
    bad = any(findings[name] for name in ERRORS)
    for name in RATCHETED:
        was = baseline.get(name)
        if was is not None and len(findings[name]) > was:
            bad = True
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
