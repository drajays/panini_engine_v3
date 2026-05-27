"""
दिक्-समास + स्त्री चतुर्थी (ङे) — प्रक्रिया: संस्कृत सूत्र + हिंदी (देवनागरी) + slp१ कोष्ठक।

Run: streamlit run streamlit_app/Home.py
"""
from __future__ import annotations

import html

import streamlit as st

import common  # noqa: E402

from pipelines.dik_caturthi_glassbox_text import GLASS_HEADER, glass_plain_text, glass_rows
from pipelines.dik_uttarapurva_demo import (
    DikCaturthiId,
    capture_caturthi_prakriya_stdout,
    caturthi_preset,
)

_PHASE_RULE = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"


@st.cache_data(show_spinner=False)
def _full_trace_cached(preset_id: str) -> str:
    return capture_caturthi_prakriya_stdout(preset_id)  # type: ignore[arg-type]


def _split_trace(full: str) -> dict[str, str]:
    i1 = full.find("PHASE 1: ALAUKIKA")
    i2 = full.find("PHASE 2: STRĪ")
    i3 = full.find("PHASE 3: VIBHAKTI")
    ia = full.find("── मार्गः A —")
    ib = full.find("── मार्गः B —")
    isum = full.find("SUMMARY")
    iapp = full.find("APPENDIX:")
    if i1 < 0:
        return {"error": full[:2000]}
    summary_slice = full[isum:iapp] if iapp >= 0 else full[isum:]
    return {
        "banner": full[:i1].strip(),
        "phase1": full[i1:i2].strip() if i2 > i1 else full[i1:].strip(),
        "phase2": full[i2:i3].strip() if i3 > i2 else "",
        "phase3_open": full[i3:ia].strip() if ia > i3 else full[i3:isum].strip(),
        "path_a": full[ia:ib].strip() if ib > ia else "",
        "path_b": full[ib:isum].strip() if isum > ib else "",
        "summary": summary_slice.strip(),
        "appendix": full[iapp:].strip() if iapp >= 0 else "",
    }


def _trace_pre(text: str, *, height_vh: float = 62.0) -> None:
    esc = html.escape(text)
    st.markdown(
        f"""
<style>
.trace-pre-wrap {{
  font-family: "JetBrains Mono", "SF Mono", ui-monospace, monospace,
    "Noto Sans Devanagari", "Noto Serif Devanagari", "Sanskrit 2003", serif;
  font-size: 0.8rem;
  line-height: 1.5;
  white-space: pre;
  margin: 0;
  padding: 0.9rem 1rem;
  border-radius: 10px;
  background: linear-gradient(160deg, #0c1222 0%, #0f172a 40%, #0a0f1a 100%);
  color: #e5e7eb;
  border: 1px solid rgba(100, 116, 139, 0.35);
  max-height: {height_vh}vh;
  overflow: auto;
}}
</style>
<pre class="trace-pre-wrap">{esc}</pre>
""",
        unsafe_allow_html=True,
    )


def _glas_box_row(
    n: str, sa_title: str, slp1: str, hi_line: str
) -> str:
    """One glass row: संस्कृत (सूत्र) + slp1 in parentheses + Hindi line — all in Devanagari for hi."""
    return f"""<div class="gstep">
  <div class="gno">{html.escape(n)}</div>
  <div class="gbody">
    <div class="gsa">{html.escape(sa_title)} <span class="slp1">(slp1: {html.escape(slp1)})</span></div>
    <div class="ghi">{html.escape(hi_line)}</div>
  </div>
</div>"""



def _render_glass_panels(pid: DikCaturthiId) -> None:
    p = caturthi_preset(pid)
    rows = glass_rows(p)
    ghdr = html.escape(GLASS_HEADER)
    parts: list[str] = [
        '<div class="glass-outer">',
        f'<p class="glass-hdr"><span class="glass-hdr-text">{ghdr}</span></p>',
    ]
    for n, s, slp, hi in rows:
        parts.append(_glas_box_row(n, s, slp, hi))
    parts.append("</div>")
    st.markdown(
        f"""
<style>
  .glass-outer {{
    background: linear-gradient(145deg, #fffdfb 0%, #f0f4ff 35%, #fdf8f3 100%);
    border: 1px solid #c7d2e3;
    border-radius: 14px;
    padding: 1rem 1.15rem 1.2rem 1.15rem;
    margin: 0.3rem 0 1.2rem 0;
    font-family: "Noto Sans Devanagari", "Noto Serif Devanagari", "Kohinoor Devanagari", serif;
    line-height: 1.6;
  }}
  .glass-hdr {{ color: #1e3a5f; font-size: 0.98rem; margin-bottom: 0.7rem; }}
  .gstep {{ display: flex; gap: 0.7rem; align-items: flex-start; border-bottom: 1px solid #e2e8f0; padding: 0.6rem 0; }}
  .gstep:last-child {{ border-bottom: none; }}
  .gno {{ font-weight: 800; min-width: 1.2rem; color: #0f4c81; font-size: 1.05rem; }}
  .gsa {{ color: #1a202c; font-size: 0.98rem; font-weight: 500; }}
  .ghi {{ color: #2d3b55; font-size: 0.9rem; margin-top: 0.35rem; font-weight: 400; }}
  .slp1 {{ font-size: 0.78rem; color: #64748b; font-family: ui-monospace, monospace; }}
  .gbody {{ flex: 1; min-width: 0; }}
</style>
{"".join(parts)}
""",
        unsafe_allow_html=True,
    )


st.set_page_config(
    page_title="दिक्-समास · चतुर्थी (ङे)",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("दिक्-समास — स्त्री-लिङ्ग, चतुर्थी एकवचन (ङे)")
st.markdown(
    '<p style="font-size:1.02rem; color:#334155;">'
    "अष्टाध्यायी-क्रम: मुख्य प्रक्रिया <b>संस्कृत (सूत्र-संकेत)</b> में, सरल बात "
    "<b>हिन्दी (देवनागरी)</b> में; <b>कोष्ठक (slp1)</b> में कम्प्यूटर-रूप।</p>",
    unsafe_allow_html=True,
)

c_opt = st.columns((1, 1, 1))
with c_opt[0]:
    choice = st.selectbox(
        "दिङ्-समास जोड़ चुनें (उपलब्ध जोड़: इंजिन में पंजीकृत) / Choose dik-pair",
        options=("uttarA_pUrvA", "dakziRA_pUrvA"),
        format_func=lambda k: "उत्तर + पूर्व (उत्तरपूर्व-दिक्)"
        if k == "uttarA_pUrvA"
        else "दक्षिण + पूर्व (दक्षिणपूर्व-दिक्)",
        help="2.2.26 के चार ठोस जोड़ों में से; दो शिक्षण-प्रेसेट।",
    )
preset: DikCaturthiId = choice  # type: ignore[assignment]
p_meta = caturthi_preset(preset)
with c_opt[1]:
    st.metric("समास-मूल (ह्रस्व-अन्त)", p_meta.title_short_deva, help=f"slp1: {p_meta.expected_merged_puM}")
with c_opt[2]:
    st.metric("उदाहरण-फल", f"अ → {p_meta.mar_a_dv}  |  ब → {p_meta.mar_b_dv}")

st.divider()
_render_glass_panels(preset)

with st.expander("काच-पेटी — टर्मिनल-रूप (कॉपी/पढ़ने हेतु)", expanded=False):
    gtxt = glass_plain_text(p_meta)
    st.code(gtxt, language=None)
    st.caption(
        f"कमान: `python3 -m pipelines.dik_uttarapurva_demo glass {preset}`"
    )
    st.download_button(
        "⬇ काच-पेटी टेक्स्ट (.txt)",
        data=gtxt.encode("utf-8"),
        file_name=f"kacapetI_glassbox_{preset}.txt",
        mime="text/plain; charset=utf-8",
        key="dl_glass_txt",
    )

st.subheader("क्रमबद्ध तकनीकी पाठ (नीचे)")
tab_gl, tab_tr = st.tabs(("संक्षिप्त विभाग", "पूर्ण इंजिन-ट्रेस"))

full_text = _full_trace_cached(preset)
sections = _split_trace(full_text)
if "error" in sections and list(sections.keys()) == ["error"]:
    st.error("पदच्छेद त्रुटि — कच्चा आउटपुट / Parse error – raw")
    _trace_pre(sections["error"], height_vh=40)
    st.stop()

with tab_gl:
    st.caption("प्रत्येक चरण: वही विवरण जो `pipelines/dik_uttarapurva_demo` से मिलता है (अंग्रेअज़ी लॉग)।")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("##### क्षेत्र १ · समास")
        _trace_pre(sections.get("phase1", ""), height_vh=42)
    with t2:
        st.markdown("##### क्षेत्र २ · स्त्री-प्रत्यय")
        _trace_pre(sections.get("phase2", ""), height_vh=32)
    with t3:
        st.markdown("##### क्षेत्र ३ · ङे + दोनों मार्ग")
        st.markdown("**6** तथा ङे-चयन, फिर A/B")
        _trace_pre(sections.get("phase3_open", ""), height_vh=28)
    st.markdown("##### मार्ग A / B")
    ca, cb = st.columns(2)
    with ca:
        st.markdown("**A** (सर्वनाम) ")
        _trace_pre(sections.get("path_a", ""), height_vh=40)
    with cb:
        st.markdown("**B** (नास्ति) ")
        _trace_pre(sections.get("path_b", ""), height_vh=40)
    st.markdown("##### सार + परिशिष्ट (शास्त्रीय क्रम) ")
    csum, capp = st.columns(2)
    with csum:
        _trace_pre(sections.get("summary", ""), height_vh=20)
    with capp:
        _trace_pre(sections.get("appendix", ""), height_vh=48)

with tab_tr:
    st.caption("डाउनलोड = वही raw UTF-8 जो टर्मिनल पर `python3 -m pipelines.dik_uttarapurva_demo caturthi` (डिफ़ाल्ट) देता है। "
               "पृष्ठ पर `selectbox` हेतु यह स्क्रिप्ट के समान *preset* से capचर होता है।")
    st.download_button(
        "⬇ पूर्ण लेख डाउनलोड (.txt)",
        data=full_text.encode("utf-8"),
        file_name=f"dik_caturthi_{preset}.txt",
        mime="text/plain; charset=utf-8",
    )
    st.markdown("##### ऊपरी-बक्स (बैनर)")
    _trace_pre(sections.get("banner", ""), height_vh=32)
    _trace_pre(full_text, height_vh=80)

st.divider()
st.caption(
    f"{_PHASE_RULE}  panini_engine_v3  ·  dik_uttarapurva_demo  "
    f"  ·  preset: {preset}  {_PHASE_RULE}"
)
