"""कृदन्त — ण्वुल् (agent) तथा तृच् (कर्तृ-नाम) पूर्ण प्रक्रिया-ट्रेस।"""
from __future__ import annotations

import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="कृदन्त — प्रक्रिया", page_icon="🧩", layout="wide")

import sutras  # noqa: F401, E402
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.dhatupatha import get_dhatu_row, list_tfc_demo_ids
from pipelines.krdanta import (
    build_dhatu_state_from_varnas,
    derive_krt,
    derive_tfc_pratipadika,
    derive_trc_nom_sg,
)
from prakriya_display import prepare_trace_display, render_trace_steps
from i18n_hi import hint_for_sutra
from phonology.tokenizer import devanagari_to_varnas


st.markdown(
    "### कृदन्त (kṛdanta)\n\n"
    "दो मार्ग:\n\n"
    "1. **ण्वुल्** — प्रायः **कर्तृ-नाम** (जैसे पाचक)। धातु SLP1 या देवनागरी में दें।\n"
    "2. **तृच्** — **कर्तृ-नाम** (चेता, नेता, भविता …)। `data/inputs/dhatupatha_upadesha.json` से "
    "चयनित पंक्ति + **प्रथमा एकवचन** सुबन्त-खण्ड तक पूर्ण ट्रेस।\n\n"
    "ट्रेस में प्रत्येक सूत्र के लिए **पूर्व/पश्चात् SLP1** और **हिन्दी सहायक** दिखता है।"
)

tab_nvul, tab_trc = st.tabs(("ण्वुल् (Nvul)", "तृच् (tfc) + प्रथमा एकवचन"))

# ── ण्वुल् ────────────────────────────────────────────────────────────────
with tab_nvul:
    st.markdown(
        "#### ण्वुल् अभिकर्तृ (उदा. पाचक)\n\n"
        "**डुपचँष्** + **Nvul** → पाचक।"
    )
    raw_dhatu = st.text_input(
        "धातु-उपदेश (देवनागरी या SLP1)",
        value="qupac~z",
        placeholder="उदा. qupac~z  या  डुपचँष्",
        help="SLP1 में अनुनासिक के लिए `~` लिखें।",
        key="nvul_dhatu",
    )

    krt = st.selectbox(
        "कृत्-प्रत्यय (उपदेश)",
        options=("Nvul",),
        format_func=lambda x: "ण्वुल् (Nvul)",
        key="nvul_krt",
    )

    run_nvul = st.button("प्रक्रिया चलाएँ (ण्वुल्)", type="primary", key="btn_nvul")

    if run_nvul:
        try:
            s_in = raw_dhatu.strip()
            if not s_in:
                st.error("धातु-उपदेश रिक्त है।")
                st.stop()
            if any(0x0900 <= ord(c) <= 0x097F for c in s_in):
                dvs = devanagari_to_varnas(s_in)
                state = derive_krt("deva_input", krt_upadesha_slp1=krt, dhatu_varnas=dvs)
            else:
                state = derive_krt(s_in, krt_upadesha_slp1=krt)
        except Exception as e:
            st.exception(e)
            st.stop()

        if not state.terms:
            st.error("कोई आउटपुट Term नहीं।")
            st.stop()

        surface_dev = slp1_to_devanagari(state.terms[0].varnas)
        surface_slp = state.render()

        st.markdown("#### निष्कर्ष")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("प्रातिपदिक (देवनागरी)", surface_dev)
        with c2:
            st.metric("SLP1", surface_slp)

        st.markdown("---")
        st.markdown("#### सूत्र-मार्ग (एक खण्ड — ण्वुल्)")

        trace_mode_nvul = st.radio(
            "ट्रेस कैसे देखें?",
            options=("full", "changes_only"),
            format_func=lambda k: {
                "full": "सभी चरण (पूर्ण ट्रेस)",
                "changes_only": "केवल बदलाव (जहाँ SLP1 बदला)",
            }[k],
            horizontal=True,
            key="trace_nvul",
        )

        full_trace = state.trace
        display_trace = prepare_trace_display(full_trace, trace_mode_nvul)
        st.caption(f"**दिख रहे चरण:** {len(display_trace)} · **कुल ट्रेस:** {len(full_trace)}")

        render_trace_steps(
            display_trace,
            hint_for_sutra=hint_for_sutra,
            sutra_registry_size=len(SUTRA_REGISTRY),
        )

# ── तृच् ───────────────────────────────────────────────────────────────────
with tab_trc:
    st.markdown(
        "#### तृच् → प्रातिपदिक → **सु** (प्रथमा एकवचन, पुंलिङ्ग)\n\n"
        "नीचे **पूर्व निर्धारित उदाहरण** (परीक्षा-सूची के समान) या अपना **पंक्ति-id** "
        "दें। प्रक्रिया **दो खण्डों** में दिखेगी: (क) धातु+तृच् → तृण्मूल, (ख) तृण्मूल+सु → "
        "पद (चेता, नेता, …)।"
    )

    demo_ids = list_tfc_demo_ids()
    if not demo_ids:
        st.error("धातु JSON में कोई tfc डेमो-id नहीं मिला।")
        st.stop()

    c1, c2 = st.columns((3, 2))
    with c1:
        choice = st.selectbox(
            "पूर्वनिर्धारित धातु (row id)",
            options=demo_ids,
            format_func=lambda i: f"{i} — {get_dhatu_row(i).get('upadesha_dev', '')}",
            key="trc_preset",
        )
    with c2:
        custom_id = st.text_input(
            "अथवा सीधा id (उदा. BvAdi_01_0123, BvAdi_BU)",
            value="",
            placeholder="खाली = ऊपर वाला प्रयोग होगा",
            key="trc_custom_id",
        )

    active_id = custom_id.strip() or choice

    try:
        row = get_dhatu_row(active_id)
    except KeyError as e:
        st.error(f"अज्ञात id: {e}")
        st.stop()

    with st.expander("चयनित पंक्ति — मेटाडाटा (JSON से)", expanded=False):
        st.json(
            {
                "id": row.get("id"),
                "tier": row.get("tier"),
                "dhatupatha_id": row.get("dhatupatha_id"),
                "upadesha_dev": row.get("upadesha_dev"),
                "upadesha_slp1": row.get("upadesha_slp1"),
                "artha_dev": row.get("artha_dev"),
                "artha_en": row.get("artha_en"),
                "it_class_label_dev": row.get("it_class_label_dev"),
                "flags": row.get("flags"),
                "notes": row.get("notes"),
            },
            expanded=True,
        )

    run_trc = st.button("पूर्ण प्रक्रिया चलाएँ (तृच् + सु)", type="primary", key="btn_trc")

    if run_trc:
        up = row["upadesha_slp1"]
        ud = bool((row.get("flags") or {}).get("udatta", False))

        try:
            k_state = derive_tfc_pratipadika(up, udatta_dhatu=ud)
            stem_slp = k_state.flat_slp1()
            stem_dev = (
                slp1_to_devanagari(k_state.terms[0].varnas) if k_state.terms else ""
            )
            s_state = derive_trc_nom_sg(
                stem_slp,
                vibhakti=1,
                vacana=1,
                linga="pulliṅga",
            )
        except Exception as e:
            st.exception(e)
            st.stop()

        if not s_state.terms:
            st.error("सुबन्त चरण में कोई पद नहीं।")
            st.stop()

        final_dev = slp1_to_devanagari(s_state.terms[0].varnas)
        final_slp = s_state.render()

        st.markdown("#### निष्कर्ष")
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("तृच्-मूल (SLP1)", stem_slp)
        with m2:
            st.metric("तृच्-मूल (देवनागरी)", stem_dev)
        with m3:
            st.metric("पद (SLP1)", final_slp)
        with m4:
            st.metric("पद (देवनागरी)", final_dev)

        meta_k = k_state.meta
        with st.expander("इन्जिन् मेटा (तृच्-खण्ड) — एकाच् / उदात्त आदि", expanded=False):
            st.code(
                "ekac_dhatu = "
                f"{meta_k.get('ekac_dhatu')!r}, "
                "udatta_dhatu = "
                f"{meta_k.get('udatta_dhatu')!r}",
                language="text",
            )
            st.caption(
                "७.२.१० प्रतिषेध के लिए पाइपलाइन इन ध्वजों को सेट करता है "
                "(एकाच् + अनुदात्त → ७.२.३५ इट् रुध्यते)।"
            )

        st.markdown("---")
        st.markdown("#### सूत्र-मार्ग — दो खण्ड")

        trace_mode_trc = st.radio(
            "ट्रेस कैसे देखें?",
            options=("full", "changes_only"),
            format_func=lambda k: {
                "full": "सभी चरण (पूर्ण ट्रेस)",
                "changes_only": "केवल बदलाव (जहाँ SLP1 बदला)",
            }[k],
            horizontal=True,
            key="trace_trc",
        )

        # खण्ड क — कृदन्त (तृच्)
        k_full = k_state.trace
        k_disp = prepare_trace_display(k_full, trace_mode_trc)
        st.markdown(
            f"**खण्ड क — धातु + तृच् (कृदन्त)** · दिख रहे: {len(k_disp)} / कुल: {len(k_full)}"
        )
        render_trace_steps(
            k_disp,
            hint_for_sutra=hint_for_sutra,
            heading=None,
        )

        st.markdown("---")

        # खण्ड ख — सुबन्त
        s_full = s_state.trace
        s_disp = prepare_trace_display(s_full, trace_mode_trc)
        st.markdown(
            f"**खण्ड ख — तृच्-मूल + सु (प्रथमा एकवचन)** · दिख रहे: {len(s_disp)} / कुल: {len(s_full)}"
        )
        render_trace_steps(
            s_disp,
            hint_for_sutra=hint_for_sutra,
            heading=None,
        )

st.divider()
st.caption(f"पंजीकृत सूत्र: {len(SUTRA_REGISTRY)} · रिपो: `{common.ROOT}`")
