"""
bench/oracle_kosha.py — Vidyut's kosha readings for a batch of surfaces, JSON in / JSON out.

The API runs in an interpreter without ``vidyut``; ``core/analyze`` pipes words here
through the repo's ``.venv``:

    echo '["gacCati", "karmaRi"]' | .venv/bin/python -m bench.oracle_kosha

Each output item is the list of readings Vidyut's kosha holds for that surface (SLP1).
They are *proposals* only (CONSTITUTION Art. 17): the engine accepts a reading only
by deriving the same string. Data: ``$PANINI_VIDYUT_DATA`` or ``.venv/vidyut-data``
(``vidyut.download_data``). Never imported by the engine.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
DATA = Path(os.environ.get("PANINI_VIDYUT_DATA", _ROOT / ".venv" / "vidyut-data"))


def _dhatu(entry) -> dict:
    d = entry.dhatu
    return {"aupadeshika": d.aupadeshika, "gana": str(d.gana), "artha": entry.artha_sa or "",
            "clean": entry.clean_text or "", "sanadi": [str(s) for s in (getattr(d, "sanadi", None) or [])],
            "prefixes": list(getattr(d, "prefixes", None) or [])}


def reading(e) -> dict:
    kind = type(e).__name__
    if kind.endswith("Tinanta"):
        return {"kind": "tinanta", "dhatu": _dhatu(e.dhatu_entry), "lakara": str(e.lakara),
                "prayoga": str(e.prayoga), "purusha": str(e.purusha), "vacana": str(e.vacana)}
    if kind.endswith("Subanta"):
        p = e.pratipadika_entry
        out = {"kind": "subanta", "linga": str(e.linga), "vibhakti": str(e.vibhakti), "vacana": str(e.vacana)}
        if type(p).__name__.endswith("Basic"):
            if p.pratipadika.is_avyaya:
                return {"kind": "avyaya", "stem": p.pratipadika.text}
            return {**out, "stem": p.pratipadika.text}
        return {**out, "stem": None, "krdanta": {"dhatu": _dhatu(p.dhatu_entry), "krt": str(p.krt)}}
    return {"kind": "other", "repr": repr(e)[:120]}


def spellings(word: str) -> list[str]:
    """The kosha keys a surface may be stored under: final visarga as s / r (8.3.15 undone), anusvāra as m."""
    if word.endswith("H"):
        return [word, word[:-1] + "s", word[:-1] + "r", word[:-1]]
    if word.endswith("M"):
        return [word, word[:-1] + "m"]
    return [word]


def main() -> int:
    from vidyut.kosha import Kosha
    kosha = Kosha(str(DATA / "kosha"))
    out = []
    for word in json.load(sys.stdin):
        try:
            entries = next((es for es in map(kosha.get, spellings(word)) if es), [])
            out.append([reading(e) for e in entries])
        except Exception:                         # the oracle's own gaps
            out.append([])
    json.dump(out, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
