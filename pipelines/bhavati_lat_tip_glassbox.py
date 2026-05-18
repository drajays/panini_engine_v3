"""
pipelines/bhavati_lat_tip_glassbox.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
भू धातोः लँट् प्रथमपुरुषैकवचनस्य सम्पूर्णा ग्लासबॉक्स-प्राकृया

Automatic glass-box derivation of भवति from bhū + laṭ kartari 3sg.
Every step is driven by apply_rule() — zero patchwork.

Run directly:
    cd panini_engine_v3
    python3 pipelines/bhavati_lat_tip_glassbox.py
"""
# ── CONSTITUTION-compliant · Art. 6 firewall · no gold shortcuts ────────────
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.tinanta import derive


# ─────────────────────────────────────────────────────────────────────────────
# SUTRA COMMENTARY (for glass-box print)  — scholarly metadata only
# ─────────────────────────────────────────────────────────────────────────────
_SUTRA_COMMENTARY: dict[str, tuple[str, str]] = {
    "1.3.1": (
        "भूवादयो धातवः",
        "भू इत्यादयः धातु-संज्ञाम् लभन्ते।",
    ),
    "1.3.2": (
        "उपदेशेऽजनुनासिक इत्",
        "उपदेशे अनुनासिकः अच् 'इत्' भवति।",
    ),
    "1.3.3": (
        "हलन्त्यम्",
        "उपदेशे अन्तिमः हल् वर्णः 'इत्' संज्ञकः।",
    ),
    "1.3.8": (
        "लशक्वतद्धिते",
        "अतद्धिते प्रत्यये परे ल्, श्, कु-वर्णाः 'इत्'।",
    ),
    "1.3.9": (
        "तस्य लोपः",
        "इत्-संज्ञकानां वर्णानां लोपः।",
    ),
    "1.3.10": (
        "यथासंख्यमनुदेशः समानाम्",
        "समसंख्यक-गणयोः यथाक्रमम् अनुदेशः।",
    ),
    "1.3.78": (
        "शेषात् कर्तरि परस्मैपदम्",
        "आत्मनेपद-रहितेभ्यो धातुभ्यः कर्तरि परस्मैपदम्।",
    ),
    "1.4.13": (
        "यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्",
        "धातुः प्रत्ययस्य विधेः पूर्वं 'अङ्ग'-संज्ञां लभते।",
    ),
    "1.4.99": (
        "लः परस्मैपदम्",
        "ल-स्थाने परस्मैपद-तिङादेशाः।",
    ),
    "1.1.5": (
        "क्ङिति च",
        "क्-इत् ङ्-इत् प्रत्यये परे गुण-वृद्धी न।",
    ),
    "3.1.1": (
        "प्रत्ययः",
        "प्रत्यय-विधानम् — अधिकारः।",
    ),
    "3.1.2": (
        "परश्च",
        "प्रत्ययः निमित्तात् परः।",
    ),
    "3.1.3": (
        "आद्युदात्तश्च",
        "प्रत्ययस्य आद्युदात्तत्वम्।",
    ),
    "3.1.68": (
        "कर्तरि शप्",
        "सार्वधातुके कर्तरि धातोः 'शप्' विकरण-प्रत्ययः।",
    ),
    "3.1.91": (
        "धातोः",
        "धातोः — प्रत्यय-विधान-अधिकारः।",
    ),
    "3.2.123": (
        "वर्तमाने लट्",
        "वर्तमान-काले धातोः लट्-प्रत्ययः।",
    ),
    "3.4.77": (
        "लस्य",
        "लकार-प्रत्ययस्य (ल-स्थाने) तिङादेशाः — अधिकारः।",
    ),
    "3.4.78": (
        "तिप्तस्झिसिप्थस्थमिब्वस्मस्...",
        "लकार-स्थाने अष्टादश तिङ्-आदेशाः। प्रथमपुरुषैकवचने → तिप्।",
    ),
    "3.4.113": (
        "तिङ्शित्सार्वधातुकम्",
        "तिङ् तथा शित्-प्रत्ययाः सार्वधातुक-संज्ञकाः।",
    ),
    "7.3.84": (
        "सार्वधातुकार्धधातुकयोः",
        "सार्वधातुके/आर्धधातुके परे अङ्गस्य इक्-वर्णस्य गुणः। भू → भो।",
    ),
    "6.1.78": (
        "एचोऽयवायावः",
        "एच् (ए/ऐ/ओ/औ) परे अचि → अय्/आय्/अव्/आव्। भो+अ → भव्+अ।",
    ),
    "__MERGE__": (
        "पद-मेलनम् (संरचनात्मकम्)",
        "सर्वे Terms एकस्मिन् पद-Term-मध्ये विलीयन्ते।",
    ),
}

_STEP_NO = {
    "1.3.1":   "①",
    "1.3.2":   "②",
    "1.3.3":   "③",
    "1.3.9":   "④",
    "1.3.78":  "⑤",
    "3.1.91":  "⑥",
    "3.1.1":   "⑦",
    "3.1.2":   "⑧",
    "3.1.3":   "⑨",
    "3.2.123": "⑩",
    "3.4.77":  "⑪",
    "3.4.78":  "⑫",
    "1.4.99":  "⑬",
    "3.1.68":  "⑭",
    "3.4.113": "⑮",
    "3.1.8":   "⑯",
    "1.3.8":   "⑰",
    "1.1.5":   "⑱",
    "1.4.13":  "⑲",
    "7.3.84":  "⑳",
    "6.1.78":  "㉑",
    "__MERGE__": "㉒",
}


def print_prakriya(state) -> None:
    """Print a Devanāgarī-annotated glass-box prakriyā table."""
    print()
    print("━" * 78)
    print("  भू धातोः लँट् प्रथमपुरुषैकवचनस्य ग्लासबॉक्स-प्राकृया (स्वचालिता)")
    print("━" * 78)

    # Collect numbered applied steps (skip pure SKIPs with no form change)
    displayed = []
    step_num = 0
    seen_sutra_forms: set = set()

    for entry in state.trace:
        sid   = entry.get("sutra_id", "?")
        ev    = entry.get("event") or entry.get("status", "")
        fb    = entry.get("form_before", "")
        fa    = entry.get("form_after", "")
        why   = entry.get("why_dev", "")

        # Skip repeated no-ops (same sutra+form combo)
        key = (sid, ev, fb, fa)
        if key in seen_sutra_forms:
            continue
        seen_sutra_forms.add(key)

        if ev in ("SKIPPED", "COND-FALSE"):
            continue  # show only applied steps

        step_num += 1
        circle = _STEP_NO.get(sid, f"[{step_num}]")
        comm   = _SUTRA_COMMENTARY.get(sid, ("", ""))
        sutra_name = comm[0] or sid
        explanation = comm[1] or why[:70]

        displayed.append((circle, sid, sutra_name, explanation, fb, fa, ev))

    # Print
    for (circle, sid, sname, expl, fb, fa, ev) in displayed:
        arrow = "→"
        tag = ""
        if ev == "AUDIT":
            tag = " [अधिकार/परिभाषा]"
        elif ev == "APPLIED_VACUOUS":
            tag = " [शून्य-लोप]"
        elif ev == "MERGE":
            tag = " [संरचना]"

        print(f"\n  {circle} सूत्रम्: {sname} ({sid}){tag}")
        print(f"    व्याख्या: {expl}")
        if fb and fa and fb != fa:
            print(f"    रूपान्तरम्: {fb} {arrow} {fa}")
        elif fa:
            print(f"    रूपम्: {fa}")

    print()
    print("━" * 78)
    result_dev = state.flat_dev()
    result_slp = state.flat_slp1()
    print(f"  ∴ सिद्धम् — {result_dev}  (SLP1: {result_slp})")
    print("━" * 78)
    print()


def derive_bhavati_glassbox() -> object:
    """Full automatic prakriyā: BU + laT + kartari + prathama + eka → भवति."""
    return derive("BU", "laT", "kartari", 3, 1)


if __name__ == "__main__":
    print("\nRunning automatic glass-box derivation: bhū + laṭ → bhavati …\n")
    s = derive_bhavati_glassbox()
    print_prakriya(s)
