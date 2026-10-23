"""tools/brain_subanta_gauge.py — ashtadhyayi.com's own subanta prakriyās (brain: derivations kind='subanta', 4,863 cells) as the oracle.
Label 'stem vibhakti vacana → form'. The liṅga is not in the label: a cell passes if the engine's form for any liṅga equals it.
A failing cell carries the sūtras the brain lists on that prakriyā = the work item.   python3 -m tools.brain_subanta_gauge [--workers 8]"""
import argparse, collections, json, pathlib, re, sqlite3, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
DB = pathlib.Path.home() / "data-master/ashtadhyayi-ai/db/ashtadhyayi.db"
OUT = pathlib.Path("docs/data/subanta_gauge.json")
VIB = {"प्रथमा": 1, "द्वितीया": 2, "तृतीया": 3, "चतुर्थी": 4, "पञ्चमी": 5, "षष्ठी": 6, "सप्तमी": 7, "सम्बोधनम्": 8}
LINGA = ("pulliṅga", "strīliṅga", "napuṃsaka")


def _cell(row):
    did, label, form = row
    m = re.match(r"^(\S+) (\S+) ([123]) → ", label)
    if not m or m.group(2) not in VIB:
        return None
    from core.transliterate import dev_to_slp1
    import sutras  # noqa: F401
    from pipelines.subanta import derive
    stem, vib, vac = dev_to_slp1(m.group(1)), VIB[m.group(2)], int(m.group(3))
    from engine.vikalpa import explore
    outs = {}
    for lg in LINGA:
        try:   # every वा / विभाषा branch is an output (engine.vikalpa): the brain's cell is one of them
            outs[lg] = "/".join(sorted({b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, linga=lg))}))
        except Exception as e:
            outs[lg] = "ERR:" + type(e).__name__
    want = form.replace("he ", "", 1).strip()
    return did, {"stem": stem, "v": vib, "n": vac, "want": form, "got": outs, "ok": any(want in o.split("/") for o in outs.values())}


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--workers", type=int, default=8); ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    db = sqlite3.connect(DB)
    rows = db.execute("select id,label,result_slp1 from derivations where kind='subanta' and source like 'ashta%' order by id").fetchall()
    if a.limit:
        rows = rows[: a.limit]
    sut = {}
    for did, in db.execute("select id from derivations where kind='subanta' and source like 'ashta%'"):
        pass
    with ProcessPoolExecutor(a.workers) as ex:
        res = [r for r in ex.map(_cell, rows, chunksize=40) if r]
    out = dict(res)
    for did in out:
        s = db.execute("select sutras from steps where deriv_id=?", (did,)).fetchall()
        out[did]["sutras"] = sorted({x for (t,) in s for x in re.findall(r"\d+\.\d+\.\d+", t or "")})
    OUT.write_text(json.dumps({str(k): v for k, v in out.items()}, ensure_ascii=False, indent=0))
    print(len(out), "cells;", sum(v["ok"] for v in out.values()), "pass")
    bad = collections.Counter(s for v in out.values() if not v["ok"] for s in v["sutras"])
    print(bad.most_common(40))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
