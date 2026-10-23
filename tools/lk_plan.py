"""Laghukaumudī-first work list: LK sūtras (brain texts, source=laghukaumudi) in Aṣṭādhyāyī order × engine status.
Writes docs/data/lk_worklist.json; prints counts per adhyāya/status. Read-only on the brain."""
import json, sqlite3, collections, pathlib
DB = pathlib.Path.home() / "data-master/ashtadhyayi-ai/db/ashtadhyayi.db"
key = lambda i: tuple(int(x) for x in i.split("."))
ids = sorted({r[0] for r in sqlite3.connect(DB).execute("select sutra_id from texts where source='laghukaumudi'")
              if r[0].count(".") == 2}, key=key)
st = {r["id"]: r["status"] for r in json.load(open("sig/sutra_class.json"))["rows"]}
rows = [{"id": i, "status": st.get(i, "?")} for i in ids]
json.dump(rows, open("docs/data/lk_worklist.json", "w"), ensure_ascii=False, indent=0)
c = collections.Counter((r["id"].split(".")[0], r["status"]) for r in rows)
print(len(rows), collections.Counter(r["status"] for r in rows))
for a in "12345678": print(a, {s: n for (x, s), n in sorted(c.items()) if x == a})
