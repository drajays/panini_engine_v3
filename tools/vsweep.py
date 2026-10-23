"""tools/vsweep.py — shipped path (derive) vs Vidyut, all lakāras of a root at once; prints only the disagreeing cells.
    python3 -m tools.vsweep --gana 2 --sample 20 [--lakaras laT,liT] [--pada parasmai] [--seed 1] > .audit/vs_g2.out
Vidyut is a validator (verdict per disagreement: reason + authority), never a template."""
from __future__ import annotations
import argparse, json, random, subprocess, sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
_V = {"laT": "Lat", "liT": "Lit", "luT": "Lut", "lRT": "Lrt", "loT": "Lot", "laG": "Lan", "liG": "VidhiLin",
      "AsIrliG": "AshirLin", "luG": "Lun", "lRG": "Lrn"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gana", type=int, required=True)
    ap.add_argument("--sample", type=float, default=100, help="percent of the gaṇa's roots (seeded)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--lakaras", default=",".join(_V))
    ap.add_argument("--pada", default="parasmai")
    a = ap.parse_args()
    import sutras  # noqa: F401
    from pipelines.dhatupatha import iter_dhatu_entries
    from pipelines.tinanta import derive
    lak = a.lakaras.split(",")
    want = {"parasmai": ("परस्मैपदी", "उभयपदी"), "atmane": ("आत्मनेपदी", "उभयपदी")}[a.pada]
    pool = [r for r in iter_dhatu_entries() if r.get("gana") == a.gana and r.get("pada_label_dev") in want and r.get("dhatupatha_id")]
    todo = random.Random(a.seed).sample(pool, max(1, round(len(pool) * a.sample / 100))) if pool else []
    bad = tot = 0
    for r in todo:
        q = {"op": "grid", "upadesha": r["upadesha_slp1"], "path_id": r["dhatupatha_id"], "prayoga": "kartari", "pada": a.pada,
             "lakaras": [_V[l] for l in lak]}
        p = subprocess.run([str(_ROOT / ".venv/bin/python"), "-m", "bench.oracle_dhaturupa"], cwd=_ROOT, input=json.dumps(q),
                           capture_output=True, text=True)
        try:
            vid = json.loads(p.stdout)
        except Exception:
            continue
        for l in lak:
            cells = vid.get(_V[l]) or []
            i = 0
            for pu in (3, 2, 1):
                for vc in (1, 2, 3):
                    v = cells[i] if i < len(cells) else []
                    i += 1
                    if not v:
                        continue
                    try:
                        rec = derive(r["dhatupatha_id"], l, "kartari", pu, vc, pada=a.pada).flat_slp1()
                    except Exception as e:
                        rec = "ERR:" + type(e).__name__
                    tot += 1
                    if rec not in v:
                        bad += 1
                        print(f"{r['upadesha_slp1']} {r['dhatupatha_id']} {l} {pu}-{vc} recipe {rec} vidyut {','.join(v)}")
    print(f"recipe≠Vidyut in {bad} of {tot} cells ({len(todo)} roots, gaṇa {a.gana}, {a.pada})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
