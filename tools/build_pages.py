"""
tools/build_pages.py — build the static GitHub Pages payload.

    python3 -m tools.build_pages          # writes docs/data/
    python3 -m tools.build_pages --sutras # only docs/data/sutras.json

Runs the pipeline trace dumper, then splits the single (~9 MB) snapshot into
one small ``index.json`` plus one file per derivation, so the static viewer
fetches only what the reader clicks. ``sutras.json`` gives the learner view
(docs/learn.html) each sūtra's pāṭha, padaccheda, Kāśikā udāharaṇa and
whether the file is still a placeholder that fires without doing anything.
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


_PLACEHOLDER = re.compile(r'state\.meta\["anga_kind"\]\s*=\s*"\d')
_MUTATES = re.compile(r"varnas|tags\.add|mk\(|terms\.insert")


def build_sutras() -> int:
    import sutras  # noqa: F401  — populates the registry
    from engine.registry import SUTRA_REGISTRY

    out = {}
    for sid, rec in SUTRA_REGISTRY.items():
        a, p, s = (sid.split(".") + ["", "", ""])[:3]
        src = ROOT / "sutras" / f"adhyaya_{a}" / f"pada_{p}" / f"sutra_{a}_{p}_{s}.py"
        body = src.read_text(encoding="utf-8") if src.exists() else ""
        ref = ROOT / "sutra_ref_out" / f"{a}_{p}_{s}.json"
        ex = []
        if ref.exists():
            ex = [e["raw"] for e in json.loads(ref.read_text(encoding="utf-8")).get("examples", [])
                  if e.get("raw")][:6]
        row = {"t": rec.text_dev, "p": rec.padaccheda_dev, "y": rec.sutra_type.name}
        if ex:
            row["ex"] = ex
        if getattr(rec, "meta_is_stub", False) or (_PLACEHOLDER.search(body) and not _MUTATES.search(body)):
            row["ph"] = 1
        out[sid] = row
    (OUT / "sutras.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
    print(f"[build_pages] {len(out)} sūtras ({sum('ph' in r for r in out.values())} placeholders) → sutras.json")
    return 0


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
    return build_sutras()


if __name__ == "__main__":
    sys.exit(build_sutras() if "--sutras" in sys.argv else build())
