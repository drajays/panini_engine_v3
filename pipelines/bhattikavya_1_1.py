"""
pipelines/bhattikavya_1_1.py — जयमङ्गला on Bhaṭṭikāvya 1.1.

Eight padāni of the first śloka, each via ``apply_rule`` (Art. 7, 11):

  अभूत् · नृपः · विबुधसखः · परंतपः · गुणाः · वरः · सनातनः · उपागमत्

Tiṅanta cells reuse canonical ``pipelines.tinanta.derive``. Kṛt / taddhita /
samāsānta cells schedule the vidhāyaka named in the ṭīkā, then inflect.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_anga_samjna_6_4_1,
    P00_guna_rapara_ayadi,
    P00_krt_it_lopa,
    P00_vikarana_it_lopa,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from core.phases.tripadi import execute_tripadi_phase
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.krdanta import build_dhatu_state
from pipelines.tinanta import derive as derive_tinanta

__pipeline_category__ = "भट्टिकाव्य"


def _applied(state: State) -> list[str]:
    return [x["sutra_id"] for x in state.trace if x.get("status") == "APPLIED" and x.get("sutra_id")]


def _krt_it_lasaku(s: State) -> State:
    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")
    return P00_vikarana_it_lopa(s)


def _prathama(s: State, *, vacana: int = 1) -> State:
    from pipelines.subanta import (
        run_subanta_preflight_through_1_4_7,
        run_subanta_sup_attach_and_finish,
    )
    from engine.phases.pada_merger import pada_merge

    if s.terms:
        s.terms[0].tags.add("pulliṅga")
        s.terms[0].tags.add("prātipadika")
        s.terms[0].tags.add("anga")
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = f"1-{vacana}"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    pada_merge(s)
    return execute_tripadi_phase(s)


def _merge_pratipadika(s: State) -> State:
    from engine.phases.pada_merger import pada_merge

    s = apply_rule("1.2.46", s)
    pada_merge(s)
    if s.terms:
        s.terms[0].tags.update({"prātipadika", "anga", "pulliṅga"})
    return s


def derive_aBUt() -> State:
    """भू + लुङ् 3sg → अभूत् (३.२.११०, च्लि/सिच्, २.४.७७, ६.४.७१)."""
    return derive_tinanta("BU", "luG", "kartari", 3, 1)


def derive_upAgamat() -> State:
    """उप+आङ्+गम् + लुङ् 3sg → उपागमत् (३.१.५५ अङ्, ६.४.७१ अट्, ६.१.१०१)."""
    return derive_tinanta("gam", "luG", "kartari", 3, 1, upasargas=["upa", "A"])


# ── १.२  जयमङ्गला ──────────────────────────────────────────────────────────


def derive_vedAH() -> State:
    """विद् + अच् (३.१.१३४) → वेदाः (७.३.८६ गुण)."""
    s = build_dhatu_state("vid")
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "ac"
    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.1.134", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = P00_anga_samjna_6_4_1(s)
    s = apply_rule("7.3.86", s)
    s = _merge_pratipadika(s)
    return _prathama(s, vacana=3)


def derive_aDyEzwa() -> State:
    """अधि+इङ् लुङ् ātmanepada 3sg, गाङ्-अभाव → अध्यैष्ट."""
    return derive_tinanta("iN", "luG", "kartari", 3, 1, upasargas=["aDi"], pada="atmane")


def derive_ayazwa() -> State:
    """यज् लुङ् ātmanepada 3sg (१.३.७२) → अयष्ट."""
    return derive_tinanta("yaj", "luG", "kartari", 3, 1, pada="atmane")


def derive_apArIt() -> State:
    """पृ लुङ् परस्मैपद 3sg → अपारीत् (७.२.१, ७.३.९६, ८.२.२८)."""
    return derive_tinanta("pF", "luG", "kartari", 3, 1)


def derive_samamaMsta() -> State:
    """सम्+मन् लुङ् ātmanepada → सममंस्त (७.२.१० इट्-निषेध)."""
    return derive_tinanta("man", "luG", "kartari", 3, 1, upasargas=["sam"], pada="atmane")


def derive_vyajezwa() -> State:
    """वि+जि लुङ् ātmanepada (१.३.१९) → व्यजेष्ट."""
    return derive_tinanta("ji", "luG", "kartari", 3, 1, upasargas=["vi"], pada="atmane")


def derive_araMsta() -> State:
    """रम् लुङ् ātmanepada → अरंस्त (७.२.१०, ८.३.२३)."""
    s = derive_tinanta("ram", "luG", "kartari", 3, 1, pada="atmane")
    s = apply_rule("8.3.23", s)
    return s


def derive_samUlaGAtam() -> State:
    """समूल + हन् + णमुल् (३.४.३६) → समूलघातम्."""
    s = build_dhatu_state("han")
    upa = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("samUla")),
        tags={"upapada", "anga", "prātipadika"},
        meta={"upadesha_slp1": "samUla"},
    )
    s.terms = [upa] + s.terms
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "Ramul"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.4.36", s)
    s = P00_anga_samjna_6_4_1(s)
    s = apply_rule("7.3.54", s)
    s = apply_rule("7.2.116", s)
    s = apply_rule("7.3.32", s)
    s = apply_rule("1.3.9", s)  # ण्/उ/ल् already tagged it in 3.4.36
    s = _merge_pratipadika(s)
    if s.terms:
        s.terms[0].tags.add("avyaya")
    from engine.phases.pada_merger import pada_merge
    pada_merge(s)
    return execute_tripadi_phase(s)


def derive_nyavaDIt() -> State:
    """नि+हन् लुङ् → वध (२.४.४३) → न्यवधीत्."""
    return derive_tinanta("han", "luG", "kartari", 3, 1, upasargas=["ni"])


def derive_nfpaH() -> State:
    """नृ + पा + क (३.२.३) → नृपः."""
    s = build_dhatu_state("pA")
    nf = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("nf")),
        tags={"upapada", "anga", "prātipadika"},
        meta={"upadesha_slp1": "nf"},
    )
    s.terms = [nf] + s.terms
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "ka"
    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.2.3", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = P00_anga_samjna_6_4_1(s)
    s = apply_rule("6.4.64", s)
    s = apply_rule("2.4.71", s)
    s = _merge_pratipadika(s)
    return _prathama(s)


def derive_vibuDasaKaH() -> State:
    """वि+बुध+क (३.१.१३५) and सखि+टच् (५.४.९१, ६.४.१४८) → विबुधसखः."""
    s = build_dhatu_state("buD")
    vi = Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("vi")),
        tags={"upasarga", "pratyaya"},
        meta={"upadesha_slp1": "vi"},
    )
    s.terms = [vi] + s.terms
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "ka"
    s = apply_rule("1.4.59", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.1.135", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = _merge_pratipadika(s)

    sakhi = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("saKi")),
        tags={"anga", "prātipadika", "samasa"},
        meta={"upadesha_slp1": "saKi"},
    )
    s.terms.append(sakhi)
    s = apply_rule("5.4.91", s)
    s = P00_krt_it_lopa(s)  # 1.3.7 चुटू + 1.3.3 (टच्) — dhātu already not upadeśa
    s = apply_rule("6.4.1", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)
    s = _merge_pratipadika(s)
    return _prathama(s)


def derive_paraMtapaH() -> State:
    """पर + ताप् + खच् (३.२.३९, ६.४.९४, ६.३.६७, ८.३.२३) → परंतपः."""
    s = build_dhatu_state("tAp")
    s.terms[0].meta["upadesha_slp1"] = "tap"
    para = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("para")),
        tags={"upapada", "anga", "prātipadika"},
        meta={"upadesha_slp1": "para"},
    )
    s.terms = [para] + s.terms
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "Kac"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.2.39", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = P00_anga_samjna_6_4_1(s)
    s = apply_rule("6.4.94", s)
    s = apply_rule("6.3.67", s)
    s = _merge_pratipadika(s)
    s = _prathama(s)
    s = apply_rule("8.3.23", s)
    return s


def derive_guNAH() -> State:
    """गुण + घञ् (३.३.१९ / ३.३.१६) → गुणाः."""
    s = build_dhatu_state("guRa")
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "GaY"
    s.meta["krt_artha"] = "karmani"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.3.18", s)
    s = apply_rule("3.3.19", s)
    s = apply_rule("3.3.16", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = apply_rule("7.2.116", s)
    s = _merge_pratipadika(s)
    return _prathama(s, vacana=3)


def derive_varaH() -> State:
    """वृ + अप् (३.३.५८) → वरः."""
    s = build_dhatu_state("vfY")
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "ap"
    s.meta["krt_artha"] = "karmani"
    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.3.58", s)
    s = P00_vikarana_it_lopa(s)
    s = apply_rule("3.4.114", s)
    s = P00_anga_samjna_6_4_1(s)
    s = P00_guna_rapara_ayadi(s)
    s = _merge_pratipadika(s)
    return _prathama(s)


def derive_sanAtanaH() -> State:
    """सना + ट्यु/तुट् (४.३.२३, ७.१.१) → सनातनः."""
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("sanA")),
        tags={"anga", "prātipadika", "avyaya"},
        meta={"upadesha_slp1": "sanA"},
    )
    s = State(terms=[stem], meta={"derivation_class": "taddhita"}, trace=[])
    s = apply_rule("4.3.23", s)
    s = P00_krt_it_lopa(s)
    s = apply_rule("7.1.1", s)
    s = _merge_pratipadika(s)
    return _prathama(s)


WORDS = (
    ("अभूत्", "derive_aBUt", "भू + लुङ्", "1.1"),
    ("नृपः", "derive_nfpaH", "नृ + पा + क", "1.1"),
    ("विबुधसखः", "derive_vibuDasaKaH", "विबुध + सखि + टच्", "1.1"),
    ("परंतपः", "derive_paraMtapaH", "पर + ताप् + खच्", "1.1"),
    ("गुणाः", "derive_guNAH", "गुण + घञ्", "1.1"),
    ("वरः", "derive_varaH", "वृ + अप्", "1.1"),
    ("सनातनः", "derive_sanAtanaH", "सना + ट्यु", "1.1"),
    ("उपागमत्", "derive_upAgamat", "उप+आङ्+गम् + लुङ्", "1.1"),
    ("वेदाः", "derive_vedAH", "विद् + अच्", "1.2"),
    ("अध्यैष्ट", "derive_aDyEzwa", "अधि+इङ् + लुङ्", "1.2"),
    ("अयष्ट", "derive_ayazwa", "यज् + लुङ्", "1.2"),
    ("अपारीत्", "derive_apArIt", "पृ + लुङ्", "1.2"),
    ("सममंस्त", "derive_samamaMsta", "सम्+मन् + लुङ्", "1.2"),
    ("व्यजेष्ट", "derive_vyajezwa", "वि+जि + लुङ्", "1.2"),
    ("अरंस्त", "derive_araMsta", "रम् + लुङ्", "1.2"),
    ("समूलघातम्", "derive_samUlaGAtam", "समूल + हन् + णमुल्", "1.2"),
    ("न्यवधीत्", "derive_nyavaDIt", "नि+हन् + लुङ्", "1.2"),
)

NOTES = {
    "derive_aBUt": "भूतार्थे लुङ् (३.२.८४/३.२.११०) · तिप् (३.४.७८) · इतश्च (३.४.१००) · अट् (६.४.७१) · च्लि/सिच् (३.१.४३/४४) · सिच्-लुक् (२.४.७७) · भू-सुवोस्तिङि (७.३.८८)",
    "derive_nfpaH": "आतोऽनुपसर्गे कः (३.२.३) · सुपो लुक् (२.४.७१) · आतो लोप इटि च (६.४.६४)",
    "derive_vibuDasaKaH": "इगुपधज्ञाप्रीकिरः कः (३.१.१३५) · राजाहःसखिभ्यष्टच् (५.४.९१) · यस्येति च (६.४.१४८)",
    "derive_paraMtapaH": "द्विषत्परयोस्तापेः (३.२.३९) · खचि ह्रस्वः (६.४.९४) · मुम् (६.३.६७) · मोऽनुस्वारः (८.३.२३)",
    "derive_guNAH": "अकर्तरि च कारके संज्ञायाम् (३.३.१९) · घञ् (३.३.१६) · अत उपधायाः (७.२.११६) · अथवा एरच् (३.३.५६)",
    "derive_varaH": "ग्रहवृदृनिश्चिगमश्च (३.३.५८) · सार्वधातुकार्धधातुकयोः (७.३.८४)",
    "derive_sanAtanaH": "सायंचिरं…ट्युट्युलो तुट् च (४.३.२३) · युवोरनाको (७.१.१)",
    "derive_upAgamat": "लुङ् + तिप् · अट् (६.४.७१) · पुषाद्युताद्यॢदितः (३.१.५५ अङ्) · अकः सवर्णे दीर्घः (६.१.१०१)",
    "derive_vedAH": "नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः (३.१.१३४) · पुगन्तलघूपधस्य च (७.३.८६)",
    "derive_aDyEzwa": "लुङ् (३.२.११०) · आडजादीनाम् (६.४.७२) · आटश्च (६.१.९०) · च्लि/सिच् · इट् (७.२.३५) · आदेशप्रत्यययोः (८.३.५९) · ष्टुना ष्टुः (८.४.४१) · इको यणचि (६.१.७७)",
    "derive_ayazwa": "स्वरितञितः (१.३.७२) · अट् (६.४.७१) · व्रश्च…षः (८.२.३६) · झलो झलि (८.२.२६) · ष्टुना ष्टुः (८.४.४१)",
    "derive_apArIt": "इट् (७.२.३५) · अस्तिसिचोऽपृक्ते (७.३.९६) · सिचि वृद्धिः (७.२.१) · इट ईटि (८.२.२८)",
    "derive_samamaMsta": "अनुदात्तङितः (१.३.१२) · एकाच उपदेशेऽनुदात्तात् (७.२.१०) · अट् (६.४.७१)",
    "derive_vyajezwa": "विपराभ्यां जेः (१.३.१९) · अट् · सिच् · इट् · आदेशप्रत्यययोः (८.३.५९)",
    "derive_araMsta": "एकाच उपदेशेऽनुदात्तात् (७.२.१०) · अट् · मोऽनुस्वारः (८.३.२३)",
    "derive_samUlaGAtam": "समूलाकृतजीवेषु हन्कृञ्ग्रहः (३.४.३६) · हो हन्तेः (७.३.५४) · अत उपधायाः (७.२.११६) · हनस्तः (७.३.३२)",
    "derive_nyavaDIt": "लुङि च (२.४.४३ वध) · अतो लोपः (६.४.४८) · इट ईटि (८.२.२८) · इको यणचि (६.१.७७)",
}
