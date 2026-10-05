"""Re-derive every group of docs/CONFLICT_CELLS.md in a fresh process and keep the ones that still differ — the sweeps showed rare
irreproducible misses, which must not be mistaken for rule gaps.  python3 -m tools.ledger_recheck > .audit/recheck.txt"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
gana = None
for line in (ROOT / "docs" / "CONFLICT_CELLS.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"^## gaṇa (\d+)", line)
    if m:
        gana = m.group(1); continue
    c = [x.strip() for x in line.split("|")]
    if len(c) < 9 or c[1] in ("root", "---") or not gana:
        continue
    root, lak, pada = c[1], c[2], c[3]
    for pd in (["parasmai", "atmane"] if pada == "ubhaya" else [pada]):
        out = subprocess.run([str(ROOT / ".venv/bin/python"), "-m", "tools.tri_compare", root, "--gana", gana, "--lakara", lak, "--pada", pd],
                             cwd=ROOT, capture_output=True, text=True).stdout
        for l in out.splitlines():
            if "loop≠V" in l and "vidyut   <--" not in l:       # an empty Vidyut cell is the oracle's gap, not ours
                print(gana, root, lak, pd, l.strip()[:140])
