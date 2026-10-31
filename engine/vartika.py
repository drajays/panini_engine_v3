"""engine/vartika.py — vārttikas / Bhāṣya rulings living INSIDE their host sūtra (Art. 25, docs/AMENDMENT_29.md).

The sūtra is the only unit that fires. A ``Vartika`` is an entry of the host's ``vartikas`` tuple; ``compose`` folds the
live entries into the host's own cond/act, so scheduler, resolver and dispatcher see one sūtra id (Art. 16 credits the host).
Relations to the host: ``apavada`` (displaces the host's own act where both hold), ``extension`` (adds a site the host
does not reach), ``restriction`` (withholds the host's own act where it holds). Paribhāṣās are NOT copied here: an entry
names them by id (``PS<num>``, data/inputs/paribhasha_shekhara.json)."""
from __future__ import annotations

import contextlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Tuple

RELATIONS = frozenset({"apavada", "extension", "restriction"})
TIERS = frozenset({"T1", "T2"})             # Art. 22: Kātyāyana, Patañjali (a vārttika / Bhāṣya ruling)
META_KEY = "__vartika__"
DISABLED: set = set()                        # tiers switched off for audit (disabled_tiers)
_PS = Path(__file__).resolve().parent.parent / "data" / "inputs" / "paribhasha_shekhara.json"


@dataclass(frozen=True)
class Vartika:
    id: str                                   # '4.2.43.v4' = host + '.v' + the vārttika's number in the host's Bhāṣya
    source: str                               # 'Kātyāyana vā. 4 (Bhāṣya 5368)'
    tier: str                                 # Art. 22 'T1' | 'T2'
    relation: str                             # RELATIONS
    text_dev: str                             # verbatim from the DB (texts, source 'vartika'/'bhashya')
    cond: Callable[[Any], bool]               # Art. 2: reads the tape only
    act: Callable[[Any], Any]
    paribhasha: Tuple[str, ...] = ()          # ids into the shared paribhāṣā layer, named in the trace when used

    @property
    def n(self) -> str:
        return self.id.rsplit(".v", 1)[1]


def paribhasha_ids() -> frozenset:
    return frozenset("PS" + e["num"] for e in json.loads(_PS.read_text())["entries"])


def validate(host_id: str, vs: Tuple[Vartika, ...]) -> None:
    seen = set()
    for v in vs:
        if not re.fullmatch(re.escape(host_id) + r"\.v\d+", v.id) or v.id in seen:
            raise ValueError(f"[{host_id}] vartika id {v.id!r} must be '{host_id}.v<n>', once")
        seen.add(v.id)
        if v.tier not in TIERS or v.relation not in RELATIONS:
            raise ValueError(f"[{v.id}] tier {v.tier!r} / relation {v.relation!r} not allowed")
        if not (v.source.strip() and v.text_dev.strip() and callable(v.cond) and callable(v.act)):
            raise ValueError(f"[{v.id}] needs source, text_dev, cond and act")
        if set(v.paribhasha) - paribhasha_ids():
            raise ValueError(f"[{v.id}] unknown paribhāṣā id in {v.paribhasha}")


def _live(vs, state, relation):
    return [v for v in vs if v.relation == relation and v.tier not in DISABLED and v.cond(state)]


def compose(host_id: str, own_cond, own_act, vs: Tuple[Vartika, ...]):
    """The host's cond/act with its vārttikas folded in (one Art. 21 rung: apavāda over the host's own, else the host's own)."""
    validate(host_id, vs)

    def _own(state) -> bool:
        return bool(own_cond(state)) and not _live(vs, state, "restriction")

    def cond(state) -> bool:
        return _own(state) or bool(_live(vs, state, "apavada") or _live(vs, state, "extension"))

    def act(state):
        win = (_live(vs, state, "apavada") or ([] if _own(state) else _live(vs, state, "extension")))
        if not win:
            return own_act(state)
        v = win[0]
        out = v.act(state)
        out.meta[META_KEY] = {"vartika": v.id, "vartika_label": f"{host_id} + vā. {v.n}", "vartika_source": v.source,
                              "vartika_tier": v.tier, "paribhasha": list(v.paribhasha)}
        return out

    return cond, act


@contextlib.contextmanager
def disabled_tiers(*tiers: str):
    """Audit switch: run with the vārttikas of these tiers ('T1', 'T2') off."""
    from engine import scheduler
    old = set(DISABLED)
    DISABLED.update(tiers)
    scheduler._EFFECTIVE_MEMO.clear()
    try:
        yield
    finally:
        DISABLED.clear()
        DISABLED.update(old)
        scheduler._EFFECTIVE_MEMO.clear()
