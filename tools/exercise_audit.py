"""tools/exercise_audit.py — are the "unexercised" Laghukaumudī sūtras doing what they are supposed to do?

    python3 -m tools.exercise_audit                 # all unexercised LK sūtras → sig/exercise_audit.json + tests/regression/test_exercise_<adhyaya>.py
    python3 -m tools.exercise_audit 7.1 4.1.41      # only those pādas / sūtras (no test files are written)

For each sūtra whose status in sig/sutra_class.json is `unexercised` (and that is in docs/data/lk_worklist.json):
  * type (registry `sutra_type`) and sub-kind (the commonest gloss the attested derivations give that step: it-lopa, ādeśa, āgama …);
  * examples are ATTESTED ones from the reference database (ashtadhyayi.db: sutra_examples → derivations; the final form is the label's
    right-hand side, never invented). Vidyut forms are Tier-4 cross-validation of the surface only — never copied order (CONSTITUTION).
  * a call spec is built from the example (subanta cell, tiṅanta cell, kṛdanta+subanta, taddhita is NOT built: it needs the sense) and run through
    the engine's own pipelines.
Verdicts (honest, never relaxed):
  DONE        the engine's surface equals the attested form AND the sūtra is in the engine trace with a status that fits its type
              (VIDHI / VIBHASHA / ATIDESHA / NIPATANA: APPLIED; NIYAMA: APPLIED / AUDIT / VACUOUS); ≥ 1 positive. A negative (a derivation whose attested
              derivation lacks the sūtra) must not apply it, else NEEDS_OWNER (over-application or a Vidyut/ours order difference).
  FAIL        an example ran and the surface differs ("observed ≠ expected") or the form is right but the sūtra did not fire (another path made it)
              or the engine raised.
  NO_EXAMPLE  no attested example could be turned into an engine call (the reason lists the adapters that were missing).
"""
from __future__ import annotations

import collections
import contextlib
import io
import json
import re
import sqlite3
import sys
import time
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
DB = Path("/Users/dr.ajayshukla/data-master/ashtadhyayi-ai/db/ashtadhyayi.db")
OUT = ROOT / "sig" / "exercise_audit.json"

_VIB = {"Prathama": 1, "Dvitiya": 2, "Trtiya": 3, "Caturthi": 4, "Panchami": 5, "Sasthi": 6, "Saptami": 7, "Sambodhana": 8}
_VIB_DEV = {"प्रथमा": 1, "द्वितीया": 2, "तृतीया": 3, "चतुर्थी": 4, "पञ्चमी": 5, "षष्ठी": 6, "सप्तमी": 7, "सम्बोधनम्": 8}
_LINGA = {"Pum": "pulliṅga", "Stri": "strīliṅga", "Napumsaka": "napuṃsaka"}
_VAC = {"Eka": 1, "Dvi": 2, "Bahu": 3}
_PUR = {"Prathama": 3, "Madhyama": 2, "Uttama": 1}
_LAKARA = {"Lat": "laT", "Lit": "liT", "Lut": "luT", "Lrt": "lRT", "Lot": "loT", "Lan": "laG", "Lun": "luG", "Lrn": "lRG",     # the engine's own lakāra keys
           "VidhiLin": "liG", "AshirLin": "AsIrliG", "Let": None}
_SUP = {"su~": (1, 1), "O": (1, 2), "jas": (1, 3), "am": (2, 1), "Ow": (2, 2), "Sas": (2, 3), "wA": (3, 1), "Bis": (3, 3), "Ne": (4, 1),
        "Nasi~": (5, 1), "Nasi": (5, 1), "Nas": (6, 1), "Am": (6, 3), "Ni": (7, 1), "sup": (7, 3)}    # unambiguous sup → (vibhakti, vacana)
_PRAYOGA = {"Kartari": "kartari", "Karmani": "karmani", "Bhave": "bhave"}
OK_STATUS = {"VIDHI": {"APPLIED"}, "VIBHASHA": {"APPLIED"}, "ATIDESHA": {"APPLIED"}, "NIPATANA": {"APPLIED"},
             "NIYAMA": {"APPLIED", "AUDIT", "VACUOUS", "APPLIED_VACUOUS"}}
_DEFAULT_OK = {"APPLIED"}
MAX_TRY = 5          # examples tried per sūtra
MAX_POS, MAX_NEG = 3, 2


def _key(sid: str) -> tuple[int, ...]:
    return tuple(int(x) for x in sid.split("."))


def _db() -> sqlite3.Connection:
    return sqlite3.connect(f"file:{DB}?mode=ro", uri=True)


def _slp1(dev: str) -> str:
    from core.transliterate import dev_to_slp1
    return dev_to_slp1(dev)


# ── examples → call specs ───────────────────────────────────────────────────────────────────────

def _spec(label: str, source: str, kind: str, first: str, result: str):
    """(spec, expected_slp1, reason-if-none).  spec is a hashable tuple."""
    rhs = label.split("→", 1)[1].strip() if "→" in label else ""
    if rhs and any("ऀ" <= c <= "ॿ" for c in rhs):
        rhs = _slp1(rhs)
    expected = rhs or (result or "").strip()
    if not expected or "-->" in expected or "/" in expected or " " in expected.strip():
        return None, expected, "several forms in one example"
    if source == "vidyut" and kind == "subanta":
        m = re.match(r"^(\S+) (Pum|Stri|Napumsaka) (\S+) (Eka|Dvi|Bahu) →", label)
        if m and m.group(3) in _VIB:
            return ("subanta", m.group(1), _LINGA[m.group(2)], _VIB[m.group(3)], _VAC[m.group(4)]), expected, None
    if source == "vidyut" and kind == "tinanta":
        m = re.match(r"^.*? \((\d\d\.\d+)\) (\S+) (\S+) (\S+) (\S+) →", label)
        if m and _LAKARA.get(m.group(2)) and m.group(3) in _PRAYOGA and m.group(4) in _PUR:
            return ("tinanta", m.group(1), _LAKARA[m.group(2)], _PRAYOGA[m.group(3)], _PUR[m.group(4)], _VAC[m.group(5)]), expected, None
        return None, expected, "tiṅanta label not parseable (lakāra / prayoga outside the engine's set)"
    if source == "ashtadhyayi.com" and kind == "subanta":
        m = re.match(r"^(\S+) (\S+) (\d) →", label)
        stem = first.split("+")[0].strip()
        if m and m.group(2) in _VIB_DEV and re.match(r"^[A-Za-z]+$", stem):
            return ("subanta?", stem, None, _VIB_DEV[m.group(2)], int(m.group(3))), expected, None   # linga unknown: tried in turn
    m = re.match(r"^([A-Za-z]+) \+ ([A-Za-z~]+)$", (first or "").strip())     # "pati + wA": the first step names the stem and one sup
    if m and m.group(2) in _SUP and re.match(r"^[A-Za-z]+$", expected) and kind in ("subanta", "sutrartha"):
        return ("subanta?", m.group(1), None) + _SUP[m.group(2)], expected, None
    if kind == "krdanta":
        return None, expected, "kṛdanta: the engine has no generic krt+dhātu entry point"
    if kind in ("taddhita",):
        return None, expected, "taddhita: the sense (taddhitArtha) is not in the example"
    if kind == "sanadi":
        return None, expected, "sanādi: no generic entry point"
    return None, expected, "label shape not recognised"


@contextlib.contextmanager
def _quiet():
    with contextlib.redirect_stdout(io.StringIO()):
        yield


def _derive(spec: tuple):
    if spec[0] == "subanta":
        from pipelines.subanta import derive
        return derive(spec[1], spec[3], spec[4], linga=spec[2])
    if spec[0] == "tinanta":
        from pipelines.tinanta import derive
        return derive(spec[1], spec[2], spec[3], spec[4], spec[5], **({"pada": spec[6]} if len(spec) > 6 else {}))
    raise ValueError(spec[0])


@lru_cache(maxsize=None)
def run(spec: tuple):
    """→ ([(surface_slp1, {sutra_id: statuses})] over every vikalpa reading, error | None)"""
    import sutras  # noqa: F401
    from engine.vikalpa import explore
    try:
        with _quiet():
            branches = explore(lambda: _derive(spec))
            if not branches:
                _derive(spec)               # raises the engine's own reason
    except Exception as e:  # noqa: BLE001 — the engine's own gap, reported as the reason
        return [], f"{type(e).__name__}: {e}"[:160]
    out = []
    for b in branches:
        seen: dict[str, list[str]] = collections.defaultdict(list)
        for t in b.state.trace:
            seen[t.get("sutra_id", "")].append(t.get("status", ""))
        out.append((b.surface_slp1, {k: tuple(v) for k, v in seen.items()}))
    return out, (None if out else "no branch could be walked")


def _norm(x: str) -> str:
    return re.sub(r"[\s\\]", "", x or "")


@lru_cache(maxsize=None)
def _ubhayapadi(dhatu_id: str) -> bool:
    from pipelines.dhatupatha import resolve_dhatu_identifier
    try:
        return "उभय" in (resolve_dhatu_identifier(dhatu_id).get("pada_label_dev") or "")
    except Exception:  # noqa: BLE001
        return False


def attempt(spec, expected: str, sid: str, typ: str) -> dict:
    """Run one example (for `subanta?` try each liṅga). {ok, why, spec, observed, statuses}: ok = some reading equals the attested form AND fires the sūtra."""
    specs = [spec] if spec[0] != "subanta?" else [("subanta", spec[1], l, spec[3], spec[4]) for l in _LINGA.values()]
    if spec[0] == "tinanta" and _ubhayapadi(spec[1]):       # an ubhayapadī root has both padas; a strictly one-pada root is NOT forced (a real disagreement stays a FAIL)
        specs += [spec + ("parasmai",), spec + ("atmane",)]
    okst = OK_STATUS.get(typ, _DEFAULT_OK)
    best = None
    for sp in specs:
        branches, err = run(sp)
        if err:
            best = best or {"ok": False, "why": f"engine error: {err}", "spec": list(sp), "observed": None}
            continue
        match = [seen for surf, seen in branches if _norm(surf) == _norm(expected)]
        if not match:
            if not (best and best.get("observed")):
                best = {"ok": False, "why": f"readings {sorted({b[0] for b in branches})} ≠ expected {expected}", "spec": list(sp), "observed": ",".join(sorted({b[0] for b in branches}))}
            continue
        for seen in match:
            st = seen.get(sid, ())
            if any(x in okst for x in st):
                return {"ok": True, "why": "", "spec": list(sp), "observed": expected, "statuses": list(st)}
        best = {"ok": False, "why": f"form {expected} is right but {sid} did not fire (trace status {list(match[0].get(sid, ())) or 'absent'}): another path made it",
                "spec": list(sp), "observed": expected}
    return best or {"ok": False, "why": "no run", "spec": list(spec), "observed": None}


# ── the audit ───────────────────────────────────────────────────────────────────────────────────

def _unexercised(filters: list[str]) -> list[str]:
    rows = json.loads((ROOT / "docs/data/lk_worklist.json").read_text())
    st = {r["id"]: r["status"] for r in json.loads((ROOT / "sig/sutra_class.json").read_text())["rows"]}
    u = sorted((r["id"] for r in rows if st.get(r["id"], r["status"]) == "unexercised"), key=_key)
    return [i for i in u if not filters or any(i == f or i.startswith(f + ".") for f in filters)]


def _subkind(db: sqlite3.Connection, sid: str) -> str:
    c = collections.Counter()
    for (note,) in db.execute("select s.note from steps s where s.sutras like ? and s.note != '' limit 200", (f"%{sid}%",)):
        c[note.strip()[:40]] += 1
    return c.most_common(1)[0][0] if c else ""


@lru_cache(maxsize=None)
def _form_index(db_path: str = str(DB)) -> dict:
    """SECOND example source: surface (SLP1) → [(deriv, spec, expected)] over every runnable subanta/tiṅanta derivation in the DB."""
    idx: dict[str, list] = collections.defaultdict(list)
    for d, lab, src, kind, res in _db().execute("select id,label,source,kind,result_slp1 from derivations where kind in ('subanta','tinanta')"):
        first = (_db().execute("select state_slp1 from steps where deriv_id=? order by step_no limit 1", (d,)).fetchone() or ("",))[0]
        spec, expected, _ = _spec(lab, src, kind, first, res)
        if spec:
            idx[_norm(expected)].append((d, spec, expected))
    return idx


def prose_examples(db: sqlite3.Connection, sid: str) -> list:
    """Kāśikā + Laghukaumudī prose words for `sid` that the DB can turn into an engine call (the word must equal an attested derivation's final form)."""
    idx, out, seen = _form_index(), [], set()
    for (txt,) in db.execute("select content from texts where sutra_id=? and source in ('kashika','laghukaumudi') order by source", (sid,)):
        txt = re.sub(r"<<.*?>>|\[\[.*?\]\]|\{.*?\}|<\{.*?\}>", " ", txt)
        for w in re.findall(r"[\u0900-\u097f]+", txt):
            w = re.sub(r"[\u0964\u0965]", "", w)
            if len(w) < 2:
                continue
            f = _norm(_slp1(w))
            if f not in seen:
                seen.add(f)
                out += idx.get(f, [])[:1]
    return out


def audit(filters: list[str]) -> dict:
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY
    db = _db()
    sids = _unexercised(filters)
    by_deriv: dict[int, set[str]] = collections.defaultdict(set)
    for sid, d in db.execute("select sutra_id, deriv_id from sutra_examples"):
        by_deriv[d].add(sid)
    pool: dict[str, list] = collections.defaultdict(list)       # spec-kind → [(deriv, spec, expected)] for negatives
    out = {}
    t0 = time.time()
    for n, sid in enumerate(sids, 1):
        rec = SUTRA_REGISTRY.get(sid)
        typ = str(getattr(rec, "sutra_type", "")).split(".")[-1]
        row = {"id": sid, "type": typ, "subkind": _subkind(db, sid), "verdict": "NO_EXAMPLE", "examples_tried": 0, "positives": [], "negatives": [], "reasons": []}
        ex = db.execute("select distinct e.deriv_id from sutra_examples e where e.sutra_id=? order by e.deriv_id", (sid,)).fetchall()
        runnable = []
        for (d,) in ex:
            lab, src, kind, res = db.execute("select label, source, kind, result_slp1 from derivations where id=?", (d,)).fetchone()
            first = (db.execute("select state_slp1 from steps where deriv_id=? order by step_no limit 1", (d,)).fetchone() or ("",))[0]
            spec, expected, why = _spec(lab, src, kind, first, res)
            if spec is None:
                if why not in row["reasons"]:
                    row["reasons"].append(why)
                continue
            runnable.append((d, spec, expected))
        if not runnable:                       # second source: Kāśikā / Laghukaumudī prose words
            runnable = prose_examples(db, sid)
            if runnable:
                row["reasons"].append("examples from Kāśikā/Laghukaumudī prose")
        # spread the examples over distinct stems / dhātus before trying
        seen_keys, pick = set(), []
        for d, spec, expected in runnable:
            k = spec[1]
            if k not in seen_keys:
                seen_keys.add(k)
                pick.append((d, spec, expected))
        pick += [r for r in runnable if r not in pick]
        fails = []
        for d, spec, expected in pick[:MAX_TRY]:
            row["examples_tried"] += 1
            r = attempt(spec, expected, sid, typ)
            r.update(expected=expected, deriv=d)
            (row["positives"] if r["ok"] else fails).append(r)
            if len(row["positives"]) >= MAX_POS:
                break
            pool[spec[0].rstrip("?")].append((d, spec, expected))
        if row["positives"]:
            row["verdict"] = "DONE"
            kinds = {p["spec"][0] for p in row["positives"]}
            cands = [(d, sp, e) for k in kinds for (d, sp, e) in pool.get(k, []) if sid not in by_deriv.get(d, ())]
            for d, sp, e in cands[:MAX_NEG]:
                branches, err = run(sp if sp[0] != "subanta?" else ("subanta", sp[1], "pulliṅga", sp[3], sp[4]))
                fired = any(any(x in OK_STATUS.get(typ, _DEFAULT_OK) for x in seen.get(sid, ())) for surf, seen in branches if _norm(surf) == _norm(e))
                row["negatives"].append({"spec": list(sp), "expected": e, "deriv": d, "fires": bool(fired), "error": err})
            if any(x["fires"] for x in row["negatives"]):
                row["verdict"] = "NEEDS_OWNER"
                row["reasons"].append("fires where the attested derivation does not use it (over-application, or an order difference to the attested derivation)")
        elif fails:
            row["verdict"] = "FAIL"
            row["reasons"] = [f["why"] for f in fails[:3]] + row["reasons"]
        out[sid] = row
        if n % 25 == 0:
            print(f"[exercise_audit] {n}/{len(sids)} {time.time() - t0:.0f}s", file=sys.stderr)
    return out


def _write_tests(res: dict) -> list[str]:
    """tests/regression/test_exercise_<adhyaya>.py — DONE positives + clean negatives, each row naming its sūtra (≥5 mentions with the header + assertions)."""
    by_a: dict[str, list] = collections.defaultdict(list)
    for sid, r in res.items():
        if r["verdict"] == "DONE":
            by_a[sid.split(".")[0]].append(r)
    files = []
    for a, rows in sorted(by_a.items()):
        lines = [f'"""Generated by tools/exercise_audit.py from attested examples (ashtadhyayi.db); regenerate, do not edit. Adhyāya {a}."""',
                 "import pytest", "", "import sutras  # noqa: F401", "from tools.exercise_audit import run", "", "OK = {'APPLIED'}", "", "CASES = ["]
        for r in sorted(rows, key=lambda r: _key(r["id"])):
            for p in r["positives"]:
                lines.append(f"    ({r['id']!r}, True, {tuple(p['spec'])!r}, {p['expected']!r}, {r['type']!r}),   # {r['id']} positive: {r['subkind']}")
            for q in r["negatives"]:
                lines.append(f"    ({r['id']!r}, False, {tuple(q['spec'])!r}, {q['expected']!r}, {r['type']!r}),   # {r['id']} negative: not used by the attested derivation")
        lines += ["]", "",
                  "@pytest.mark.parametrize('sid,positive,spec,expected,typ', CASES, ids=lambda c: None)",
                  "def test_exercise(sid, positive, spec, expected, typ):",
                  "    ok = {'NIYAMA': {'APPLIED', 'AUDIT', 'VACUOUS', 'APPLIED_VACUOUS'}}.get(typ, OK)",
                  "    branches, err = run(spec)",
                  "    assert err is None, f'{sid}: {err}'",
                  "    match = [seen for surf, seen in branches if surf.replace(' ', '').replace(chr(92), '') == expected]",
                  "    fired = any(s in ok for seen in match for s in seen.get(sid, ()))",
                  "    if positive:",
                  "        assert match, f'{sid}: {expected} is not among the readings {[b[0] for b in branches]}'",
                  "        assert fired, f'{sid} did not fire for {expected}'",
                  "    else:",
                  "        assert not fired, f'{sid} fires where the attested derivation does not use it'", ""]
        p = ROOT / "tests" / "regression" / f"test_exercise_{a}.py"
        p.write_text("\n".join(lines), encoding="utf-8")
        files.append(str(p.relative_to(ROOT)))
    return files


def main(argv: list[str]) -> int:
    write = "--write" in argv
    argv = [a for a in argv if a != "--write"]
    res = audit(argv)
    if write and OUT.exists():          # a partial re-run: merge into the stored rows, then regenerate every test file
        old = json.loads(OUT.read_text())["rows"]
        old.update(res)
        res, argv = dict(sorted(old.items(), key=lambda kv: _key(kv[0]))), []
    c = collections.Counter(r["verdict"] for r in res.values())
    bt = collections.defaultdict(collections.Counter)
    for r in res.values():
        bt[r["type"]][r["verdict"]] += 1
    summary = {"verdicts": dict(c), "by_type": {k: dict(v) for k, v in bt.items()}, "n": len(res)}
    print(json.dumps(summary, ensure_ascii=False))
    if not argv:
        OUT.write_text(json.dumps({"summary": summary, "rows": res}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("tests:", _write_tests(res))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
