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


# Ending → stem-repair, longest first. A *guess* to reach the kośa headword, not a derivation.
_ENDINGS = ("ेभ्यः", "ाणाम्", "ाभ्याम्", "ानाम्", "ेषु", "ैः", "ेन", "स्य", "ात्", "ाय", "ाः", "ान्",
            "ानि", "ाम्", "ौ", "े", "ः", "म्", "ं", "ि", "ी", "ु", "ू", "ा", "ाभिः", "ेण")
_PUNCT = "।॥॰,.;:!?\"'()[]{}-–—०१२३४५६७८९0123456789|"


def tokens(text: str) -> list[str]:
    for ch in _PUNCT:
        text = text.replace(ch, " ")
    return text.split()


def candidates(word: str) -> list[str]:
    out = [word]
    if word.endswith("ः"):
        out.append(word[:-1] + "र्")  # स्वः → स्वर् (visarga from r)
    for e in sorted(_ENDINGS, key=len, reverse=True):
        if word.endswith(e) and len(word) > len(e):
            base = word[: -len(e)]
            out += [base, base + "ा", base + "ि", base + "ु", base + "्"]
    return list(dict.fromkeys(out))


def analyze(text: str, limit: int = 3) -> list[dict]:
    """Per word: first candidate stem found in the kośas, with entries (hypothesis, not a derivation)."""
    idx = _index()
    res = []

    def find(w):
        return next((c for c in candidates(w) if c in idx), None)

    def split(w, depth=0):  # ponytail: greedy longest-prefix, no sandhi repair; real padaccheda = sandhi-aware segmenter
        hit = find(w)
        if hit:
            return [(w, hit)]
        if depth < 4:
            for i in range(len(w) - 1, 2, -1):
                head = find(w[:i])
                if head and (rest := split(w[i:], depth + 1)) and all(h for _, h in rest):
                    return [(w[:i], head)] + rest
        return [(w, None)]

    for w in tokens(text):
        parts = split(w)
        if len(parts) == 1:
            _, hit = parts[0]
            res.append({"word": w, "stem": hit, "entries": idx[hit][:limit] if hit else []})
        else:  # sandhi/samāsa guess: one row per part
            res += [{"word": p, "stem": h, "entries": idx[h][:limit], "part_of": w} for p, h in parts]
    return res
