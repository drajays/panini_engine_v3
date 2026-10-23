"""tools/brain_prakriya_gauge.py — the brain's authentic prakriyās as an oracle for the engine.
Each tiṅanta derivation in the brain (ashtadhyayi.com prakriyā) names its dhātu (<{path id}>), its lakāra (the 'xxx + law/liw…' step)
and its tiṅ (the next step). We derive the same cell and compare the final form; the sūtras the brain lists on that prakriyā
get an evidence row (pass/fail). Output: docs/data/prakriya_gauge.json {deriv_id: {...}} and a per-sūtra summary.
    python3 -m tools.brain_prakriya_gauge [--limit N] [--offset K]
Authority: the brain's prakriyā is a source (T-tier by its own tag), never a template; a failure is a work item or a verdict."""
import argparse, collections, json, pathlib, re, sqlite3, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
DB = pathlib.Path.home() / "data-master/ashtadhyayi-ai/db/ashtadhyayi.db"
OUT = pathlib.Path("docs/data/prakriya_gauge.json")
LAK = {"law": "laT", "liw": "liT", "luw": "luT", "lfw": "lRT", "low": "loT", "laN": "laG", "liN": "liG", "luN": "luG", "lfN": "lRG"}
TIN = {"tip": (3, 1, "parasmai"), "tas": (3, 2, "parasmai"), "Ji": (3, 3, "parasmai"), "sip": (2, 1, "parasmai"), "Tas": (2, 2, "parasmai"),
       "Ta": (2, 3, "parasmai"), "mip": (1, 1, "parasmai"), "vas": (1, 2, "parasmai"), "mas": (1, 3, "parasmai"),
       "ta": (3, 1, "atmane"), "AtAm": (3, 2, "atmane"), "Ja": (3, 3, "atmane"), "TAs": (2, 1, "atmane"), "ATAm": (2, 2, "atmane"),
       "Dvam": (2, 3, "atmane"), "iw": (1, 1, "atmane"), "vahi": (1, 2, "atmane"), "mahiN": (1, 3, "atmane")}


def parse(steps):
    """(dhatu_id, lakara, purusha, vacana, pada) or None. Steps are (no, sutras, state_slp1, note)."""
    if len(steps) < 3:
        return None
    m = re.search(r"<\{([0-9]+\.[0-9]+)\}>", steps[0][3] or "")
    lak = re.fullmatch(r"\S+ \+ (law|liw|luw|lfw|low|laN|liN|luN|lfN)", (steps[1][2] or "").strip())   # one dhātu, no upasarga / sanādi
    tin = re.fullmatch(r"\S+ \+ (\w+)", (steps[2][2] or "").strip())
    if not (m and lak and tin) or tin.group(1) not in TIN:
        return None
    pid = m.group(1)
    g, n = pid.split(".")
    pu, vc, pada = TIN[tin.group(1)]
    return f"{int(g):02d}.{int(n):04d}", LAK[lak.group(1)], pu, vc, pada


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int, default=0); ap.add_argument("--offset", type=int, default=0)
    a = ap.parse_args()
    import sutras  # noqa: F401
    from pipelines.tinanta import derive
    db = sqlite3.connect(DB)
    ders = db.execute("select id, label, result_slp1 from derivations where kind='sutrartha' order by id").fetchall()
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    done = n = 0
    for did, label, res in ders[a.offset:]:
        if str(did) in out:
            continue
        steps = db.execute("select step_no, sutras, state_slp1, note from steps where deriv_id=? order by step_no", (did,)).fetchall()
        req = parse(steps)
        if not req:
            continue
        ref, lak, pu, vc, pada = req
        want = {x.strip(" .") for x in re.split(r"[/,]", res.replace("-->", "")) if x.strip(" .")}
        try:
            got = derive(ref, lak, "kartari", pu, vc, pada=pada).flat_slp1()
            status = "pass" if got in want else "fail"
        except Exception as e:
            got, status = type(e).__name__, "error"
        sut = sorted({s.strip() for st in steps for s in (st[1] or "").split(",") if re.fullmatch(r"\d+\.\d+\.\d+", s.strip())})
        out[str(did)] = {"label": label, "cell": [ref, lak, pu, vc, pada], "want": sorted(want), "got": got, "status": status, "sutras": sut}
        n += 1
        if a.limit and n >= a.limit:
            break
        if n % 100 == 0:
            OUT.write_text(json.dumps(out, ensure_ascii=False, indent=0)); print(n, flush=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=0))
    print(collections.Counter(v["status"] for v in out.values()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
