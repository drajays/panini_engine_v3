"""
8.4.41  ष्टुना ष्टुः  —  VIDHI  (Tripāḍī)

संहितायाम् a स् or a तवर्ग letter that directly follows or precedes a ष् or a टवर्ग
letter becomes the matching ष् / टवर्ग letter (स→ष, त→ट, थ→ठ, द→ड, ध→ढ, न→ण):

    रामस् + षष्ठः → रामष्षष्ठः        रामस् + टीकते → रामष्टीकते (across words)
    पिष् + त → पिष्ट                  ईड् + ते → ईड्टे → ईट्टे         राजन् + डयसे → राजण्डयसे

Exceptions built in (they are *pratiṣedha* of this very rule, so they are read here):
**8.4.43 तोः षि** — a तवर्ग before ष् is not changed (सन् षष्ठः stays);
**8.4.42 न पदान्ताट्टोरनाम्** — a तवर्ग after a *pada-final* टवर्ग is not changed
(*pada* = a Term tagged ``pada``; the *anām* vārttika's ``ṣaḍ+navati`` is not modelled).
3.1.45's क्स recipe (अशिक्षत्): the ष् from सिच्'s स् does not retroflex the तिङ् त्/द्.

Scans the flattened varṇa stream across Terms (saṃhitā); Tripāḍī-only — it is asiddha
for everything before 8.2.1 and never runs earlier.  The former P031 (``n+ś→ṇ``, not
ṣṭutva at all) and P001-B (pre-Tripāḍī ``ṣṭ``) hacks are removed: *dhṛṣṭaḥ* takes
4.1.2 first, then the Tripāḍī runs this rule (see ``krdanta.derive_DfzwaH``).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84041 · ष्टुना ष्टुः
              padaccheda: ष्टुना · ष्टुः
              anuvṛtti:   82108: संहितायाम् | 84040: स्तोः
  Source #2 — Kāśikā 8.4.41 udāharaṇa:
                वृक्षष्षण्डे
                प्लक्षष्षण्डे
                वृक्षष्टीकते
  Cross-check — surface pinned by: tests/unit/test_BitzIzwa_ashir_ling.py, tests/unit/test_adhyagIzwa.py, tests/unit/test_dhRSTaH_kta_YiDfzf.py, tests/unit/test_8_4_41.py
  Reference record: sutra_ref_out/8_4_41.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_STU = {"s": "z", "t": "w", "T": "W", "d": "q", "D": "Q", "n": "R"}   # s/tu-varga → ṣ/ṭu-varga
_ZTU = frozenset("zwWqQR")                                             # ṣ + ṭu-varga
_TU = frozenset("tTdDn")


def _find_zt(state: State):
    """First (Term, index) that ṣṭutva applies to, or None."""
    if not state.tripadi_zone or state.meta.get("_3_1_45_ksa_recipe"):
        return None
    flat = [(t, i) for t in state.terms for i in range(len(t.varnas))]
    for k, (t, i) in enumerate(flat):
        c = t.varnas[i].slp1
        if c not in _STU:
            continue
        prev = flat[k - 1][0].varnas[flat[k - 1][1]].slp1 if k else ""
        nxt = flat[k + 1][0].varnas[flat[k + 1][1]].slp1 if k + 1 < len(flat) else ""
        if nxt == "z" and c != "s":                      # 8.4.43 तोः षि
            continue
        if nxt in _ZTU:
            return t, i
        if prev in _ZTU:
            pt, pi = flat[k - 1]
            padanta = "pada" in pt.tags and pi == len(pt.varnas) - 1
            if padanta and prev != "z" and c in _TU:     # 8.4.42 न पदान्ताट्टोरनाम्
                continue
            return t, i
    return None


def cond(state: State) -> bool:
    return _find_zt(state) is not None


def act(state: State) -> State:
    changes = []
    while (hit := _find_zt(state)) is not None:
        t, i = hit
        old = t.varnas[i].slp1
        t.varnas[i] = mk(_STU[old])
        changes.append(f"{old}→{_STU[old]}")
    if changes:
        state.meta["__why_now_dev__"] = (
            f"ष्/टवर्गयोगे स्/तवर्गः ष्टुः ({', '.join(changes)}); "
            "यथा रामस्+टीकते → रामष्टीकते, पिष्+त → पिष्ट; षि परे तोः न (८.४.४३), पदान्तटवर्गात् परस्य न (८.४.४२)। (८.४.४१)"
        )
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.41",
    sutra_type=SutraType.VIDHI,
    text_slp1="zwunA zwuH",
    text_dev="ष्टुना ष्टुः",
    padaccheda_dev="ष्टुना / ष्टुः",
    why_dev="ष्/टवर्गयोगे संहितायां स्/तवर्गस्य ष्/टवर्गादेशः; तोः षि (८.४.४३) न पदान्ताट्टोः (८.४.४२) इति निषेधौ।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
