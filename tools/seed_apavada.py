"""
tools/seed_apavada.py — declare the apavāda graph from the reference corpus.

CONSTITUTION Art. 15: a conflict is won by a *declared* relation, never by a
narrowed cond. The relations themselves are not ours to invent — the vendored
reference records in ``sutra_ref_out/`` carry a ``resolver.apavada_of`` field,
and this tool copies it onto the SutraRecord where both sūtras are registered.

    python3 -m tools.seed_apavada            # dry run
    python3 -m tools.seed_apavada --apply

Every write records where it came from. A declared apavāda changes who wins a
conflict, so the suite is the check: a derivation that changes is a finding to
look at, not a number to update.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

PROVENANCE = "sutra_ref_out resolver.apavada_of"


def declared_pairs() -> dict[str, list[str]]:
    """{exception: [general, ...]} as the reference corpus states it."""
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    pairs: dict[str, list[str]] = {}
    for path in sorted((_ROOT / "sutra_ref_out").glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        value = (record.get("resolver") or {}).get("apavada_of")
        if not value:
            continue
        sid = record.get("id")
        generals = [v for v in (value if isinstance(value, list) else [value]) if v]
        if sid in SUTRA_REGISTRY and all(g in SUTRA_REGISTRY for g in generals):
            pairs[sid] = generals
    return pairs


def sutra_file(sutra_id: str) -> Path | None:
    hits = list((_ROOT / "sutras").rglob("sutra_" + sutra_id.replace(".", "_") + ".py"))
    return hits[0] if len(hits) == 1 else None


def declare(path: Path, generals: list[str]) -> str | None:
    """Insert `apavada_of=(...)` into the SutraRecord. None if already declared."""
    source = path.read_text(encoding="utf-8")
    if "apavada_of" in source:
        return None
    match = re.search(r"(\n(\s*))anuvritti_from\s*=", source)
    if not match:
        return None
    indent = match.group(2)
    ids = ", ".join(f'"{g}"' for g in generals)
    line = (f'\n{indent}apavada_of     = ({ids},),'
            f'   # अपवाद of {", ".join(generals)} — {PROVENANCE}')
    return source[: match.start()] + line + source[match.start():]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Seed the apavāda graph from the corpus.")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args(argv)

    pairs = declared_pairs()
    written = already = missing = 0
    for sid, generals in sorted(pairs.items())[: args.limit]:
        path = sutra_file(sid)
        if path is None:
            print(f"  gap: {sid} has no unique sūtra file")
            missing += 1
            continue
        updated = declare(path, generals)
        if updated is None:
            already += 1
            continue
        if args.apply:
            path.write_text(updated, encoding="utf-8")
        written += 1
        print(f"  {'wrote' if args.apply else 'would'} {sid:>9} अपवाद of {', '.join(generals)}")
    print(f"\n  {len(pairs)} pairs in the corpus · {written} declared · "
          f"{already} already · {missing} unresolvable"
          + ("" if args.apply else "   (dry run — pass --apply)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
