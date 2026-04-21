"""अकारान्त/इकारान्त पुंलिङ्ग — पूर्ण 8×3 सारणी + एक कोष्ठक की प्रक्रिया।"""
from __future__ import annotations

import pandas as pd
import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="शब्दरूप + प्रक्रिया (8×3)", page_icon="📊", layout="wide")

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.subanta import (
    derive,
    derive_akarant_pullinga,
    derive_ikarant_pullinga,
    stem_slp1_looks_akarant_pullinga,
    stem_slp1_looks_ikarant_pullinga,
)
from stem_input import (
    normalize_pratipadika_input,
    stem_slp1_to_display_devanagari,
)
from trace_view import filter_steps_surface_changed

from i18n_hi import (
    VACANA_HINDI,
    VACANA_SANSKRIT,
    VIBHAKTI_HINDI,
    VIBHAKTI_SANSKRIT,
    hint_for_sutra,
)

st.markdown(
    "### पुंलिङ्ग शब्दरूप (८ विभक्ति × ३ वचन) + प्रक्रिया\n\n"
    "यह पृष्ठ अभी **दो** stem प्रकार सपोर्ट करता है:\n\n"
    "- **अकारान्त** (अन्त में `a`) — उदा. `rAma`, `gaja`\n"
    "- **इकारान्त** (अन्त में `i`) — उदा. `hari`\n\n"
    "इनपुट **देवनागरी** (`राम`, `हरि`) या **SLP1/Velthuis** (`rAma`, `hari`) में दें।"
)

raw_stem = st.text_input(
    "प्रातिपदिक (देवनागरी या SLP1)",
    value="rAma",
    placeholder="राम / हरि  या  rAma / hari",
    help="देवनागरी: राम, गज, हरि। SLP1: rAma, gaja, hari। एक समय में दोनों लिपियाँ मिलाकर न लिखें।",
)

try:
    stem_slp = normalize_pratipadika_input(raw_stem)
except ValueError as e:
    st.error(str(e))
    st.stop()

if not stem_slp:
    st.warning("कृपया प्रातिपदिक भरें।")
    st.stop()

is_akar = stem_slp1_looks_akarant_pullinga(stem_slp)
is_ikar = stem_slp1_looks_ikarant_pullinga(stem_slp)
if not (is_akar or is_ikar):
    st.error(
        "अभी केवल **अकारान्त** (SLP1 अन्तिम `a`) या **इकारान्त** (SLP1 अन्तिम `i`) "
        "पुंलिङ्ग प्रातिपदिक समर्थित हैं। उदाहरण: `rAma`, `gaja`, `hari`।"
    )
    st.stop()

stem_dev = stem_slp1_to_display_devanagari(stem_slp)
st.caption(
    f"**आंतरिक SLP1 (इन्जिन्):** `{stem_slp}` · "
    f"**देवनागरी प्रातिपदिक:** {stem_dev}"
)

gold = None
gold_label = None
if stem_slp == "rAma":
    gold = common.load_rama_gold()
    gold_label = "राम (gold)"
elif stem_slp == "hari":
    gold = common.load_hari_gold()
    gold_label = "हरि (gold)"

use_gold = gold is not None
stem_label = f"`{stem_slp}`"

col_opt1, col_opt2 = st.columns(2)
with col_opt1:
    show_gold = st.toggle("gold दिखाएँ (यदि उपलब्ध)", value=True, disabled=not use_gold)
    if not use_gold:
        st.caption("gold केवल `rAma` और `hari` पर उपलब्ध।")
with col_opt2:
    compare = st.toggle("इन्जिन् vs gold भिन्नता सूची", value=True, disabled=not (use_gold and show_gold))


def surface_for_cell(v: int, vac: int) -> tuple[str, str]:
    if is_akar:
        state = derive_akarant_pullinga(stem_slp, v, vac)
    elif is_ikar:
        state = derive_ikarant_pullinga(stem_slp, v, vac)
    else:
        state = derive(stem_slp, v, vac, linga="pulliṅga")
    if not state.terms:
        return "", ""
    dev = slp1_to_devanagari(state.terms[0].varnas)
    slp = state.render()
    return dev, slp


cells: dict[tuple[int, int], tuple[str, str]] = {}
for v in range(1, 9):
    for vac in range(1, 4):
        cells[(v, vac)] = surface_for_cell(v, vac)

rows = []
mismatches: list[tuple[int, int, str, str]] = []
for v in range(1, 9):
    label = f"{VIBHAKTI_SANSKRIT[v - 1]} ({v})\n{VIBHAKTI_HINDI[v - 1]}"
    row = {"विभक्ति (हिन्दी सहित)": label}
    for vac in range(1, 4):
        key = f"{v}-{vac}"
        dev, slp = cells[(v, vac)]
        if use_gold and gold is not None:
            g_dev = gold["cells"].get(key, {}).get("form_dev", "—")
            if g_dev and dev and g_dev != dev:
                mismatches.append((v, vac, g_dev, dev))
            if show_gold:
                row[f"{VACANA_SANSKRIT[vac - 1]}\n{VACANA_HINDI[vac - 1]}"] = (
                    f"{dev}  \n`{slp}`  |  gold: {g_dev}"
                )
            else:
                row[f"{VACANA_SANSKRIT[vac - 1]}\n{VACANA_HINDI[vac - 1]}"] = f"{dev}  \n`{slp}`"
        else:
            row[f"{VACANA_SANSKRIT[vac - 1]}\n{VACANA_HINDI[vac - 1]}"] = f"{dev}  \n`{slp}`"
    rows.append(row)

stem_kind = "अकारान्त" if is_akar else "इकारान्त"
st.markdown(f"**प्रातिपदिक:** {stem_dev} · **SLP1:** {stem_label} · **लिङ्ग:** पुंलिङ्ग · **विशेष:** {stem_kind}")

st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

if use_gold and gold is not None and compare and show_gold:
    if mismatches:
        st.warning(
            f"{len(mismatches)} कोष्ठक(ों) में सोने के रूप से भिन्नता — इन्जिन् अभी पूरा नहीं हो सकता।"
        )
        for v, vac, g, d in mismatches[:16]:
            st.caption(f"({v},{vac}): gold `{g}` · इन्जिन् `{d}`")
        if len(mismatches) > 16:
            st.caption("…")
    else:
        st.success(f"सभी २४ कोष्ठकों पर इन्जिन् {gold_label} से मेल खाता है।")

st.divider()

st.markdown("### एक कोष्ठक — प्रक्रिया (उसी प्रातिपदिक पर)")

c1, c2 = st.columns(2)
with c1:
    vib = st.selectbox(
        "विभक्ति",
        range(1, 9),
        format_func=lambda x: f"{x} — {VIBHAKTI_SANSKRIT[x - 1]}",
        key="vib_select",
    )
with c2:
    vac = st.selectbox(
        "वचन",
        range(1, 4),
        format_func=lambda x: f"{x} — {VACANA_SANSKRIT[x - 1]}",
        key="vac_select",
    )

cell_key = f"{vib}-{vac}"
state = (
    derive_akarant_pullinga(stem_slp, vib, vac)
    if is_akar
    else derive_ikarant_pullinga(stem_slp, vib, vac)
)
surface_dev = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
surface_slp = state.render()

m1, m2 = st.columns(2)
with m1:
    st.markdown("##### सन्दर्भ रूप (यदि उपलब्ध)")
    if use_gold and gold is not None:
        g_dev = gold["cells"].get(cell_key, {}).get("form_dev", "—")
        st.metric("gold", g_dev)
    else:
        st.metric("gold", "—")
with m2:
    st.markdown("##### इन्जिन् निष्कर्ष")
    st.metric("प्रक्रिया से रूप", surface_dev)
    st.caption(f"SLP1: `{surface_slp}`")

trace_mode = st.radio(
    "ट्रेस कैसे देखें?",
    options=("full", "changes_only"),
    format_func=lambda k: {
        "full": "सभी चरण (पूर्ण ट्रेस)",
        "changes_only": "केवल बदलाव (जहाँ SLP1 बदला)",
    }[k],
    horizontal=True,
    key="trace_mode",
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
