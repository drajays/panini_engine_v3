"""एक कोष्ठक — विस्तृत प्रक्रिया (हिन्दी + देवनागरी)।"""
from __future__ import annotations

import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="एक कोष्ठक — प्रक्रिया", page_icon="🔍", layout="wide")

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.subanta import derive_akarant_pullinga, stem_slp1_looks_akarant_pullinga

from i18n_hi import (
    VACANA_HINDI,
    VACANA_SANSKRIT,
    VIBHAKTI_HINDI,
    VIBHAKTI_SANSKRIT,
    hint_for_sutra,
)

st.markdown(
    "### एक विभक्ति × एक वचन — पूरी प्रक्रिया\n\n"
    "**अकारान्त पुंलिङ्ग** के लिए प्रातिपदिक SLP1 में दें (अन्त में `a`)। नीचे प्रत्येक चरण पर "
    "संस्कृत व्याख्या और हिन्दी संक्षिप्त टिप्पणी है।"
)

stem_slp1 = st.text_input("प्रातिपदिक (SLP1)", value="rAma", key="stem_cell")

c1, c2 = st.columns(2)
with c1:
    vib = st.selectbox(
        "विभक्ति",
        range(1, 9),
        format_func=lambda x: f"{x} — {VIBHAKTI_SANSKRIT[x - 1]}",
    )
with c2:
    vac = st.selectbox(
        "वचन",
        range(1, 4),
        format_func=lambda x: f"{x} — {VACANA_SANSKRIT[x - 1]}",
    )

with st.expander("विभक्ति और वचन — हिन्दी में संक्षिप्त अर्थ", expanded=False):
    st.markdown(
        f"**चुनी विभक्ति:** {VIBHAKTI_SANSKRIT[vib - 1]} — {VIBHAKTI_HINDI[vib - 1]}\n\n"
        f"**चुना वचन:** {VACANA_SANSKRIT[vac - 1]} — {VACANA_HINDI[vac - 1]}"
    )

if not stem_slp1_looks_akarant_pullinga(stem_slp1):
    st.error(
        "अकारान्त हेतु अन्तिम अक्षर छोटा **`a`** होना चाहिए (उदा. `rAma`)।"
    )
    st.stop()

use_gold = stem_slp1.strip() == "rAma"
gold = common.load_rama_gold() if use_gold else None
key = f"{vib}-{vac}"
gcell = gold["cells"].get(key, {}) if gold else {}
gold_dev = gcell.get("form_dev", "—") if use_gold else "— (केवल rAma)"
gold_slp = gcell.get("form_slp1", "—") if use_gold else "—"

state = derive_akarant_pullinga(stem_slp1.strip(), vib, vac)
surface_dev = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
surface_slp = state.render()

m1, m2 = st.columns(2)
with m1:
    st.markdown("##### सन्दर्भ रूप (यदि उपलब्ध)")
    st.metric("gold (राम)", gold_dev if use_gold else "—", delta=None)
    st.caption(f"SLP1: `{gold_slp}`")
with m2:
    st.markdown("##### इन्जिन् निष्कर्ष")
    st.metric("प्रक्रिया से रूप", surface_dev)
    st.caption(f"SLP1: `{surface_slp}`")

st.markdown("---")
st.markdown("#### सूत्र-मार्ग (क्रम से) — संस्कृत + हिन्दी सहायक")

for step in state.trace:
    sid = step.get("sutra_id", "")
    hi = hint_for_sutra(sid)
    type_l = step.get("type_label", "")
    why = step.get("why_dev", "")
    before = step.get("form_before", "")
    after = step.get("form_after", "")
    st.markdown(
        f"**{sid}** · {type_l}\n\n"
        f"{before} → {after}\n\n"
        f"*शास्त्रीय टिप्पणी:* {why}"
    )
    if hi:
        st.info(f"**हिन्दी:** {hi}")
    st.divider()

st.caption(f"चरण: `{state.phase}` · नियम सूची में: {len(SUTRA_REGISTRY)}")
