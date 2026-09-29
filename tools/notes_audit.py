"""
tools/notes_audit.py — compare hand-written prakriyā notes with the engine's traces.

A folder of Markdown notes, one form per file (the filename is the form). For
each note the sūtras it cites are collected (by number, Devanāgarī or Latin
digits, and by quoted pāṭha text); the engine derivation of the same form is
found among the recipe pipelines (docs/data/index.json); and the two sets are
compared:

    note-only    the note applies it, the engine never does → check the engine
    engine-only  the engine applies it, the note never cites it → check the note
                 (or it is a saṃjñā/paribhāṣā the note takes for granted)

The notes are a reference, not gold: they are read, never loaded by the engine.

    python3 -m tools.notes_audit "/path/to/my panini notes"   # → docs/NOTES_AUDIT.md
"""
from __future__ import annotations

import argparse
import importlib
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
_ID = re.compile(r"(?<![\d.])([1-8])\.([1-4])\.(\d{1,3})(?![\d.])")
OUT = _ROOT / "docs" / "NOTES_AUDIT.md"


def cited_sutras(text: str, patha: dict[str, str]) -> set[str]:
    from tools.sync_sutrapatha import norm
    t = text.translate(_DIGITS)
    ids = {f"{a}.{b}.{c}" for a, b, c in _ID.findall(t)}
    flat = norm(text)
    for sid, s in patha.items():                  # quoted by text (≥ 5 letters, to stay specific)
        n = norm(s)
        if len(n) >= 5 and n in flat:
            ids.add(sid)
    return {i for i in ids if i in patha}


def engine_forms() -> dict[str, list[tuple[str, str]]]:
    """SLP1 form → [(module, callable)] from the Pages index of recipe pipelines."""
    idx = json.loads((_ROOT / "docs" / "data" / "index.json").read_text())
    out: dict[str, list[tuple[str, str]]] = {}
    for r in idx["derivations"]:
        if r.get("ok") and r.get("form"):
            out.setdefault(r["form"], []).append((r["module"], r["callable"]))
    return out


def applied(module: str, fn: str) -> set[str]:
    mod = importlib.import_module(f"pipelines.{module}")
    st = getattr(mod, fn)()
    return {e["sutra_id"] for e in st.trace
            if e.get("status") == "APPLIED" and not (e.get("sutra_id") or "").startswith("__")}


def audit(notes_dir: Path) -> str:
    from phonology.tokenizer import devanagari_to_slp1_flat
    from tools.sync_sutrapatha import patha
    ref = patha()
    forms = engine_forms()
    rows, unmatched = [], []
    for f in sorted(notes_dir.glob("*.md")):
        name = f.stem.strip(" ‘’'\"")
        try:
            key = devanagari_to_slp1_flat(name.split()[0])
        except Exception:
            unmatched.append((f.name, "not a form"))
            continue
        cands = forms.get(key) or forms.get(key.rstrip("H") + "H") or forms.get(key.rstrip("H"))
        note = cited_sutras(f.read_text(encoding="utf-8"), ref)
        if not cands:
            unmatched.append((f.name, f"no engine recipe for {key}"))
            continue
        mod, fn = cands[0]
        try:
            eng = applied(mod, fn)
        except Exception as ex:
            unmatched.append((f.name, f"{mod}.{fn} raised {type(ex).__name__}"))
            continue
        rows.append((f.name, key, f"{mod}.{fn}", sorted(note - eng, key=_k), sorted(eng - note, key=_k),
                     len(note & eng)))
    lines = ["# Notes vs engine — sūtra paths", "",
             f"{len(rows)} notes matched to an engine recipe; {len(unmatched)} not matched.",
             "note-only: the note applies it, the engine never does. engine-only: the "
             "engine applies it, the note does not cite it (often a saṃjñā the note assumes).", ""]
    for name, key, where, n_only, e_only, both in rows:
        lines += [f"## {name} — `{key}`", f"engine: `{where}` · shared: {both}",
                  f"- note-only: {', '.join(n_only) or '—'}",
                  f"- engine-only: {', '.join(e_only) or '—'}", ""]
    lines += ["## Not matched", ""] + [f"- {n}: {why}" for n, why in unmatched]
    return "\n".join(lines) + "\n"


def _k(sid: str):
    return tuple(int(x) for x in sid.split("."))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("notes_dir", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=OUT)
    a = ap.parse_args(argv)
    a.out.write_text(audit(a.notes_dir), encoding="utf-8")
    print(f"→ {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
