"""Multi-agent gate: claims, preflight, scope check, ratchet compare. Stdlib only.

  python -m tools.agent_gate claim ID "6.1.97 6.1.98" [--out "…"]   (AGENT=name)
  python -m tools.agent_gate release ID
  python -m tools.agent_gate status
  python -m tools.agent_gate preflight 6.1.97
  python -m tools.agent_gate scope [--staged]      (AGENT=name → strict)
  python -m tools.agent_gate ratchets [--base REF]
Scope entries: sūtra IDs ("6.1.97") or path globs ("engine/foo.py", "tools/**").
"""
from __future__ import annotations
import fnmatch, json, os, re, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "audit" / "claims.json"
TTL = 48 * 3600
HOTSPOTS = ["engine/scheduler.py", "engine/resolver.py", "engine/core_loop.py",
            "engine/dispatcher.py", "pipelines/tinanta.py", "CONSTITUTION.md"]
RATCHETS = {  # file -> constant; each may only go DOWN vs base
    "tests/constitutional/test_no_new_duplicates.py": "MAX_DUPLICATE_GROUPS",
    "tests/constitutional/test_no_new_arm_gates.py": "ARM_GATE_BASELINE",
    "tests/constitutional/test_glassbox_ratchet.py": "MAX_TRACE_GAPS",
    "tests/constitutional/test_exempt_ratchet.py": "BASELINE",
}
SID = re.compile(r"^\d\.\d\.\d+$")


def sh(*a):
    return subprocess.run(a, cwd=ROOT, capture_output=True, text=True).stdout


def load():
    c = json.loads(CLAIMS.read_text()) if CLAIMS.exists() else []
    now = time.time()
    return [x for x in c if x["status"] != "released" and now - x["updated"] < TTL]


def save(all_claims):
    CLAIMS.write_text(json.dumps(all_claims, indent=1, ensure_ascii=False) + "\n")


def globs(scope):
    out = []
    for s in scope:
        if SID.match(s):
            a, p, _ = s.split(".")
            out.append(f"sutras/adhyaya_{a}/pada_{p}/sutra_{s.replace('.', '_')}*.py")
        else:
            out.append(s)
    return out


def overlap(g1, g2):
    return any(fnmatch.fnmatch(a, b) or fnmatch.fnmatch(b, a)
               or a.rstrip("*/") .startswith(b.rstrip("*/")) or b.rstrip("*/").startswith(a.rstrip("*/"))
               for a in g1 for b in g2)


def cmd_claim(id_, scope, out=""):
    agent = os.environ.get("AGENT", "human")
    sc = scope.split()
    if any(s in ("*", "**", "sutras", "sutras/", "sutras/**") for s in sc) or not sc:
        sys.exit("REFUSED: scope too broad; name exact sūtra IDs/paths")
    allc = json.loads(CLAIMS.read_text()) if CLAIMS.exists() else []
    live = load()
    if any(c["id"] == id_ for c in live):
        sys.exit(f"REFUSED: claim id {id_} exists")
    g = globs(sc)
    for c in live:
        if overlap(g, globs(c["scope"])):
            sys.exit(f"REFUSED: overlaps live claim {c['id']} ({c['agent']}): {c['scope']}")
    hot = [h for h in HOTSPOTS if overlap(g, [h])]
    allc.append(dict(id=id_, agent=agent, scope=sc, out_of_scope=out, status="in-progress",
                     hotspots=hot, updated=time.time()))
    save(allc)
    print(f"claimed {id_} for {agent}" + (f"  (HOTSPOT — coordinator only: {hot})" if hot else ""))


def cmd_release(id_):
    allc = json.loads(CLAIMS.read_text())
    for c in allc:
        if c["id"] == id_:
            c["status"] = "released"; c["updated"] = time.time()
    save(allc); print("released", id_)


def cmd_status():
    for c in load():
        print(f"{c['id']:<14}{c['agent']:<10}{c['status']:<12}{' '.join(c['scope'])}")
    print("(no live claims)" if not load() else "")


def cmd_preflight(sid):
    if not SID.match(sid):
        sys.exit("usage: preflight <a.b.c>")
    g = globs([sid])[0]
    files = sorted(p.relative_to(ROOT) for p in ROOT.glob(g))
    print(f"sūtra file : {files[0] if files else 'NONE (new rule)'}")
    tok = sid.replace(".", "_")
    print("tests      :", sh("git", "ls-files", "tests").count("\n") and
          [l for l in sh("git", "grep", "-l", "-E", f"{sid.replace('.', r'\.')}|{tok}", "--", "tests").split()][:8])
    print("pipelines  :", sh("git", "grep", "-l", f'"{sid}"', "--", "pipelines", "engine").split()[:8])
    live = [c for c in load() if overlap(globs([sid]), globs(c["scope"]))]
    print("live claim :", [(c["id"], c["agent"]) for c in live] or "none")
    if live:
        sys.exit("BLOCKED: already claimed")
    if files:
        print("NOTE: exists — task must be 'fix/extend', not 'add'. Read it + its tests first.")


def changed(staged):
    if staged:
        return sh("git", "diff", "--cached", "--name-only").split()
    br = os.environ.get("BASE_REF", "origin/main")
    return sh("git", "diff", "--name-only", f"{br}...HEAD").split() or sh("git", "diff", "--name-only", "HEAD").split()


def cmd_scope(staged):
    files = changed(staged)
    agent, live = os.environ.get("AGENT"), load()
    bad = []
    for f in files:
        owners = [c for c in live if any(fnmatch.fnmatch(f, g) for g in globs(c["scope"]))]
        mine = [c for c in owners if c["agent"] == agent]
        if agent and not mine:
            bad.append(f"{f}: outside {agent}'s claims" + (f" (owned by {owners[0]['agent']})" if owners else ""))
        elif not agent and owners and not os.environ.get("ALLOW_CLAIMED"):
            bad.append(f"{f}: claimed by {owners[0]['agent']} ({owners[0]['id']}); set ALLOW_CLAIMED=1 to override")
        elif any(f == h for h in HOTSPOTS) and not os.environ.get("COORDINATOR"):
            bad.append(f"{f}: hotspot, set COORDINATOR=1")
    if bad:
        sys.exit("SCOPE FAIL\n  " + "\n  ".join(bad))
    print(f"scope ok ({len(files)} files)")


def const(text, name):
    m = re.search(rf"^{name}\s*=\s*(\d+)", text, re.M)
    return int(m.group(1)) if m else None


def cmd_ratchets(base):
    bad = []
    for f, n in RATCHETS.items():
        now = const((ROOT / f).read_text(), n)
        old = const(sh("git", "show", f"{base}:{f}"), n)
        print(f"{n:<24}{old} -> {now}")
        if now is None or (old is not None and now > old):
            bad.append(f"{n} loosened/missing ({old} -> {now})")
    if bad:
        sys.exit("RATCHET FAIL: " + "; ".join(bad))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    c = a[0]
    if c == "claim": cmd_claim(a[1], a[2], a[a.index("--out") + 1] if "--out" in a else "")
    elif c == "release": cmd_release(a[1])
    elif c == "status": cmd_status()
    elif c == "preflight": cmd_preflight(a[1])
    elif c == "scope": cmd_scope("--staged" in a)
    elif c == "ratchets":
        b = a[a.index("--base") + 1] if "--base" in a else ("origin/main" if sh("git", "rev-parse", "--verify", "-q", "origin/main").strip() else "HEAD")
        cmd_ratchets(b)
    else: sys.exit(__doc__)
