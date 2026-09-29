"""
8.2.36  व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः  —  VIDHI (narrow demos: j→z, S→z)

Glass-box scope for `mArzwi`:
  When the stem contains "...rj" (from mFj vṛddhi), replace that final 'j' with 'z' (ष्).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82036 · व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः
              padaccheda: व्रश्च-भ्रस्ज-सृज-मृज-यज-राज-भ्राज-छ-शाम् षः
              anuvṛtti:   81016: पदस्य | 82026: झलि | 82029: अन्ते च | 82032: धातोः
  Source #2 — Kāśikā 8.2.36 udāharaṇa:
                व्रश्च — व्रष्टा
                व्रष्टुम्
                व्रष्टव्यम्
  Cross-check — surface pinned by: tests/unit/test_pfzwvA_pracch_ktvA.py
  Reference record: sutra_ref_out/8_2_36.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_8.pada_2._tape import (
    AC, BAS_TO_BHAS, JHAS, dhatu_span, flat, followed_by_jhal_or_end, slp, substitute,
)


_J_ROOTS = frozenset({"sfj", "mfj", "mArj", "yaj", "rAj", "BrAj"})


def _site(state: State):
    if not state.tripadi_zone:
        return None
    c = flat(state)
    for k in range(len(c)):
        ch = slp(c[k])
        if ch not in ("S", "C", "j") or not followed_by_jhal_or_end(c, k):
            continue
        span = dhatu_span(c, k)
        if not span or span[1] != k:
            continue
        root = "".join(slp(x) for x in c[span[0]:span[1] + 1])
        if ch in ("S", "C") or root in _J_ROOTS:
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, "z")
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.36",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'vraScaBrasjasfjamfjayajarAjaBrAjacCaSAM zaH',
    text_dev       = 'व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः',
    padaccheda_dev = "व्रश्च-भ्रस्ज-सृज-मृज-यज-राज-भ्राज-च्छ-शाम् / षः",
    why_dev        = "व्रश्चभ्रस्ज…च्छशां षः: a dhātu-final श्/छ् (and सृज्, मृज्, यज्, राज्, भ्राज्) → ष् before a jhal or at the pada end (apavāda of 8.2.30) — दंश्+स्य, सृज्+त → सृष्ट.",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

