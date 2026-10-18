"""The rule loop must not depend on Python's set hashing (glass box: the same request, the same derivation).

Before the fix, PYTHONHASHSEED=2 made pac laṭ diverge (pacmi): ``tape_fingerprint`` repr'd meta sets, so two equal
tapes could look different and a vacuous rule look effective.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from engine.scheduler import tape_fingerprint
from engine.state import State, Term

ROOT = Path(__file__).resolve().parents[2]
_SCRIPT = """
import json, sys
sys.path.insert(0, '.')
import sutras
from types import SimpleNamespace as NS
from tools.autonomy_report import run_autonomously, start_state
out = {}
for root, lak, pu, vc in (("pac", "laT", 1, 1), ("pac", "laT", 3, 3), ("BU", "luG", 3, 1)):
    run = run_autonomously(start_state(NS(kind="tinanta", args=(root, lak, pu, vc), pada=None)), "", root, 250)
    out[f"{root} {lak} {pu}-{vc}"] = [run.surface, [s[0] for s in run.steps]]
print(json.dumps(out))
"""


def _derive_under(seed: int) -> dict:
    env = dict(os.environ, PYTHONHASHSEED=str(seed))
    p = subprocess.run([sys.executable, "-c", _SCRIPT], cwd=ROOT, env=env, capture_output=True, text=True, timeout=600)
    assert p.returncode == 0, p.stderr[-2000:]
    return json.loads(p.stdout.strip().splitlines()[-1])


def test_same_derivation_under_every_seed():
    runs = {seed: _derive_under(seed) for seed in (0, 2, 7)}
    assert runs[0]["pac laT 1-1"][0] == "pacAmi"
    assert runs[0] == runs[2] == runs[7]


def test_fingerprint_ignores_set_insertion_order():
    a, b = set(), set()
    for x in ("Rit", "it", "Udit", "zit", "kit"):
        a.add(x)
    for x in reversed(("Rit", "it", "Udit", "zit", "kit")):
        b.add(x)
    ta = Term(kind="prakriti", meta={"dhatu_it": a, "nested": {"s": set(a)}})
    tb = Term(kind="prakriti", meta={"nested": {"s": set(b)}, "dhatu_it": b})
    assert tape_fingerprint(State(terms=[ta])) == tape_fingerprint(State(terms=[tb]))
