"""
tools/build_pages.py — build the static GitHub Pages payload.

    python3 -m tools.build_pages          # writes docs/data/

Runs the pipeline trace dumper, then splits the single (~9 MB) snapshot into
one small ``index.json`` plus one file per derivation, so the static viewer
fetches only what the reader clicks.
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

from tools.dump_pipelines_trace import main as dump_main

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "data"


def slug(rec: dict) -> str:
    raw = f"{rec['module'].removeprefix('pipelines.')}.{rec['callable']}"
    return re.sub(r"[^A-Za-z0-9._-]", "_", raw)


def build() -> int:
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as fp:
        tmp = Path(fp.name)
    if dump_main(["-o", str(tmp)]) != 0:
        return 1
    payload = json.loads(tmp.read_text())
    tmp.unlink()

    traces = OUT / "traces"
    traces.mkdir(parents=True, exist_ok=True)
    for stale in traces.glob("*.json"):
        stale.unlink()

    index = []
    for rec in payload["records"]:
        s = slug(rec)
        (traces / f"{s}.json").write_text(
            json.dumps(rec, ensure_ascii=False, default=str)
        )
        index.append(
            {
                "slug": s,
                "module": rec["module"].removeprefix("pipelines."),
                "callable": rec["callable"],
                "ok": rec["ok"],
                "form": rec.get("final_flat_slp1"),
                "steps": rec.get("trace_len"),
                "phase": rec.get("phase"),
                "note": rec.get("smoke_note"),
                "error": rec.get("error"),
            }
        )
    index.sort(key=lambda r: r["slug"].lower())
    (OUT / "index.json").write_text(
        json.dumps(
            {"generated_at": payload["generated_at"], "derivations": index},
            ensure_ascii=False,
        )
    )
    print(f"[build_pages] {len(index)} derivations → {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(build())
