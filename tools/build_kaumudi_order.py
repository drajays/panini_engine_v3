"""tools/build_kaumudi_order.py — the book order of the Laghusiddhāntakaumudī and the Siddhāntakaumudī, per sūtra.

    python3 -m tools.build_kaumudi_order [--src ~/data-master/sutraani/data.txt]

ashtadhyayi.com numbers every sūtra by its place in each book (fields lskn / skn of its sutraani data.txt; 0 = the book
does not have it; lsk_chapter / sk_chapter = the prakaraṇa number). Only those numbers are stored here — no book text.
Writes data/reference/kaumudi/order.json:  {"6.1.77": {"lsk": 15, "sk": 47, "lskc": 2, "skc": 3}, ...}
(lsk / sk are omitted when the book lacks the sūtra.)  The page /sutras and /sutra/<id> read it (webui); no engine rule does.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "reference" / "kaumudi" / "order.json"


def build(src: Path) -> dict:
    out = {}
    for r in json.loads(src.read_text(encoding="utf-8"))["data"]:
        sid = f"{r['a']}.{r['p']}.{r['n']}"
        row = {}
        for key, f, c in (("lsk", "lskn", "lskc"), ("sk", "skn", "skc")):
            n = int(r[f]) if str(r.get(f, "")).isdigit() else 0
            if n > 0:
                row[key] = n
                ch = r.get(key + "_chapter", "")
                if str(ch).isdigit() and int(ch) > 0:
                    row[c] = int(ch)
        if row:
            out[sid] = row
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(Path.home() / "data-master/sutraani/data.txt"))
    o = build(Path(ap.parse_args().src))
    OUT.write_text(json.dumps(o, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")
    print(f"{len(o)} sūtras; LSK {sum('lsk' in v for v in o.values())}, SK {sum('sk' in v for v in o.values())} -> {OUT.relative_to(ROOT)}")
