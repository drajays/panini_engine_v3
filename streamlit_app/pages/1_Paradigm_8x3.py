"""अकारान्त पुंलिङ्ग — पूर्ण 8×3 सारणी (कोई भी अ-ान्त प्रातिपदिक)।"""
from __future__ import annotations

import pandas as pd
import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="अकारान्त पुं — 8×3", page_icon="📊", layout="wide")

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.subanta import derive_akarant_pullinga, stem_slp1_looks_akarant_pullinga
from stem_input import (
    normalize_pratipadika_input,
    stem_slp1_to_display_devanagari,
)

from i18n_hi import (
    VACANA_HINDI,
    VACANA_SANSKRIT,
    VIBHAKTI_HINDI,
    VIBHAKTI_SANSKRIT,
)

st.markdown(
    "### अकारान्त पुंलिङ्ग शब्दरूप (८ विभक्ति × ३ वचन)\n\n"
    "**अकारान्त** = प्रातिपदिक अन्त में **अ** (जैसे राम, गज)। यहाँ **देवनागरी** "
    "(जैसे `राम`, `गज`) **या** **SLP1 / Velthuis** (`rAma`, `gaja`) दोनों चलते हैं — "
    "इन्जिन् अन्दर **SLP1** में बदलकर चलता है।\n\n"
    "**सोने के पैमाने (gold)** केवल **राम** (`rAma` / `राम`) के लिए; अन्य प्रातिपदिकों पर केवल इन्जिन्-आउटपुट।"
)

raw_stem = st.text_input(
    "प्रातिपदिक (देवनागरी या SLP1, अ-ान्त)",
    value="rAma",
    placeholder="राम  या  rAma",
    help="देवनागरी: राम, गज। SLP1: rAma, gaja। एक समय में दोनों लिपियाँ मिलाकर न लिखें।",
)

try:
    stem_slp = normalize_pratipadika_input(raw_stem)
except ValueError as e:
    st.error(str(e))
    st.stop()

if not stem_slp:
    st.warning("कृपया प्रातिपदिक भरें।")
    st.stop()

if not stem_slp1_looks_akarant_pullinga(stem_slp):
    st.error(
        "यह प्रातिपदिक अकारान्त पुंलिङ्ग के रूप में मान्य नहीं: अन्त में ह्रस्व **अ** चाहिए "
        "(देवनागरी में जैसे `राम`, `गज`; SLP1 में अन्तिम `a` — उदा. `rAma`, `gaja`)। "
        "`हरि` या विसर्गान्त रूप यहाँ नहीं चलेंगे।"
    )
    st.stop()

stem_dev = stem_slp1_to_display_devanagari(stem_slp)
st.caption(
    f"**आंतरिक SLP1 (इन्जिन्):** `{stem_slp}` · "
    f"**देवनागरी प्रातिपदिक:** {stem_dev}"
)

use_gold = stem_slp == "rAma"
gold = common.load_rama_gold() if use_gold else None
stem_label = f"`{stem_slp}`"

col_opt1, col_opt2 = st.columns(2)
with col_opt1:
    show_gold = st.toggle("राम के लिए सोना (gold) दिखाएँ", value=True, disabled=not use_gold)
    if not use_gold:
        st.caption("केवल `rAma` / `राम` पर gold उपलब्ध।")
with col_opt2:
    compare = st.toggle("इन्जिन् vs gold भिन्नता सूची", value=True, disabled=not (use_gold and show_gold))


def surface_for_cell(v: int, vac: int) -> tuple[str, str]:
    state = derive_akarant_pullinga(stem_slp, v, vac)
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

st.markdown(f"**प्रातिपदिक:** {stem_dev} · **SLP1:** {stem_label} · **लिङ्ग:** पुंलिङ्ग · **विशेष:** अकारान्त")

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
        st.success("सभी २४ कोष्ठकों पर इन्जिन् सोने से मेल खाता है।")

st.divider()
st.caption(f"पंजीकृत सूत्र: {len(SUTRA_REGISTRY)} · रिपो: `{common.ROOT}`")
