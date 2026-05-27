"""
तिङन्त प्रक्रिया — किसी भी धातु से कोई भी लकार, सम्पूर्ण ग्लासबॉक्स।
"""
from __future__ import annotations

import streamlit as st
import common  # noqa: E402

st.set_page_config(page_title="तिङन्त प्रक्रिया", page_icon="⚙️", layout="wide")

import sutras  # noqa: F401, E402
import json
from pathlib import Path

from phonology.joiner import slp1_to_devanagari
from pipelines.tinanta import derive, _dhatu_row_by_upadesha
from pipelines.dhatupatha import _payload, _envelope
from trace_view import filter_steps_surface_changed
from i18n_hi import hint_for_sutra

ROOT = Path(__file__).resolve().parent.parent.parent

# ── load lakāra metadata ──────────────────────────────────────────────────
@st.cache_data
def _lakara_meta() -> dict:
    p = ROOT / "data" / "inputs" / "lakara_metadata.json"
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}

@st.cache_data
def _dhatu_options() -> list[dict]:
    raw = _payload()
    env = _envelope(raw)
    return [
        e for e in env["entries"]
        if e.get("upadesha_slp1") and e.get("mula_dhatu_dev")
    ]

LAK_META = _lakara_meta()
LAK_CHOICES = {
    k: f"{v['dev']} ({v['en']})"
    for k, v in LAK_META.items()
    if not k.startswith("_")
}

PURUSHA_LABELS = {3: "प्रथमपुरुष (3rd)", 2: "मध्यमपुरुष (2nd)", 1: "उत्तमपुरुष (1st)"}
VACANA_LABELS  = {1: "एकवचन (sg)", 2: "द्विवचन (du)", 3: "बहुवचन (pl)"}

st.markdown(
    "## ⚙️ तिङन्त प्रक्रिया — स्वचालित ग्लासबॉक्स\n\n"
    "धातु + लकार + पुरुष + वचन → **सम्पूर्ण अष्टाध्यायी-क्रम**।  \n"
    "प्रत्येक चरण `apply_rule()` से — कोई shortcut नहीं।"
)
st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    raw_dhatu = st.text_input(
        "धातु उपदेश (SLP1 या देवनागरी-नाम)",
        value="BU",
        placeholder="BU / pac / kf / nI …",
        help="SLP1 upadeśa जैसे BU, pac, nI; या alias BvAdi_BU आदि।",
        key="tin_dhatu",
    )

with col2:
    lakara_key = st.selectbox(
        "लकार",
        options=list(LAK_CHOICES.keys()),
        format_func=lambda k: LAK_CHOICES.get(k, k),
        index=0,
        key="tin_lakara",
    )

col3, col4, col5 = st.columns(3)
with col3:
    purusha = st.selectbox("पुरुष", [3, 2, 1], format_func=lambda x: PURUSHA_LABELS[x], key="tin_p")
with col4:
    vacana  = st.selectbox("वचन",   [1, 2, 3], format_func=lambda x: VACANA_LABELS[x],  key="tin_v")
with col5:
    prayoga = st.radio("प्रयोग", ["kartari", "karmani", "bhave"],
                       format_func=lambda x: {"kartari":"कर्तरि","karmani":"कर्मणि","bhave":"भावे"}[x],
                       horizontal=True, key="tin_prayoga")

run = st.button("▶ प्रक्रिया चलाएँ", type="primary", key="tin_run")

if run:
    raw = raw_dhatu.strip()
    if not raw:
        st.error("धातु उपदेश भरें।")
        st.stop()

    # Check if Devanāgarī input — try to find by mula_dhatu_dev
    if any(0x0900 <= ord(c) <= 0x097F for c in raw):
        opts = _dhatu_options()
        match = [e for e in opts if e.get("mula_dhatu_dev","").strip() == raw.strip()]
        if not match:
            st.error(f"देवनागरी '{raw}' धातुपाठ में नहीं मिली। SLP1 upadeśa उपयोग करें।")
            st.stop()
        raw = match[0]["upadesha_slp1"]

    # Validate lakāra support
    if lakara_key not in ("laT",) and prayoga == "kartari":
        st.warning(
            f"लकार **{lakara_key}** के लिए pipeline अभी निर्माणाधीन है — "
            "केवल **laT** पूर्णतः समर्थित है। laT पर चला रहे हैं।"
        )
        lakara_key = "laT"

    try:
        row = _dhatu_row_by_upadesha(raw)
        gana = row.get("gana", 1)
        if gana not in (1, 4, 6):
            st.warning(
                f"गण {gana} ({row.get('gana_label_dev','')}) के लिए vikaraṇa अभी "
                "implement नहीं है। bhvādi (गण 1) पर चला रहे हैं।"
            )
    except KeyError as e:
        st.error(str(e))
        st.stop()

    try:
        state = derive(raw, lakara_key, prayoga, purusha, vacana)
    except NotImplementedError as e:
        st.error(f"अभी उपलब्ध नहीं: {e}")
        st.stop()
    except Exception as e:
        st.exception(e)
        st.stop()

    surface_slp = state.flat_slp1()
    surface_dev = state.flat_dev()

    # ── Result banner ──────────────────────────────────────────────────────
    st.success(f"### {surface_dev}  `{surface_slp}`")

    meta_cols = st.columns(5)
    with meta_cols[0]: st.metric("धातु",    row.get("mula_dhatu_dev", raw))
    with meta_cols[1]: st.metric("लकार",    LAK_META.get(lakara_key, {}).get("dev", lakara_key))
    with meta_cols[2]: st.metric("गण",      f"{gana} · {row.get('gana_label_dev','')}")
    with meta_cols[3]: st.metric("अर्थ",    row.get("artha_dev",""))
    with meta_cols[4]: st.metric("पद",      row.get("pada_label_dev",""))

    st.divider()

    # ── Trace ─────────────────────────────────────────────────────────────
    trace_mode = st.radio(
        "ट्रेस कैसे देखें?",
        ["changes_only", "full"],
        format_func=lambda k: {
            "changes_only": "केवल बदलाव (जहाँ SLP1 बदला)",
            "full": "सभी चरण (पूर्ण ट्रेस)",
        }[k],
        horizontal=True, key="tin_trace",
    )

    steps = (filter_steps_surface_changed(state.trace)
             if trace_mode == "changes_only" else state.trace)

    st.markdown(f"**{len(steps)} चरण** ({len(state.trace)} कुल)")

    for i, step in enumerate(steps):
        sid   = step.get("sutra_id", "?")
        fb    = step.get("form_before", "")
        fa    = step.get("form_after", "")
        why   = step.get("why_dev", "")
        hint  = hint_for_sutra(sid)
        changed = fb != fa

        label = f"{'🔄' if changed else '📋'}  {sid}"
        if changed:
            label += f"  `{fb}` → `{fa}`"
        else:
            label += f"  `{fa}`"

        with st.expander(label, expanded=(changed and i < 10)):
            cols = st.columns(2)
            with cols[0]:
                st.markdown(f"**सूत्रम्:** {sid}")
                st.markdown(f"**व्याख्या:** {why}")
                if hint:
                    st.caption(f"💡 {hint}")
            with cols[1]:
                if changed:
                    try:
                        dev_before = slp1_to_devanagari(
                            [v for t in (state.trace[i-1]["state_terms"] if "state_terms" in step else []) for v in []]
                        ) if False else fb
                        dev_after = fa
                        st.markdown(f"**पूर्व (SLP1):** `{fb}`")
                        st.markdown(f"**पश्चात् (SLP1):** `{fa}`")
                    except Exception:
                        st.markdown(f"**पूर्व:** `{fb}`")
                        st.markdown(f"**पश्चात्:** `{fa}`")
                else:
                    st.markdown(f"**रूप:** `{fa}`")

    st.divider()
    # Download trace JSON
    trace_json = json.dumps(state.trace, ensure_ascii=False, indent=2)
    st.download_button(
        "⬇ ट्रेस JSON डाउनलोड करें",
        data=trace_json,
        file_name=f"tinanta_{raw}_{lakara_key}_{purusha}_{vacana}.json",
        mime="application/json",
    )

st.divider()
st.markdown(
    "### त्वरित संदर्भ — सामान्य तिङन्त\n\n"
    "| धातु | लकार | रूप | अर्थ |\n"
    "|------|------|-----|------|\n"
    "| भू | लट् | भवति | he/she/it is/becomes |\n"
    "| पच् | लट् | पचति | he/she cooks |\n"
    "| नी | लट् | नयति | he/she leads |\n"
    "| गम् | लट् | गच्छति | he/she goes |\n"
    "| कृ | लट् | करोति | he/she does |\n"
    "| द्रु | लट् | द्रवति | he/she runs |\n"
)
