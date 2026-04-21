"""
Streamlit helpers — ट्रेस / प्रक्रिया दर्शन (UI only; not imported by engine).
"""
from __future__ import annotations

from typing import Any, Dict, List

import streamlit as st

from trace_view import filter_steps_surface_changed


def prepare_trace_display(
    trace: List[Dict[str, Any]],
    trace_mode: str,
) -> List[Dict[str, Any]]:
    if trace_mode == "changes_only":
        return filter_steps_surface_changed(trace)
    return list(trace)


def render_trace_steps(
    display_trace: List[Dict[str, Any]],
    *,
    hint_for_sutra,
    heading: str | None = None,
    sutra_registry_size: int | None = None,
) -> None:
    """
    Render one trace (list of step dicts) with optional section heading.

    ``hint_for_sutra`` is typically ``i18n_hi.hint_for_sutra`` (injected to avoid
    import cycles in tests).
    """
    if heading:
        st.markdown(f"##### {heading}")

    if not display_trace:
        st.warning("इस खण्ड में दिखाने के लिए कोई चरण नहीं।")
        return

    for step in display_trace:
        sid = step.get("sutra_id", "")
        status = step.get("status", "")
        type_l = step.get("type_label", "")
        why = step.get("why_dev", "")
        before = step.get("form_before", "")
        after = step.get("form_after", "")
        st.markdown(
            f"**{sid}** · `{type_l}`"
            + (f" · *{status}*" if status else "")
            + f"\n\n`{before}` → `{after}`\n\n"
            f"*शास्त्रीय टिप्पणी:* {why}"
        )
        hi = hint_for_sutra(sid)
        if hi:
            st.info(f"**हिन्दी:** {hi}")
        st.divider()

    if sutra_registry_size is not None:
        st.caption(f"पंजीकृत सूत्र गणना: {sutra_registry_size}")
