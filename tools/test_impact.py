"""
tools/test_impact.py — which tests can a change reach? (test-impact selection)
─────────────────────────────────────────────────────────────────────────────

The recorder wraps each registered ``cond`` and notes, per test, every sūtra whose cond came out true or that ``apply_rule`` dispatched.
Written to ``sig/test_impact.json`` (git-ignored; regenerate with ``record``).

Known limit — widening: if an edit makes a cond true where it was always false, no recorded test names it, so ``quick`` can miss
that test (recording *consulted* conds instead selects ~88 % of the suite for one sūtra: the scanner asks every cond every step).
So ``quick`` is the fast loop and the full serial run at the end of a batch is the proof; for a cond you widened, also run the
tests of that sūtra's own prakaraṇa by name.

    python3 -m tools.test_impact record-lite -n8     # sūtras only, no profiler, parallel: ≈ one full run; writes the map
    python3 -m tools.test_impact record              # + per-function profile (10×+ slower, serial): lets shared-source edits select too
    python3 -m tools.test_impact quick               # run only the tests a git change can reach
    python3 -m tools.test_impact quick --base HEAD~3 # changes since a commit
    python3 -m tools.test_impact why                 # print the selection, run nothing

Selection (sound by construction, never narrower than the dependency):
  * a changed ``sutras/**/sutra_A_B_C.py`` → the tests that consulted sūtra A.B.C;
  * a changed shared .py file → the tests that called one of the functions whose lines changed (``f`` in the map, recorded with
    ``sys.setprofile``); a change outside any function (imports, module/class body, decorators) or in a non-.py shared file → every test;
    tools/api/docs select nothing;
  * a test absent from the map (new, edited, or run in a subprocess) always runs; so does a test file that changed;
  * tests/constitutional always run (they read source, not derivations).
"""
from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

MAP_PATH = _ROOT / "sig" / "test_impact.json"
_SUTRA_FILE = re.compile(r"^sutras/adhyaya_\d+/pada_\d+/sutra_(\d+)_(\d+)_(\d+)\.py$")

# Source that every derivation runs through. tools/, api/, docs/, audit/, Makefile … never shape a derivation, so they select nothing.
_SHARED = ("engine/", "pipelines/", "phonology/", "core/", "data/", "sutras/__init__", "sutras/_", "tests/conftest", "conftest", "pytest.ini")

_CURRENT: set[str] | None = None
_MAP: dict[str, dict[str, Any]] = {}
_FUNCS: list[str] = []                    # "file::qualname" table, indexed by the "f" lists in the map (append-only on disk)
_FIDX: dict[str, int] = {}
_FCUR: set[int] | None = None
_CODE: dict[Any, int | None] = {}         # code object → function index (None: not shared source)
_TABLE = "__funcs__"


# ── recording ──────────────────────────────────────────────────────────────

class _Consulting:
    """A ``cond`` that notes it was consulted. Keeps ``__code__`` so static checks on the original (``is_gate_only``) still see it."""

    def __init__(self, sid: str, fn):
        self._sid, self._fn = sid, fn
        self.__code__ = getattr(fn, "__code__", None)
        self.__name__ = getattr(fn, "__name__", "cond")
        self.__wrapped__ = fn

    def __call__(self, state):
        out = self._fn(state)
        if out and _CURRENT is not None:
            _CURRENT.add(self._sid)          # only a cond that came out true shapes a derivation (see the module note on widening)
        return out


def _profile(frame, event, arg):
    if event != "call" or _FCUR is None:
        return
    code = frame.f_code
    i = _CODE.get(code, -1)
    if i == -1:
        rel = code.co_filename[len(str(_ROOT)) + 1:] if code.co_filename.startswith(str(_ROOT)) else ""
        i = None
        if rel.endswith(".py") and rel.startswith(_SHARED) and not _SUTRA_FILE.match(rel) and code.co_name != "<module>":
            key = f"{rel}::{code.co_qualname}"
            i = _FIDX.setdefault(key, len(_FUNCS))
            if i == len(_FUNCS):
                _FUNCS.append(key)
        _CODE[code] = i
    if i is not None:
        _FCUR.add(i)


def _install() -> None:
    import sutras  # noqa: F401  (fills the registry)
    from engine import SUTRA_REGISTRY

    for sid, rec in SUTRA_REGISTRY.items():
        if rec.cond is not None and not isinstance(rec.cond, _Consulting):
            object.__setattr__(rec, "cond", _Consulting(sid, rec.cond))

    import engine
    import engine.dispatcher as dispatcher

    original = dispatcher.apply_rule

    def noting_apply_rule(sutra_id, state, *a, **k):
        if _CURRENT is not None:
            _CURRENT.add(sutra_id)
        return original(sutra_id, state, *a, **k)

    dispatcher.apply_rule = noting_apply_rule
    engine.apply_rule = noting_apply_rule


# ── selection ──────────────────────────────────────────────────────────────

def _git(*args: str) -> list[str]:
    out = subprocess.run(["git", *args], cwd=_ROOT, capture_output=True, text=True, check=True).stdout
    return [l for l in out.splitlines() if l]


def changed_files(base: str = "HEAD") -> list[str]:
    return sorted(set(_git("diff", "--name-only", base)) | set(_git("ls-files", "--others", "--exclude-standard")))


def _qualnames(tree: ast.AST):
    """(first line incl. decorators, last line, qualname) for every def, nested ones as ``f.<locals>.g`` like ``co_qualname``."""
    def walk(node, prefix, in_func):
        for ch in ast.iter_child_nodes(node):
            if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef)):
                q = prefix + ch.name
                yield min([ch.lineno, *(d.lineno for d in ch.decorator_list)]), ch.end_lineno, q
                yield from walk(ch, q + ".<locals>.", True)
            elif isinstance(ch, ast.ClassDef):
                yield from walk(ch, prefix + ch.name + ".", in_func)
            else:
                yield from walk(ch, prefix, in_func)
    return list(walk(tree, "", False))


def changed_functions(path: str, base: str = "HEAD") -> set[str] | None:
    """Qualnames of the defs whose lines the diff touches, or None if any hunk lies outside every def (or the file is new/unparsable)."""
    defs = _qualnames(ast.parse((_ROOT / path).read_text(encoding="utf-8"))) if (_ROOT / path).exists() else None
    if defs is None or path in _git("ls-files", "--others", "--exclude-standard"):
        return None
    out: set[str] = set()
    for h in _git("diff", "-U0", base, "--", path):
        if not (m := re.match(r"@@ -\S+ \+(\d+)(?:,(\d+))?", h)):
            continue
        a, n = int(m[1]), int(m[2] or 1)
        lo, hi = (a, a + n - 1) if n else (a, a + 1)     # n == 0: pure deletion between lines a and a+1
        inside = [q for s, e, q in defs if s <= hi and e >= lo and (n or (s < a + 1 <= e))]
        if not inside:
            return None
        out |= set(inside)
    return out


_IMPORT = re.compile(r"sutra_(\d+)_(\d+)_(\d+)")


def with_importers(ids: set[str]) -> set[str]:
    """A sūtra file that another sūtra file imports (iyanuvan_sthana, NGIT_SUPS …) changes the other's behaviour too: close the set over
    'imports sutra_A_B_C' so a test that fired only the importer is still selected."""
    graph: dict[str, set[str]] = {}
    for f in (_ROOT / "sutras").rglob("sutra_*.py"):
        m = _SUTRA_FILE.match(str(f.relative_to(_ROOT)))
        if not m:
            continue
        me = ".".join(m.groups())
        for a, b, c in _IMPORT.findall(f.read_text(encoding="utf-8")):
            dep = f"{a}.{b}.{c}"
            if dep != me:
                graph.setdefault(dep, set()).add(me)
    out, todo = set(ids), list(ids)
    while todo:
        for importer in graph.get(todo.pop(), ()):
            if importer not in out:
                out.add(importer)
                todo.append(importer)
    return out


def select(items_ids: list[str], base: str = "HEAD") -> tuple[list[str], str]:
    """(node ids to run, why)."""
    files = [f for f in changed_files(base) if f.endswith((".py", ".json")) and not f.startswith(("docs/", "sig/", ".audit/", "scratch/"))]
    test_files = {f for f in files if f.startswith("tests/")}
    src = [f for f in files if not f.startswith("tests/")]
    if not MAP_PATH.exists():
        return items_ids, "no map yet: run `python3 -m tools.test_impact record`"
    shared = [f for f in src if not _SUTRA_FILE.match(f) and f.startswith(_SHARED)]
    mapped = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    table = mapped.pop(_TABLE, [])
    funcs: set[int] = set()
    for f in shared:
        names = changed_functions(f, base) if f.endswith(".py") else None
        if names is None:
            return items_ids, f"shared source changed outside a function ({f}): every test can reach it"
        funcs |= {table.index(k) for n in names if (k := f"{f}::{n}") in table}
    ids = with_importers({".".join(m.groups()) for f in src if (m := _SUTRA_FILE.match(f))})
    run = []
    for nid in items_ids:
        f = nid.split("::")[0]
        entry = mapped.get(nid)
        if entry is None or f in test_files or f.startswith("tests/constitutional/") or ids & set(entry["s"]) or "f" not in entry or funcs & set(entry["f"]):
            run.append(nid)
    return run, f"{len(ids)} sūtra file(s), {len(funcs)} mapped function(s) changed: {', '.join(sorted(ids)) or 'none'}"


# ── pytest plugin ──────────────────────────────────────────────────────────

def pytest_addoption(parser):
    g = parser.getgroup("test-impact")
    g.addoption("--impact-record", action="store_true", help="record the sūtras each test consults → sig/test_impact.json")
    g.addoption("--impact-lite", action="store_true", help="with --impact-record: sūtras only (no per-function profile, ~free; a shared-source change then selects every test)")
    g.addoption("--impact", action="store_true", help="run only the tests the git change can reach")
    g.addoption("--impact-base", default="HEAD", help="git ref to diff against (default HEAD)")


def pytest_configure(config):
    if config.getoption("--impact-record"):
        _install()


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--impact"):
        return
    keep, why = select([i.nodeid for i in items], config.getoption("--impact-base"))
    kept = set(keep)
    config.hook.pytest_deselected(items=[i for i in items if i.nodeid not in kept])
    items[:] = [i for i in items if i.nodeid in kept]
    print(f"\n[test_impact] {len(items)} test(s) selected — {why}")


def pytest_runtest_call(item):
    global _CURRENT, _FCUR
    if item.config.getoption("--impact-record"):
        _CURRENT, _FCUR = set(), set()
        if not item.config.getoption("--impact-lite"):
            sys.setprofile(_profile)


def pytest_runtest_teardown(item):
    global _CURRENT, _FCUR
    if item.config.getoption("--impact-record") and _CURRENT is not None:
        if not item.config.getoption("--impact-lite"):
            sys.setprofile(None)
        _MAP[item.nodeid] = {"s": sorted(_CURRENT)} if item.config.getoption("--impact-lite") else {"s": sorted(_CURRENT), "f": sorted(_FCUR or ())}
        _CURRENT = _FCUR = None


_PARTS = _ROOT / "sig" / ".impact_parts"


def pytest_sessionfinish(session, exitstatus):
    worker = getattr(session.config, "workerinput", None)
    if worker is not None:                       # an xdist worker: hand the controller our share, do not touch the shared file
        if session.config.getoption("--impact-record") and _MAP:
            _PARTS.mkdir(parents=True, exist_ok=True)
            (_PARTS / f"{worker['workerid']}.json").write_text(json.dumps({"map": _MAP, "funcs": _FUNCS}), encoding="utf-8")
        return
    if session.config.getoption("--impact-record") and _PARTS.exists():
        for part in sorted(_PARTS.glob("*.json")):
            got = json.loads(part.read_text(encoding="utf-8"))
            base = len(_FUNCS)
            _FUNCS.extend(got["funcs"])
            for nid, e in got["map"].items():
                _MAP[nid] = {"s": e["s"], **({"f": [i + base for i in e["f"]]} if "f" in e else {})}
            part.unlink()
        _PARTS.rmdir()
    if session.config.getoption("--impact-record") and _MAP:
        MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
        merged = json.loads(MAP_PATH.read_text(encoding="utf-8")) if MAP_PATH.exists() else {}
        table = merged.get(_TABLE, [])           # append-only, so indices in older entries stay valid
        pos = {k: i for i, k in enumerate(table)}
        for k in _FUNCS:
            if k not in pos:
                pos[k] = len(table)
                table.append(k)
        for e in _MAP.values():
            if "f" in e:
                e["f"] = sorted(pos[_FUNCS[i]] for i in e["f"])
        merged[_TABLE] = table
        merged.update(_MAP)                      # a partial run refreshes its own tests and keeps the rest
        MAP_PATH.write_text(json.dumps(merged, ensure_ascii=False, separators=(",", ":"), sort_keys=True), encoding="utf-8")
        print(f"\n[test_impact] {len(_MAP)} tests (re)mapped → {MAP_PATH.relative_to(_ROOT)}")


def main(argv: list[str] | None = None) -> int:
    import pytest

    args = list(argv if argv is not None else sys.argv[1:])
    cmd = args.pop(0) if args else "quick"
    base = ["-p", "tools.test_impact", "-q", "-p", "no:cacheprovider"]
    if cmd == "record":
        return pytest.main(["tests", *args, "--impact-record", *base])
    if cmd == "record-lite":                       # sūtras only, cheap enough to run under xdist:  record-lite -n8
        return pytest.main(["tests", *args, "--impact-record", "--impact-lite", *base])
    if cmd == "quick":
        return pytest.main(["tests", *args, "--impact", *base])
    if cmd == "why":
        return pytest.main(["tests", *args, "--impact", "--collect-only", *base])
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
