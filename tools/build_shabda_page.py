"""
tools/build_shabda_page.py — the śabda table as data for the web page.

For every vendored paradigm, derive all 24 cells and record each one as a
*reading sequence*: the form after each change, and the sūtras that made it.
That is the shape ashtadhyayi.com's detail panel uses, and it is the shape a
scholar reads —

    राम
    → राम + टा   [ स्वौजसमौट्… ४.१.२ इति टा-प्रत्ययः । सुप्तिङन्तं पदम् १.४.१४ … ]
    → राम + आ    [ चुटू १.३.७ इति इत्संज्ञा । तस्य लोपः १.३.९ इति लोपः । ]
    → रामेन      [ आद्गुणः ६.१.८७ इति गुणैकादेशः । ]
    → रामेण      [ अट्कुप्वाङ्… ८.४.२ इति णत्वम् । ]

Steps that leave the form untouched (saṃjñā, adhikāra) are not dropped — they
are folded into the bracket of the change they licensed, which is how the
tradition cites them.

    python3 -m tools.build_shabda_page      # writes docs/data/shabda.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

OUT = _ROOT / "docs" / "data" / "shabda.json"

VIBHAKTI_DEV = ("प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
                "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधनम्")
VACANA_DEV = ("एकवचनम्", "द्विवचनम्", "बहुवचनम्")

# Rows that describe rather than act: keep them as citations, never as steps.
QUIET_STATUSES = {"SKIPPED", "BLOCKED"}
# An adhikāra row is bookkeeping, not a reason; and only the few saṃjñās just
# before a change are worth citing with it. Without this the page is 6 MB of
# preamble repeated 312 times.
LICENSING_STATUSES = {"APPLIED"}
MAX_LICENSING = 2


class TermRecorder:
    """Capture the tape's *term split* after each rule.

    The trace stores the flat form, so a step reads रामटा where the tradition
    writes राम + टा. The split is what makes a derivation legible, so it is
    recorded alongside — by wrapping the dispatcher, the way the coverage
    ledger does, rather than by changing the trace schema.
    """

    def __init__(self) -> None:
        self.rows: list[tuple[str, str]] = []
        self._restore = None

    def __enter__(self) -> "TermRecorder":
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
        if self._restore:
            self._restore()

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


def build() -> dict[str, Any]:
    import sutras  # noqa: F401
    from pipelines.subanta import derive
    from tools.shabda_table import paradigms

    words = []
    for stem, data in paradigms().items():
        cells = {}
        for vibhakti in range(1, 9):
            for vacana in range(1, 4):
                key = f"{vibhakti}-{vacana}"
                attested = data["cells"].get(key, [])
                try:
                    with TermRecorder() as recorder:
                        state = derive(stem, vibhakti, vacana, linga=data["linga"])
                    form, steps, error = state.flat_dev(), reading(state, recorder), ""
                except Exception as ex:                    # a gap, shown as one
                    form, steps, error = "", [], f"{type(ex).__name__}: {ex}"
                cells[key] = {
                    "form_dev": form,
                    "attested": attested,
                    "agrees": bool(form) and form in attested,
                    "steps": steps,
                    "error": error,
                }
        words.append({
            "stem_slp1": stem,
            "word": data["word"],
            "linga": data["linga"],
            "artha": data.get("artha", ""),
            "cells": cells,
        })
    return {
        "labels": {"vibhakti": VIBHAKTI_DEV, "vacana": VACANA_DEV},
        "source": "derived by this engine; attested forms from ashtadhyayi-com/data",
        "words": sorted(words, key=lambda w: w["stem_slp1"].lower()),
    }


def main() -> int:
    payload = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                   encoding="utf-8")
    cells = sum(len(w["cells"]) for w in payload["words"])
    agree = sum(1 for w in payload["words"] for c in w["cells"].values() if c["agrees"])
    size = OUT.stat().st_size / 1024
    print(f"  {len(payload['words'])} paradigms · {cells} cells · {agree} agree")
    print(f"  {OUT.relative_to(_ROOT)}  ({size:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
