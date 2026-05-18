#!/usr/bin/env python3
"""
Extract stable applied-path sūtra sequence groups from SIG artifacts.

This is intentionally tooling/test infrastructure. Runtime derivation must not
consult these locks; pipelines remain rule schedulers that call ``apply_rule``.
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

_DEFAULT_SIG_DIR = _ROOT / "sig"
_DEFAULT_OUT = _ROOT / "tests" / "regression" / "sig_sequence_groups_baseline.json"


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _subanta_gold_files(manifest: dict[str, Any]) -> list[str]:
    files: list[str] = []
    for corpus in manifest.get("corpora", []):
        recipe = str(corpus.get("recipe", ""))
        file_name = corpus.get("file")
        if recipe.startswith("pipelines.subanta.derive") and isinstance(file_name, str):
            files.append(file_name)
    return sorted(dict.fromkeys(files))


def _chain_high_confidence_edges(
    transitions: dict[str, Any],
    *,
    min_probability: float,
    min_count: int,
    min_length: int,
) -> list[dict[str, Any]]:
    edges = []
    for edge in transitions.get("high_confidence", []):
        probability = float(edge.get("probability", 0.0))
        count = int(edge.get("count", 0))
        src = str(edge.get("from", ""))
        dst = str(edge.get("to", ""))
        if src and dst and probability >= min_probability and count >= min_count:
            edges.append((src, dst, count, probability))

    by_src: dict[str, tuple[str, int, float]] = {}
    incoming: dict[str, set[str]] = {}
    for src, dst, count, probability in edges:
        if src in by_src:
            # A branching source is not a lockable linear group.
            by_src.pop(src, None)
            continue
        by_src[src] = (dst, count, probability)
        incoming.setdefault(dst, set()).add(src)

    starts = sorted(src for src in by_src if src not in incoming)
    groups: list[dict[str, Any]] = []
    seen_edges: set[tuple[str, str]] = set()
    for start in starts:
        sequence = [start]
        counts: list[int] = []
        probabilities: list[float] = []
        current = start
        local_seen: set[str] = set()

        while current in by_src and current not in local_seen:
            local_seen.add(current)
            dst, count, probability = by_src[current]
            edge_key = (current, dst)
            if edge_key in seen_edges:
                break
            seen_edges.add(edge_key)
            sequence.append(dst)
            counts.append(count)
            probabilities.append(probability)
            current = dst

        if len(sequence) >= min_length:
            groups.append(
                {
                    "sequence": sequence,
                    "edge_count_min": min(counts),
                    "probability_min": min(probabilities),
                }
            )

    groups.sort(key=lambda g: (-len(g["sequence"]), g["sequence"][0]))
    return groups


def build_sequence_group_baseline(
    sig_dir: Path = _DEFAULT_SIG_DIR,
    *,
    min_probability: float = 1.0,
    min_count: int | None = None,
    min_length: int = 3,
) -> dict[str, Any]:
    """Build a committed regression baseline from generated SIG JSON."""
    manifest = _load_json(sig_dir / "sig_manifest.json")
    transitions = _load_json(sig_dir / "sig_transitions.json")
    total_derivations = int(manifest.get("total_derivations", 0))
    required_count = total_derivations if min_count is None else min_count
    raw_groups = _chain_high_confidence_edges(
        transitions,
        min_probability=min_probability,
        min_count=required_count,
        min_length=min_length,
    )

    groups = []
    for idx, group in enumerate(raw_groups, start=1):
        sequence = group["sequence"]
        group_id = f"common_applied_spine_{idx:03d}"
        if sequence[:2] == ["1.1.2", "1.1.7"]:
            group_id = "subanta_common_opening_applied_spine"
        groups.append(
            {
                "id": group_id,
                "description": (
                    "Deterministic applied-only sūtra spine extracted from SIG "
                    "high-confidence transitions."
                ),
                "layer": "applied_only",
                "sequence": sequence,
                "edge_count_min": group["edge_count_min"],
                "probability_min": group["probability_min"],
                "applies_to": {
                    "kind": "subanta_gold_manifest",
                    "files": _subanta_gold_files(manifest),
                },
            }
        )

    return {
        "schema_version": 1,
        "source": {
            "sig_dir": sig_dir.relative_to(_ROOT).as_posix()
            if sig_dir.is_relative_to(_ROOT)
            else sig_dir.as_posix(),
            "manifest_generated_utc": manifest.get("generated_utc"),
            "total_derivations": total_derivations,
            "transition_file": "sig_transitions.json",
        },
        "extraction_policy": {
            "layer": "applied_only",
            "min_probability": min_probability,
            "min_count": required_count,
            "min_length": min_length,
        },
        "groups": groups,
    }


def write_sequence_group_baseline(
    out_path: Path = _DEFAULT_OUT,
    *,
    sig_dir: Path = _DEFAULT_SIG_DIR,
    min_probability: float = 1.0,
    min_count: int | None = None,
    min_length: int = 3,
) -> dict[str, Any]:
    payload = build_sequence_group_baseline(
        sig_dir,
        min_probability=min_probability,
        min_count=min_count,
        min_length=min_length,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return payload


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sig-dir", type=Path, default=_DEFAULT_SIG_DIR)
    ap.add_argument("--out", type=Path, default=_DEFAULT_OUT)
    ap.add_argument("--min-probability", type=float, default=1.0)
    ap.add_argument("--min-count", type=int, default=None)
    ap.add_argument("--min-length", type=int, default=3)
    args = ap.parse_args(argv)

    payload = write_sequence_group_baseline(
        args.out,
        sig_dir=args.sig_dir,
        min_probability=args.min_probability,
        min_count=args.min_count,
        min_length=args.min_length,
    )
    print(f"wrote {len(payload['groups'])} sequence group(s) to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
