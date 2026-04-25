#!/usr/bin/env python3
"""
Export ``global_sutra_edges.json`` (or any { edges: [{source,target,weight}] })
to Mermaid or Graphviz ``.dot`` for visualization.

  python3 -m tools.sig_graph_export --format mermaid --out sig/journey.mmd
  python3 -m tools.sig_graph_export --format dot --out sig/journey.dot
  python3 -m tools.sig_graph_export --format mermaid --top 60   # print to stdout
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


def load_edges(path: Path) -> List[Dict[str, Any]]:
    d = json.loads(path.read_text(encoding="utf-8"))
    return list(d.get("edges") or [])


def top_edges(
    edges: List[Dict[str, Any]], *, n: int | None = None
) -> List[Dict[str, Any]]:
    out = sorted(
        edges,
        key=lambda e: (-int(e.get("weight", 0)), e.get("source", ""), e.get("target", "")),
    )
    return out if n is None or n <= 0 else out[:n]


def edges_to_mermaid(
    edges: List[Dict[str, Any]],
    *,
    direction: str = "LR",
    top_n: int | None = 80,
) -> str:
    """Mermaid *flowchart*; quote ids so dots in sūtra names are safe."""
    use = top_edges(edges, n=top_n)
    lines = [f"flowchart {direction}"]
    seen: set[Tuple[str, str]] = set()
    for e in use:
        s = str(e.get("source", "")).replace('"', "'")
        t = str(e.get("target", "")).replace('"', "'")
        w = int(e.get("weight", 0))
        key = (s, t)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f'  "{s}" -->|"{w}"| "{t}"')
    return "\n".join(lines) + "\n"


def edges_to_dot(
    edges: List[Dict[str, Any]],
    *,
    graph_id: str = "sutra_chrono",
    top_n: int | None = 80,
) -> str:
    use = top_edges(edges, n=top_n)
    lines = [
        f'digraph {graph_id} {{',
        '  rankdir=LR; node [fontname="Helvetica", fontsize=10]; edge [fontsize=8];',
    ]
    for e in use:
        s = str(e.get("source", "")).replace("\\", "\\\\").replace('"', '\\"')
        t = str(e.get("target", "")).replace("\\", "\\\\").replace('"', '\\"')
        w = int(e.get("weight", 0))
        lines.append(f'  "{s}" -> "{t}" [label="{w}"];')
    lines.append("}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--in",
        dest="in_path",
        type=Path,
        default=_ROOT / "sig" / "global_sutra_edges.json",
        help="input JSON (default: sig/global_sutra_edges.json)",
    )
    p.add_argument(
        "--out", type=Path, default=None,
        help="output file (default: print to stdout)",
    )
    p.add_argument(
        "--format", choices=("mermaid", "dot"), default="mermaid",
    )
    p.add_argument(
        "--top", type=int, default=80,
        help="limit to the N heaviest edges (0 = all)",
    )
    p.add_argument(
        "--direction", default="LR",
        help="Mermaid only: flowchart direction (LR, TB, ...)",
    )
    args = p.parse_args(argv)

    edges = load_edges(args.in_path)
    n = None if args.top == 0 else args.top
    if args.format == "mermaid":
        text = edges_to_mermaid(edges, top_n=n, direction=args.direction)
    else:
        text = edges_to_dot(edges, top_n=n)

    if args.out is None:
        print(text, end="")
    else:
        args.out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
