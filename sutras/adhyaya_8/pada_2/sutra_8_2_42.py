"""
8.2.42  रदाभ्यां निष्ठातो नः पूर्वस्य च दः  —  VIDHI (narrow demos)

The audited ``corrected_prakriyas_v2`` bundle cites **8.2.42** for *niṣṭhā*
substitution before *sup*:

- **P001-A**: ``Bid`` + ``ta``/``t`` → *bhinna* (``corrected_v2_P001_A_8_2_42_arm``).
- **P001-C**: ``svid`` + ``ta``/``t`` → *svinna* after **6.1.64** (arm
  ``corrected_v2_P001_C_8_2_42_arm``).

General *rad*-classes / full *niṣṭhā* scope are **not** attempted (Art. 7).

CONSTITUTION Art. 2: ``cond`` reads tags / tape shape / recipe meta only.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM_A = "corrected_v2_P001_A_8_2_42_arm"
META_ARM_C = "corrected_v2_P001_C_8_2_42_arm"


def _match_rad_nistha_two_terms(state: State, stem_slp1: str, meta_arm: str) -> bool:
    if not state.meta.get(meta_arm):
        return False
    if len(state.terms) != 2:
        return False
    a, b = state.terms[0], state.terms[1]
    if "dhatu" not in a.tags:
        return False
    if "".join(v.slp1 for v in a.varnas) != stem_slp1:
        return False
    aff = "".join(v.slp1 for v in b.varnas)
    # Kit *kta* *it*-*lopa* yields ``t`` on some tapes; v3 often keeps ``ta`` on the
    # *kṛt* ``Term`` after **7.3.84** / **3.4.114** auditing (*ciY* row matches ``ta``).
    if aff not in {"t", "ta"}:
        return False
    if "krt" not in b.tags:
        return False
    return True


def cond(state: State) -> bool:
    return _match_rad_nistha_two_terms(state, "Bid", META_ARM_A) or _match_rad_nistha_two_terms(
        state, "svid", META_ARM_C
    )


def act(state: State) -> State:
    if _match_rad_nistha_two_terms(state, "Bid", META_ARM_A):
        merged = Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("bhinna")),
            tags={"anga"},
            meta={
                "upadesha_slp1": "bhinna",
                "corrected_v2_P001_A_nistha_stem": True,
            },
        )
        state.terms = [merged]
        state.meta.pop(META_ARM_A, None)
        return state
    if _match_rad_nistha_two_terms(state, "svid", META_ARM_C):
        merged = Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("svinna")),
            tags={"anga"},
            meta={
                "upadesha_slp1": "svinna",
                "corrected_v2_P001_C_nistha_stem": True,
            },
        )
        state.terms = [merged]
        state.meta.pop(META_ARM_C, None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.42",
    sutra_type=SutraType.VIDHI,
    text_slp1="radAByAm niRTAto naH pUrvasya ca daH",
    text_dev="रदाभ्यां निष्ठातो नः पूर्वस्य च दः",
    padaccheda_dev="रदाभ्याम् / निष्ठातः / नः / पूर्वस्य / च / दः",
    why_dev="भिद् / स्विद् + निष्ठा-तकारः → भिन्न / स्विन्न (P001-A/C आर्म्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
