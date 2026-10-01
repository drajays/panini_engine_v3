"""
tools/kosha.py — kośa lookup (synonymic/homonymic lexicons) for the reader's artha layer.

Source: sanskrit-kosha/kosha (GPL v3, kept outside this repo). Directory comes
from ``$KOSHA_DIR`` (default ``~/kosha-master``); every ``*/json/*.json`` is read:
``headword -> [[headword, linga, [synonyms], verse, index, page], ...]``.
Tools-layer (Art. 6): display/provenance only, never read by ``cond()``.
"""
from __future__ import annotations

import json
import os
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

_ROOT = Path(os.environ.get("KOSHA_DIR", "~/kosha-master")).expanduser()


@lru_cache(maxsize=1)
def _index() -> dict[str, list[dict]]:
    idx: dict[str, list[dict]] = defaultdict(list)
    for f in sorted(_ROOT.glob("*/json/*.json")):
        for key, entries in json.loads(f.read_text(encoding="utf-8")).items():
            for head, linga, syns, verse, ref, *_ in entries:
                rec = {"kosha": f.stem, "headword": head, "linga": linga,
                       "synonyms": syns, "verse": verse.replace("<BR>", "\n"), "ref": ref}
                for w in {key, head, *syns}:
                    idx[w].append(rec)
    return idx


def lookup(word_dev: str, limit: int = 5) -> list[dict]:
    """Entries naming ``word_dev`` (Devanāgarī stem) as headword or synonym; [] if none."""
    idx = _index()
    w = word_dev.strip()
    for cand in (w, w.rstrip("ःंम्")):
        if cand in idx:
            return idx[cand][:limit]
    return []
