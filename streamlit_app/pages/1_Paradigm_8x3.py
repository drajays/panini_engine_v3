"""Full राम paradigm: 8 विभक्ति × 3 वचन."""
from __future__ import annotations

import pandas as pd
import streamlit as st

import common  # noqa: E402 — path + repo root via common

st.set_page_config(page_title="राम — 8×3", page_icon="📊", layout="wide")

import sutras  # noqa: F401, E402 — registry
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


def surface_for_cell(v: int, vac: int) -> tuple[str, str]:
    state = derive("rAma", v, vac, linga="pulliṅga")
    if not state.terms:
        return "", ""
    dev = slp1_to_devanagari(state.terms[0].varnas)
    slp = state.render()
    return dev, slp


st.title("राम — विभक्ति × वचन")
gold = common.load_rama_gold()
stem_dev = gold.get("stem_dev", "राम")

col_opt1, col_opt2 = st.columns(2)
with col_opt1:
    show_gold = st.toggle("Show gold reference (JSON)", value=True)
with col_opt2:
    compare = st.toggle("List engine vs gold mismatches", value=True)

cells: dict[tuple[int, int], tuple[str, str]] = {}
for v in range(1, 9):
    for vac in range(1, 4):
        cells[(v, vac)] = surface_for_cell(v, vac)

rows = []
mismatches: list[tuple[int, int, str, str]] = []
for v in range(1, 9):
    row = {"विभक्ति": f"{VIBHAKTI_DEV[v - 1]} ({v})"}
    for vac in range(1, 4):
        key = f"{v}-{vac}"
        g_dev = gold["cells"].get(key, {}).get("form_dev", "—")
        dev, slp = cells[(v, vac)]
        if g_dev and dev and g_dev != dev:
            mismatches.append((v, vac, g_dev, dev))
        if show_gold:
            row[VACANA_DEV[vac - 1]] = f"{dev} ({slp})  |  gold: {g_dev}"
        else:
            row[VACANA_DEV[vac - 1]] = f"{dev}  ({slp})"
    rows.append(row)

st.markdown(f"**प्रातिपदिक:** {stem_dev} · **लिङ्ग:** पुं · **Stem (SLP1):** `rAma`")
st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

if compare and show_gold:
    if mismatches:
        st.warning(
            f"{len(mismatches)} cell(s) differ from gold reference "
            "(expected while the cascade is incomplete)."
        )
        for v, vac, g, d in mismatches[:16]:
            st.caption(f"({v},{vac}): gold `{g}` · engine `{d}`")
        if len(mismatches) > 16:
            st.caption("…")
    else:
        st.success("Engine output matches gold for all 24 cells.")

st.divider()
st.caption(f"Sūtras registered: {len(SUTRA_REGISTRY)} · Repo: `{common.ROOT}`")
