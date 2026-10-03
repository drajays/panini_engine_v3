"""
tools/loop_vs_recipe.py — the strangler's gauge (plan: "subanta lists → resolver").

For each derivation class the recipe stays the oracle until the rule-driven path agrees with it on a
whole grid; only then is the default flipped, the pins regenerated, and the recipe deleted. Disagreement is
a ranked work item — almost always a rule that is missing or wrongly scoped — never a reason to edit a
pipeline. Nothing here changes the engine.

    python3 -m tools.loop_vs_recipe subanta [--limit N]      # 24 cells × every stem in the lexicon
    python3 -m tools.loop_vs_recipe tinanta [--limit N]      # laṭ kartari 9 cells × bhvādi roots
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

OUT = ROOT / "sig" / "loop_vs_recipe.json"


def _applied(state) -> list[str]:
    return [t["sutra_id"] for t in state.trace
            if t.get("status") == "APPLIED" and t.get("form_before") != t.get("form_after")]


def _first_divergence(a: list[str], b: list[str]) -> tuple[str | None, str | None]:
    i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
    return (a[i] if i < len(a) else None, b[i] if i < len(b) else None)


def subanta(limit: int | None) -> dict:
    import sutras  # noqa: F401
    from pipelines.subanta import derive
    from tools.build_form_index import stem_lexicon

    stems = stem_lexicon()[:limit] if limit else stem_lexicon()
    cells = agree = 0
    clusters: collections.Counter = collections.Counter()
    examples: dict = {}
    errors: collections.Counter = collections.Counter()
    for stem, linga in stems:
        for vibhakti in range(1, 9):
            for vacana in range(1, 4):
                cells += 1
                try:
                    a = derive(stem, vibhakti, vacana, linga=linga, autonomous_scanner=False)
                    b = derive(stem, vibhakti, vacana, linga=linga, autonomous_scanner=True)
                except Exception as ex:
                    errors[type(ex).__name__] += 1
                    continue
                if a.flat_slp1() == b.flat_slp1():
                    agree += 1
                    continue
                key = "→".join(str(x) for x in _first_divergence(_applied(a), _applied(b)))
                clusters[key] += 1
                examples.setdefault(key, {"stem": stem, "cell": f"{vibhakti}-{vacana}", "linga": linga,
                                          "recipe": a.flat_slp1(), "loop": b.flat_slp1()})
    return {"class": "subanta", "stems": len(stems), "cells": cells, "agree": agree,
            "errors": dict(errors),
            "clusters": [{"first_divergence": k, "count": n, **examples[k]} for k, n in clusters.most_common()]}


def tinanta(limit: int | None, lakara: str = "laT") -> dict:
    import sutras  # noqa: F401
    from types import SimpleNamespace as NS

    from pipelines.dhatupatha import iter_dhatu_entries
    from pipelines.tinanta import derive
    from tools.autonomy_report import run_autonomously, start_state

    roots = [r["upadesha_slp1"] for r in iter_dhatu_entries() if r.get("gana") == 1]
    roots = roots[:limit] if limit else roots
    cells = agree = 0
    clusters: collections.Counter = collections.Counter()
    examples: dict = {}
    for root in roots:
        for purusha in (1, 2, 3):
            for vacana in (1, 2, 3):
                try:
                    expect = derive(root, lakara, "kartari", purusha, vacana).flat_slp1()
                except Exception:
                    continue
                cells += 1
                try:
                    run = run_autonomously(start_state(NS(kind="tinanta", args=(root, lakara, purusha, vacana))),
                                           expect, root, 120)
                except Exception as ex:
                    clusters[type(ex).__name__] += 1
                    continue
                if run.outcome == "reached":
                    agree += 1
                else:
                    clusters[root] += 1
                    examples.setdefault(root, {"cell": f"{purusha}-{vacana}", "recipe": expect, "loop": run.surface})
    return {"class": f"tinanta({lakara} kartari, gaṇa 1)", "roots": len(roots), "cells": cells, "agree": agree,
            "clusters": [{"first_divergence": k, "count": n, **examples.get(k, {})} for k, n in clusters.most_common()]}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("kind", choices=["subanta", "tinanta"])
    ap.add_argument("--limit", type=int)
    ap.add_argument("--lakara", default="laT")
    args = ap.parse_args(argv)
    t0 = time.time()
    report = subanta(args.limit) if args.kind == "subanta" else tinanta(args.limit, args.lakara)
    report["seconds"] = round(time.time() - t0)
    book = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    book[args.kind if args.kind == "subanta" or args.lakara == "laT" else f"tinanta:{args.lakara}"] = report
    OUT.write_text(json.dumps(book, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{report['class']}: {report['agree']}/{report['cells']} cells agree ({report['seconds']}s)")
    for c in report["clusters"][:15]:
        print(f"  {c['count']:>4}  {c['first_divergence']:<22} e.g. {c.get('stem', '')} {c.get('cell', '')}: "
              f"recipe {c.get('recipe')} · loop {c.get('loop')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
