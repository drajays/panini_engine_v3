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

st.title("पुंलिङ्ग शब्दरूप + प्रक्रिया")
st.markdown(
    "**अष्टाध्यायी-क्रम** से चलने वाला इन्जिन् — अभी **पुंलिङ्ग** के दो stem प्रकार:\n\n"
    "- **अकारान्त** (`...a`) — उदा. `राम` / `rAma`, `गज` / `gaja`\n"
    "- **इकारान्त** (`...i`) — उदा. `हरि` / `hari`\n\n"
    "एक ही पृष्ठ पर **२४ रूप (8×3)** + किसी भी **एक कोष्ठक की पूर्ण प्रक्रिया (ट्रेस)** देख सकते हैं।"
)

st.info(
    "📊 **Paradigm (8×3)** — पूरी सारणी, प्रातिपदिक बदलकर देखें।\n\n"
    "🔍 **Cell derivation** — एक कोष्ठक चुनकर ट्रेस: **सभी चरण** अथवा **केवल वे चरण जहाँ SLP1 रूप बदला**।"
)

st.divider()
st.caption("Panini Engine v3 · `pipelines.subanta.derive` (+ stem guards) + देवनागरी जोड़")
