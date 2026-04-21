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

st.title("अकारान्त पुंलिङ्ग शब्दरूप")
st.markdown(
    "**अष्टाध्यायी-क्रम** से चलने वाला इन्जिन् — **अकारान्त** (अन्त में अ) **पुंलिङ्ग** "
    "प्रातिपदिकों के **२४ रूप** (८ विभक्ति × ३ वचन)।\n\n"
    "डिफ़ॉल्ट उदाहरण **राम** (`rAma`); आप **गज** (`gaja`) जैसे दूसरे अ-ान्त शब्द भी SLP1 में टाइप कर सकते हैं।"
)

st.info(
    "📊 **Paradigm (8×3)** — पूरी सारणी, प्रातिपदिक बदलकर देखें।\n\n"
    "🔍 **Cell derivation** — एक कोष्ठक चुनकर हर सूत्र का क्रम, संस्कृत व्याख्या और हिन्दी संक्षिप्त वर्णन।"
)

st.divider()
st.caption("Panini Engine v3 · `pipelines.subanta.derive_akarant_pullinga` / `derive` + देवनागरी जोड़")
