"""tools/tri_compare.py — one root, one lakāra: recipe vs loop vs Vidyut, cell by cell (who is right?).

    .venv/bin/python -m tools.tri_compare cakziN --gana 2 --lakara laT [--pada atmane]
Runs under the venv with vidyut. Presentation/diagnostic only."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace as NS

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
_V = {"laT": "Lat", "liT": "Lit", "luT": "Lut", "lRT": "Lrt", "loT": "Lot", "laG": "Lan", "liG": "VidhiLin",
      "AsIrliG": "AshirLin", "luG": "Lun", "lRG": "Lrn"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--gana", type=int)
    ap.add_argument("--lakara", default="laT")
    ap.add_argument("--pada", default="")
    ap.add_argument("--limit", type=int, default=12)
    a = ap.parse_args()
    import sutras  # noqa: F401
    from pipelines.dhatupatha import iter_dhatu_entries
    from pipelines.tinanta import derive
    from tools.autonomy_report import run_autonomously, start_state
    if a.root == "ALL":          # every loop≠Vidyut cell of the first --limit roots of the gaṇa (the real work list)
        want = {"parasmai": "परस्मैपदी", "atmane": "आत्मनेपदी"}.get(a.pada)
        todo = [r for r in iter_dhatu_entries() if r.get("gana") == a.gana and (not want or r.get("pada_label_dev") == want)][: a.limit]
        bad = tot = 0
        for r in todo:
            sub = subprocess.run([sys.executable, "-m", "tools.tri_compare", r["upadesha_slp1"], "--gana", str(a.gana),
                                  "--lakara", a.lakara] + (["--pada", a.pada] if a.pada else []),
                                 cwd=_ROOT, capture_output=True, text=True).stdout
            for line in sub.splitlines():
                tot += 1
                if "loop≠V" in line:
                    bad += 1
                    print(r["upadesha_slp1"], line)
        print(f"loop≠Vidyut in {bad} of {tot} cells")
        return 0
    rows = [r for r in iter_dhatu_entries() if r["upadesha_slp1"] == a.root and (not a.gana or r.get("gana") == a.gana)]
    if not rows:
        print("no such root"); return 1
    r = rows[0]
    ref = r.get("id") or a.root
    q = {"op": "grid", "upadesha": r["upadesha_slp1"], "path_id": r["dhatupatha_id"], "prayoga": "kartari",
         "pada": a.pada or None, "lakaras": [_V[a.lakara]]}
    p = subprocess.run([str(_ROOT / ".venv/bin/python"), "-m", "bench.oracle_dhaturupa"], cwd=_ROOT, input=json.dumps(q),
                       capture_output=True, text=True)
    vid = json.loads(p.stdout)[_V[a.lakara]]
    kw = {"pada": a.pada} if a.pada else {}
    i = 0
    for pu in (3, 2, 1):
        for vc in (1, 2, 3):
            try: rec = derive(ref, a.lakara, "kartari", pu, vc, **kw).flat_slp1()
            except Exception as e: rec = "ERR"
            try: loop = run_autonomously(start_state(NS(kind="tinanta", args=(ref, a.lakara, pu, vc))), "", ref, 250).surface
            except Exception as e: loop = "ERR"
            v = vid[i]; i += 1
            flag = "" if (loop in v and rec in v) else "  <-- " + ("recipe≠V " if rec not in v else "") + ("loop≠V" if loop not in v else "")
            print(f"{pu}-{vc}  recipe {rec:<14} loop {loop:<14} vidyut {','.join(v)}{flag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
