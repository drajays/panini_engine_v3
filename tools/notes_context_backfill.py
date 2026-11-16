"""python3 -m tools.notes_context_backfill — fill `context` on old notes from what they saved (trace header + first rows).
New notes get their context from the page (webui/static/prakriya.js pkContext); this only covers notes written before that.
Every value found here is marked `inferred` and `liṅga` is given only when the stem has one liṅga in the corpus index."""
import glob, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IX = json.load(open(ROOT / "webui/static/shabda_index.json", encoding="utf-8"))
BY = {}
for d in IX:
    BY.setdefault(d["slp"], set()).add(d["l"])
VIB = {"su~": (1, 1), "O": (1, 2), "jas": (1, 3), "am": (2, 1), "Sas": (2, 3), "wA": (3, 1), "ByAm": (3, 2), "Bis": (3, 3), "Ne": (4, 1),
       "Byas": (4, 3), "Nasi": (5, 1), "Nas": (6, 1), "os": (6, 2), "Am": (6, 3), "Ni": (7, 1), "sup": (7, 3)}
n = 0
for f in glob.glob(str(ROOT / "data/reviews/notes/*.json")):
    d = json.load(open(f, encoding="utf-8")); ch = False
    for note in d["notes"]:
        if note.get("context") and not note["context"].get("inferred"):
            continue
        tr, c = note.get("trace") or "", {"inferred": True}
        m = re.search(r"^Derivation: (.*?) → (.*?) \((.*?)\)", tr, re.M)
        if m: c["surface_dev"], c["surface_slp1"] = m.group(2), m.group(3)
        pg = re.search(r"^Page: (\S+)", tr, re.M)
        if pg: c["page"] = pg.group(1)
        r1 = re.search(r"^#1 1\.2\.45 \[APPLIED\] (\S+) →", tr, re.M)
        if r1 and c.get("page", "").startswith("/shabdarupa"):
            c["kind"], c["stem_slp1"] = "shabda", r1.group(1)
            ls = sorted(BY.get(r1.group(1), []))
            c["linga"] = ls[0] if len(ls) == 1 else None
            c["linga_candidates"] = ls                 # >1 = the corpus has the stem in several liṅgas: unknown from the note alone
        sp = re.search(r'^#\d+ 4\.1\.2 \[APPLIED\].*?\["[^"]*","sup","([^"]*)"\]', tr, re.M)
        if sp and sp.group(1) in VIB:
            c["vibhakti"], c["vacana"] = VIB[sp.group(1)]; c["sup_upadesha"] = sp.group(1)
        if len(c) > 1:
            note["context"] = c; ch = True; n += 1
    if ch:
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("notes given an inferred context:", n)
