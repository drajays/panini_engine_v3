"""
Every adhikāra gate a sūtra cites must name a registered ADHIKARA whose declared
``adhikara_scope`` covers the citing sūtra (H ≤ sūtra ≤ scope_end(H)); an
अर्थनिर्देश head (Art. 20) also covers back to ``artha_nirdesha.purva_from``.

A gate outside its head's scope can never open (``engine.gates.adhikara_in_effect``
enforces ``scope_end``) — 518 taddhita modules once cited 5.1.1, whose scope
ends at 5.1.17, and silently never fired.
"""
from __future__ import annotations

import ast
from pathlib import Path

import sutras  # noqa: F401
from engine import SutraType
from engine.registry import get_sutra

_SUTRAS = Path(__file__).resolve().parents[2] / "sutras"


def _t(sid: str) -> tuple[int, ...]:
    return tuple(int(p) for p in sid.split("."))


def _const(node) -> str | None:
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None


def _gate_citations():
    """(file, citing sūtra, cited head) for literal adhikara_in_effect / adhikara_id= gates."""
    for path in sorted(_SUTRAS.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for n in ast.walk(tree):
            if not isinstance(n, ast.Call):
                continue
            name = getattr(n.func, "id", None) or getattr(n.func, "attr", None)
            if name == "adhikara_in_effect" and len(n.args) >= 3:
                sid, head = _const(n.args[0]), _const(n.args[2])
                if sid and head:
                    yield path.relative_to(_SUTRAS.parent), sid, head
            for kw in n.keywords:
                if kw.arg == "adhikara_id" and len(n.args) >= 2:
                    sid, head = _const(n.args[1]), _const(kw.value)
                    if sid and head:
                        yield path.relative_to(_SUTRAS.parent), sid, head


def test_every_gate_cites_an_adhikara_whose_scope_covers_it():
    cites = list(_gate_citations())
    assert len(cites) > 1500, "gate scan found too few citations — scanner broken?"
    bad = []
    for rel, sid, head in cites:
        rec = get_sutra(head)
        if rec.sutra_type is not SutraType.ADHIKARA:
            bad.append(f"{rel}: {sid} cites {head}, which is {rec.sutra_type.name}, not ADHIKARA")
            continue
        start, end = rec.adhikara_scope
        if rec.artha_nirdesha is not None:
            start = rec.artha_nirdesha.purva_from
        if not (start and end):
            bad.append(f"{rel}: {sid} cites {head}, which declares no scope")
        elif not (_t(start) <= _t(sid) <= _t(end)):
            bad.append(f"{rel}: {sid} cites {head} (scope {start}–{end})")
    assert not bad, f"{len(bad)} gates outside their head's scope:\n" + "\n".join(bad[:40])
