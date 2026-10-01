"""
tools/glassbox_gaps.py — find form changes that no sūtra step accounts for.

    python3 -m tools.glassbox_gaps            # summary by location
    python3 -m tools.glassbox_gaps --list     # every gap

A trace is glass-box when each row's form_before equals the previous row's
form_after, and only APPLIED rows change the form. Anything else is a pipeline
mutating the tape outside apply_rule (CONSTITUTION Art. 11).

Also reports placeholder sūtra files: registered, but their act() only sets
``state.meta["anga_kind"]`` and changes nothing.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

_PLACEHOLDER = re.compile(r'state\.meta\["anga_kind"\]\s*=\s*"\d')
_MUTATES = re.compile(r"varnas|tags\.add|mk\(|terms\.insert")


def placeholder_files() -> list[str]:
    out = []
    for f in sorted(glob.glob(str(ROOT / "sutras/adhyaya_*/pada_*/sutra_*.py"))):
        body = Path(f).read_text(encoding="utf-8")
        if _PLACEHOLDER.search(body) and not _MUTATES.search(body):
            out.append(str(Path(f).relative_to(ROOT)))
    return out


def trace_gaps(trace: list[dict]) -> list[tuple[str, str, str, str]]:
    """(after-row, before-row, form, next form) for each unaccounted change."""
    gaps = []
    prev = None
    for row in trace:
        if prev is not None and prev.get("form_after") != row.get("form_before"):
            gaps.append((f"{prev['sutra_id']}({prev['status']})", f"{row['sutra_id']}({row['status']})",
                         prev.get("form_after"), row.get("form_before")))
        if row.get("status") != "APPLIED" and row.get("form_before") != row.get("form_after"):
            gaps.append((f"{row['sutra_id']}({row['status']})", "-", row.get("form_before"), row.get("form_after")))
        prev = row
    return gaps


def all_gaps() -> dict[str, list]:
    from tools.dump_pipelines_trace import main as dump_main

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as fp:
        tmp = Path(fp.name)
    if dump_main(["-o", str(tmp)]) != 0:
        raise RuntimeError("trace dump failed")
    payload = json.loads(tmp.read_text())
    tmp.unlink()
    out = {}
    for rec in payload["records"]:
        g = trace_gaps(rec.get("trace") or [])
        if g:
            out[f"{rec['module']}.{rec['callable']}"] = g
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args(argv)
    gaps = all_gaps()
    n = sum(len(v) for v in gaps.values())
    where = Counter(f"{x[0]} -> {x[1]}" for v in gaps.values() for x in v)
    print(f"[glassbox_gaps] {n} unaccounted form changes in {len(gaps)} derivations")
    for k, c in where.most_common(20):
        print(f"  {c:4}  {k}")
    if a.list:
        for name, v in sorted(gaps.items()):
            for x in v:
                print(f"{name}: {x[0]} -> {x[1]}  {x[2]} => {x[3]}")
    print(f"[glassbox_gaps] {len(placeholder_files())} placeholder sūtra files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
