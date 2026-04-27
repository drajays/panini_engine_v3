"""
tools/dump_pipelines_trace.py
─────────────────────────────

Discover ``derive_*`` entry points under ``pipelines/*.py``, invoke each with
safe smoke arguments (introspection + small heuristics), and emit a JSON
snapshot suitable for offline diff / issue triage.

Usage (repo root)::

    python3 -m tools.dump_pipelines_trace -o /tmp/pipeline_traces.json
    python3 -m tools.dump_pipelines_trace --format jsonl -o traces.jsonl
    python3 -m tools.dump_pipelines_trace --dry-run
    python3 -m tools.dump_pipelines_trace --only sarva
    python3 -m tools.dump_pipelines_trace --include-subanta-smoke

This is a **tool** only (CONSTITUTION: no ``data/reference`` in engine ``cond``).
"""
from __future__ import annotations

import argparse
import importlib
import inspect
import json
import pkgutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Callable, Iterable

# Repo root on sys.path
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# Do not import ``pipelines`` package until after path fix (subpackages).


# Internal / duplicate / parameterised helpers — covered by other exports.
_SKIP_NAMES: frozenset[str] = frozenset(
    {
        "derive_demo",
        "derive_kumAri_taddhita_core",
        "derive_uttarapurva_from_vigraha",
    }
)


def _state_snapshot(s: Any) -> dict[str, Any]:
    from engine.state import State

    if not isinstance(s, State):
        return {"error": f"expected State, got {type(s).__name__}"}
    return {
        "final_flat_slp1": s.flat_slp1(),
        "phase": getattr(s, "phase", None),
        "tripadi_zone": getattr(s, "tripadi_zone", None),
        "trace_len": len(s.trace),
        "trace": list(s.trace),
    }


def _dik_default_preset() -> Any:
    from pipelines.dik_uttarapurva_demo import caturthi_preset

    return caturthi_preset("uttarA_pUrvA")


def _infer_bind(
    fn: Callable[..., Any],
    *,
    module_name: str,
    qualname: str,
) -> tuple[tuple[Any, ...], dict[str, Any], str] | None:
    """
    Return (args, kwargs, note) for a smoke invocation, or None if unsupported.
    ``note`` documents heuristics (empty if plain defaults-only).
    """
    notes: list[str] = []
    try:
        sig = inspect.signature(fn)
    except (TypeError, ValueError):
        return None

    params = list(sig.parameters.values())
    pos: list[Any] = []
    kw: dict[str, Any] = {}

    # First pass: every parameter satisfiable without smoke heuristics?
    # (Use ``bind``, not ``bind_partial``: 3.13+ ``bind_partial()`` can omit
    # required positionals until call-time, which would yield invalid invocations.)
    try:
        b = sig.bind()
        b.apply_defaults()
        if module_name == "pipelines.dik_uttarapurva_demo" and "verbose" in b.arguments:
            b.arguments["verbose"] = False
            notes.append("verbose=False for dik_uttarapurva_demo")
        return tuple(), dict(b.arguments), ("; ".join(notes) if notes else "")
    except TypeError:
        pass

    for p in params:
        if p.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            continue
        if p.default is not inspect.Parameter.empty:
            continue

        name = p.name
        if p.kind == inspect.Parameter.POSITIONAL_ONLY:
            kind = "positional_only"
        elif p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            kind = "positional_or_keyword"
        else:
            kind = "keyword_only"

        if name == "dhatu_upadesha_slp1":
            v = "ciY" if "tfc" in qualname.lower() else "qupac~z"
            if kind == "keyword_only":
                kw[name] = v
            else:
                pos.append(v)
            notes.append(f"{name}={v!r} (smoke)")
        elif name == "dhatu_id":
            pos.append("BvAdi_ciY")
            notes.append("dhatu_id=BvAdi_ciY (smoke)")
        elif name == "stem_slp1":
            v = "cetf" if qualname == "derive_trc_nom_sg" else "hari" if "ikarant" in qualname else "rAma"
            if kind == "keyword_only":
                kw[name] = v
            else:
                pos.append(v)
            notes.append(f"stem_slp1={v!r} (smoke)")
        elif name == "vibhakti":
            vv = 3 if "aabhyam" in module_name or "idam_dvibhi" in qualname else 1
            if kind == "keyword_only":
                kw[name] = vv
            else:
                pos.append(vv)
            notes.append(f"vibhakti={vv} (smoke)")
        elif name == "vacana":
            if kind == "keyword_only":
                kw[name] = 1
            else:
                pos.append(1)
        elif name == "p":
            preset = _dik_default_preset()
            if kind == "keyword_only":
                kw[name] = preset
            else:
                pos.append(preset)
            notes.append("p=caturthi_preset('uttarA_pUrvA')")
        elif name == "case":
            return None
        else:
            return None

    try:
        b = sig.bind(*pos, **kw)
        b.apply_defaults()
        if module_name == "pipelines.dik_uttarapurva_demo" and "verbose" in b.arguments:
            b.arguments["verbose"] = False
            notes.append("verbose=False for dik_uttarapurva_demo")
        final_kw = dict(b.arguments)
        return tuple(), final_kw, ("; ".join(notes) if notes else "")
    except TypeError:
        return None


def _iter_pipeline_modules() -> Iterable[str]:
    import pipelines as pipelines_pkg

    for m in pkgutil.iter_modules(pipelines_pkg.__path__, pipelines_pkg.__name__ + "."):
        if m.ispkg:
            continue
        if m.name.endswith(".__init__"):
            continue
        yield m.name


def _discover_derive_callables(mod: ModuleType) -> list[tuple[str, Callable[..., Any]]]:
    out: list[tuple[str, Callable[..., Any]]] = []
    for name, obj in inspect.getmembers(mod):
        if not name.startswith("derive_"):
            continue
        if name in _SKIP_NAMES:
            continue
        if not callable(obj):
            continue
        out.append((name, obj))
    out.sort(key=lambda x: x[0])
    return out


def _run_one(
    module_name: str,
    fn_name: str,
    fn: Callable[..., Any],
) -> dict[str, Any]:
    inferred = _infer_bind(fn, module_name=module_name, qualname=fn_name)
    if inferred is None:
        return {
            "module": module_name,
            "callable": fn_name,
            "ok": False,
            "skip": True,
            "reason": "could not infer smoke arguments from signature",
        }
    _args, kwargs, note = inferred
    sig = inspect.signature(fn)
    bound = None
    try:
        bound = sig.bind(*_args, **kwargs)
        bound.apply_defaults()
        result = fn(*bound.args, **bound.kwargs)
    except Exception as exc:  # noqa: BLE001 — tool boundary
        inv = {"args": list(_args), "kwargs": dict(kwargs)}
        if bound is not None:
            inv = {"args": list(bound.args), "kwargs": dict(bound.kwargs)}
        return {
            "module": module_name,
            "callable": fn_name,
            "ok": False,
            "skip": False,
            "smoke_note": note or None,
            "invocation": inv,
            "error": f"{type(exc).__name__}: {exc}",
        }

    if isinstance(result, tuple):
        segs = []
        labels = ("segment_0", "segment_1", "segment_2")
        for i, st in enumerate(result):
            segs.append(
                {
                    "label": labels[i] if i < len(labels) else f"segment_{i}",
                    **_state_snapshot(st),
                }
            )
        return {
            "module": module_name,
            "callable": fn_name,
            "ok": True,
            "smoke_note": note or None,
            "invocation": {"args": list(bound.args), "kwargs": dict(bound.kwargs)},
            "result_kind": "tuple_of_states",
            "segments": segs,
        }

    return {
        "module": module_name,
        "callable": fn_name,
        "ok": True,
        "smoke_note": note or None,
        "invocation": {"args": list(bound.args), "kwargs": dict(bound.kwargs)},
        "result_kind": "state",
        **_state_snapshot(result),
    }


@dataclass
class RunManifest:
    generated_at: str
    python: str
    records: list[dict[str, Any]]
    import_errors: list[dict[str, str]]


def _gather(
    *,
    only_substring: str | None,
    dry_run: bool,
    include_subanta_smoke: bool,
) -> RunManifest:
    import sutras  # noqa: F401

    records: list[dict[str, Any]] = []
    import_errors: list[dict[str, str]] = []

    for module_name in sorted(_iter_pipeline_modules()):
        if only_substring is not None and only_substring not in module_name:
            continue
        try:
            mod = importlib.import_module(module_name)
        except Exception as exc:  # noqa: BLE001
            import_errors.append({"module": module_name, "error": f"{type(exc).__name__}: {exc}"})
            continue
        pairs = _discover_derive_callables(mod)
        for fn_name, fn in pairs:
            if dry_run:
                records.append(
                    {
                        "module": module_name,
                        "callable": fn_name,
                        "dry_run": True,
                    }
                )
                continue
            records.append(_run_one(module_name, fn_name, fn))

    if include_subanta_smoke and not dry_run:
        if only_substring is None or only_substring in "subanta":
            from pipelines.subanta import derive as derive_subanta

            try:
                s = derive_subanta("rAma", 1, 1, linga="pulliṅga")
                rec = {
                    "module": "pipelines.subanta",
                    "callable": "derive",
                    "ok": True,
                    "smoke_note": "explicit --include-subanta-smoke: rAma 1-1 pulliṅga",
                    "invocation": {
                        "args": [],
                        "kwargs": {
                            "stem_slp1": "rAma",
                            "vibhakti": 1,
                            "vacana": 1,
                            "linga": "pulliṅga",
                        },
                    },
                    "result_kind": "state",
                    **_state_snapshot(s),
                }
                records.append(rec)
            except Exception as exc:  # noqa: BLE001
                records.append(
                    {
                        "module": "pipelines.subanta",
                        "callable": "derive",
                        "ok": False,
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                )
    elif include_subanta_smoke and dry_run:
        records.append(
            {
                "module": "pipelines.subanta",
                "callable": "derive",
                "dry_run": True,
                "note": "--include-subanta-smoke",
            }
        )

    return RunManifest(
        generated_at=datetime.now(timezone.utc).isoformat(),
        python=sys.version.split()[0],
        records=records,
        import_errors=import_errors,
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Dump full trace snapshots for discoverable pipelines.derive_* entry points.",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        metavar="FILE",
        help="Write JSON or JSONL here (default: stdout).",
    )
    ap.add_argument(
        "--format",
        choices=("json", "jsonl"),
        default="json",
        help="json: single manifest object; jsonl: one JSON object per derive_* (and errors).",
    )
    ap.add_argument(
        "--only",
        metavar="SUBSTRING",
        help="Keep modules whose dotted name contains this substring (case-sensitive).",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="List module/callable pairs without executing.",
    )
    ap.add_argument(
        "--include-subanta-smoke",
        action="store_true",
        help="Append one explicit pipelines.subanta.derive('rAma',1,1) snapshot (bare derive is not auto-discovered).",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit with status 1 if any module failed to import or any derive_* raised.",
    )
    args = ap.parse_args(argv)

    manifest = _gather(
        only_substring=args.only,
        dry_run=args.dry_run,
        include_subanta_smoke=args.include_subanta_smoke,
    )

    out_fp = sys.stdout
    opened: Any = None
    if args.output is not None:
        opened = args.output.open("w", encoding="utf-8")
        out_fp = opened

    try:
        if args.format == "json":
            payload = {
                "generated_at": manifest.generated_at,
                "python": manifest.python,
                "import_errors": manifest.import_errors,
                "records": manifest.records,
            }
            json.dump(payload, out_fp, ensure_ascii=False, indent=2, default=str)
            out_fp.write("\n")
        else:
            header = {
                "kind": "manifest_header",
                "generated_at": manifest.generated_at,
                "python": manifest.python,
                "import_errors": manifest.import_errors,
            }
            out_fp.write(json.dumps(header, ensure_ascii=False, default=str) + "\n")
            for rec in manifest.records:
                out_fp.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
    finally:
        if opened is not None:
            opened.close()

    n_ok = sum(1 for r in manifest.records if r.get("ok"))
    n_bad = sum(1 for r in manifest.records if not r.get("ok") and not r.get("dry_run"))
    n_skip = sum(1 for r in manifest.records if r.get("skip"))
    print(
        f"[dump_pipelines_trace] records={len(manifest.records)} ok={n_ok} "
        f"errors={n_bad} skipped_infer={n_skip} import_errors={len(manifest.import_errors)}",
        file=sys.stderr,
    )
    fail = bool(manifest.import_errors) or n_bad > 0
    if args.strict and fail:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
