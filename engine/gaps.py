"""
engine/gaps.py — Article 18: a gap is an output.

When the engine cannot derive or cannot analyse, it must say **what is
missing**, naming the sūtra, the dhātu or the lexical entry that would close
the gap. Silence is a bug.

What counts as a gap here is deliberately narrow. The suite produces 164,048
SKIPPED steps, and almost all of them are the scheduler asking a rule whose
condition is correctly false — that is the machine working, not a gap.
Reporting those would bury the signal. Three shapes are real:

``unscheduled``
    At some point in a derivation a registered sūtra's own ``cond`` was true,
    **applying it there would have changed the form**, and no pipeline ever
    asked it. The second half is what makes this a signal: the scheduler
    offers hundreds of candidates per state, most of them saṃjñā or
    placeholder rules that would leave the tape exactly as it is. Without the
    dry run, 40 cells produce 17,285 "gaps"; with it, only rules that would
    have done something are named.

``missing_data``
    The derivation was refused for want of a lexical entry: a dhātu absent
    from the dhātupāṭha, a stem absent from the śabda list. शास्ति fails this
    way, and no sūtra is at fault.

``oracle_disagreement``
    The derivation finished and an independent implementation disagrees
    (Art. 19). The missing rule is unknown; the cell is the evidence.

An ``unscheduled`` finding has two possible readings, and both are worth a
human: either the rule belongs in that pipeline and is missing, or its
``cond`` is too loose and it would have fired where it must not. 7.3.101
offering to write *rāmaṇe → rāmāṇe* inside a **subanta** is the second kind —
that rule is the tiṅanta one, and सुपि च (7.3.102) governs sup. The report
names the rule and the write it wanted to make; the scholar decides which
reading is right.

Gaps aggregate into a frequency-ranked worklist, and that list — not
intuition — orders implementation.
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Callable, Iterator

_MISSING_DATA_RE = re.compile(
    r"not found in dh[āa]tup[āa][ṭt]ha|unknown dh[āa]tu|no entry for|"
    r"unknown sūtra|not in the lexicon|has no entry",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Gap:
    """One named thing the engine could not do, and what would close it."""

    kind: str          # unscheduled | missing_data | oracle_disagreement
    subject: str       # the sūtra id, dhātu, or cell that names the gap
    detail: str        # what would close it, in one line
    where: str         # the derivation it showed up in

    def __str__(self) -> str:
        return f"{self.kind}: {self.subject} — {self.detail}  [{self.where}]"


@dataclass
class GapProbe:
    """Watch a derivation and record the sūtras that were never asked.

    Install **before** importing any pipeline: pipelines bind ``apply_rule``
    at import time, so a probe installed afterwards sees nothing.

        with GapProbe() as probe:
            from pipelines.subanta import derive
            derive("rAma", 1, 2)
        probe.gaps("rAma 1-2")
    """

    fired: list[str] = field(default_factory=list)
    offered: dict[str, int] = field(default_factory=dict)
    max_probed: int = 250
    _snapshots: dict[str, Any] = field(default_factory=dict)
    _restore: Callable[[], None] | None = None

    def __enter__(self) -> "GapProbe":
        import engine
        import engine.dispatcher as dispatcher
        from engine.scheduler import enumerate_candidates

        original = dispatcher.apply_rule

        def probing_apply_rule(sutra_id: str, state: Any, *args: Any, **kwargs: Any) -> Any:
            result = original(sutra_id, state, *args, **kwargs)
            self.fired.append(sutra_id)
            try:
                for candidate in enumerate_candidates(result):
                    if candidate in self.offered:
                        continue
                    self.offered[candidate] = len(self.fired)
                    if len(self._snapshots) < self.max_probed:
                        try:
                            self._snapshots[candidate] = result.clone()
                        except Exception:
                            pass
            except Exception:
                pass                      # a probe may never break a derivation
            return result

        dispatcher.apply_rule = probing_apply_rule
        engine.apply_rule = probing_apply_rule

        def restore() -> None:
            dispatcher.apply_rule = original
            engine.apply_rule = original

        self._restore = restore
        return self

    def __exit__(self, *exc: Any) -> None:
        if self._restore:
            self._restore()

    def reset(self) -> None:
        self.fired.clear()
        self.offered.clear()
        self._snapshots.clear()

    def gaps(self, where: str) -> list[Gap]:
        """Offered, never asked, **and** it would have changed the form."""
        from engine.dispatcher import apply_rule as _dispatch   # the real one

        asked = set(self.fired)
        out: list[Gap] = []
        for sutra_id, step in sorted(self.offered.items(), key=lambda kv: kv[1]):
            if sutra_id in asked:
                continue
            snapshot = self._snapshots.get(sutra_id)
            if snapshot is None:
                continue
            try:
                before = snapshot.flat_slp1()
                after = _dispatch(sutra_id, snapshot.clone()).flat_slp1()
            except Exception:
                continue
            if after == before:
                continue                  # would have been vacuous: not a gap
            out.append(Gap(
                kind="unscheduled",
                subject=sutra_id,
                detail=(f"after step {step} it would have written "
                        f"{before} → {after}, and no pipeline asked it"),
                where=where,
            ))
        return out


def gap_from_exception(exc: BaseException, where: str) -> Gap | None:
    """A refusal for want of data is a gap that names the datum, not a crash."""
    message = str(exc)
    if isinstance(exc, (KeyError, LookupError)) or _MISSING_DATA_RE.search(message):
        return Gap(
            kind="missing_data",
            subject=_subject_of(message) or type(exc).__name__,
            detail=message.strip('"').strip()[:200],
            where=where,
        )
    return None


_QUOTED_RE = re.compile(r"'([^']{1,40})'")


def _subject_of(message: str) -> str:
    hit = _QUOTED_RE.search(message)
    return hit.group(1) if hit else ""


def oracle_gaps(report: dict[str, Any]) -> Iterator[Gap]:
    """Bench disagreements as gaps (Art. 19 → Art. 18)."""
    for item in report.get("disagreements", ()):
        yield Gap(
            kind="oracle_disagreement",
            subject=item["key"],
            detail=f"we derive {item['ours']}, the oracle derives "
                   f"{'|'.join(item['theirs'])}",
            where="bench",
        )


def rank(gaps: list[Gap]) -> list[dict[str, Any]]:
    """The worklist: what is missing, how often, and where it showed up."""
    counts: Counter[tuple[str, str]] = Counter()
    examples: dict[tuple[str, str], list[str]] = {}
    details: dict[tuple[str, str], str] = {}
    for gap in gaps:
        key = (gap.kind, gap.subject)
        counts[key] += 1
        details.setdefault(key, gap.detail)
        examples.setdefault(key, [])
        if len(examples[key]) < 3:
            examples[key].append(gap.where)
    return [
        {
            "kind": kind,
            "subject": subject,
            "count": n,
            "detail": details[(kind, subject)],
            "seen_in": examples[(kind, subject)],
        }
        for (kind, subject), n in counts.most_common()
    ]
