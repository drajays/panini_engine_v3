"""tools/loop_gauge.py — per (gaṇa, lakāra, pada) class: the loop vs Vidyut on a seeded sample of roots, in parallel.
    python3 -m tools.loop_gauge --gana 4 --pada parasmai --roots 8 [--workers 4]   → appends to sig/loop_gauge.json
A class with loop errors ≪ recipe errors (tools.vsweep) is a candidate for engine.core_loop.LOOP_CLASSES."""
from __future__ import annotations
import argparse, json, random, subprocess, sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from types import SimpleNamespace as NS

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
OUT = _ROOT / "sig" / "loop_gauge.json"
_V = {"laT": "Lat", "liT": "Lit", "luT": "Lut", "lRT": "Lrt", "loT": "Lot", "laG": "Lan", "liG": "VidhiLin",
      "AsIrliG": "AshirLin", "luG": "Lun", "lRG": "Lrn"}


def _one(args):
    ref, upa, pada = args
    import sutras  # noqa: F401
    from tools.autonomy_report import run_autonomously, start_state
    q = {"op": "grid", "upadesha": upa, "path_id": ref, "prayoga": "kartari", "pada": pada, "lakaras": list(_V.values())}
    p = subprocess.run([str(_ROOT / ".venv/bin/python"), "-m", "bench.oracle_dhaturupa"], cwd=_ROOT, input=json.dumps(q), capture_output=True, text=True)
    try:
        vid = json.loads(p.stdout)
    except Exception:
        return {}
    res = {}
    for lak, vk in _V.items():
        cells, bad, tot = vid.get(vk) or [], 0, 0
        for i, (pu, vc) in enumerate((pu, vc) for pu in (3, 2, 1) for vc in (1, 2, 3)):
            v = cells[i] if i < len(cells) else []
            if not v:
                continue
            try:
                got = run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface
            except Exception:
                got = "ERR"
            tot += 1
            bad += got not in v
        res[lak] = [bad, tot]
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gana", type=int, required=True)
    ap.add_argument("--pada", default="parasmai")
    ap.add_argument("--roots", type=int, default=8)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    from pipelines.dhatupatha import iter_dhatu_entries
    want = {"parasmai": ("परस्मैपदी", "उभयपदी"), "atmane": ("आत्मनेपदी", "उभयपदी")}[a.pada]
    pool = [r for r in iter_dhatu_entries() if r.get("gana") == a.gana and r.get("pada_label_dev") in want and r.get("dhatupatha_id")]
    todo = random.Random(a.seed).sample(pool, min(a.roots, len(pool)))
    with ProcessPoolExecutor(a.workers) as ex:
        results = list(ex.map(_one, [(r["dhatupatha_id"], r["upadesha_slp1"], a.pada) for r in todo]))
    agg = {}
    for res in results:
        for lak, (b, t) in res.items():
            x = agg.setdefault(lak, [0, 0]); x[0] += b; x[1] += t
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    data[f"{a.gana}:{a.pada}"] = {"roots": [r["upadesha_slp1"] for r in todo], "loop_errors": agg}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    print(a.gana, a.pada, {k: f"{b}/{t}" for k, (b, t) in agg.items()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
