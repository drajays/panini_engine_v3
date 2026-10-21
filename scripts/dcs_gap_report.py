"""Engine coverage of DCS-tagged texts -> .audit/dcs_gaps.json; print counts and top gap clusters.

Usage: python scripts/dcs_gap_report.py [TEXT ...] [--limit N] [--every K] [--out PATH]
(default: every fetched text; fetch with tools.fetch_dcs). --every K samples every K-th chapter (Mahābhārata: 3,990).
"""
import argparse, collections, json, sys
sys.path.insert(0, ".")
from tools import dcs_reader as rd

ap = argparse.ArgumentParser()
ap.add_argument("texts", nargs="*")
ap.add_argument("--limit", type=int, help="sentences per text")
ap.add_argument("--every", type=int, default=1, help="every K-th chapter")
ap.add_argument("--out", default=".audit/dcs_gaps.json")
a = ap.parse_args()
if not rd.available():
    raise SystemExit("no DCS snapshot: python3 -m tools.fetch_dcs")

report, gaps = {}, []
for t in a.texts or rd.texts():
    r = rd.coverage(t, a.limit, a.every)
    report[t] = r["counts"]
    gaps += [dict(g, text=t) for g in r["gaps"]]
    row = []
    for kind in ("subanta", "tinanta"):
        c = r["counts"].get(kind, {})
        n, ok = sum(c.values()), sum(c.get(s, 0) for s in rd.DERIVED)
        row.append(f"{kind} {ok}/{n} ({100 * ok / max(n, 1):.1f}%)")
    print(f"{t}: " + " · ".join(row), flush=True)
json.dump({"counts": report, "gaps": gaps}, open(a.out, "w"), ensure_ascii=False)

for kind in ("subanta", "tinanta"):
    print(f"\n── {kind}: differs (lemma · attested → produced)")
    for (l, w, p), n in collections.Counter((g["lemma"], g["word"], str(g.get("produced"))) for g in gaps
                                            if g["kind"] == kind and g["status"] == "differs").most_common(30):
        print(f"{n:5}  {l} · {w} → {p}")
    print(f"── {kind}: unresolved / error reasons")
    for why, n in collections.Counter((g["status"], (g.get("note") or "")[:70]) for g in gaps
                                      if g["kind"] == kind and g["status"] != "differs").most_common(15):
        print(f"{n:5}  {why[0]}: {why[1]}")
