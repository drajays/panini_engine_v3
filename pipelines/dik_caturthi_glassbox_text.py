"""
काच-पेटी (ग्लासबॉक्स) — देवनागरी व्याख्या; slp1 Roman कोष्ठक में।

    python3 -m pipelines.dik_uttarapurva_demo glass
    python3 -m pipelines.dik_uttarapurva_demo glass dakziRA_pUrvA
"""
from __future__ import annotations

from typing import List, Tuple

from pipelines.dik_uttarapurva_demo import DikCaturthiId, DikCaturthiPreset, caturthi_preset

# देवनागरी सूत्र-क्रम: 7.3.113 / 7.3.114 / 6.1.88 (CJK-अंक नहीं)।
D_7_3_113 = f"\N{DEVANAGARI DIGIT SEVEN}.\N{DEVANAGARI DIGIT THREE}.\N{DEVANAGARI DIGIT ONE}\N{DEVANAGARI DIGIT ONE}\N{DEVANAGARI DIGIT THREE}"
D_7_3_114 = f"\N{DEVANAGARI DIGIT SEVEN}.\N{DEVANAGARI DIGIT THREE}.\N{DEVANAGARI DIGIT ONE}\N{DEVANAGARI DIGIT ONE}\N{DEVANAGARI DIGIT FOUR}"
D_6_1_88 = f"\N{DEVANAGARI DIGIT SIX}.\N{DEVANAGARI DIGIT ONE}.\N{DEVANAGARI DIGIT EIGHT}\N{DEVANAGARI DIGIT EIGHT}"
D_1_1_28 = f"\N{DEVANAGARI DIGIT ONE}.\N{DEVANAGARI DIGIT ONE}.\N{DEVANAGARI DIGIT TWO}\N{DEVANAGARI DIGIT EIGHT}"
D_1_1_46 = f"\N{DEVANAGARI DIGIT ONE}.\N{DEVANAGARI DIGIT ONE}.\N{DEVANAGARI DIGIT FOUR}\N{DEVANAGARI DIGIT SIX}"


# प्रत्येक पंक्ति: संस्कृत-शीर्षक; नीचे सरल हिन्दी; slp1-रूप कोष्ठक में।
GLASS_HEADER = (
    "काँच-पेटी व्याख्या (देवनागरी) — प्रत्येक पंक्ति: संस्कृत-शीर्षक; नीचे सरल हिन्दी; "
    "slp1-रूप कोष्ठक में।"
)

_SA_KA = (
    "समासाधिकार २.१.३; अनन्तरं २.४.७१ (अन्तःसुपो लुक्), ततः २.२.२६ दिङ्नामान्यन्तराले, "
    f"१.२.\N{DEVANAGARI DIGIT FOUR}\N{DEVANAGARI DIGIT THREE} उपसर्जनम्, वार्तिक — "
    f"सर्वनाम्नो वृत्तिमात्रे पुंवद्भावो वक्तव्यः, १.२.\N{DEVANAGARI DIGIT FOUR}\N{DEVANAGARI DIGIT EIGHT} "
    f"ह्रस्व, १.२.\N{DEVANAGARI DIGIT FOUR}\N{DEVANAGARI DIGIT SIX} प्रातिपदिक-संज्ञा"
)
_SA_KH = (
    f"स्त्री-प्रक्रिया: ४.१.१ अधिकार, ४.१.\N{DEVANAGARI DIGIT FOUR} अजाद्यतष्टाप्, इत्-लोप, "
    f"१.२.\N{DEVANAGARI DIGIT FOUR}\N{DEVANAGARI DIGIT FIVE} प्रातिपदिक"
)
_SA_GA = f"चतुर्थी एकवचन ४.१.२: प्रत्यय Ne (ङे); यहाँ {D_1_1_28} विभाषा से A/B दोनों मार्ग खुलते हैं"
_SA_GH1 = f"मार्ग अ — {D_1_1_28}: सर्वनाम-संज्ञा, {D_7_3_114} स्याट् + ह्रस्व, {D_1_1_46}, इत्-लोप, {D_6_1_88}"
_SA_GH2 = f"मार्ग ब — {D_1_1_28}: सर्वनाम-संज्ञा नास्ति, {D_7_3_113} याड्, {D_1_1_46}, इत्-लोप, {D_6_1_88}"


def slp1_chain_ka(p: DikCaturthiPreset) -> str:
    """slp1 अनुक्रम (शिक्षण-कोष्ठक)।"""
    if p.id == "uttarA_pUrvA":
        return "uttarA + pUrvA → uttarApUrvA → uttarapUrvA → uttarapUrva"
    if p.id == "dakziRA_pUrvA":
        return "dakziRA + pUrvA → dakziRApUrvA → dakziRapUrvA → dakziRapUrva"
    raise KeyError(p.id)


def _hindi_ka(p: DikCaturthiPreset) -> str:
    m1, m2, stem = p.m1_slp, p.m2_slp, p.expected_merged_puM
    if p.id == "uttarA_pUrvA":
        return (
            "सबसे पहले अलौकिक विग्रह रहता है; अन्तःसुप् २.४.७१ से लुप्त होते हैं; फिर समास बनता है। "
            f"पूर्वपद '{m1}' पर वार्तिकेन पुंवद्भाव होकर 'uttara' होता है; उसके बाद उत्तरपद '{m2}' का "
            f"ह्रस्व होकर 'pUrva' बनता है। इस प्रकार समास-प्रातिपदिक = {stem}।"
        )
    return (
        "सबसे पहले अलौकिक विग्रह रहता है; अन्तःसुप् २.४.७१ से लुप्त होते हैं; फिर समास बनता है। "
        f"पूर्वपद '{m1}' पर वार्तिकेन पुंवद्भाव होकर 'dakziRa' होता है; उसके बाद उत्तरपद '{m2}' का "
        f"ह्रस्व होकर 'pUrva' बनता है। इस प्रकार समास-प्रातिपदिक = {stem}।"
    )


def _hindi_kh(p: DikCaturthiPreset) -> str:
    s = p.strI_ā_banta
    return (
        f"यह अकारान्त समास अब स्त्री-प्रातिपदिक बनता है — यहाँ ङीप नहीं, ४.१.४ से टाप् (इंजिन-उपदेशः wAp) "
        f"आता है। इत्-लोप के बाद रूप '{s}' मिलता है।"
    )


def _hindi_ga() -> str:
    return (
        f"ङे पर दो रास्ते हैं: सर्वनाम-संज्ञा हो तो {D_7_3_114}, न हो तो {D_7_3_113}; "
        f"अंत में {D_6_1_88} से ऐ-रूप सिद्ध होता है।"
    )


def _hindi_gh1(p: DikCaturthiPreset) -> str:
    return (
        "यदि सर्वनाम-संज्ञा स्वीकार की जाए, तो अङ्ग पर ह्रस्व होता है और 'स्याट्' आगम आता है; "
        f"फिर वृद्धि-संधि से अन्तिम रूप '{p.mar_a_dv}' सिद्ध होता है।"
    )


def _hindi_gh2(p: DikCaturthiPreset) -> str:
    return (
        f"यदि सर्वनाम-संज्ञा न मानी जाए, तो 'याड्' आगम होता है; अन्त में रूप '{p.mar_b_dv}' सिद्ध होता है।"
    )


def glass_rows(p: DikCaturthiPreset) -> List[Tuple[str, str, str, str]]:
    """
    (लेबल, संस्कृत-पंक्ति, slp1-पाठ, हिन्दी) — UI में ``(slp1: …)`` के अन्दर slp1-पाठ।
    """
    return [
        ("क", _SA_KA, slp1_chain_ka(p), _hindi_ka(p)),
        (
            "ख",
            _SA_KH,
            f"{p.expected_merged_puM} + wAp → {p.strI_ā_banta}",
            _hindi_kh(p),
        ),
        (
            "ग",
            _SA_GA,
            f"{p.strI_ā_banta} + Ne",
            _hindi_ga(),
        ),
        (
            "घ-१",
            _SA_GH1,
            p.caturthi_slp1_marA,
            _hindi_gh1(p),
        ),
        (
            "घ-२",
            _SA_GH2,
            p.caturthi_slp1_marB,
            _hindi_gh2(p),
        ),
    ]


def glass_plain_text(p: DikCaturthiPreset) -> str:
    """टर्मिनल/क्लिपबोर्ड — शीर्षक + प्रत्येक पंक्ति: संस्कृत, (slp1: …), हिन्दी।"""
    out: list[str] = [GLASS_HEADER, ""]
    for lab, sa, slp, hi in glass_rows(p):
        out.append(lab)
        out.append(sa)
        out.append(f"(slp1: {slp})")
        out.append(hi)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def glassbox_for_id(pid: DikCaturthiId) -> str:
    return glass_plain_text(caturthi_preset(pid))

