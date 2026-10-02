import json
import os
from core.transliterate import dev_to_slp1

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
        # convert P -> pulliṅga, S -> strīliṅga, N -> napuṃsaka
        if l == "P": linga = "pulliṅga"
        elif l == "S": linga = "strīliṅga"
        elif l == "N": linga = "napuṃsaka"
        else: linga = l
        
        slp1 = dev_to_slp1(w)
        a = item.get("artha", "")
        ae = item.get("artha_eng", "")
        
        index.append({
            "w": w,
            "slp": slp1,
            "l": linga,
            "a": a,
            "ae": ae
        })
    
    out_path = "webui/static/shabda_index.json"
    with open(out_path, "w", encoding="utf-8") as outf:
        json.dump(index, outf, ensure_ascii=False, separators=(',', ':'))
    print(f"Dumped {len(index)} stems to {out_path}")

if __name__ == "__main__":
    dump_index()
