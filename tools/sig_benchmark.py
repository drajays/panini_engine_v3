#!/usr/bin/env python3
"""
tools/sig_benchmark.py — Run paradigm cells, collect SIG, write JSON.
───────────────────────────────────────────────────────────────────────

Usage:
    python -m tools.regenerate_sig_artifacts      # full sig/ — **preferred**
    python -m tools.sig_benchmark
    python -m tools.sig_benchmark --out sig/ --with-jayati
    python -m tools.sig_benchmark --subanta-corpus data/reference/subanta_gold/rama_pullinga.json
    python -m tools.sig_benchmark --freeze      # also refresh tests/.../sig_applied_paths_baseline.json

**Discovery (default):** recursively scans ``data/reference/`` (or
``--reference-root``) for any ``.json`` whose top-level object has either
``"cells"`` (subanta-style) or ``"recipe"`` (``module.path:callable``) or, for
the canonical *jayati* file, ``"steps"`` + ``"surface_target_slp1"`` so
future ``krdanta_gold/`` or ``taddhita_gold/`` drop-ins are included without
hardcoded folder names.

Modes:
    (default)  Collect SIG, diff vs existing sig/sig_baseline.json
               (if present), exit code 0 iff no CRITICAL anomalies.
    --freeze   Overwrite sig/sig_baseline.json with this run's timings.

This is the v3.1 answer to v2's benchmark.  We don't compare schedulers
(we have one scheduler); we compare THIS RUN to the LAST KNOWN GOOD run.
"""
from __future__ import annotations

import argparse
import importlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401 — trigger registry fill
from engine          import SIGCollector, SUTRA_REGISTRY, coverage_report
from engine.sig      import replay_subanta_trace
from pipelines.subanta import derive
from tools.gold_corpora import data_reference_root, list_reference_gold_jsons


def _ingest_subanta_cell(
    col: SIGCollector,
    cell_id: str,
    stem: str,
    v: int,
    vv: int,
    linga: str,
) -> None:
    """
    One subanta cell: use the real ``derive`` trace, then timed replay of the
    same *apply_rule* list so SKIPPED / BLOCKED rows still accrue wall time.
    """
    final = derive(stem, v, vv, linga=linga)
    per_step_times: dict = {}
    replayed = replay_subanta_trace(
        stem, v, vv, final.trace, linga=linga, per_step_times=per_step_times
    )
    if replayed.render() != final.render():
        raise RuntimeError(
            f"SIG replay diverged for {cell_id!r}: replay={replayed.render()!r} "
            f"derive={final.render()!r}"
        )
    col.ingest(
        cell_id, final.trace, per_step_timing_ns=per_step_times
    )


def _ingest_jayati_gold(col: SIGCollector) -> None:
    """
    Add the full *jayati* gold *tin*anta prakriyā (steps 1–9) so SIG edges
    include tripāḍī / *it* paths not exercised by *rāma* *subanta* alone.
    """
    from pipelines.tinanta_jayati_gold import run_jayati_gold_through_step

    s = run_jayati_gold_through_step(9)
    col.ingest("jayati:gold-1-9", s.trace)


def _ingest_samasa_dik_uttarapurva(col: SIGCollector) -> None:
    """*Dik* *samāsa* *uttarapūrvā* — compound + internal *luk* path (apply_rule)."""
    from pipelines.dik_uttarapurva_demo import caturthi_preset, derive_dik_caturthi_compound

    s = derive_dik_caturthi_compound(
        caturthi_preset("uttarA_pUrvA"), verbose=False
    )
    col.ingest("samasa:dik_uttarapurva_compound", s.trace)


def _ingest_krdanta_pacaka(col: SIGCollector) -> None:
    """Kṛdanta scaffold: *qupac~z* + *Nvul* → ``pAcaka`` prātipadika."""
    from pipelines.krdanta import derive_pAcaka_pratipadika

    s = derive_pAcaka_pratipadika()
    col.ingest("krdanta:pAcaka_Nvul", s.trace)


def _is_jayati_tinanta_shape(gpath: Path, d: Dict[str, Any]) -> bool:
    """*Jayati* gold in-repo is a single file; we key off *id* / name."""
    st = (gpath.stem or "").lower()
    if "jayati" in st:
        return True
    gid = d.get("id", "")
    return isinstance(gid, str) and "jayati" in gid.lower()


def _ingest_tinanta_jayati_synthetic(col: SIGCollector, gpath: Path) -> None:
    from pipelines.tinanta_jayati_gold import run_jayati_gold_through_step

    s = run_jayati_gold_through_step(9)
    if gpath.name == "jayati_prakriya.json":
        cell = "jayati:gold-1-9"
    else:
        try:
            rel = gpath.relative_to(data_reference_root()).as_posix()
        except ValueError:
            rel = gpath.as_posix()
        cell = f"{rel}:jayati-1-9"
    col.ingest(cell, s.trace)


def _call_top_level_recipe(
    recipe: str, recipe_args: Optional[List[Any]],
) -> Any:
    """
    *recipe* = ``"module_name.submodule:function_name"`` (single ``:`` split
    for attribute resolution on the imported module if needed, or
    ``module:attr`` for one function at module top level only).

    This repo’s convention: ``"pipelines.foo:bar"`` (no nested attributes in
    *function_name* for simplicity).
    """
    if ":" not in recipe:
        raise ValueError(f"recipe {recipe!r} must look like 'module:callable'")
    mod_name, fn_name = recipe.rsplit(":", 1)
    m = importlib.import_module(mod_name)
    fn = getattr(m, fn_name)
    if recipe_args is None:
        return fn()
    return fn(*tuple(recipe_args))


def _ingest_recipe_json(
    col: SIGCollector,
    gpath: Path,
    d: Dict[str, Any],
) -> str:
    raw = d["recipe"]
    if not isinstance(raw, str):
        raise TypeError(
            f"{gpath}: top-level 'recipe' must be a string, got {type(raw).__name__}. "
        )
    args: Optional[List[Any]] = None
    if "recipe_args" in d:
        ra = d["recipe_args"]
        if not isinstance(ra, list):
            raise TypeError(f"{gpath}: 'recipe_args' must be a JSON list")
        args = ra
    s = _call_top_level_recipe(raw, args)
    trace = getattr(s, "trace", None)
    if trace is None:
        raise TypeError(
            f"{gpath}: recipe {raw!r} did not return an object with .trace (got {s!r})."
        )
    rid = d.get("id", gpath.stem)
    cell = f"{gpath.parent.name}/{gpath.stem}:recipe:{rid}" if gpath.parent else f"{gpath.stem}:recipe:{rid}"
    col.ingest(cell, trace)
    return raw


def _process_gold_file(
    col: SIGCollector,
    gpath: Path,
) -> tuple[Optional[Dict[str, Any]], bool]:
    """
    Ingest a single *gold* file if it matches a known pattern.

    Returns
    -------
    (corpus_record, canonical_jayati_ingested)
        *corpus_record* is *None* when the file is skipped.  The boolean is
        True iff ``jayati_prakriya.json`` was run as the tinānta driver, so
        ``--with-jayati`` can be deduplicated.
    """
    try:
        raw = gpath.read_text(encoding="utf-8")
    except OSError as ex:  # pragma: no cover — defensive
        print(f"skip {gpath} (read error: {ex})", file=sys.stderr)
        return None, False
    try:
        gold = json.loads(raw)
    except json.JSONDecodeError as ex:
        print(f"skip {gpath} (invalid JSON: {ex})", file=sys.stderr)
        return None, False
    if not isinstance(gold, dict):
        print(f"skip {gpath} (root must be a JSON object)", file=sys.stderr)
        return None, False

    rel: str
    try:
        rel = gpath.relative_to(_ROOT).as_posix()
    except ValueError:  # pragma: no cover
        rel = gpath.as_posix()

    if isinstance(gold.get("recipe"), str):
        recipe_str = _ingest_recipe_json(col, gpath, gold)
        return {
            "id"    : f"recipe:{gpath.stem}",
            "file"  : rel,
            "cells" : 1,
            "recipe": recipe_str
            + (f"  args={gold['recipe_args']!r}" if "recipe_args" in gold else ""),
        }, False
    if "cells" in gold and "stem_slp1" in gold:
        stem = gold["stem_slp1"]
        linga = gold.get("linga", "pulliṅga")
        n_cells = 0
        for key in gold["cells"]:
            v, vv = (int(x) for x in str(key).split("-"))
            cell_id = f"{gpath.stem}:{stem}:{key}"
            _ingest_subanta_cell(col, cell_id, stem, v, vv, linga)
            n_cells += 1
        return {
            "id"   : f"subanta:{gpath.parent.name}/{gpath.stem}",
            "file" : rel,
            "cells": n_cells,
            "recipe": "pipelines.subanta.derive + engine.sig.replay_subanta_trace (timed)",
        }, False
    if "steps" in gold and "surface_target_slp1" in gold:
        if not _is_jayati_tinanta_shape(gpath, gold):
            print(
                f"skip {gpath} (has steps + surface — add top-level 'recipe' "
                "for a non-jayati tinānta driver)",
                file=sys.stderr,
            )
            return None, False
        _ingest_tinanta_jayati_synthetic(col, gpath)
        return {
            "id"    : f"tinanta:{gpath.parent.name}/{gpath.stem}_jayati",
            "file"  : rel,
            "cells" : 1,
            "recipe": "pipelines.tinanta_jayati_gold.run_jayati_gold_through_step(9)",
        }, gpath.name == "jayati_prakriya.json"
    return None, False


def _write_sig_manifest(
    out_dir: Path,
    col: SIGCollector,
    cov: Dict[str, Any],
    corpora: List[Dict[str, Any]],
    file_names: List[str],
) -> None:
    """Index file so `sig/` is self-describing in CI and clones."""
    payload = {
        "generated_utc"    : datetime.now(timezone.utc).isoformat(),
        "generator"        : "panini_engine_v3.tools.sig_benchmark",
        "total_derivations": col.test_count,
        "sutra_coverage"   : {
            "implemented"   : cov.get("implemented"),
            "total_registry": cov.get("total"),
            "coverage_pct"  : cov.get("coverage_pct"),
        },
        "corpora"          : corpora,
        "artifacts"        : sorted(file_names),
    }
    p = out_dir / "sig_manifest.json"
    p.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=_ROOT / "sig",
                    help="output directory for SIG JSON files")
    ap.add_argument("--freeze", action="store_true",
                    help="overwrite sig_baseline.json with this run's timings")
    ap.add_argument(
        "--reference-root",
        type=Path,
        default=data_reference_root(),
        help="root for recursive gold JSON discovery (default: data/reference/)",
    )
    ap.add_argument(
        "--subanta-dir",
        type=Path,
        default=None,
        help="if set, restrict *recursive* JSON discovery to this directory only",
    )
    ap.add_argument(
        "--subanta-corpus",
        type=Path,
        default=None,
        help="single gold file; if set, do not scan a directory (subanta, recipe, or jayati JSON)",
    )
    ap.add_argument(
        "--with-jayati",
        action="store_true",
        help="also ingest tinanta *jayati* gold (run_jayati_gold_through_step(9)) "
             "when it was not already ingested from the reference scan; "
             "redundant with a full data/reference/ scan of jayati_prakriya.json",
    )
    ap.add_argument(
        "--with-samasa-demo",
        action="store_true",
        help="ingest *dik* *uttarapūrvā* *samāsa* compound (derive_dik_caturthi_compound).",
    )
    ap.add_argument(
        "--with-krdanta-pacaka",
        action="store_true",
        help="ingest *pAcaka* kṛdanta (derive_pAcaka_pratipadika).",
    )
    args = ap.parse_args(argv)

    # Load prior baseline (if any).
    prior_baseline_path = args.out / "sig_baseline.json"
    prior_baseline = None
    if prior_baseline_path.exists() and not args.freeze:
        prior_baseline = json.loads(
            prior_baseline_path.read_text(encoding="utf-8")
        )

    col = SIGCollector()
    corpora: List[Dict[str, Any]] = []

    if args.subanta_corpus is not None:
        gfile = args.subanta_corpus.resolve()
        if not gfile.is_file():
            print(f"not a file: {gfile}", file=sys.stderr)
            return 2
        rec, jn = _process_gold_file(col, gfile)
        if rec is None:
            print(
                f"{gfile} is not a recognized gold file — need top-level 'recipe' (str), "
                "or subanta 'cells' + 'stem_slp1', or jayati *steps* + *surface* "
                "(id/path contains 'jayati', or see tools/sig_benchmark header).",
                file=sys.stderr,
            )
            return 2
        corpora.append(rec)
        canonical_jayati_done = jn
    else:
        scan_root = (args.subanta_dir or args.reference_root).resolve()
        if not scan_root.is_dir():
            print(f"not a directory: {scan_root}", file=sys.stderr)
            return 2
        gold_paths = list_reference_gold_jsons(scan_root)
        if not gold_paths:
            print(f"no .json under {scan_root}", file=sys.stderr)
            return 2
        canonical_jayati_done = False
        n_recognized = 0
        for gpath in gold_paths:
            rec, jn = _process_gold_file(col, gpath)
            if jn:
                canonical_jayati_done = True
            if rec is not None:
                n_recognized += 1
                corpora.append(rec)
        if n_recognized == 0:
            print(
                f"no gold JSONs matched (under {scan_root}): expected "
                "'cells' + 'stem_slp1' (subanta), or 'recipe' (str), or "
                "tinānta 'steps' + 'surface' with a jayati *id* / filename hint.",
                file=sys.stderr,
            )
            return 2

    if args.with_jayati and not canonical_jayati_done:
        _ingest_jayati_gold(col)
        corpora.append(
            {
                "id"   : "tinanta:jayati_gold",
                "cells": 1,
                "recipe": "pipelines.tinanta_jayati_gold.run_jayati_gold_through_step(9)",
            }
        )

    if args.with_samasa_demo:
        _ingest_samasa_dik_uttarapurva(col)
        corpora.append(
            {
                "id"    : "samasa:dik_uttarapurva",
                "cells" : 1,
                "recipe": "pipelines.dik_uttarapurva_demo.derive_dik_caturthi_compound",
            }
        )
    if args.with_krdanta_pacaka:
        _ingest_krdanta_pacaka(col)
        corpora.append(
            {
                "id"    : "krdanta:pAcaka",
                "cells" : 1,
                "recipe": "pipelines.krdanta.derive_pAcaka_pratipadika",
            }
        )

    # Dump all nine JSON files.
    files = col.dump_all(args.out, prior_baseline=prior_baseline)

    # Dump coverage.json too.
    cov = coverage_report(SUTRA_REGISTRY)
    (args.out / "coverage.json").write_text(
        json.dumps(cov, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    files["coverage.json"] = args.out / "coverage.json"

    manifest_names = sorted(list(files.keys()) + ["sig_manifest.json"])
    _write_sig_manifest(args.out, col, cov, corpora, manifest_names)
    files["sig_manifest.json"] = args.out / "sig_manifest.json"

    # On --freeze, also write the applied-paths baseline that
    # tests/regression/test_sig_baseline.py reads.  This is what makes
    # SIG into a true truth-teller: surface-correct but path-changed
    # is a caught regression.
    #
    # We use pipelines.subanta.derive (the REAL pipeline) here rather
    # than _derive_with_timing + _RECIPE so the baseline matches what
    # the test module actually invokes.  They would otherwise drift.
    if args.freeze:
        from engine.sig       import extract_applied_path
        from pipelines.subanta import derive as real_derive
        applied_paths = {}
        for v in range(1, 9):
            for vv in range(1, 4):
                cell = f"{v}-{vv}"
                state = real_derive("rAma", v, vv)
                applied_paths[cell] = {
                    "applied_path": extract_applied_path(state.trace),
                }
        baseline_path = (_ROOT / "tests" / "regression" /
                         "sig_applied_paths_baseline.json")
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline_path.write_text(
            json.dumps(applied_paths, ensure_ascii=False,
                       indent=2, sort_keys=True),
            encoding="utf-8",
        )
        print(f"  ✓ applied-paths baseline frozen at {baseline_path}")

    # Exit-code policy: fail on CRITICAL anomalies (regression oracle).
    anomalies = json.loads(
        (args.out / "sig_anomalies.json").read_text(encoding="utf-8")
    )
    critical = [a for a in anomalies.get("anomalies", [])
                if a.get("severity") == "CRITICAL"]

    print(f"\n{'═' * 60}")
    print(f"  SIG benchmark complete  ({col.test_count} derivations)")
    print(f"{'═' * 60}")
    print(f"  Wrote {len(files)} files to {args.out}/")
    for name in sorted(files):
        print(f"    {name}")
    print(f"\n  Coverage      : {cov['implemented']}/{cov['total']} "
          f"({cov['coverage_pct']}%)")
    print(f"  Anomalies     : {len(anomalies.get('anomalies', []))}"
          f" ({len(critical)} CRITICAL)")
    if args.freeze:
        print(f"\n  ✓ baseline frozen at {prior_baseline_path}")
        return 0
    if critical:
        print("\n  ✗ CRITICAL regressions vs baseline — see sig_anomalies.json")
        return 2
    print("\n  ✓ no critical regressions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
