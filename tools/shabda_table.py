"""
tools/shabda_table.py — the śabda-rūpa table, with the prakriyā behind each cell.

The table a student reads (ashtadhyayi.com/shabda) and the derivation a scholar
audits are the same object seen from two distances. This prints the 8 × 3 grid
for a stem, marks every cell against the **attested** paradigm vendored in
``data/reference/shabda_gold/``, and will show the prakriyā for any cell you
name.

    python3 -m tools.shabda_table --list
    python3 -m tools.shabda_table rAma
    python3 -m tools.shabda_table rAma --cell 3-1      # the derivation of रामेण
    python3 -m tools.shabda_table --check              # every vendored paradigm

A cell is ``✓`` when our derivation matches the attested form, ``✗`` when it
does not, and ``—`` when the engine refuses. Nothing is smoothed over: the ✗
cells are the worklist.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

GOLD_DIR = _ROOT / "data" / "reference" / "shabda_gold"

VIBHAKTI_DEV = ("प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
                "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन")
VACANA_DEV = ("एकवचन", "द्विवचन", "बहुवचन")


def paradigms() -> dict[str, dict[str, Any]]:
    out = {}
    for path in sorted(GOLD_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        out[data["stem_slp1"]] = data
    return out


def derive_cell(stem: str, linga: str, vibhakti: int, vacana: int) -> tuple[str, str]:
    """(devanāgarī, error) for one cell."""
    import sutras  # noqa: F401
    from pipelines.subanta import derive

    try:
        state = derive(stem, vibhakti, vacana, linga=linga)
        return state.flat_dev(), ""
    except Exception as ex:
        return "", f"{type(ex).__name__}"


def table(stem: str) -> dict[str, Any]:
    data = paradigms()[stem]
    linga, rows, hits, misses, refused = data["linga"], [], 0, [], 0
    for vibhakti in range(1, 9):
        row = []
        for vacana in range(1, 4):
            key = f"{vibhakti}-{vacana}"
            attested = data["cells"].get(key, [])
            ours, error = derive_cell(stem, linga, vibhakti, vacana)
            if error or not ours:
                mark, refused = "—", refused + 1
            elif ours in attested:
                mark, hits = "✓", hits + 1
            else:
                mark = "✗"
                misses.append({"cell": key, "ours": ours, "attested": attested})
            row.append({"cell": key, "ours": ours or error, "attested": attested, "mark": mark})
        rows.append(row)
    return {"stem": stem, "word": data["word"], "linga": linga, "artha": data.get("artha", ""),
            "rows": rows, "hits": hits, "misses": misses, "refused": refused}


def print_table(result: dict[str, Any]) -> None:
    print(f"\n  {result['word']} ({result['stem']}) · {result['linga']}"
          + (f" · {result['artha']}" if result["artha"] else ""))
    print(f"  {'':<10}" + "".join(f"{v:<22}" for v in VACANA_DEV))
    for vibhakti, row in enumerate(result["rows"]):
        cells = "".join(f"{cell['mark']} {cell['ours'] or '—':<18}" for cell in row)
        print(f"  {VIBHAKTI_DEV[vibhakti]:<10}{cells}")
    total = result["hits"] + len(result["misses"]) + result["refused"]
    print(f"\n  {result['hits']}/{total} cells match the attested paradigm")
    for miss in result["misses"]:
        print(f"    ✗ {miss['cell']}  ours {miss['ours']}   attested {'/'.join(miss['attested'])}")


def show_cell(stem: str, cell: str) -> int:
    from core.trace_view import enrich_trace

    data = paradigms()[stem]
    vibhakti, vacana = (int(x) for x in cell.split("-"))
    attested = data["cells"].get(cell, [])
    import sutras  # noqa: F401
    from pipelines.subanta import derive

    state = derive(stem, vibhakti, vacana, linga=data["linga"])
    ours = state.flat_dev()
    print(f"\n  {data['word']} · {VIBHAKTI_DEV[vibhakti - 1]} {VACANA_DEV[vacana - 1]}")
    print(f"  attested: {'/'.join(attested)}")
    print(f"  {'─' * 72}")
    for n, step in enumerate(enrich_trace(state.trace), 1):
        if step.get("form_before") == step.get("form_after"):
            continue
        print(f"  {n:>3} → {step.get('sutra_id',''):<9} {step.get('form_before_dev','')} ⇒ "
              f"{step.get('form_after_dev','')}")
        if step.get("_sutra_text_dev"):
            print(f"        {step['_sutra_text_dev']}")
    print(f"  {'─' * 72}")
    print(f"  {'✓' if ours in attested else '✗'} {ours} ({state.flat_slp1()})")
    return 0 if ours in attested else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="śabda-rūpa table with its prakriyā.")
    ap.add_argument("stem", nargs="?")
    ap.add_argument("--cell", help="e.g. 3-1 for तृतीया एकवचन")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    known = paradigms()
    if args.list or (not args.stem and not args.check):
        for stem, data in known.items():
            print(f"  {stem:<8} {data['word']:<10} {data['linga']:<12} {data.get('artha','')}")
        return 0
    if args.check:
        worst = 0
        for stem in known:
            result = table(stem)
            total = result["hits"] + len(result["misses"]) + result["refused"]
            print(f"  {result['hits']:>2}/{total}  {stem:<8} {result['word']:<10}"
                  + ("" if not result["misses"] else
                     "  ✗ " + ", ".join(m["cell"] for m in result["misses"])))
            worst = max(worst, len(result["misses"]) + result["refused"])
        return 1 if worst else 0
    if args.stem not in known:
        print(f"no vendored paradigm for {args.stem!r} (try --list)")
        return 2
    if args.cell:
        return show_cell(args.stem, args.cell)
    print_table(table(args.stem))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
