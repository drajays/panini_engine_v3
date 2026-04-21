"""
Streamlit helpers — ट्रेस / प्रक्रिया दर्शन (UI only; not imported by engine).
"""
from __future__ import annotations

from typing import Any, Dict, List

import streamlit as st

from phonology.joiner import slp1_to_devanagari
from phonology.varna import parse_slp1_upadesha_sequence
from trace_view import filter_steps_surface_changed


def slp1_flat_to_devanagari_ui(slp_flat: str) -> str:
    """
    Render engine ``flat_slp1()`` / trace ``form_*`` strings as Devanāgarī.

    Falls back to em-dash when parsing fails (should be rare).
    """
    if not slp_flat or not str(slp_flat).strip():
        return "—"
    try:
        varnas = parse_slp1_upadesha_sequence(str(slp_flat).strip())
        return slp1_to_devanagari(varnas)
    except Exception:
        return "—"


def format_slp1_deva_pair(slp_flat: str) -> str:
    """Single-line `` `SLP1` · देवनागरी `` for metrics and inline use."""
    deva = slp1_flat_to_devanagari_ui(slp_flat)
    return f"`{slp_flat}` · {deva}"


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
        b_dev = slp1_flat_to_devanagari_ui(before)
        a_dev = slp1_flat_to_devanagari_ui(after)
        st.markdown(
            f"**{sid}** · `{type_l}`"
            + (f" · *{status}*" if status else "")
            + "\n\n"
            f"**पूर्व:** {format_slp1_deva_pair(before)}\n\n"
            f"**पश्चात्:** {format_slp1_deva_pair(after)}\n\n"
            f"*शास्त्रीय टिप्पणी:* {why}"
        )
        hi = hint_for_sutra(sid)
        if hi:
            st.info(f"**हिन्दी:** {hi}")
        st.divider()

    if sutra_registry_size is not None:
        st.caption(f"पंजीकृत सूत्र गणना: {sutra_registry_size}")
