"""
bench/gita_coverage.py — how much of the real Gītā does this engine derive?
────────────────────────────────────────────────────────────────────────────

For every tagged subanta / tiṅanta word in ``data/reference/gita/words.jsonl``
(built by ``tools.build_gita_words``):

  surface  — forms.db has this surface under any analysis
  tagged   — … with the book's tag (vibhakti/vacana, or puruṣa/vacana)
  verified — … and that cell is Vidyut-verified (bench/practice_key)

    python3 -m bench.gita_coverage            # print, and the top misses
    python3 -m bench.gita_coverage --write    # also bench/report/gita_coverage.json

The miss list, ranked by frequency, is the coverage work queue (plan, Track C).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from engine.form_index import connect  # noqa: E402

WORDS = _ROOT / "data" / "reference" / "gita" / "words.jsonl"
VERIFIED = _ROOT / "bench" / "oracle" / "practice_verified.json"
REPORT = _ROOT / "bench" / "report" / "gita_coverage.json"


def tag_matches(word: dict, features: dict, kind: str) -> bool:
    if kind != word["kind"]:
        return False
    if kind == "subanta":   # the book tags a vocative 1/n (सम्बोधने); we index it as 8
        return (features["vacana"] == word["vacana"]
                and features["vibhakti"] in ({1, 8} if word["vibhakti"] == 1 else {word["vibhakti"]}))
    return features["purusha"] == word["purusha"] and features["vacana"] == word["vacana"]


def measure() -> dict:
    words = [json.loads(ln) for ln in WORDS.read_text().splitlines()
             if json.loads(ln)["kind"] != "avyaya"]
    verified = set(json.loads(VERIFIED.read_text())["verified"]) if VERIFIED.exists() else set()
    counts = Counter()
    misses: Counter = Counter()
    with closing(connect()) as conn:
        for w in words:
            rows = conn.execute("SELECT kind, features, cell_key FROM forms WHERE surface_slp1 = ?",
                                (w["slp1"],)).fetchall()
            tagged = [r for r in rows if tag_matches(w, json.loads(r["features"]), r["kind"])]
            counts["surface"] += bool(rows)
            counts["tagged"] += bool(tagged)
            counts["verified"] += any(r["cell_key"] in verified for r in tagged)
            if not tagged:
                misses[(w["iast"], w["kind"])] += 1
    n = len(words)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "words": n,
        **{k: counts[k] for k in ("surface", "tagged", "verified")},
        **{f"{k}_pct": round(100 * counts[k] / n, 1) for k in ("surface", "tagged", "verified")},
        "top_misses": [[w, k, c] for (w, k), c in misses.most_common(60)],
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)
    r = measure()
    print(f"Gītā (ch. 1–6), {r['words']} tagged subanta/tiṅanta words:")
    for k in ("surface", "tagged", "verified"):
        print(f"  {k:9} {r[k]:5}  {r[k + '_pct']:5}%")
    print("top misses:", ", ".join(f"{w}×{c}" for w, _, c in r["top_misses"][:30]))
    if args.write:
        REPORT.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n")
        print(f"→ {REPORT.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
