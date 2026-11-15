"""Tag helpers for ashtadhyayi.com-style dhātu / śabda filter panels.

Tags mirror the letter / prakriyā-option tagging used on ashtadhyayi.com
(dhatufilters / shabdafilters). Used by the web UI index dump and the
/api/dhaturupa/roots payload — never by engine cond() (Art. 6).
"""
from __future__ import annotations

from typing import Iterable

# SLP1 → Devanāgarī letter name used in *कारान्त / *कारादि / *कारोपध tags
_SLP_NAME = {
    "a": "अ", "A": "आ", "i": "इ", "I": "ई", "u": "उ", "U": "ऊ",
    "f": "ऋ", "F": "ॠ", "x": "ऌ", "X": "ॡ", "e": "ए", "E": "ऐ",
    "o": "ओ", "O": "औ",
    "k": "क", "K": "ख", "g": "ग", "G": "घ", "N": "ङ",
    "c": "च", "C": "छ", "j": "ज", "J": "झ", "Y": "ञ",
    "w": "ट", "W": "ठ", "q": "ड", "Q": "ढ", "R": "ण",
    "t": "त", "T": "थ", "d": "द", "D": "ध", "n": "न",
    "p": "प", "P": "फ", "b": "ब", "B": "भ", "m": "म",
    "y": "य", "r": "र", "l": "ल", "v": "व",
    "S": "श", "z": "ष", "s": "स", "h": "ह", "M": "ं", "H": "ः",
}
_VOWELS = set("aAiIuUfFxXeEoO")
_JHAL = set("kKgGcCjJwWqQtTdDpPbBSzsh")  # approx झल् (no nasals/semivowels)
_RAL = set("rl")  # रल्
_PANCAM = set("NYRnm")  # varga-pañcama + m
_ANUBANDHA = {
    "a": "अदित्", "A": "आदित्", "i": "इदित्", "I": "ईदित्", "u": "उदित्", "U": "ऊदित्",
    "f": "ऋदित्", "x": "ऌदित्", "e": "एदित्", "o": "ओदित्",
    "k": "कित्", "N": "ङित्", "Y": "ञित्", "w": "टित्", "R": "णित्",
    "m": "मित्", "p": "पित्", "z": "षित्",
}

_GANA = ["", "भ्वादिः", "अदादिः", "जुहोत्यादिः", "दिवादिः", "स्वादिः",
         "तुदादिः", "रुधादिः", "तनादिः", "क्र्यादिः", "चुरादिः"]


def _name(slp: str) -> str:
    if slp == "r":
        return "रेफ"
    return _SLP_NAME.get(slp, slp)


def letter_tags_from_slp(slp: str) -> list[str]:
    """आदि / अन्त्य / उपधा tags from an SLP1 stem or upadeśa (it-marks stripped lightly)."""
    s = (slp or "").replace("~", "").replace("\\", "")
    # drop trailing nasal/visarga for ending class; keep body for upadha
    body = s.rstrip("MH")
    if not body:
        return []
    tags: list[str] = []
    first, last = body[0], body[-1]
    # आदि
    if first in _SLP_NAME:
        tags.append(("रेफादिः" if first == "r" else f"{_name(first)}कारादिः"))
        if first in _VOWELS:
            tags.append("अजादिः")
            if first not in "aA":
                tags.append("इजादिः")
        else:
            tags.append("हलादिः")
            if first in _JHAL:
                tags.append("झलादिः")
    # अन्त्य
    if last in _SLP_NAME:
        tags.append(("रेफान्तः" if last == "r" else f"{_name(last)}कारान्तः"))
        if last in _VOWELS:
            tags.append("अजन्तः")
            if last not in "aA":
                tags.append("इजन्तः")
                if last in "eEoO":
                    tags.append("एजन्तः")
        else:
            tags.append("हलन्तः")
            if last in _RAL:
                tags.append("रलन्तः")
            if last in _JHAL:
                tags.append("झलन्तः")
            if last in _PANCAM:
                tags.append("अनुनासिकान्तः")
    # उपधा
    if len(body) >= 2:
        up = body[-2]
        if up in _SLP_NAME:
            tags.append(("रेफोपधः" if up == "r" else f"{_name(up)}कारोपधः"))
    # अच् count (rough: vowels in body)
    ac = sum(1 for c in body if c in _VOWELS)
    tags.append("एकाच्" if ac <= 1 else "अनेकाच्")
    return tags


def anubandha_tags_from_slp(upadesha: str, it_markers: Iterable[str] | None = None) -> list[str]:
    """इत् tags from explicit it_markers when present; else only clear trailing markers.

    Do not scan every vowel in the upadeśa (that falsely tags भू as ऊदित्).
    """
    out: list[str] = []
    for m in it_markers or []:
        m = str(m).strip()
        if not m:
            continue
        # markers may already be Devanāgarī labels or SLP1 letters
        if m in _ANUBANDHA.values() or m.endswith("ित्"):
            out.append(m)
        elif m in _ANUBANDHA:
            out.append(_ANUBANDHA[m])
        elif m.endswith("~") and m[0] in _ANUBANDHA:
            out.append(_ANUBANDHA[m[0]])
    s = (upadesha or "").replace("\\", "")
    if "ir" in s[-4:] or s.endswith("ir~") or "ir~" in s:
        out.append("इरित्")
    # nasalized anubandha in SLP1 often written with trailing ~
    if "~" in s:
        # letters immediately before ~ are इत्
        for i, ch in enumerate(s):
            if ch == "~" and i > 0 and s[i - 1] in _ANUBANDHA:
                out.append(_ANUBANDHA[s[i - 1]])
        if any(s[i] in "ufx" and i + 1 < len(s) and s[i + 1] == "~" for i in range(len(s))):
            out.append("उगित्")
    seen, uniq = set(), []
    for t in out:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq

def shabda_tags(word_slp: str, linga_code: str, prakriya_options: dict | None,
                sk: str = "", lsk: str = "") -> list[str]:
    """Tags for one śabda row (antyavarṇa + speciality + grantha)."""
    tags = letter_tags_from_slp(word_slp)
    # keep only ending-side tags for shabda antyavarṇa panel (drop आदि/उपधा/अच्)
    keep_pref = ("अजन्तः", "हलन्तः", "इजन्तः", "एजन्तः", "झलन्तः", "रलन्तः", "अनुनासिकान्तः")
    tags = [t for t in tags if t in keep_pref or t.endswith("कारान्तः") or t == "रेफान्तः"]

    n = prakriya_options or {}
    if n.get("एकवचनाभावः") and n.get("बहुवचनाभावः"):
        tags.append("नित्यद्विवचनान्तः")
    if n.get("द्विवचनाभावः") and n.get("बहुवचनाभावः"):
        tags.append("नित्यैकवचनान्तः")
    if n.get("एकवचनाभावः") and n.get("द्विवचनाभावः"):
        tags.append("नित्यबहुवचनान्तः")
    if any(n.get(k) for k in ("यू_स्त्र्याख्यौ_नदी", "प्रथमलिङ्गग्रहणं_च")):
        tags.append("नदीसंज्ञकः")
    if any(n.get(k) for k in ("वामि", "ङिति_ह्रस्वश्च")):
        tags.append("विशिष्टस्थलेषु_विकल्पेन_नदीसंज्ञकः")

    slp = (word_slp or "")
    if slp.endswith("an"):
        tags.append("अन्नन्तः")
    if slp.endswith("in"):
        tags.append("इन्नन्तः")
    if slp.endswith("as"):
        tags.append("असन्तः")
    if len(slp) >= 4 and slp.endswith("van") and slp[-4] not in _VOWELS:
        tags.append("संयोगपूर्व_वन्नन्तः")
    if len(slp) >= 4 and slp.endswith("man") and slp[-4] not in _VOWELS:
        tags.append("संयोगपूर्व_मन्नन्तः")

    mapping = [
        ("सम्बोधनाभावः", "सम्बोधनाभावः"),
        ("सर्वादीनि_सर्वनामानि", "सर्वनामशब्दः"),
        ("इगन्त_नपुंसकलिङ्ग_भाषितपुंस्क", "भाषितपुंस्कः"),
        ("घि", "घिसंज्ञकः"),
        ("आबन्त", "आबन्तः"),
        ("ङ्यन्त", "ङ्यन्तः"),
        ("उगित्", "उगित्"),
        ("अत्वन्त", "अत्वन्तः"),
        ("तृजन्त_तृन्नन्त", "तृजन्तः"),
        ("क्विन्", "क्विन्नन्तः"),
    ]
    for src, dst in mapping:
        if n.get(src):
            tags.append(dst)

    if sk:
        tags.append("sk")
    if lsk:
        tags.append("lsk")
    if linga_code:
        tags.append(linga_code)  # P/S/N/A for linga filter field match too
    # unique
    seen, uniq = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq


def dhatu_tags(*, upadesha_slp1: str, gana: int | str | None, pada: str,
               settva: str, karma: str, antarganas: str = "",
               raw_tags: str | Iterable[str] = "",
               flags: dict | None = None,
               it_markers: Iterable[str] | None = None) -> list[str]:
    """Union of letter tags, field tags, antargaṇa, and upstream tag string."""
    tags = letter_tags_from_slp(upadesha_slp1)
    tags.extend(anubandha_tags_from_slp(upadesha_slp1, it_markers=it_markers))
    try:
        g = int(gana or 0)
    except (TypeError, ValueError):
        g = 0
    if 1 <= g < len(_GANA):
        tags.append(_GANA[g])
        tags.append(str(g))
    if pada:
        tags.append(pada)
    if settva:
        tags.append(settva)
    if karma:
        tags.append(karma)
    for a in (antarganas or "").split(","):
        a = a.strip()
        if a:
            tags.append(a)
    if isinstance(raw_tags, str):
        parts = [p.strip() for p in raw_tags.split(",") if p.strip()]
    else:
        parts = [str(p).strip() for p in (raw_tags or []) if str(p).strip()]
    tags.extend(parts)
    fl = flags or {}
    if fl.get("ekac"):
        if "एकाच्" not in tags:
            tags.append("एकाच्")
    if fl.get("udatta"):
        tags.append("उदात्तोपदेशः")
    elif "उदात्तोपदेशः" not in tags and "अनुदात्तोपदेशः" not in tags:
        # leave unset unless upstream said so
        pass
    # षोपदेश / णोपदेश from upadeśa
    u = (upadesha_slp1 or "").replace("~", "")
    if u.startswith("z") or "z" in u[:2]:
        tags.append("षोपदेशः")
    if "R" in u or u[:1] in ("R",) or "R" == u[0:1]:
        pass
    if u.startswith("R") or (len(u) > 1 and u[0] in "kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh" and "R" in u):
        # coarse: initial ṇ after it-strip is rare; use citation if starts with R
        if u.lstrip("aAiIuUfFxXeEoO").startswith("R") or u.startswith("R"):
            tags.append("णोपदेशः")
    seen, uniq = set(), []
    for t in tags:
        if t and t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq


DHATU_FILTER_SPEC = [
    ("gana", "गणः", [(g, str(i)) for i, g in enumerate(_GANA) if g]),
    ("antargana", "अन्तर्गणः", [
        "आकुस्मीयः", "आगर्वीयः", "आधृषीयः", "काण्यादिः", "किरादिः", "कुटादिः", "घटादिः",
        "णिजादिः", "जक्षित्यादिः", "ज्ञपादिः", "ज्वलादिः", "तनोत्यादिः", "तुजादिः", "तृम्फादिः",
        "द्युतादिः", "पुषादिः", "फणादिः", "प्वादिः", "भिदादिः", "भृञादिः", "मुचादिः", "यजादिः",
        "रधादिः", "रुदादिः", "ल्वादिः", "वृतादिः", "शमादिः", "सिवादिः", "स्वादिः",
    ]),
    ("pada", "पदम्", [("परस्मैपदम्", "P"), ("आत्मनेपदम्", "A"), ("उभयपदम्", "U")]),
    ("idaagam", "इडागमः", [("सेट्", "S"), ("अनिट्", "A"), ("वेट्", "V")]),
    ("karma", "कर्म", [("सकर्मकः", "S"), ("अकर्मकः", "A"), ("द्विकर्मकः", "D")]),
    ("achcount", "अचां सङ्ख्या", ["एकाच्", "अनेकाच्"]),
    ("upadesh", "उपदेशः", ["षोपदेशः", "णोपदेशः"]),
    ("swarabheda", "स्वरभेदः", ["उदात्तोपदेशः", "अनुदात्तोपदेशः"]),
    ("anubandha", "अनुबन्धः (इत्संज्ञा)", [
        "अदित्", "आदित्", "इदित्", "ईदित्", "उदित्", "ऊदित्", "उगित्", "ऋदित्", "ऌदित्",
        "एदित्", "ओदित्", "कित्", "ङित्", "ञित्", "टित्", "णित्", "मित्", "पित्", "षित्",
        "ट्वित्", "ड्वित्", "ञीत्", "इरित्",
    ]),
    ("adivarna", "आदिवर्णः", [
        "अजादिः", "इजादिः", "झलादिः", "हलादिः",
        "अकारादिः", "आकारादिः", "इकारादिः", "ईकारादिः", "उकारादिः", "ऊकारादिः",
        "ऋकारादिः", "ॠकारादिः", "एकारादिः", "ऐकारादिः", "ओकारादिः", "औकारादिः",
        "ककारादिः", "खकारादिः", "गकारादिः", "घकारादिः", "ङकारादिः",
        "चकारादिः", "छकारादिः", "जकारादिः", "झकारादिः", "ञकारादिः",
        "टकारादिः", "ठकारादिः", "डकारादिः", "ढकारादिः", "णकारादिः",
        "तकारादिः", "थकारादिः", "दकारादिः", "धकारादिः", "नकारादिः",
        "पकारादिः", "फकारादिः", "बकारादिः", "भकारादिः", "मकारादिः",
        "यकारादिः", "रेफादिः", "लकारादिः", "वकारादिः",
        "शकारादिः", "षकारादिः", "सकारादिः", "हकारादिः",
    ]),
    ("antyavarna", "अन्त्यवर्णः", [
        "अजन्तः", "इजन्तः", "एजन्तः", "झलन्तः", "रलन्तः", "अनुनासिकान्तः", "हलन्तः",
        "अकारान्तः", "आकारान्तः", "इकारान्तः", "ईकारान्तः", "उकारान्तः", "ऊकारान्तः",
        "ऋकारान्तः", "ॠकारान्तः", "एकारान्तः", "ऐकारान्तः", "ओकारान्तः", "औकारान्तः",
        "ककारान्तः", "खकारान्तः", "गकारान्तः", "घकारान्तः", "ङकारान्तः",
        "चकारान्तः", "छकारान्तः", "जकारान्तः", "झकारान्तः", "ञकारान्तः",
        "टकारान्तः", "ठकारान्तः", "डकारान्तः", "ढकारान्तः", "णकारान्तः",
        "तकारान्तः", "थकारान्तः", "दकारान्तः", "धकारान्तः", "नकारान्तः",
        "पकारान्तः", "फकारान्तः", "बकारान्तः", "भकारान्तः", "मकारान्तः",
        "यकारान्तः", "रेफान्तः", "लकारान्तः", "वकारान्तः",
        "शकारान्तः", "षकारान्तः", "सकारान्तः", "हकारान्तः",
    ]),
    ("upadhavarna", "उपधावर्णः", [
        "अकारोपधः", "आकारोपधः", "इकारोपधः", "ईकारोपधः", "उकारोपधः", "ऊकारोपधः",
        "ऋकारोपधः", "ॠकारोपधः", "एकारोपधः", "ऐकारोपधः", "ओकारोपधः", "औकारोपधः",
        "ककारोपधः", "खकारोपधः", "गकारोपधः", "घकारोपधः", "ङकारोपधः",
        "चकारोपधः", "छकारोपधः", "जकारोपधः", "झकारोपधः", "ञकारोपधः",
        "टकारोपधः", "ठकारोपधः", "डकारोपधः", "ढकारोपधः", "णकारोपधः",
        "तकारोपधः", "थकारोपधः", "दकारोपधः", "धकारोपधः", "नकारोपधः",
        "पकारोपधः", "फकारोपधः", "बकारोपधः", "भकारोपधः", "मकारोपधः",
        "यकारोपधः", "रेफोपधः", "लकारोपधः", "वकारोपधः",
        "शकारोपधः", "षकारोपधः", "सकारोपधः", "हकारोपधः",
    ]),
    ("swarthik", "स्वार्थिकप्रत्ययः", [
        ("सन्", "सन्"), ("नित्यं णिच्", "नित्यणिच्"), ("णिज्विकल्पः", "णिज्विकल्पः"),
        ("आय", "आय"), ("ईयङ्", "ईयङ्"), ("णिङ्", "णिङ्"),
    ]),
    ("grantha", "ग्रन्थः", [
        ("सिद्धान्तकौमुदी", "sk"), ("लघुकौमुदी", "lsk"), ("पाठभेदाः", "pathabhed"),
        ("कौमुदीबहिस्थाः", "nonsk"), ("गणसूत्राणि", "ganasutra"),
        ("प्रसिद्धधातवः", "common"), ("छान्दसधातवः", "छान्दसः"), ("सौत्रधातवः", "सौत्रः"),
    ]),
]

SHABDA_FILTER_SPEC = [
    ("antyavarna", "अन्त्यवर्णः", [
        "अजन्तः", "हलन्तः",
        "अकारान्तः", "आकारान्तः", "इकारान्तः", "ईकारान्तः", "उकारान्तः", "ऊकारान्तः",
        "ऋकारान्तः", "ॠकारान्तः", "एकारान्तः", "ऐकारान्तः", "ओकारान्तः", "औकारान्तः",
        "ककारान्तः", "खकारान्तः", "गकारान्तः", "घकारान्तः", "ङकारान्तः",
        "चकारान्तः", "छकारान्तः", "जकारान्तः", "झकारान्तः", "ञकारान्तः",
        "टकारान्तः", "ठकारान्तः", "डकारान्तः", "ढकारान्तः", "णकारान्तः",
        "तकारान्तः", "थकारान्तः", "दकारान्तः", "धकारान्तः", "नकारान्तः",
        "पकारान्तः", "फकारान्तः", "बकारान्तः", "भकारान्तः", "मकारान्तः",
        "यकारान्तः", "रेफान्तः", "लकारान्तः", "वकारान्तः",
        "शकारान्तः", "षकारान्तः", "सकारान्तः", "हकारान्तः",
    ]),
    ("antyavarna_speciality", "अन्त्यवर्णविशेषः", [
        ("आबन्तः", "आबन्तः"), ("ङ्यन्तः", "ङ्यन्तः"), ("तृजन्तः", "तृजन्तः"),
        ("अत्वन्तः", "अत्वन्तः"), ("क्विन्नन्तः", "क्विन्नन्तः"), ("असन्तः", "असन्तः"),
        ("अन्नन्तः", "अन्नन्तः"), ("इन्नन्तः", "इन्नन्तः"),
        ("संयोगपूर्वः वन्नन्तः", "संयोगपूर्व_वन्नन्तः"),
        ("संयोगपूर्वः मन्नन्तः", "संयोगपूर्व_मन्नन्तः"),
    ]),
    ("linga", "लिङ्गम्", [
        ("पुंलिङ्गः", "P"), ("स्त्रीलिङ्गः", "S"), ("नपुंसकलिङ्गः", "N"), ("अलिङ्गः", "A"),
    ]),
    ("text", "ग्रन्थः", [("सिद्धान्तकौमुदी", "sk"), ("लघुकौमुदी", "lsk")]),
    ("speciality", "शब्दविशेषः", [
        "नित्यैकवचनान्तः", "नित्यद्विवचनान्तः", "नित्यबहुवचनान्तः", "सम्बोधनाभावः",
        "भाषितपुंस्कः", "घिसंज्ञकः", "नदीसंज्ञकः",
        ("विशिष्टस्थलेषु नदीसंज्ञकः", "विशिष्टस्थलेषु_विकल्पेन_नदीसंज्ञकः"),
    ]),
]


def normalize_spec(spec):
    """Return [{id,label,options:[{label,value}]}] for JSON/JS."""
    out = []
    for fid, label, opts in spec:
        options = []
        for o in opts:
            if isinstance(o, tuple):
                options.append({"label": o[0], "value": o[1]})
            else:
                options.append({"label": o, "value": o})
        out.append({"id": fid, "label": label, "options": options})
    return out
