"""
राम शब्द-रूप — Panini Engine v3 (Streamlit)

Run from repo root:
  pip install streamlit
  streamlit run streamlit_app/Home.py
"""
from __future__ import annotations

import streamlit as st

import common  # noqa: E402 — ensures repo root on sys.path for multipage

st.set_page_config(
    page_title="राम शब्द-रूप",
    page_icon="📿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("राम शब्द-रूप")
st.markdown(
    "अष्टाद्यायी-क्रमेन **पुल्लिङ्ग** अकारान्त प्रातिपदिक **राम** — "
    "८ विभक्ति × ३ वचन = २४ रूपाः।"
)

st.info(
    "Use the sidebar to open **Paradigm (8×3)** for the full table, or "
    "**Cell derivation** to inspect one विभक्ति/वचन with the live engine trace."
)

st.divider()
st.caption("Panini Engine v3 · `pipelines.subanta.derive` + Devanāgarī joiner")
