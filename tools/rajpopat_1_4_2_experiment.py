"""Run: PYTHONPATH=. .venv/bin/python tools/rajpopat_1_4_2_experiment.py <stems> <step>   (e.g. 40 220; ~4 min). OFFLINE ONLY: monkeypatches the resolver in this process, never imported by the engine.
Rajpopat 1.4.2 (right-hand operand wins) vs our resolver, offline, scratch only (docs/RESEARCH_PAPERS_PLAN.md idea 6).
Modes: base = the engine as it is (nitya / antaraṅga / apavāda / para ladder).  rp = every contested decision settled by
'the rule whose operand is rightmost wins'; same operand -> the engine's own choice (SOI is not re-implemented).
Gold = the hand-checked upstream paradigm (data/reference/ashtadhyayi_com/shabda__data2.txt)."""
import json, sys, time, dataclasses
import engine.resolver as R, engine.core_loop as CL
from engine.scheduler import probe
from core.transliterate import dev_to_slp1
from pipelines.subanta import derive

MODE = {"m": "base"}
LOG = []                     # (candidates, engine winner, layer, rp winner)
CONTEST = {"para", "antaranga", "apavada"}
orig = R.resolve_with_reason

def operand(c, state):
    """The set of Term indices rule c changes (None if probe fails / nothing changes)."""
    try:
        s2 = probe(c, state)
    except Exception:
        return None
    sig = lambda ts: [("".join(v.slp1 for v in t.varnas), t.kind) for t in ts]
    a, b = sig(state.terms), sig(s2.terms)
    ch = frozenset(i for i in range(max(len(a), len(b))) if i >= len(a) or i >= len(b) or a[i] != b[i])
    return ch or None

def wrap(c, state, specificity=None):
    d = orig(c, state, specificity)
    if d.layer not in CONTEST or len(d.losers) == 0:
        return d
    group = [d.winner] + [x for x in d.losers if x in c]
    ops = {x: operand(x, state) for x in group}
    known = {x: o for x, o in ops.items() if o is not None}
    # Rajpopat: same operand (SOI) -> the more specific rule wins (the engine's own choice here); different operands (DOI) -> the right-hand one.
    # DOI only if the Term sets the rules change are DISJOINT; overlapping sets (ekādeśa across the junction) are the same operand.
    xs = list(known)
    doi = len(xs) >= 2 and all(not (known[x] & known[y]) for i, x in enumerate(xs) for y in xs[i + 1:])
    if not doi:
        return d
    rp = [x for x in xs if max(known[x]) == max(max(v) for v in known.values())]
    rpw = rp[0] if len(rp) == 1 else d.winner
    LOG.append((tuple(sorted(group)), d.winner, d.layer, rpw, MODE["m"]))
    if MODE["m"] == "rp" and rpw != d.winner:
        return dataclasses.replace(d, winner=rpw, losers=tuple(x for x in group if x != rpw))
    return d

CL.resolve_with_reason = wrap
R.resolve_with_reason = wrap

LG = {"P": "pulliṅga", "S": "strīliṅga", "N": "napuṃsaka"}
rows = json.load(open("data/reference/ashtadhyayi_com/shabda__data2.txt"))["data"]
N, STEP = int(sys.argv[1]), int(sys.argv[2])
sample = rows[::STEP][:N]
out = {"base": {"ok": 0, "bad": 0, "err": 0}, "rp": {"ok": 0, "bad": 0, "err": 0}}
diffs = []
t0 = time.time()
for r in sample:
    stem = dev_to_slp1(r["word"]); lg = LG.get(r["linga"], "pulliṅga")
    gold = [[x.replace("हे ", "").strip() for x in c.split("-") if x.strip()] for c in r["forms"].split(";")]
    for vb in range(1, 9):
        for vc in (1, 2, 3):
            g = gold[(vb - 1) * 3 + (vc - 1)] if (vb - 1) * 3 + (vc - 1) < len(gold) else []
            res = {}
            for m in ("base", "rp"):
                MODE["m"] = m
                try:
                    res[m] = derive(stem, vb, vc, linga=lg).flat_dev()
                except Exception as e:
                    res[m] = None
                k = "err" if res[m] is None else ("ok" if res[m] in g else "bad")
                out[m][k] += 1
            if res["base"] != res["rp"]:
                diffs.append({"stem": r["word"], "linga": lg, "cell": (vb, vc), "gold": g, "base": res["base"], "rp": res["rp"]})
print(f"{len(sample)} stems x 24 cells in {time.time()-t0:.0f}s")
print(json.dumps(out, ensure_ascii=False))
dis = [x for x in LOG if x[4] == "base" and x[1] != x[3]]
print("contested decisions (base run, different operands):", len([x for x in LOG if x[4] == "base"]), "| right-operand rule differs from engine winner:", len(dis))
from collections import Counter
print(Counter((x[1], x[3], x[2]) for x in dis).most_common(12))
print("cells whose form changes under rp:", len(diffs))
for d in diffs[:25]: print(d)
json.dump({"out": out, "diffs": diffs, "dis": Counter(f"{x[1]}>{x[3]}|{x[2]}" for x in dis).most_common(40)}, open("scratch/rp_experiment.json", "w"), ensure_ascii=False, indent=1)
