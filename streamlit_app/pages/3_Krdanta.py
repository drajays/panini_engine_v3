"""कृदन्त — धातु + कृत् (Nvul) → प्रातिपदिक + ट्रेस।"""
from __future__ import annotations

import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="कृदन्त", page_icon="🧩", layout="wide")

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.krdanta import derive_krt
from stem_input import normalize_pratipadika_input
from trace_view import filter_steps_surface_changed

from i18n_hi import hint_for_sutra


st.markdown(
    "### कृदन्त (kṛdanta) — धातु + कृत्-प्रत्यय\n\n"
    "अभी यह पृष्ठ **वृद्धि (आ)** के उदाहरण हेतु **`डुपचँष्` + `ण्वुल्`** "
    "(SLP1: `qupac~z` + `Nvul`) को सपोर्ट करता है, परिणाम: **पाचक**।\n\n"
    "इनपुट **धातु-उपदेश** SLP1 में दें (उदा. `qupac~z`)।"
)

raw_dhatu = st.text_input(
    "धातु-उपदेश (SLP1)",
    value="qupac~z",
    placeholder="उदा. qupac~z",
    help="यहाँ देवनागरी नहीं — कृत्-उपदेश/इत्-चिन्ह (~) सहित SLP1 दें।",
)

krt = st.selectbox(
    "कृत्-प्रत्यय (उपदेश)",
    options=("Nvul",),
    format_func=lambda x: "ण्वुल् (Nvul)",
)

run = st.button("Derive", type="primary")
if run:
    try:
        # dhātu input is SLP1 upadeśa; normalization here only strips.
        dhatu_slp1 = raw_dhatu.strip()
        if not dhatu_slp1:
            st.error("धातु-उपदेश रिक्त है।")
            st.stop()
        state = derive_krt(dhatu_slp1, krt_upadesha_slp1=krt)
    except Exception as e:
        st.exception(e)
        st.stop()

    if not state.terms:
        st.error("कोई आउटपुट Term नहीं।")
        st.stop()

    surface_dev = slp1_to_devanagari(state.terms[0].varnas)
    surface_slp = state.render()

    st.markdown("#### निष्कर्ष")
    c1, c2 = st.columns(2)
    with c1:
        st.metric("प्रातिपदिक (देवनागरी)", surface_dev)
    with c2:
        st.metric("SLP1", surface_slp)

    st.markdown("---")
    st.markdown("#### सूत्र-मार्ग (ट्रेस)")

    trace_mode = st.radio(
        "ट्रेस कैसे देखें?",
        options=("full", "changes_only"),
        format_func=lambda k: {
            "full": "सभी चरण (पूर्ण ट्रेस)",
            "changes_only": "केवल बदलाव (जहाँ SLP1 बदला)",
        }[k],
        horizontal=True,
    )

    full_trace = state.trace
    display_trace = (
        filter_steps_surface_changed(full_trace)
        if trace_mode == "changes_only"
        else list(full_trace)
    )
    st.caption(f"**दिख रहे चरण:** {len(display_trace)} · **कुल ट्रेस:** {len(full_trace)}")

    for step in display_trace:
        sid = step.get("sutra_id", "")
        type_l = step.get("type_label", "")
        why = step.get("why_dev", "")
        before = step.get("form_before", "")
        after = step.get("form_after", "")
        st.markdown(
            f"**{sid}** · {type_l}\n\n"
            f"{before} → {after}\n\n"
            f"*शास्त्रीय टिप्पणी:* {why}"
        )
        hi = hint_for_sutra(sid)
        if hi:
            st.info(f"**हिन्दी:** {hi}")
        st.divider()

st.caption(f"पंजीकृत सूत्र: {len(SUTRA_REGISTRY)} · रिपो: `{common.ROOT}`")

