"""एक कोष्ठक — विस्तृत प्रक्रिया (हिन्दी + देवनागरी)।"""
from __future__ import annotations

import streamlit as st

import common  # noqa: E402

st.set_page_config(page_title="एक कोष्ठक — प्रक्रिया", page_icon="🔍", layout="wide")

import sutras  # noqa: F401, E402
from sutras.adhyaya_1.pada_1.sutra_1_1_1 import VRIDHI_SAMJNA_REFERENCING_SUTRAS
from engine import SUTRA_REGISTRY
from phonology.joiner import slp1_to_devanagari
from pipelines.sarva_subanta import derive_sarva_pulliṅga
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
    "### एक विभक्ति × एक वचन — पूरी प्रक्रिया\n\n"
    "अभी यह पृष्ठ **पुंलिङ्ग** के दो stem प्रकार सपोर्ट करता है:\n\n"
    "- **अकारान्त** (SLP1 अन्तिम `a`) — उदा. `राम` / `rAma`, `गज` / `gaja`\n"
    "- **इकारान्त** (SLP1 अन्तिम `i`) — उदा. `हरि` / `hari`\n\n"
    "नीचे प्रत्येक चरण पर संस्कृत व्याख्या और हिन्दी संक्षिप्त टिप्पणी।"
)

raw_stem = st.text_input(
    "प्रातिपदिक (देवनागरी या SLP1)",
    value="rAma",
    placeholder="राम / हरि  या  rAma / hari",
    key="stem_cell",
    help="एक समय में एक ही लिपि।",
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

stem_dev = stem_slp1_to_display_devanagari(stem_slp)
stem_kind = "अकारान्त" if is_akar else "इकारान्त"
st.caption(
    f"**आंतरिक SLP1:** `{stem_slp}` · **देवनागरी प्रातिपदिक:** {stem_dev} · **विशेष:** {stem_kind}"
)

gold = None
gold_label = None
if stem_slp == "rAma":
    gold = common.load_rama_gold()
    gold_label = "राम (gold)"
elif stem_slp == "hari":
    gold = common.load_hari_gold()
    gold_label = "हरि (gold)"
elif stem_slp == "sarva":
    gold = common.load_sarva_gold()
    gold_label = "सर्व (gold)"
elif stem_slp == "jYAna":
    gold = common.load_jnana_gold()
    gold_label = "ज्ञान (gold)"
elif stem_slp == "tad":
    gold = common.load_tad_gold()
    gold_label = "तद् (gold)"

use_gold = gold is not None
key = f"{vib}-{vac}"
gcell = gold["cells"].get(key, {}) if gold else {}
gold_dev = gcell.get("form_dev", "—") if use_gold else "—"
gold_slp = gcell.get("form_slp1", "—") if use_gold else "—"

if stem_slp == "sarva":
    state = derive_sarva_pulliṅga(vib, vac)
elif is_akar:
    state = derive_akarant_pullinga(stem_slp, vib, vac)
else:
    state = derive_ikarant_pullinga(stem_slp, vib, vac)
surface_dev = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
surface_slp = state.render()

m1, m2 = st.columns(2)
with m1:
    st.markdown("##### सन्दर्भ रूप (यदि उपलब्ध)")
    st.metric("gold", gold_dev if use_gold else "—", delta=None)
    if gold_label:
        st.caption(gold_label)
    st.caption(f"SLP1: `{gold_slp}`")
with m2:
    st.markdown("##### इन्जिन् निष्कर्ष")
    st.metric("प्रक्रिया से रूप", surface_dev)
    st.caption(f"SLP1: `{surface_slp}`")

st.markdown("---")
st.markdown("#### सूत्र-मार्ग — संस्कृत + हिन्दी सहायक")

trace_mode = st.radio(
    "ट्रेस कैसे देखें?",
    options=("full", "changes_only"),
    format_func=lambda k: {
        "full": "सभी चरण (पूर्ण ट्रेस — हर नियम)",
        "changes_only": "केवल बदलाव (जहाँ SLP1 रूप बदला)",
    }[k],
    horizontal=True,
    help=(
        "‘केवल बदलाव’ में वे चरण दिखते हैं जहाँ `form_before` ≠ `form_after`। "
        "संज्ञा/अनुवाद जो रूप नहीं बदलते वे छिप जाते हैं।"
    ),
)

full_trace = state.trace
if trace_mode == "changes_only":
    display_trace = filter_steps_surface_changed(full_trace)
else:
    display_trace = list(full_trace)

st.caption(
    f"**दिख रहे चरण:** {len(display_trace)} · **कुल ट्रेस में:** {len(full_trace)}"
)
if trace_mode == "changes_only" and not display_trace:
    st.warning(
        "इस कोष्ठक पर कोई सतह-परिवर्तन चरण नहीं मिला (असामान्य) — पूर्ण ट्रेस देखें।"
    )

for step in display_trace:
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
    if sid == "1.1.1":
        with st.expander("१.१.१ वृद्धि-संज्ञा — विस्तार (शास्त्रीय)", expanded=False):
            st.markdown(
                "**सार्वत्रिक संज्ञा** — किसी **अधिकार**-खण्ड के अन्तर्गत नहीं; "
                "‘वृद्धि’ शब्द का अर्थ यहाँ **नाम-निर्देश** मात्र (आ/ऐ/ौ वर्णसमूह)। "
                "**वृद्धि-क्रिया** (वास्तविक बदलाव) तब होती है जब **विधि**-सूत्र "
                "(जैसे ६.१.८८) अपनी **cond** से चलते हैं — अर्थात् जब ‘वृद्धि’ "
                "प्रयोग में आवश्यक हो।\n\n"
                "*[रेसिपि में १.१.१ शीघ्र नियतम् — परन्तु वृद्धि-**प्रयोग** अत्र न, "
                "यतो हि अद्यापि कस्यचिद् विधि-सूत्रेण तदर्थं नाह्वानम्; केवल संज्ञा-पञ्जीकरणम्।]*\n\n"
                "अष्टाध्याय्यां **साक्षात्** ‘वृद्धि’-संज्ञा यत्र प्रयुक्ता (नव सूत्र) —"
            )
            for ref_id, lemma in VRIDHI_SAMJNA_REFERENCING_SUTRAS:
                st.markdown(f"- **{ref_id}** — {lemma}")
            st.caption("अनुवृत्ति से अन्यत्र अपि अस्याः संज्ञायाः ग्रहणं भवितुम् अर्हति।")
    st.divider()

st.caption(f"चरण: `{state.phase}` · नियम सूची में: {len(SUTRA_REGISTRY)}")
