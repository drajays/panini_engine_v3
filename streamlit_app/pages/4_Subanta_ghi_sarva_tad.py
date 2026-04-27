"""घि (हरि) · सर्वनाम (सर्व) · त्यदादि (तद्) · ज्ञान (नपुंसक) — सारणी + कोष्ठक ट्रेस।"""
from __future__ import annotations

from typing import Callable

import pandas as pd
import streamlit as st

import common  # noqa: E402

st.set_page_config(
    page_title="घि · सर्व · तद् · ज्ञान — सुबन्त",
    page_icon="📿",
    layout="wide",
)

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from engine.state import State
from phonology.joiner import slp1_to_devanagari
from pipelines.sarva_subanta import derive_sarva_pulliṅga
from pipelines.subanta import (
    derive,
    derive_akarant_pullinga,
    derive_ikarant_pullinga,
)
from prakriya_display import prepare_trace_display, render_trace_steps
from stem_input import stem_slp1_to_display_devanagari
from trace_view import filter_steps_surface_changed

from i18n_hi import (
    VACANA_HINDI,
    VACANA_SANSKRIT,
    VIBHAKTI_HINDI,
    VIBHAKTI_SANSKRIT,
    hint_for_sutra,
)

def _surface_pullinga(stem: str, v: int, vac: int) -> tuple[str, str]:
    """देवनागरी, SLP1 — केवल पुंलिङ्ग सुबन्त।"""
    stt = derive(stem, v, vac, linga="pulliṅga")
    if not stt.terms:
        return "", ""
    dev = slp1_to_devanagari(stt.terms[0].varnas)
    return dev, stt.render()


def _surface_napumsaka(stem: str, v: int, vac: int) -> tuple[str, str]:
    """देवनागरी, SLP1 — नपुंसकलिङ्ग सुबन्त।"""
    stt = derive(stem, v, vac, linga="napuṃsaka")
    if not stt.terms:
        return "", ""
    dev = slp1_to_devanagari(stt.terms[0].varnas)
    return dev, stt.render()


def _paradigm_block(
    *,
    tab_key: str,
    title_md: str,
    stem_slp: str,
    stem_dev: str,
    gold: dict,
    gold_label: str,
    derive_cell: Callable[[int, int], tuple[str, str]],
    derive_state: Callable[[int, int], State],
    vibhakti_range: range,
    linga_label: str = "पुंलिङ्ग",
) -> None:
    st.markdown(title_md)
    st.caption(
        f"**प्रातिपदिक:** {stem_dev} · **SLP1:** `{stem_slp}` · **लिङ्ग:** {linga_label}"
    )

    col_a, col_b = st.columns(2)
    with col_a:
        show_gold = st.toggle(
            "gold दिखाएँ",
            value=True,
            key=f"gold_{tab_key}",
        )
    with col_b:
        compare = st.toggle(
            "इन्जिन् vs gold भिन्नता",
            value=True,
            key=f"cmp_{tab_key}",
            disabled=not show_gold,
        )

    cells: dict[tuple[int, int], tuple[str, str]] = {}
    for v in vibhakti_range:
        for vac in range(1, 4):
            cells[(v, vac)] = derive_cell(v, vac)

    rows = []
    mismatches: list[tuple[int, int, str, str]] = []
    for v in vibhakti_range:
        label = f"{VIBHAKTI_SANSKRIT[v - 1]} ({v})\n{VIBHAKTI_HINDI[v - 1]}"
        row = {"विभक्ति (हिन्दी सहित)": label}
        for vac in range(1, 4):
            key = f"{v}-{vac}"
            dev, slp = cells[(v, vac)]
            g_dev = gold["cells"].get(key, {}).get("form_dev", "—")
            if show_gold and dev and g_dev and g_dev != dev:
                mismatches.append((v, vac, g_dev, dev))
            if show_gold:
                row[f"{VACANA_SANSKRIT[vac - 1]}\n{VACANA_HINDI[vac - 1]}"] = (
                    f"{dev}  \n`{slp}`  |  gold: {g_dev}"
                )
            else:
                row[f"{VACANA_SANSKRIT[vac - 1]}\n{VACANA_HINDI[vac - 1]}"] = (
                    f"{dev}  \n`{slp}`"
                )
        rows.append(row)

    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    if show_gold and compare:
        if mismatches:
            st.warning(
                f"{len(mismatches)} कोष्ठक(ों) में gold से भिन्नता — इन्जिन् अपूर्ण हो सकता है।"
            )
            for v, vac, g, d in mismatches[:16]:
                st.caption(f"({v},{vac}): gold `{g}` · इन्जिन् `{d}`")
            if len(mismatches) > 16:
                st.caption("…")
        else:
            st.success(f"सभी कोष्ठकों पर इन्जिन् {gold_label} से मेल खाता है।")

    st.divider()
    st.markdown("##### एक कोष्ठक — पूर्ण ट्रेस")

    vib_choices = list(vibhakti_range)
    c1, c2 = st.columns(2)
    with c1:
        vib = st.selectbox(
            "विभक्ति",
            vib_choices,
            format_func=lambda x: f"{x} — {VIBHAKTI_SANSKRIT[x - 1]}",
            key=f"vib_{tab_key}",
        )
    with c2:
        vac = st.selectbox(
            "वचन",
            range(1, 4),
            format_func=lambda x: f"{x} — {VACANA_SANSKRIT[x - 1]}",
            key=f"vac_{tab_key}",
        )

    trace_mode = st.radio(
        "ट्रेस कैसे देखें?",
        options=("full", "changes_only"),
        format_func=lambda k: {
            "full": "सभी चरण (पूर्ण ट्रेस)",
            "changes_only": "केवल बदलाव (जहाँ SLP1 बदला)",
        }[k],
        horizontal=True,
        key=f"trace_{tab_key}",
    )

    # Legacy bilingual trace (form_before/after only) — ऊपर की सारणी के अतिरिक्त
    use_prakriya = st.toggle(
        "ट्रेस: पूर्व/पश्चात् SLP1 + देवनागरी (विस्तृत)",
        value=True,
        key=f"prak_{tab_key}",
    )

    state = derive_state(vib, vac)

    surface_dev = (
        slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    )
    surface_slp = state.render()
    gcell = gold["cells"].get(f"{vib}-{vac}", {})
    gold_dev = gcell.get("form_dev", "—")

    m1, m2 = st.columns(2)
    with m1:
        st.markdown("###### सन्दर्भ (gold)")
        st.metric("gold", gold_dev)
        st.caption(gold_label)
    with m2:
        st.markdown("###### निष्कर्ष")
        st.metric("प्रक्रिया से रूप", surface_dev)
        st.caption(f"SLP1: `{surface_slp}`")

    full_trace = state.trace
    if use_prakriya:
        display_trace = prepare_trace_display(full_trace, trace_mode)
        st.caption(
            f"**दिख रहे चरण:** {len(display_trace)} · **कुल ट्रेस:** {len(full_trace)}"
        )
        render_trace_steps(
            display_trace,
            hint_for_sutra=hint_for_sutra,
            sutra_registry_size=len(SUTRA_REGISTRY),
        )
    else:
        display_trace = (
            filter_steps_surface_changed(full_trace)
            if trace_mode == "changes_only"
            else list(full_trace)
        )
        st.caption(
            f"**दिख रहे चरण:** {len(display_trace)} · **कुल ट्रेस:** {len(full_trace)}"
        )
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


st.markdown(
    "### घि · सर्वनाम · त्यदादि · ज्ञान\n\n"
    "चार **पूर्ण सुबन्त-सारणियाँ** (परीक्षा-सूची वाले प्रातिपदिक) + किसी भी "
    "कोष्ठक की **पूर्ण प्रक्रिया**। मुख्य पृष्ठ पर केवल **अ/इ-अन्त** पुंलिङ्ग "
    "खुला है; **तद्** व्यञ्जनान्त तथा **ज्ञान** नपुंसक इसलिए यहाँ अलग हैं।"
)

tab_ghi, tab_sarva, tab_tad, tab_jnana = st.tabs(
    ("घि — हरि", "सर्वनाम — सर्व", "त्यदादि — तद्", "ज्ञान — नपुंसक")
)

# ── घि / हरि ───────────────────────────────────────────────────────────────
with tab_ghi:

    def _hari_cell(v: int, vac: int) -> tuple[str, str]:
        stt = derive_ikarant_pullinga("hari", v, vac)
        if not stt.terms:
            return "", ""
        dev = slp1_to_devanagari(stt.terms[0].varnas)
        return dev, stt.render()

    def _hari_state(v: int, vac: int):
        return derive_ikarant_pullinga("hari", v, vac)

    _paradigm_block(
        tab_key="ghi",
        title_md=(
            "#### घि-संज्ञा — **हरि** (इकारान्त पुंलिङ्ग)\n\n"
            "१.४.७ से **घि**; इकारान्त विशेष सुबन्त-नियम (७.३.११०–१२० आदि)।"
        ),
        stem_slp="hari",
        stem_dev=stem_slp1_to_display_devanagari("hari"),
        gold=common.load_hari_gold(),
        gold_label="हरि (gold)",
        derive_cell=_hari_cell,
        derive_state=_hari_state,
        vibhakti_range=range(1, 9),
    )

with tab_sarva:

    def _sarva_cell(v: int, vac: int) -> tuple[str, str]:
        stt = derive_sarva_pulliṅga(v, vac)
        if not stt.terms:
            return "", ""
        dev = slp1_to_devanagari(stt.terms[0].varnas)
        return dev, stt.render()

    def _sarva_state(v: int, vac: int):
        return derive_sarva_pulliṅga(v, vac)

    _paradigm_block(
        tab_key="sarva",
        title_md=(
            "#### सर्वनाम — **सर्व** (अदन्त, पुंलिङ्ग)\n\n"
            "२४ **रूप** = एक *prakriyā*: ``derive_sarva_pulliṅga`` (``run_subanta_pipeline``)।\n"
            "१.१.२७ **सर्वादि**; ७.१.१४–१७ (*जसः शी* → *सर्वे*), ६.१.८७; ७.१.५२, ७.३.१०३ *आदि*।"
        ),
        stem_slp="sarva",
        stem_dev=stem_slp1_to_display_devanagari("sarva"),
        gold=common.load_sarva_gold(),
        gold_label="सर्व (gold)",
        derive_cell=_sarva_cell,
        derive_state=_sarva_state,
        vibhakti_range=range(1, 9),
    )

with tab_tad:

    def _tad_cell(v: int, vac: int) -> tuple[str, str]:
        return _surface_pullinga("tad", v, vac)

    def _tad_state(v: int, vac: int) -> State:
        return derive("tad", v, vac, linga="pulliṅga")

    _paradigm_block(
        tab_key="tad",
        title_md=(
            "#### त्यदादि — **तद्** (व्यञ्जनान्त पुंलिङ्ग)\n\n"
            "१.२.७२, ७.२.१०६ (**तदोः सः**), … — **सम्बोधन (८-*) रूप नहीं**।"
        ),
        stem_slp="tad",
        stem_dev=stem_slp1_to_display_devanagari("tad"),
        gold=common.load_tad_gold(),
        gold_label="तद् (gold)",
        derive_cell=_tad_cell,
        derive_state=_tad_state,
        vibhakti_range=range(1, 8),
    )

with tab_jnana:

    def _jnana_cell(v: int, vac: int) -> tuple[str, str]:
        return _surface_napumsaka("jYAna", v, vac)

    def _jnana_state(v: int, vac: int) -> State:
        return derive("jYAna", v, vac, linga="napuṃsaka")

    _paradigm_block(
        tab_key="jnana",
        title_md=(
            "#### अकारान्त — **ज्ञान** (नपुंसकलिङ्ग)\n\n"
            "नपुंसक **अ-**अन्त विशेष (७.१.१९–२०, ७.१.७२, ६.४.८ …); परीक्षा-सूची `jYAna`।"
        ),
        stem_slp="jYAna",
        stem_dev=stem_slp1_to_display_devanagari("jYAna"),
        gold=common.load_jnana_gold(),
        gold_label="ज्ञान (gold, नपुंसक)",
        derive_cell=_jnana_cell,
        derive_state=_jnana_state,
        vibhakti_range=range(1, 9),
        linga_label="नपुंसकलिङ्ग",
    )

st.divider()
st.caption(f"पंजीकृत सूत्र: {len(SUTRA_REGISTRY)} · रिपो: `{common.ROOT}`")
