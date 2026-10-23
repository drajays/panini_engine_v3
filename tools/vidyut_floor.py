"""tools/vidyut_floor.py — the Vidyut floor on the brain's Vidyut-sourced tiṅanta derivations (T10: a minimum, never a template).
For each 'dhātu (id) Lakāra Prayoga Puruṣa Vacana → form' derivation: derive the cell, compare the sūtras Vidyut fired with the
sūtras this engine applied (trace APPLIED). Output docs/data/vidyut_floor.json: per-derivation missing sūtras, plus a ranked summary.
    python3 -m tools.vidyut_floor [--limit N]"""
import argparse, collections, json, pathlib, re, sqlite3, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
DB = pathlib.Path.home() / "data-master/ashtadhyayi-ai/db/ashtadhyayi.db"
OUT = pathlib.Path("docs/data/vidyut_floor.json")
LAK = {"Lat": "laT", "Lit": "liT", "Lut": "luT", "Lrt": "lRT", "Lot": "loT", "Lan": "laG", "VidhiLin": "liG", "AshirLin": "AsIrliG", "Lun": "luG", "Lrn": "lRG"}
PU = {"Prathama": 3, "Madhyama": 2, "Uttama": 1}
VC = {"Eka": 1, "Dvi": 2, "Bahu": 3}


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int, default=0); a = ap.parse_args()
    import sutras  # noqa: F401
    from pipelines.tinanta import derive
    db = sqlite3.connect(DB)
    out, n = {}, 0
    for did, label, res in db.execute("select id,label,result_slp1 from derivations where kind='tinanta' order by id"):
        m = re.match(r".*\((\d\d\.\d{4})\) (\w+) (Kartari) (\w+) (\w+) → (\S+)", label)
        if not m or m.group(2) not in LAK:
            continue
        ref, lak, _, pu, vc, form = m.groups()
        steps = db.execute("select sutras from steps where deriv_id=? order by step_no", (did,)).fetchall()
        floor = sorted({s for (x,) in steps for s in re.findall(r"\d+\.\d+\.\d+", x or "")}, key=lambda s: tuple(map(int, s.split("."))))
        mine, got = set(), "ERR"
        for pada in (None, "atmane"):          # Vidyut's label does not name the pada: the form decides
            try:
                st = derive(ref, LAK[lak], "kartari", PU[pu], VC[vc], **({"pada": pada} if pada else {}))
                mine = {t["sutra_id"] for t in st.trace if t.get("status") == "APPLIED"}
                got = st.flat_slp1()
            except Exception as e:
                got = type(e).__name__
            if got == form:
                break
        out[str(did)] = {"cell": [ref, LAK[lak], PU[pu], VC[vc]], "form": form, "got": got, "ok": got == form,
                         "missing": [s for s in floor if s not in mine]}
        n += 1
        if a.limit and n >= a.limit:
            break
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=0))
    miss = collections.Counter(s for v in out.values() for s in v["missing"])
    print(len(out), "derivations;", sum(v["ok"] for v in out.values()), "same form;", len(miss), "sūtras missing somewhere")
    print(miss.most_common(40))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
