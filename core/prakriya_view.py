"""
core/prakriya_view.py — a derivation as the tradition writes it.

The trace is a flat list of rule firings. A reader wants the other shape: the
form after each change, and the sūtras that made it —

    → राम + टा   [ स्वौजसमौट्… ४.१.२ इति ]
    → राम + आ    [ उपदेशे इतस्य लोपः १.३.९ इति ]
    → रामेण      [ अट्कुप्वाङ्नुम्व्यवायेऽपि ८.४.२ इति णत्वम् ]

Two things make that readable and neither belongs in the engine:

* the trace stores the flat form, so a step reads रामटा where the tradition
  writes राम + टा. :class:`TermRecorder` wraps the dispatcher to capture the
  term split as the derivation runs;
* a saṃjñā that changed nothing is not dropped but folded into the bracket of
  the change it licensed, which is how the tradition cites it.

Presentation only: nothing here is read by a sūtra's ``cond`` or ``act``
(Art. 2), and the reading is always built from a live derivation — never
stored and replayed, which would make it a second grammar (Art. 17).
"""
from __future__ import annotations

import threading
from typing import Any

# Rows that describe rather than act: keep them as citations, never as steps.
QUIET_STATUSES = {"SKIPPED", "BLOCKED"}
# An adhikāra row is bookkeeping, not a reason; only the saṃjñās just before a
# change are worth citing with it.
LICENSING_STATUSES = {"APPLIED"}
MAX_LICENSING = 2


class TermRecorder:
    """Capture the tape's *term split* after each rule.

    The trace stores the flat form, so a step reads रामटा where the tradition
    writes राम + टा. The split is what makes a derivation legible, so it is
    recorded alongside — by wrapping the dispatcher, the way the coverage
    ledger does, rather than by changing the trace schema.

    Rebinding is process-wide, so two recorders running at once would write
    into each other's rows: the lock makes the recorded section serial. The
    API's threadpool makes that reachable — one request per browser cell.
    """

    _lock = threading.Lock()

    def __init__(self) -> None:
        self.rows: list[tuple[str, str]] = []
        self._restore = None

    def __enter__(self) -> "TermRecorder":
        TermRecorder._lock.acquire()
        try:
            return self._install()
        except Exception:            # never leave the lock held on a failure
            TermRecorder._lock.release()
            raise

    def _install(self) -> "TermRecorder":
        import engine
        import engine.dispatcher as dispatcher
        from phonology.joiner import slp1_to_devanagari

        original = dispatcher.apply_rule

        def recording(sutra_id: str, state: Any, *args: Any, **kwargs: Any) -> Any:
            result = original(sutra_id, state, *args, **kwargs)
            try:
                parts = [
                    slp1_to_devanagari(term.varnas)
                    for term in result.terms if term.varnas
                ]
                self.rows.append((sutra_id, " + ".join(p for p in parts if p)))
            except Exception:
                self.rows.append((sutra_id, ""))
            return result

        # Pipelines bind `apply_rule` at import time, so patching the
        # dispatcher alone is invisible to them: rebind every module that is
        # already holding the original.
        import sys as _sys

        patched = [dispatcher, engine]
        for module in list(_sys.modules.values()):
            if getattr(module, "apply_rule", None) is original:
                module.apply_rule = recording
                patched.append(module)
        dispatcher.apply_rule = recording
        engine.apply_rule = recording

        def restore() -> None:
            for module in patched:
                module.apply_rule = original

        self._restore = restore
        return self

    def __exit__(self, *exc: Any) -> None:
        try:
            if self._restore:
                self._restore()
        finally:
            TermRecorder._lock.release()

    def split_for(self, index: int, sutra_id: str) -> str:
        if index < len(self.rows) and self.rows[index][0] == sutra_id:
            return self.rows[index][1]
        for recorded_id, text in self.rows[index:]:
            if recorded_id == sutra_id:
                return text
        return ""


def reading(state: Any, recorder: "TermRecorder | None" = None) -> list[dict[str, Any]]:
    """The derivation as a sequence of forms, each with the sūtras behind it."""
    from core.trace_view import enrich_trace

    out: list[dict[str, Any]] = []
    pending: list[dict[str, str]] = []
    for index, step in enumerate(enrich_trace(state.trace)):
        sutra_id = step.get("sutra_id") or ""
        if sutra_id.startswith("__"):
            continue
        text_dev = step.get("_sutra_text_dev") or ""
        status = step.get("status", "")
        if step.get("form_before") == step.get("form_after"):
            if status in LICENSING_STATUSES and text_dev:
                pending.append({"id": sutra_id, "text_dev": text_dev})
                pending[:] = pending[-MAX_LICENSING:]
            continue
        acting = {
            "id": sutra_id,
            "text_dev": text_dev,
            "why_dev": step.get("why_dev") or "",
            "acts": True,
        }
        if step.get("_hint_hi"):
            acting["hint_hi"] = step["_hint_hi"]
        out.append({
            "form_dev": (recorder.split_for(index, sutra_id) if recorder else "")
                        or step.get("form_after_dev", ""),
            "form_slp1": step.get("form_after", ""),
            "sutras": [*pending, acting],
        })
        pending = []
    return out


def reading(state: Any, recorder: "TermRecorder | None" = None) -> list[dict[str, Any]]:
    """The derivation as a sequence of forms, each with the sūtras behind it."""
    from core.trace_view import enrich_trace

    out: list[dict[str, Any]] = []
    pending: list[dict[str, str]] = []
    for index, step in enumerate(enrich_trace(state.trace)):
        sutra_id = step.get("sutra_id") or ""
        if sutra_id.startswith("__"):
            continue
        text_dev = step.get("_sutra_text_dev") or ""
        status = step.get("status", "")
        if step.get("form_before") == step.get("form_after"):
            if status in LICENSING_STATUSES and text_dev:
                pending.append({"id": sutra_id, "text_dev": text_dev})
                pending[:] = pending[-MAX_LICENSING:]
            continue
        acting = {
            "id": sutra_id,
            "text_dev": text_dev,
            "why_dev": step.get("why_dev") or "",
            "acts": True,
        }
        if step.get("_hint_hi"):
            acting["hint_hi"] = step["_hint_hi"]
        out.append({
            "form_dev": (recorder.split_for(index, sutra_id) if recorder else "")
                        or step.get("form_after_dev", ""),
            "form_slp1": step.get("form_after", ""),
            "sutras": [*pending, acting],
        })
        pending = []
    return out
