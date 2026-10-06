"""
8.2.42  रदाभ्यां निष्ठातो नः पूर्वस्य च दः  —  VIDHI (narrow demos)

The audited ``corrected_prakriyas_v2`` bundle cites **8.2.42** for *niṣṭhā*
substitution before *sup*:

- **P001-A**: ``Bid`` + ``ta``/``t`` → *bhinna* (``corrected_v2_P001_A_8_2_42_arm``).
- **P001-C**: ``svid`` + ``ta``/``t`` → *svinna* after **6.1.64** (arm
  ``corrected_v2_P001_C_8_2_42_arm``).

General *rad*-classes / full *niṣṭhā* scope are **not** attempted (Art. 7).

CONSTITUTION Art. 2: ``cond`` reads tags / tape shape / recipe meta only.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82042 · रदाभ्यां निष्ठातो नः पूर्वस्य च दः
              padaccheda: र-दाभ्याम् निष्ठा-तः नः पूर्वस्य च दः
  Source #2 — Kāśikā 8.2.42 udāharaṇa:
                विस्तीर्णम्
                विशीर्णम्
                निगीर्णम्
  Cross-check — surface pinned by: tests/unit/test_bhinnaH_kta_Bidi.py, tests/unit/test_corrected_prakriyas_v2_bundle.py, tests/unit/test_svinnaH_kta_YizvidA.py
  Reference record: sutra_ref_out/8_2_42.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM_A = "corrected_v2_P001_A_8_2_42_arm"
META_ARM_C = "corrected_v2_P001_C_8_2_42_arm"


_NISTHA = frozenset({"kta", "ktavatu", "ktavatu~"})     # 1.1.26 क्तक्तवतू निष्ठा


def _site(state: State):
    """रदाभ्यां निष्ठातो नः पूर्वस्य च दः: after a root-final र् or द्, the niṣṭhā's
    त् becomes न्, and a preceding द् becomes न् too — भिद्+त → भिन्न, स्विद्+त → स्विन्न,
    शॄ+त → शीर्ण (8.4.1). Read on the dhātu and niṣṭhā terms (before the pada merge)."""
    if not state.tripadi_zone:
        return None
    for a, b in zip(state.terms, state.terms[1:]):
        if "dhatu" not in a.tags or not a.varnas or not b.varnas:
            continue
        if (b.meta.get("upadesha_slp1") or "").strip() not in _NISTHA or b.varnas[0].slp1 != "t":
            continue
        if a.varnas[-1].slp1 in ("d", "r"):
            return a, b
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    a, b = _site(state)
    b.varnas[0] = mk("n")
    if a.varnas[-1].slp1 == "d":
        a.varnas[-1] = mk("n")
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.42",
    sutra_type=SutraType.VIDHI,
    text_slp1='radAByAM nizWAto naH pUrvasya ca daH',
    text_dev='रदाभ्यां निष्ठातो नः पूर्वस्य च दः',
    samagra_slp1="padasya pUrvatrAsidDam radAByAm nizWAtaH naH pUrvasya ca daH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="पदस्य पूर्वत्रासिद्धम् रदाभ्याम् निष्ठातः नः पूर्वस्य च दः",
    padaccheda_dev="रदाभ्याम् / निष्ठातः / नः / पूर्वस्य / च / दः",
    why_dev="भिद् / स्विद् + निष्ठा-तकारः → भिन्न / स्विन्न (P001-A/C आर्म्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
