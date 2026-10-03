"""
tools/sutra_class.py — one row per sūtra; the source of every number in
docs/SUTRA_COVERAGE_100_PLAN.md and of the per-phase "confident" list.

    python3 -m tools.sutra_class            # writes sig/sutra_class.json + docs/CONFIDENT_SUTRAS.md

"confident" is stricter than Art. 16's `implemented`: the exemption flag does NOT
count as movement, a gate-only placeholder never counts, and tests must name the
sūtra ≥5 times (proxy for ≥3 positive + ≥2 negative until test metadata exists).
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import sutras  # noqa: F401 — fills SUTRA_REGISTRY
from engine import SUTRA_REGISTRY
from engine.coverage import _PLACEHOLDER_WHY, _cited_ids, _test_mentions, load_ledger

ROOT = Path(__file__).resolve().parent.parent
OPERATIONAL = {"VIDHI", "NIYAMA", "NIPATANA", "ATIDESHA", "VIBHASHA"}
MIN_MENTIONS = 5


def _key(sid: str):
    return tuple(int(x) for x in sid.split("."))


def _source(sid: str) -> str:
    a, b, c = sid.split(".")
    p = ROOT / f"sutras/adhyaya_{a}/pada_{b}/sutra_{a}_{b}_{c}.py"
    return p.read_text(encoding="utf-8") if p.exists() else ""


def rows() -> list[dict]:
    ledger = load_ledger() or {}
    invoked, moved = set(ledger.get("invoked", ())), set(ledger.get("moved", ()))
    cited, mentions = _cited_ids(), _test_mentions()
    out = []
    for sid in sorted(SUTRA_REGISTRY, key=_key):
        rec = SUTRA_REGISTRY[sid]
        src = _source(sid)
        typ = rec.sutra_type.name
        r = dict(
            id=sid, pada=".".join(sid.split(".")[:2]), type=typ,
            exempt=bool(getattr(rec, "r1_form_identity_exempt", False)),
            placeholder="return samhita_gate_eligible" in src,
            stub_gloss=bool(_PLACEHOLDER_WHY.search(src)),
            invoked=sid in invoked, moved=sid in moved,
            cited=sid in cited, mentions=mentions.get(sid, 0),
        )
        if typ in OPERATIONAL:
            ok = r["invoked"] and r["moved"] and r["cited"] and not r["placeholder"] \
                and r["mentions"] >= MIN_MENTIONS
            r["status"] = "confident" if ok else (
                "working" if r["invoked"] and r["moved"] and not r["placeholder"] else
                "placeholder" if r["placeholder"] else
                "unexercised" if not r["invoked"] else "gate_only")
        else:  # structural / definitional: invoked, cited, tested, real cond
            ok = r["invoked"] and r["cited"] and not r["placeholder"] and r["mentions"] >= 1
            r["status"] = "confident_structural" if ok else "pending_structural"
        out.append(r)
    return out


def main() -> None:
    rs = rows()
    (ROOT / "sig/sutra_class.json").write_text(json.dumps(
        {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "min_mentions": MIN_MENTIONS, "rows": rs}, ensure_ascii=False, indent=1), encoding="utf-8")

    total = Counter(r["status"] for r in rs)
    by_pada = defaultdict(list)
    for r in rs:
        if r["status"].startswith("confident"):
            by_pada[r["pada"]].append(r)
    n_conf = sum(len(v) for v in by_pada.values())
    L = ["# Sūtras the engine does confidently (generated — do not edit)", "",
         f"Generated {datetime.now(timezone.utc):%Y-%m-%d} by `python3 -m tools.sutra_class`. "
         f"**{n_conf} of {len(rs)}** are confident.", "",
         "*Operational*: invoked + really moves the tape (exempt flag ignored) + cited + not a "
         f"gate-only placeholder + named in tests ≥{MIN_MENTIONS}×. *(S)* = structural/definitional "
         "class: invoked + cited + tested + real cond (class proof pending, plan §1).", "",
         "| status | count |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(total.items())] + [""]
    pr = Counter(r["pada"] for r in rs)
    L += ["| pāda | confident | of |", "|---|---|---|"]
    for p in sorted(pr, key=_key):
        L.append(f"| {p} | {len(by_pada.get(p, []))} | {pr[p]} |")
    L.append("")
    for p in sorted(by_pada, key=_key):
        ids = ", ".join(r["id"].split(".", 2)[2] + ("ˢ" if r["status"] == "confident_structural" else "")
                        for r in by_pada[p])
        L.append(f"**{p}** — {ids}  ")
    L.append("\nˢ = structural class.")
    (ROOT / "docs/CONFIDENT_SUTRAS.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(dict(total), "confident:", n_conf)


if __name__ == "__main__":
    main()
