"""web/display.py — rendering helpers (no Streamlit dependency)."""
from __future__ import annotations
from typing import Any

from phonology.joiner import slp1_to_devanagari
from phonology.varna import parse_slp1_upadesha_sequence


def slp1_to_deva(slp: str) -> str:
    if not slp or not slp.strip():
        return "—"
    try:
        return slp1_to_devanagari(parse_slp1_upadesha_sequence(slp.strip()))
    except Exception:
        return slp


def filter_surface_changed(trace: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [s for s in trace if s.get("form_before") != s.get("form_after")]


def prepare_trace(trace: list[dict[str, Any]], surface_only: bool = False) -> list[dict]:
    steps = filter_surface_changed(trace) if surface_only else trace
    out = []
    for step in steps:
        out.append({
            "sutra_id": step.get("sutra_id", ""),
            "type_label": step.get("type_label", step.get("sutra_type", "")),
            "status": step.get("status", ""),
            "before_slp": step.get("form_before", ""),
            "before_deva": slp1_to_deva(step.get("form_before", "")),
            "after_slp": step.get("form_after", ""),
            "after_deva": slp1_to_deva(step.get("form_after", "")),
            "why": step.get("why_dev", step.get("why", "")),
        })
    return out


VIBHAKTI_LABELS = [
    "प्र. (nominative)", "द्वि. (accusative)", "तृ. (instrumental)",
    "च. (dative)", "प. (ablative)", "ष. (genitive)",
    "स. (locative)", "सं. (vocative)",
]
VACANA_LABELS = ["एक. (sg)", "द्वि. (du)", "बहु. (pl)"]


def build_paradigm_table(stem: str, linga: str = "pulliṅga") -> list[list[dict]]:
    """Return 8×3 table of {form, slp1, vibhakti, vacana} dicts."""
    import sutras  # noqa: F401
    from pipelines.subanta import derive

    table = []
    for vi in range(1, 9):
        row = []
        for va in range(1, 4):
            try:
                state = derive(stem, vi, va, linga)
                slp = state.flat_slp1()
                deva = slp1_to_deva(slp)
            except Exception as e:
                slp, deva = "—", "—"
            row.append({"slp": slp, "deva": deva, "vi": vi, "va": va})
        table.append(row)
    return table
