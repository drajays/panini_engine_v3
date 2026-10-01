"""Cluster reader gaps over the whole Gītā unit -> .audit/gita_gaps.json; print top clusters. Usage: python scripts/gita_gap_report.py"""
import collections, json, sys
sys.path.insert(0, ".")
from tools import samsaadhanii_reader as rd

u = next(x for x in rd.catalogue() if x["book"] == "श्रीमद्भगवद्गीता")
gaps, tot = [], collections.Counter()
for ch in u["chapters"]:
    r = rd.coverage(u["id"], ch)
    tot.update(r["counts"])
    gaps += [dict(g, ch=ch) for g in r["gaps"]]
json.dump(gaps, open(".audit/gita_gaps.json", "w"), ensure_ascii=False)
print(dict(tot))
for (w, p), n in collections.Counter((g["word"], g["produced"]) for g in gaps if g["status"] == "differs").most_common(25):
    print(n, w, "→", p)
