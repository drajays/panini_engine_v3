"""Build webui/static/shabda_index.json from ashtadhyayi.com shabda__data2.txt.

Includes filter tags for the ashtadhyayi-style śabda filter panel (antyavarṇa,
liṅga, grantha, śabdaviśeṣa). Tags are UI-only (Art. 6 — not engine input).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.transliterate import dev_to_slp1
from tools.patha_filter_tags import shabda_tags


def dump_index():
    path = "data/reference/ashtadhyayi_com/shabda__data2.txt"
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    index = []
    for item in data.get("data", []):
        w = item.get("word", "")
        l = item.get("linga", "")
        if l == "P":
            linga = "pulliṅga"
        elif l == "S":
            linga = "strīliṅga"
        elif l == "N":
            linga = "napuṃsaka"
        else:
            linga = l

        slp1 = dev_to_slp1(w)
        po = item.get("prakriya_options") or {}
        tags = shabda_tags(slp1, l, po, sk=item.get("sk") or "", lsk=item.get("lsk") or "")
        index.append({
            "w": w,
            "slp": slp1,
            "l": linga,
            "lc": l,  # P/S/N/A
            "a": item.get("artha", ""),
            "ae": item.get("artha_eng", ""),
            "t": tags,
        })

    out_path = "webui/static/shabda_index.json"
    with open(out_path, "w", encoding="utf-8") as outf:
        json.dump(index, outf, ensure_ascii=False, separators=(",", ":"))
    print(f"Dumped {len(index)} stems to {out_path}")


if __name__ == "__main__":
    dump_index()
