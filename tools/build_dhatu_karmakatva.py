"""tools/build_dhatu_karmakatva.py — AMENDMENT 25 §4: sakarmaka / akarmaka per dhātu, from ashtadhyayi.com.

    python3 -m tools.build_dhatu_karmakatva [path/to/dhatu/data.txt]   # writes data/inputs/dhatu_karmakatva.json

Source: ashtadhyayi.com dhātupāṭha `dhatu/data.txt`, field `karma` (A akarmaka, S sakarmaka, D dvikarmaka), keyed by
`baseindex` (= our dhatupatha_id). A row with no value ("-" or absent) is listed under `gaps` (Art. 18), never guessed.
Default source path: ~/data-master/dhatu/data.txt (the synced ashtadhyayi-com/data checkout).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
OUT = _ROOT / "data" / "inputs" / "dhatu_karmakatva.json"
DEFAULT_SRC = Path.home() / "data-master" / "dhatu" / "data.txt"
_CODE = {"A": "akarmaka", "S": "sakarmaka", "D": "dvikarmaka"}


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
    data = json.loads(src.read_text(encoding="utf-8"))["data"]
    by_id = {x["baseindex"]: _CODE.get((x.get("karma") or "").strip()) for x in data}
    from pipelines.dhatupatha import iter_dhatu_entries

    values, gaps = {}, []
    for row in iter_dhatu_entries():
        pid = row.get("dhatupatha_id")
        v = by_id.get(pid)
        if v:
            values[pid] = v
        else:
            gaps.append(pid or row.get("id"))
    out = {"source": "ashtadhyayi.com dhatu/data.txt field 'karma' (A/S/D), keyed by baseindex",
           "values": dict(sorted(values.items())), "gaps": sorted(set(gaps))}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(values)} rows with a cited value, {len(out['gaps'])} gaps → {OUT.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
