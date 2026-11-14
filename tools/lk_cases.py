"""tools/lk_cases.py — the LK case gate: do a sūtra's use-case tests prove it works?

    python3 -m tools.lk_cases init  ~/lk_unexercised_tests.json   # owner JSON -> tests/fixtures/lk_cases.json (skeleton; spec filled later)
    python3 -m tools.lk_cases run [7.1 4.1.41 ...]                # run the cases -> sig/lk_case_verdicts/aN.json
    python3 -m tools.lk_cases summary                             # grades + FAIL sūtras by sub-kind (engine_error, not_fired, mismatch, …)

Case = {text, expected (SLP1), positive, spec (tools.exercise_audit tuple, or null = not yet machine-runnable), source (citation)}.
  positive: expected ∈ the vikalpa readings AND the sūtra is APPLIED in the branch that gives it (exercise_audit.attempt).
  negative: the sūtra must NOT be APPLIED in any branch giving `expected` (or `expected` is not produced at all when expected is a wrong form).
  mutation (positives only, recorded not required): with the sūtra's cond forced False the form either changes ("sensitive") or still arises
            by another route ("redundant": the rules that replaced it are listed) — honest evidence, never a pass/fail by itself.
Grade (per sūtra): FAIL if any runnable case fails · working: ≥1 positive passes, none fail · confident: ≥3 positives + ≥2 negatives pass, ≥2 distinct
sourced forms, none fail. Cases without a spec count as `unrunnable` and never as passes."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXD = ROOT / "tests/fixtures/lk_cases"          # one file per adhyāya (a1.json … a8.json): agents never share a file
OUTD = ROOT / "sig/lk_case_verdicts"            # one file per adhyāya, same reason


def _key(s: str):
    return tuple(int(x) for x in s.split("."))


def init(src: str) -> None:
    raw = json.loads(Path(src).read_text(encoding="utf-8"))
    old = load()
    out = {}
    for sid in sorted(raw, key=_key):
        have = {c["text"]: c for c in old.get(sid, [])}
        out[sid] = [have.get(c["spec"]) or {"text": c["spec"], "expected_iast": c["expected"], "expected": None, "positive": c["positive"],
                                           "spec": None, "source": None} for c in raw[sid]]
    for a in sorted({k.split(".")[0] for k in out}):
        (FIXD / f"a{a}.json").write_text(json.dumps({k: v for k, v in out.items() if k.startswith(a + ".")}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(out)} sūtras, {sum(len(v) for v in out.values())} cases -> {FIXD.relative_to(ROOT)}/")


def load() -> dict:
    out: dict = {}
    for f in sorted(FIXD.glob("a*.json")):
        out.update(json.loads(f.read_text(encoding="utf-8")))
    return out


def _norm_spec(spec):
    spec = list(spec)
    if spec[0] == "krdanta" and len(spec) > 6 and isinstance(spec[6], list):
        spec[6] = tuple(tuple(p) for p in spec[6])
    return tuple(spec)


def _mutate(sid, spec, expected):
    """disable `sid`, rerun: ('sensitive', None) | ('redundant', [replacing sūtras])"""
    from engine import SUTRA_REGISTRY
    from tools.exercise_audit import run, _norm
    rec = SUTRA_REGISTRY[sid]
    base, _ = run(spec)
    keep = rec.cond
    object.__setattr__(rec, "cond", lambda state: False)
    try:
        mut, err = run.__wrapped__(spec)        # run() is lru_cached: the cached reading is the unmutated one
    finally:
        object.__setattr__(rec, "cond", keep)
    if err or not any(_norm(s) == _norm(expected) for s, _ in mut):
        return "sensitive", None
    a = {k for s, seen in base if _norm(s) == _norm(expected) for k in seen}
    b = {k for s, seen in mut if _norm(s) == _norm(expected) for k in seen}
    rep = sorted(b - a, key=_key)[:8]
    return ("redundant" if rep else "indeterminate"), rep       # indeterminate: the form survives but no other rule shows up in the trace (cond-only sūtra, or its act is also done elsewhere)


def sub_kind(why: str) -> str:
    """Why a runnable case failed — reporting only, never a grade input:
    engine_error · not_fired (form right, the sūtra is not in that branch's trace) · mismatch (form wrong) ·
    over_applied (a negative: the sūtra fired) · over_generated (an excluded form is produced)."""
    if why.startswith("engine error"):
        return "engine_error"
    if "did not fire" in why:
        return "not_fired"
    if "applied in a branch" in why:
        return "over_applied"
    if why.startswith("excluded form"):
        return "over_generated"
    return "mismatch"


def check(sid: str, c: dict, typ: str, mutate: bool = True) -> dict:
    r = _check(sid, c, typ, mutate)
    if r["result"] == "fail":
        r["sub"] = sub_kind(r.get("why", ""))
    return r


def _check(sid: str, c: dict, typ: str, mutate: bool = True) -> dict:
    from tools.exercise_audit import attempt, run, _norm, OK_STATUS, _DEFAULT_OK
    if not c.get("spec") or not c.get("expected"):
        return {"result": "unrunnable"}
    spec = _norm_spec(c["spec"])
    if c["positive"]:
        r = attempt(spec, c["expected"], sid, typ)
        out = {"result": "pass" if r["ok"] else "fail", "why": r.get("why", ""), "spec": r.get("spec")}
        if r["ok"] and mutate:
            out["mutation"], out["replaced_by"] = _mutate(sid, tuple(r["spec"]), c["expected"])
        return out
    branches, err = run(spec)
    if err:
        return {"result": "fail", "why": f"engine error: {err}"}
    ok = OK_STATUS.get(typ, _DEFAULT_OK)
    giving = [(s, seen) for s, seen in branches if _norm(s) == _norm(c["expected"])]
    fired = [s for s, seen in giving if any(x in ok for x in seen.get(sid, ()))]
    kind = c.get("kind")          # "declined": the form IS produced, by a branch where the sūtra is declined/blocked · "produced": the form IS produced, the sūtra not applying · "excluded": a wrong form, never produced
    if fired:
        return {"result": "fail", "why": f"{sid} applied in a branch giving {c['expected']}"}
    if kind in ("declined", "produced") and not giving:      # "produced": the form must arise, by a route without the sūtra (वारिणा beside 7.1.74)
        return {"result": "fail", "why": f"{kind} reading {c['expected']} is not produced at all (readings {sorted({s for s, _ in branches})})"}
    if kind == "excluded" and giving:
        return {"result": "fail", "why": f"excluded form {c['expected']} is produced"}
    return {"result": "pass", "kind": kind or ("produced" if giving else "unproven"), "why": ""}     # produced: the form arises with the sūtra not applied · unproven: never produced, passes only vacuously


def grade(rows: list[dict], cases: list[dict]) -> str:
    runs = [r for r in rows if r["result"] != "unrunnable"]
    if any(r["result"] == "fail" for r in runs):
        return "FAIL"
    pos = [(r, c) for r, c in zip(rows, cases) if c["positive"] and r["result"] == "pass"]
    neg = [r for r, c in zip(rows, cases) if not c["positive"] and r["result"] == "pass" and r.get("kind") in ("produced", "declined", "excluded")]   # an unproven negative (never produced, no declared kind) is weak
    if len(pos) >= 3 and len(neg) >= 2 and len({c["expected"] for _, c in pos}) >= 3 and all(c.get("source") for _, c in pos):
        return "confident"
    return "working" if pos else ("UNRUNNABLE" if not runs else "NO_POSITIVE")


def run_all(filters: list[str]) -> None:
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY
    fx = load()
    OUTD.mkdir(exist_ok=True)
    done: set = set()
    prev = {}
    for f in OUTD.glob("a*.json"):
        prev.update(json.loads(f.read_text(encoding="utf-8")))
    for sid in sorted(fx, key=_key):
        if filters and not any(sid == f or sid.startswith(f + ".") for f in filters):
            continue
        done.add(sid)
        typ = SUTRA_REGISTRY[sid].sutra_type.name
        rows = [check(sid, c, typ) for c in fx[sid]]
        prev[sid] = {"grade": grade(rows, fx[sid]), "type": typ, "cases": rows}
        print(sid, prev[sid]["grade"], flush=True)
    for a in {k.split(".")[0] for k in done}:          # write only the adhyāyas this run touched: parallel runs per adhyāya never clobber each other
        (OUTD / f"a{a}.json").write_text(json.dumps({k: v for k, v in prev.items() if k.startswith(a + ".")}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    summary()


def verdicts() -> dict:
    out: dict = {}
    for f in sorted(OUTD.glob("a*.json")):
        out.update(json.loads(f.read_text(encoding="utf-8")))
    return out


def summary() -> None:
    """Grades, and each FAIL sūtra under the sub-kinds of its failing cases (a sūtra may sit under several)."""
    from collections import Counter, defaultdict
    v = verdicts()
    print("grades:", dict(Counter(r["grade"] for r in v.values())))
    by_sub = defaultdict(list)
    for sid in sorted(v, key=_key):
        if v[sid]["grade"] == "FAIL":
            for s in sorted({c.get("sub") or sub_kind(c.get("why", "")) for c in v[sid]["cases"] if c["result"] == "fail"}):
                by_sub[s].append(sid)
    for s, ids in sorted(by_sub.items()):
        print(f"FAIL/{s}: {len(ids)}  {' '.join(ids)}")


if __name__ == "__main__":
    if sys.argv[1] == "init":
        init(sys.argv[2])
    elif sys.argv[1] == "summary":
        summary()
    else:
        run_all(sys.argv[2:])
