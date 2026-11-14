"""Neelesh Bodas, प्रक्रियापद्धति: worked examples (fixtures/prakriya_paddhati_gold.json): the attested form is among the readings and the
sūtras he orders occur in that order in the trace. Divergences found by the cross-check (docs/PRAKRIYA_PADDHATI_CROSSCHECK.md) are listed, not hidden."""
import json
import pathlib

import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from tools.exercise_audit import _derive

ITEMS = json.loads((pathlib.Path(__file__).parents[1] / "fixtures" / "prakriya_paddhati_gold.json").read_text())["items"]
# id -> why his order is not the engine's (engine order differs; the form is the same). P4a stage-audit inputs.
ORDER_DIVERGES = {
    "pp1.2b": "engine does 3.4.78 (tiP) before 6.4.71 (aT); Bodas: aT (stage 2) before the adesha of l (stage 3)",
    "pp6.3": "engine: 3.4.100 before 3.4.103 and no 3.4.107 (suT) in vidhi-liN; Bodas: yAsuT + suT, then 3.4.100",
}


def _spec(it):
    a = it["args"]
    if it["kind"] == "subanta":
        return ("subanta", a[0], a[3], a[1], a[2])
    if it["kind"] == "tinanta":
        return ("tinanta", *a)
    return ("krdanta", a[0], None, a[3], a[1], a[2], tuple(a[4].items()))


@pytest.mark.parametrize("it", ITEMS, ids=lambda i: i["id"])
def test_paddhati_example(it):
    branches = explore(lambda: _derive(_spec(it)))
    hit = [b for b in branches if b.surface_slp1 in it["expected"]]
    assert hit, f'{it["id"]}: {it["expected"]} not among {sorted(b.surface_slp1 for b in branches)}'
    if it["kind"] == "krdanta" or it["id"] in ORDER_DIVERGES:     # krdanta stem trace lives in chain.krt, not in the sup state
        return
    ids = [t.get("sutra_id") for t in hit[0].state.trace if t.get("status") in ("APPLIED", "APPLIED_VACUOUS")]
    for x, y in it["order"]:
        assert x in ids and y in ids and ids.index(x) < ids.index(y), f'{it["id"]}: {x} before {y} ({it["note"]})'
