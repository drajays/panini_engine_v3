"""
4.1.98  गोत्रे कुञ्जादिभ्यश्च्फञ्  —  VIDHI (narrow: corrected-v2 **P004-A**)

Sources consulted:
- ashtadhyayi.com data.txt row i=41098
- Kāśikā: "चकारो विशेषणार्थः … ञकारो वृद्ध्यर्थः — कौञ्जायन्यः, कौञ्जायन्यौ, कौञ्जायनाः"
- Cross-validation: regression test tests/unit/test_corrected_prakriyas_v2_bundle.py
  (P004-A कौञ्जायन्यः)

Glass-box: after **4.1.92** *apatya* *adhikāra*, append the *taddhita* upadeśa
**cPaY** (च्फञ्) to the frame ``kuYja`` + internal **6-1** *Nas* (*ṣaṣṭhī* proviso).
The it-prakaraṇa then names च् *it* (1.3.7) and ञ् *it* (1.3.3); the residue फ
is 7.1.2's sthānin (→ आयन).

Recipe arms ``corrected_v2_P004_A_4_1_98_arm`` (CONSTITUTION Art. 7).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM = "corrected_v2_P004_A_4_1_98_arm"
_STEM_UPA = "kuYja"
_TAD_UPA = "cPaY"


def _has_caPaY(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == _TAD_UPA for t in state.terms)


def _stem_idx(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "prātipadika" not in t.tags:   # a prātipadika saṃjñā, not aṅga
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != _STEM_UPA:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not adhikara_in_effect("4.1.98", state, "4.1.92"):
        return False
    if _stem_idx(state) is None:
        return False
    if _has_caPaY(state):
        return False
    return True


def act(state: State) -> State:
    if not adhikara_in_effect("4.1.98", state, "4.1.92"):
        return state
    if _stem_idx(state) is None:
        return state
    if _has_caPaY(state):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(_TAD_UPA)),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": _TAD_UPA},
    )
    state.terms.append(pr)
    return state


SUTRA = SutraRecord(
    sutra_id="4.1.98",
    sutra_type=SutraType.VIDHI,
    text_slp1='gotre kuYjAdiByaScPaY',
    text_dev='गोत्रे कुञ्जादिभ्यश्च्फञ्',
    samagra_slp1="tasya gotre apatyam iti kuYjAdiByaH cPaY",
    samagra_dev="'तस्य गोत्रे अपत्यम्' (इति) कुञ्जादिभ्यः च्फञ्",
    padaccheda_dev="गोत्रे / कुञ्जादिभ्यः / च्फञ्",
    why_dev="कुञ्जादिगणे गोत्रापत्ये च्फञ् — प००४-अ।",
    anuvritti_from=("4.1.92",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
