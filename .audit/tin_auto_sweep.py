"""Sweep: autonomous loop vs recipe, laT kartari 3sg, every gaṇa-1 root the recipe derives."""
import sys, json, time, collections
import sutras
from types import SimpleNamespace as N
from tools.autonomy_report import run_autonomously, start_state
from pipelines.tinanta import derive
from pipelines.dhatupatha import iter_dhatu_entries
lim = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9
out = []; t0 = time.time()
rows = [r for r in iter_dhatu_entries() if r.get("gana") == 1][:lim]
for r in rows:
    u = r["upadesha_slp1"]
    try:
        exp = derive(u, "laT", "kartari", 3, 1).flat_slp1()
    except Exception as e:
        continue
    try:
        run = run_autonomously(start_state(N(kind="tinanta", args=(u, "laT", 3, 1))), exp, u, 120)
        out.append((u, run.outcome, run.surface, exp))
    except Exception as e:
        out.append((u, "error:" + type(e).__name__, str(e)[:50], exp))
c = collections.Counter(o[1] for o in out)
print(dict(c), f"{time.time()-t0:.0f}s")
json.dump(out, open(".audit/tin_auto_sweep.json", "w"), ensure_ascii=False, indent=0)
for o in out:
    if o[1] != "reached": print(o)
