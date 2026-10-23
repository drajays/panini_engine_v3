"""tools/lk_gaps.py — the Laghukaumudī work list measured on real forms.
For every LK sūtra not yet confident, take the forms of its prakriyā examples (brain: sutra_examples → derivations.result)
and ask the engine (core.analyze: Vidyut kosha proposes, every reading is re-derived by the engine) whether it reproduces them.
    python3 -m tools.lk_gaps [--limit N]   → docs/data/lk_gaps.json  {sutra: {words, verified, oracle_only, unknown, gap_words[]}}
Ranked output = the engine work list: a sūtra whose words are all verified is exercised; oracle_only words are rule gaps."""
import argparse, collections, re, json, pathlib, sqlite3, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
DB = pathlib.Path.home() / "data-master/ashtadhyayi-ai/db/ashtadhyayi.db"
OUT = pathlib.Path("docs/data/lk_gaps.json")


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int, default=0); a = ap.parse_args()
    import sutras  # noqa: F401
    from core.analyze import analyze
    wl = json.load(open("docs/data/lk_worklist.json"))
    todo = {r["id"] for r in wl if r["status"] not in ("confident", "confident_structural")}
    db = sqlite3.connect(DB)
    by = collections.defaultdict(set)
    for sid, res in db.execute("select se.sutra_id, d.result from sutra_examples se join derivations d on d.id = se.deriv_id"):
        if sid in todo and res and re.fullmatch(r"[\u0900-\u097F]+", res.strip()) and not re.search(r"[०-९।॥]", res):
            by[sid].add(res.strip())
    words = sorted({w for v in by.values() for w in v})
    if a.limit:
        words = words[: a.limit]
    verdict = {}
    for i in range(0, len(words), 100):
        chunk = words[i:i + 100]
        try:
            res = analyze(chunk)["words"]
        except Exception:                      # one odd word must not sink the chunk: ask one by one
            res = []
            for w in chunk:
                try:
                    res.append(analyze([w])["words"][0])
                except Exception:
                    res.append({"status": "error"})
        for w, r in zip(chunk, res):
            verdict[w] = r["status"]
        print(i + len(chunk), "/", len(words), flush=True)
    out = {}
    for sid, ws in by.items():
        c = collections.Counter(verdict.get(w, "?") for w in ws)
        out[sid] = {"words": len(ws), "verified": c["verified"], "oracle_only": c["oracle_only"], "unknown": c["unknown"],
                    "gap_words": sorted(w for w in ws if verdict.get(w) == "oracle_only")[:12]}
    OUT.write_text(json.dumps(dict(sorted(out.items(), key=lambda kv: tuple(map(int, kv[0].split("."))))), ensure_ascii=False, indent=0))
    tot = collections.Counter(verdict.values())
    print(dict(tot))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
