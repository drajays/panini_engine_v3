"""
tools/build_gita_words.py — tagged words of the Bhagavad Gītā, for coverage.
──────────────────────────────────────────────────────────────────────────────

Source: Medhā Michika, *Grammatical Analysis of Bhagavad Gita* (Arsha Avinash
Foundation), whose word analyses give clean IAST plus a case/number or
person/number tag:

    • त्वम् [tvam] = you = युष्मद् (pron. m.) + कर्तरि to करिष्यसि 1/1
    • करिष्यसि [kariṣyasi] = (you) will do = कृ (8U) + लृट्/कर्तरि/II/1

Only the verse, the word and its tag are kept — no glosses, no book text
(all rights reserved). Indeclinables (अव्ययम्) are counted but untagged.

    python3 -m tools.build_gita_words [--src "~/read_panini/Grammatical Analysis of Bhagavad Gita.pdf"]

Writes ``data/reference/gita/words.jsonl``, one object per (verse, word):
    {"verse": "2.33", "iast": "kariṣyasi", "slp1": "karizyasi",
     "kind": "tinanta", "purusha": 2, "vacana": 1}
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "data" / "reference" / "gita" / "words.jsonl"
SRC = Path.home() / "read_panini" / "Grammatical Analysis of Bhagavad Gita.pdf"

# IAST → SLP1, digraphs first.
_IAST = [("ai", "E"), ("au", "O"), ("kh", "K"), ("gh", "G"), ("ch", "C"), ("jh", "J"),
         ("ṭh", "W"), ("ḍh", "Q"), ("th", "T"), ("dh", "D"), ("ph", "P"), ("bh", "B"),
         ("ā", "A"), ("ī", "I"), ("ū", "U"), ("ṝ", "F"), ("ṛ", "f"), ("ḷ", "x"),
         ("ṃ", "M"), ("ḥ", "H"), ("ṅ", "N"), ("ñ", "Y"), ("ṭ", "w"), ("ḍ", "q"),
         ("ṇ", "R"), ("ś", "S"), ("ṣ", "z")]
_WORD = re.compile(r"\[([a-zāīūṛṝḷṃḥṅñṭḍṇśṣ'’\-]+)\]\s*=")
_VERSE = re.compile(r"\|\|\s*(\d+)[.-](\d+)\s*\|\|")   # ch. 1 prints ||1-12||
_SUP = re.compile(r"(?<![/\d])([1-8])/([1-3])\s*$")
_TIN = re.compile(r"/(I{1,3})/([1-3])\s*$")


def iast_to_slp1(word: str) -> str:
    out = word.lower().replace("-", "").replace("'", "").replace("’", "")
    for a, b in _IAST:
        out = out.replace(a, b)
    return out


def parse(text: str) -> list[dict]:
    lines = [ln.strip() for ln in text.splitlines()]
    verse, out, seen = None, [], set()
    for i, ln in enumerate(lines):
        if m := _VERSE.search(ln):
            verse = f"{m.group(1)}.{m.group(2)}"
        m = _WORD.search(ln)
        if not m or verse is None:
            continue
        entry = ln                                  # a tag may wrap onto the next line
        for nxt in lines[i + 1:i + 3]:
            if not nxt or _WORD.search(nxt) or nxt.startswith(("•", "o ")):
                break
            entry += " " + nxt
        rec = {"verse": verse, "iast": m.group(1), "slp1": iast_to_slp1(m.group(1))}
        if (t := _TIN.search(entry)):
            rec |= {"kind": "tinanta", "purusha": len(t.group(1)), "vacana": int(t.group(2))}
        elif (t := _SUP.search(entry)):
            rec |= {"kind": "subanta", "vibhakti": int(t.group(1)), "vacana": int(t.group(2))}
        elif "अव्यय" in entry:
            rec |= {"kind": "avyaya"}
        else:
            continue                                # untagged (compound part, gloss line)
        key = (verse, rec["slp1"], rec["kind"])
        if key not in seen:
            seen.add(key)
            out.append(rec)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=SRC)
    args = ap.parse_args(argv)
    text = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(args.src), "-"],
                          capture_output=True, text=True, check=True).stdout
    words = parse(text)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(json.dumps(w, ensure_ascii=False) + "\n" for w in words))
    kinds: dict[str, int] = {}
    for w in words:
        kinds[w["kind"]] = kinds.get(w["kind"], 0) + 1
    print(f"{len(words)} words, {len({w['verse'] for w in words})} verses {kinds} "
          f"→ {OUT.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
