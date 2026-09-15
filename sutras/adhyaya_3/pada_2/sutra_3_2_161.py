"""
3.2.161  भञ्जभासमिदो घुरच्  —  VIDHI (narrow: corrected-v2 **P007** *bhaṅguram*)

Glass-box: after ``BaYj`` (from ``BaYjo`` + *it*), append *kṛt* upadeśa **Gurc**
(घुरच् → **G** + **u** + **r** + **c**; **G**/**c** *it*) tagged ``ghiti`` for
**7.3.52** *cajoḥ ku …*.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 32161 · भञ्जभासमिदो घुरच्
              padaccheda: भञ्ज-भास-मिदः घुरच्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ् | 32123: वर्त्तमाने | 32134: तच्छीलतद्धर्मतत्साधुकारिषु
  Source #2 — Kāśikā 3.2.161 udāharaṇa:
                भङ्गुरं काष्ठम्
                घित्त्वात् कुत्वम्
                भासुरं ज्योतिः
  Cross-check — surface pinned by: tests/unit/test_bhaNguram_Ghurac.py
  Reference record: sutra_ref_out/3_2_161.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM = "corrected_v2_P007_3_2_161_arm"
_DHATU_UPA = "BaYjo"
_REG = "3.2.161_ghurac_attached"


def _stem_slp1(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def cond(state: State) -> bool:
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != _DHATU_UPA:
        return False
    if _stem_slp1(t0) != "BaYj":
        return False
    if state.samjna_registry.get(_REG):
        return False
    return True


def act(state: State) -> State:
    if len(state.terms) != 1:
        return state
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return state
    if (t0.meta.get("upadesha_slp1") or "").strip() != _DHATU_UPA:
        return state
    if _stem_slp1(t0) != "BaYj":
        return state
    if state.samjna_registry.get(_REG):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Gurc")),
        tags={"pratyaya", "krt", "upadesha", "ghiti"},
        meta={"upadesha_slp1": "Gurc"},
    )
    state.terms.append(pr)
    state.samjna_registry[_REG] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.161",
    sutra_type=SutraType.VIDHI,
    text_slp1="BaYja-BAsa-mido Gurac",
    text_dev="भञ्जभासमिदो घुरच्",
    padaccheda_dev="भञ्ज-भास-मिदः / घुरच्",
    why_dev="भञ्जादिभ्यो घुरच् — प००७ (*भङ्गुर*).",
    anuvritti_from=("3.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
