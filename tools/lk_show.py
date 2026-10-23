"""Compact view of one sūtra for a batch: pāṭha, LK/Kāśikā text, status. Usage: python3 -m tools.lk_show 6.1.37 ..."""
import sqlite3, sys, json, pathlib
db = sqlite3.connect(pathlib.Path.home() / "data-master/ashtadhyayi-ai/db/ashtadhyayi.db")
st = {r["id"]: r["status"] for r in json.load(open("sig/sutra_class.json"))["rows"]}
for sid in sys.argv[1:]:
    print(f"== {sid} [{st.get(sid)}]")
    for src in ("laghukaumudi", "kashika"):
        for (c,) in db.execute("select content from texts where sutra_id=? and source=? limit 1", (sid, src)):
            print(f" {src[:3]}: {c[:700]}")
