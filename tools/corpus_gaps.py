"""
tools/corpus_gaps.py — what the engine cannot yet derive in Subhastini's library, ranked by use (Art. 18).

Every distinct word of the chosen works is put through ``core.analyze`` (form index + Vidyut
propose, the engine verifies). Results are weighted by how often the word occurs, so the
worklist is ordered by the text, not by intuition:

    python3 -m tools.corpus_gaps                      # default works, 2,000 most frequent words
    python3 -m tools.corpus_gaps --works gita --all   # every distinct word of the Gītā
    make corpus-gaps

The library is read by path, read-only (Art. 6): ``$SUBHASTINI_LIBRARY`` or ``~/subhastini/library``.
Its text never enters ``data/inputs``. Rāmāyaṇa and Mahābhārata are measured with DCS tags
(``tools/dcs_reader``); the Vedic saṃhitās and the Awadhi works are left out of the default set.
Output: ``.audit/corpus_gaps.json`` (a measurement, not committed).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from core.analyze import analyze, tokens  # noqa: E402

LIBRARY = Path(os.environ.get("SUBHASTINI_LIBRARY", Path.home() / "subhastini" / "library"))
DEFAULT_WORKS = ("gita", "bhagavatam", "manusmriti", "arthashastra", "nitishataka", "shatakatrayam",
                 "subhashita", "panchatantra", "kiratarjuniya", "meghaduta", "prasthanabheda")
OUT = _ROOT / ".audit" / "corpus_gaps.json"


def counts(works: tuple[str, ...], library: Path = LIBRARY) -> tuple[Counter, dict[str, set[str]]]:
    """Token frequency over the works, and which works each word occurs in."""
    freq: Counter = Counter()
    where: dict[str, set[str]] = defaultdict(set)
    for work in works:
        path = library / f"{work}.jsonl"
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as fp:
            for line in fp:
                for w in tokens(json.loads(line).get("sanskrit_text", "")):
                    freq[w] += 1
                    where[w].add(work)
    return freq, where


def cluster(word: dict) -> str:
    """The worklist bucket of a word the engine does not derive: what blocked its best proposal."""
    r = next((x for x in word["readings"] if x["status"] in ("differs", "error")), None) \
        or next((x for x in word["readings"] if x["status"] == "not_attempted"), None)
    if r is None:
        return "no proposal"
    q = r.get("request") or {}
    if r["status"] == "not_attempted":
        return "not attempted: " + r["note"].split(" — ")[-1].split(" (")[0]
    head = f"{q.get('kind')} {q.get('lakara')}" if q.get("kind") == "tinanta" else f"subanta vibhakti {q.get('vibhakti')}"
    if q.get("upasargas"):
        head += " + upasarga"
    if q.get("sanadi"):
        head += f" + {q['sanadi']}"
    return f"{head}: {'engine error ' + r['note'].split(':')[0] if r['status'] == 'error' else 'engine derives another form'}"


def run(works: tuple[str, ...], top: int | None, library: Path = LIBRARY, batch: int = 200) -> dict:
    freq, where = counts(works, library)
    vocab = [w for w, _ in freq.most_common(top)]
    t0 = time.time()
    words: list[dict] = []
    for i in range(0, len(vocab), batch):
        words += analyze(vocab[i:i + batch])["words"]
        print(f"  {min(i + batch, len(vocab))}/{len(vocab)} words · {time.time() - t0:.0f} s", file=sys.stderr)
    by_status: Counter = Counter()
    clusters: dict[str, dict] = {}
    for w in words:
        n = freq[w["word_dev"]]
        by_status[w["status"]] += n
        if w["status"] == "oracle_only":
            c = clusters.setdefault(cluster(w), {"tokens": 0, "words": []})
            c["tokens"] += n
            c["words"].append(f"{w['word_dev']} ×{n}")
    analysed = sum(freq[w["word_dev"]] for w in words)

    def brief(w: dict) -> dict:
        r = next((x for x in w["readings"] if x["status"] != "avyaya"), w["readings"][0] if w["readings"] else None)
        return {"word": w["word_dev"], "count": freq[w["word_dev"]], "works": sorted(where[w["word_dev"]]),
                "reading": r and r["label_dev"], "verdict": r and r["status"],
                "engine": r and (r.get("produced_dev") or r.get("note") or "")}

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "command": "python3 -m tools.corpus_gaps --works " + ",".join(works) + (f" --top {top}" if top else " --all"),
        "works": list(works), "tokens_total": sum(freq.values()), "unique_total": len(freq),
        "unique_analysed": len(words), "tokens_analysed": analysed,
        "tokens_by_status": dict(by_status),
        "clusters": sorted(({"cluster": k, **v, "words": v["words"][:12]} for k, v in clusters.items()),
                           key=lambda c: -c["tokens"]),
        "oracle_only": [brief(w) for w in words if w["status"] == "oracle_only"][:400],
        "unknown": [{"word": w["word_dev"], "count": freq[w["word_dev"]]} for w in words if w["status"] == "unknown"][:400],
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--works", default=",".join(DEFAULT_WORKS))
    ap.add_argument("--top", type=int, default=2000, help="most frequent distinct words to analyse")
    ap.add_argument("--all", action="store_true", help="every distinct word")
    ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args(argv)
    rep = run(tuple(a.works.split(",")), None if a.all else a.top)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
    t = rep["tokens_analysed"] or 1
    print(f"{rep['unique_analysed']}/{rep['unique_total']} distinct words · {rep['tokens_analysed']}/{rep['tokens_total']} tokens")
    for s in ("verified", "split", "avyaya", "oracle_only", "unknown"):
        print(f"  {s:12} {rep['tokens_by_status'].get(s, 0):7}  {rep['tokens_by_status'].get(s, 0) / t:.1%}")
    print("top engine gaps (tokens):")
    for c in rep["clusters"][:15]:
        print(f"  {c['tokens']:6}  {c['cluster']}  — {', '.join(c['words'][:5])}")
    print(f"→ {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
