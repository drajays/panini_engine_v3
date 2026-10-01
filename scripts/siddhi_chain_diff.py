"""Compare Jijñāsu siddhi_inventory key_operations against our engine's fired sūtras -> docs/SIDDHI_CHAIN_DIFF.md"""
import glob, json, sqlite3, sys
sys.path.insert(0, ".")
from core.transliterate import dev_to_slp1
INV = "/Users/dr.ajayshukla/xxxpanini_engine_v2/data/siddhi_inventory.json"
cases = json.load(open(INV))["siddhis"]
db = sqlite3.connect("data/index/forms.db")
traces = {}  # surface_slp1 -> set of APPLIED sutras (from exported traces)
for f in glob.glob("docs/data/traces/*.json"):
    d = json.load(open(f))
    if d.get("ok") and d.get("trace"):
        traces.setdefault(d["final_flat_slp1"], set()).update(
            s["sutra_id"] for s in d["trace"] if s["status"] in ("APPLIED", "DEFINED"))
rows, stat = [], {"match": 0, "partial": 0, "form-only": 0, "absent": 0}
for c in cases:
    w = dev_to_slp1(c["siddhi_word"]); exp = c["key_operations"]
    fired = set(traces.get(w, ()))
    for (cell,) in db.execute("select cell_key from forms where surface_slp1=?", (w,)):
        fired |= {r[0] for r in db.execute("select sutra_id from firings where cell_key=?", (cell,))}
    if not fired and w not in traces and not db.execute("select 1 from forms where surface_slp1=?", (w,)).fetchone():
        st, miss = "absent", exp
    else:
        miss = [s for s in exp if s not in fired]
        st = "match" if not miss else ("partial" if len(miss) < len(set(exp)) else "form-only")
    stat[st] += 1
    rows.append((c["id"], c["prakriya_type"], c["siddhi_word"], st, miss))
out = ["# Siddhi chain diff (Jijñāsu inventory vs engine)", "", f"Cases: {len(cases)} — " + ", ".join(f"{k}: {v}" for k, v in stat.items()),
       "", "Note: set-comparison of fired sūtras (order not checked); 'absent' = surface not derived/indexed by v3.", "",
       "| id | type | word | status | expected sūtras not fired |", "|---|---|---|---|---|"]
out += [f"| {i} | {t} | {w} | {s} | {', '.join(m) if s != 'absent' else '—'} |" for i, t, w, s, m in rows]
open("docs/SIDDHI_CHAIN_DIFF.md", "w").write("\n".join(out) + "\n")
print(stat)
