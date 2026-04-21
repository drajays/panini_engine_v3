"""Single विभक्ति/वचन — surface + trace."""
from __future__ import annotations

import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="राम — प्रक्रिया", page_icon="🔍", layout="wide")

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.subanta import derive

VIBHAKTI_DEV = (
    "प्रथमा",
    "द्वितीया",
    "तृतीया",
    "चतुर्थी",
    "पञ्चमी",
    "षष्ठी",
    "सप्तमी",
    "सम्बोधन",
)
VACANA_DEV = ("एकवचन", "द्विवचन", "बहुवचन")

st.title("एक कोष्ठकम् — प्रक्रिया")
gold = common.load_rama_gold()

c1, c2, c3 = st.columns(3)
with c1:
    vib = st.selectbox("विभक्ति", range(1, 9), format_func=lambda x: f"{x} — {VIBHAKTI_DEV[x - 1]}")
with c2:
    vac = st.selectbox("वचन", range(1, 4), format_func=lambda x: f"{x} — {VACANA_DEV[x - 1]}")
with c3:
    linga = st.selectbox("लिङ्ग", ["pulliṅga", "strīliṅga", "napuṃsaka"], index=0)

key = f"{vib}-{vac}"
gcell = gold["cells"].get(key, {})
gold_dev = gcell.get("form_dev", "—")
gold_slp = gcell.get("form_slp1", "—")

state = derive("rAma", vib, vac, linga=linga)
surface_dev = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
surface_slp = state.render()

m1, m2 = st.columns(2)
with m1:
    st.metric("पृष्ठभूमि (gold)", gold_dev, delta=None)
    st.caption(f"SLP1: `{gold_slp}`")
with m2:
    st.metric("इन्जिन् प्रक्रिया", surface_dev)
    st.caption(f"SLP1: `{surface_slp}`")

with st.expander("सूत्र-मार्गः (trace)", expanded=True):
    for step in state.trace:
        sid = step.get("sutra_id", "")
        st.markdown(
            f"**{sid}** — {step.get('type_label', '')}  \n"
            f"{step.get('form_before', '')} → {step.get('form_after', '')}  \n"
            f"<small>{step.get('why_dev', '')}</small>",
            unsafe_allow_html=True,
        )
        st.divider()

st.caption(f"Phase: `{state.phase}` · Rules in registry: {len(SUTRA_REGISTRY)}")
