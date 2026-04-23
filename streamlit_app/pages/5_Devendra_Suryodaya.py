"""देवेन्द्र / सूर्योदय — devendra.md guided demo."""
from __future__ import annotations

import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="देवेन्द्र / सूर्योदय", page_icon="🧩", layout="wide")

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.devendra import DEVENDRA, SURYODAYA, derive_demo
from trace_view import filter_steps_surface_changed
from i18n_hi import hint_for_sutra


st.markdown(
    "### देवेन्द्र / सूर्योदय — चरणबद्ध प्रक्रिया\n\n"
    "यह पृष्ठ `/Users/dr.ajayshukla/Documents/my panini notes/devendra.md` के अनुसार "
    "**डेमो-डिराइवेशन** चलाता है:\n\n"
    "- `deva + indra → devendraḥ`\n"
    "- `sUrya + udaya → sUryodayaḥ`\n\n"
    "नोट: समास-चरण यहाँ *संरचनात्मक* डेमो है; फिर पूर्ण सुबन्त-रेसिपि रन होती है।"
)

case_label = st.radio(
    "उदाहरण",
    options=("devendraḥ", "sūryodayaḥ"),
    horizontal=True,
)
case = DEVENDRA if case_label == "devendraḥ" else SURYODAYA

state = derive_demo(case)
surface_slp = state.render()
surface_dev = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("पहला पद", case.first)
with c2:
    st.metric("दूसरा पद", case.second)
with c3:
    st.metric("आउटपुट", surface_dev)
    st.caption(f"SLP1: `{surface_slp}`")

st.divider()

trace_mode = st.radio(
    "ट्रेस",
    options=("changes_only", "full"),
    format_func=lambda k: {"changes_only": "केवल बदलाव", "full": "पूर्ण"}[k],
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
        f"`{before}` → `{after}`\n\n"
        f"*शास्त्रीय टिप्पणी:* {why}"
    )
    hi = hint_for_sutra(sid)
    if hi:
        st.info(f"**हिन्दी:** {hi}")
    st.divider()

st.caption(f"पंजीकृत सूत्र: {len(SUTRA_REGISTRY)} · रिपो: `{common.ROOT}`")

