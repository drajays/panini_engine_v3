"""tools/gcell.py — re-derive the brain's subanta cells for the given stems (from docs/data/subanta_gauge.json) and print the misses.
    python3 -m tools.gcell saKi go div            (prints  v-n want | engine per liṅga)   exit: number of misses"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive

LINGA = ("pulliṅga", "strīliṅga", "napuṃsaka")


def main(stems) -> int:
    d = json.load(open("docs/data/subanta_gauge.json"))
    miss = tot = 0
    for v in d.values():
        if v["stem"] not in stems:
            continue
        want = v["want"].replace("he ", "", 1).strip()
        outs = {}
        for lg in LINGA:
            try:
                outs[lg[:2]] = "/".join(sorted({b.surface_slp1 for b in explore(lambda: derive(v["stem"], v["v"], v["n"], linga=lg))}))
            except Exception as e:
                outs[lg[:2]] = "ERR:" + type(e).__name__
        tot += 1
        if not any(want in o.split("/") for o in outs.values()):
            miss += 1
            print(f"{v['stem']} {v['v']}-{v['n']} want {want} | {outs}")
    print(f"{tot - miss}/{tot} ok")
    return miss


if __name__ == "__main__":
    raise SystemExit(main(set(sys.argv[1:])))
