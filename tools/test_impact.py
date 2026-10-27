"""
tools/test_impact.py — which tests can a change reach? (test-impact selection)
─────────────────────────────────────────────────────────────────────────────

The recorder wraps each registered ``cond`` and notes, per test, every sūtra whose cond came out true or that ``apply_rule`` dispatched.
Written to ``sig/test_impact.json`` (git-ignored; regenerate with ``record``).

Known limit — widening: if an edit makes a cond true where it was always false, no recorded test names it, so ``quick`` can miss
that test (recording *consulted* conds instead selects ~88 % of the suite for one sūtra: the scanner asks every cond every step).
So ``quick`` is the fast loop and the full serial run at the end of a batch is the proof; for a cond you widened, also run the
tests of that sūtra's own prakaraṇa by name.

    python3 -m tools.test_impact record              # one full run (≈ the full suite); writes the map
    python3 -m tools.test_impact quick               # run only the tests a git change can reach
    python3 -m tools.test_impact quick --base HEAD~3 # changes since a commit
    python3 -m tools.test_impact why                 # print the selection, run nothing

Selection (sound by construction, never narrower than the dependency):
  * a changed ``sutras/**/sutra_A_B_C.py`` → the tests that consulted sūtra A.B.C;
  * a changed shared file (engine, pipelines, phonology, core, data) → every test; tools/api/docs select nothing;
  * a test absent from the map (new, edited, or run in a subprocess) always runs; so does a test file that changed;
  * tests/constitutional always run (they read source, not derivations).
"""
from __future__ import annotations

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


def select(items_ids: list[str], base: str = "HEAD") -> tuple[list[str], str]:
    """(node ids to run, why)."""
    files = [f for f in changed_files(base) if f.endswith((".py", ".json")) and not f.startswith(("docs/", "sig/", ".audit/", "scratch/"))]
    test_files = {f for f in files if f.startswith("tests/")}
    src = [f for f in files if not f.startswith("tests/")]
    if not MAP_PATH.exists():
        return items_ids, "no map yet: run `python3 -m tools.test_impact record`"
    other = [f for f in src if not _SUTRA_FILE.match(f) and f.startswith(_SHARED)]
    if other:
        return items_ids, f"shared source changed ({other[0]}{' …' if len(other) > 1 else ''}): every test can reach it"
    ids = {".".join(m.groups()) for f in src if (m := _SUTRA_FILE.match(f))}
    mapped = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    run = []
    for nid in items_ids:
        f = nid.split("::")[0]
        entry = mapped.get(nid)
        if entry is None or f in test_files or f.startswith("tests/constitutional/") or ids & set(entry["s"]):
            run.append(nid)
    return run, f"{len(ids)} sūtra file(s) changed: {', '.join(sorted(ids)) or 'none'}"


# ── pytest plugin ──────────────────────────────────────────────────────────

def pytest_addoption(parser):
    g = parser.getgroup("test-impact")
    g.addoption("--impact-record", action="store_true", help="record the sūtras each test consults → sig/test_impact.json")
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
    global _CURRENT
    if item.config.getoption("--impact-record"):
        _CURRENT = set()


def pytest_runtest_teardown(item):
    global _CURRENT
    if item.config.getoption("--impact-record") and _CURRENT is not None:
        _MAP[item.nodeid] = {"s": sorted(_CURRENT)}
        _CURRENT = None


def pytest_sessionfinish(session, exitstatus):
    if session.config.getoption("--impact-record") and _MAP:
        MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
        merged = json.loads(MAP_PATH.read_text(encoding="utf-8")) if MAP_PATH.exists() else {}
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
    if cmd == "quick":
        return pytest.main(["tests", *args, "--impact", *base])
    if cmd == "why":
        return pytest.main(["tests", *args, "--impact", "--collect-only", *base])
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
