"""
engine/coverage.py — Article 16: coverage is firing, not registration.
──────────────────────────────────────────────────────────────────────

A sūtra counts as **implemented** only when all four hold:

  1. invoked   — some derivation in the test suite calls it;
  2. moved     — it changes the state (or is ``r1_form_identity_exempt``);
  3. cited     — its file names the source that justifies its predicate (Art. 14);
  4. tested    — the test suite exercises it by id.

Everything else is **registered**. The two counts are reported separately and
the registered count may never be presented as coverage (Art. 16).

Conditions 1 and 2 are facts about execution, so they come from a *ledger*
produced by running the suite once with the instrumentation in
``tools/firing_coverage.py``::

    python3 -m tools.firing_coverage        # writes sig/firing_coverage.json

Conditions 3 and 4 are facts about the repository and are read from disk.

Condition 4 is currently satisfied by "the id appears in a test"; the finer
requirement of Art. 16 — ≥3 positive and ≥2 negative tests — needs test-level
metadata and lands with ``sutra_lint`` (ROADMAP Phase A2). Until then the
report exposes ``tested_ge5`` as a rough proxy and says so.
"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterable

_ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = _ROOT / "sig" / "firing_coverage.json"

_SUTRA_ID_RE = re.compile(r"\b\d\.\d\.\d{1,3}\b")

# The placeholder gloss left by the scaffolding: "(सूत्रम् 6.1.104) नादिचि।"
_PLACEHOLDER_WHY = re.compile(r"\(सूत्रम्\s")

# Art. 14 roster markers: an ashtadhyayi.com row index, or a named commentary.
# Art. 14's *minimum* citation is source #1 (row index) plus source #2 (Kāśikā),
# so those are the markers that matter. Later-tier commentaries are deliberately
# absent here — Art. 3 keeps their names out of the engine tree entirely.
_CITATION_MARKERS = (
    "काशिका", "Kāśikā", "Kasika", "Kāśikāvṛtti",
    "महाभाष्य", "Mahābhāṣya", "Mahabhasya",
    "परिभाषेन्दुशेखर", "Paribhāṣenduśekhara",
    "ashtadhyayi.com", "GRETIL",
)
_ROW_INDEX_RE = re.compile(r"\bi\s*=\s*\d{5}\b")


# ─────────────────────────────────────────────────────────────────
# ledger (conditions 1 and 2)
# ─────────────────────────────────────────────────────────────────

def load_ledger(path: Path | None = None) -> Dict[str, Any] | None:
    """The firing ledger, or None when the suite has not been instrumented yet."""
    p = path or LEDGER_PATH
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


# ─────────────────────────────────────────────────────────────────
# repository facts (conditions 3 and 4)
# ─────────────────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _cited_ids() -> frozenset[str]:
    """Sūtra ids whose file names an Art. 14 source and is not a placeholder."""
    cited: set[str] = set()
    for path in (_ROOT / "sutras").rglob("sutra_*.py"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        head = text[:4000]                       # docstring + record header
        has_source = _ROW_INDEX_RE.search(head) or any(m in head for m in _CITATION_MARKERS)
        if not has_source:
            continue
        m = re.search(r'sutra_id\s*=\s*"([\d.]+)"', text)
        if m and not _PLACEHOLDER_WHY.search(text):
            cited.add(m.group(1))
    return frozenset(cited)


@lru_cache(maxsize=1)
def _test_mentions() -> Dict[str, int]:
    """How many times each sūtra id is named under ``tests/``."""
    counts: Dict[str, int] = {}
    for path in (_ROOT / "tests").rglob("*.py"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for sid in _SUTRA_ID_RE.findall(text):
            counts[sid] = counts.get(sid, 0) + 1
    return counts


# ─────────────────────────────────────────────────────────────────
# the report
# ─────────────────────────────────────────────────────────────────

def honest_coverage(
    registry: Dict[str, Any],
    ledger: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """Article 16's report: registered and implemented, counted separately."""
    ledger = ledger if ledger is not None else load_ledger()
    invoked = frozenset(ledger.get("invoked", ())) if ledger else frozenset()
    moved = frozenset(ledger.get("moved", ())) if ledger else frozenset()
    cited = _cited_ids()
    mentions = _test_mentions()

    registered = sorted(registry)
    exempt = {
        sid for sid, rec in registry.items()
        if getattr(rec, "r1_form_identity_exempt", False)
    }

    def conditions(sid: str) -> Dict[str, bool]:
        return {
            "invoked": sid in invoked,
            "moved": sid in moved or (sid in invoked and sid in exempt),
            "cited": sid in cited,
            "tested": mentions.get(sid, 0) > 0,
        }

    per_sutra = {sid: conditions(sid) for sid in registered}
    implemented = sorted(sid for sid, c in per_sutra.items() if all(c.values()))

    def count(key: str) -> int:
        return sum(1 for c in per_sutra.values() if c[key])

    total = len(registered)
    return {
        # Article 16 headline
        "registered": total,
        "implemented": len(implemented),
        "implemented_pct": round(100.0 * len(implemented) / total, 2) if total else 0.0,
        "implemented_ids": implemented,
        # the four conditions, so the near-misses are visible and actionable
        "conditions": {
            "invoked": count("invoked"),
            "moved": count("moved"),
            "cited": count("cited"),
            "tested": count("tested"),
        },
        # the immediate worklist: rules that do real work but are not yet countable
        "moving_but_uncited": sorted(
            sid for sid, c in per_sutra.items() if c["moved"] and not c["cited"]
        ),
        "tested_ge5": sum(1 for sid in registered if mentions.get(sid, 0) >= 5),
        "ledger": str(LEDGER_PATH.relative_to(_ROOT)) if ledger else None,
        "ledger_generated_at": (ledger or {}).get("generated_at"),
        "notes": (
            "Art. 16: 'implemented' requires invoked + moved + cited + tested. "
            "The ≥3 positive / ≥2 negative split lands with sutra_lint (Phase A2); "
            "'tested' here means the id is exercised by at least one test."
            + ("" if ledger else " NO LEDGER: run 'python3 -m tools.firing_coverage'.")
        ),
    }


def worklist(report: Dict[str, Any], limit: int = 50) -> Iterable[str]:
    """Sūtras that already do real work and only lack a citation — cite these first."""
    return report["moving_but_uncited"][:limit]
