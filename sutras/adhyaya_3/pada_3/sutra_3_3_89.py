"""
3.3.89  ट्वितोऽथुच्  —  VIDHI (narrow **corrected-v2 P002-A** / **P002-B**)

**Pāṭha:** *ṭvitō'thuc* — after a *ṭvit* dhātu, the kṛt affix *athuc* (*bhāva*).

Implemented rows (recipe arms only; CONSTITUTION Art. 7):

• **P002-A:** ``wuvepf~`` → ``vep`` + *athuc* → *vepathuḥ*.
• **P002-B:** Human पाठ *ṭuoñśvi* (टुओँश्वि): machine upadeśa ``wzvi`` — initial ``w``
  is *ṭit* (**1.3.5**); surviving stem ``zvi`` + *athuc* → *śvayathuḥ* (**7.3.84**,
  **6.1.78** before *pada* merge in the pipeline).

General *ṭvit* scope is **not** implemented.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM_A = "corrected_v2_P002_A_3_3_89_arm"
META_ARM_B = "corrected_v2_P002_B_3_3_89_arm"
_UPADESHA_A = "wuvepf~"
_UPADESHA_B = "wzvi"


def cond(state: State) -> bool:
    if state.samjna_registry.get("3.3.89_athuc_attached"):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    up = (t0.meta.get("upadesha_slp1") or "").strip()
    stem = "".join(v.slp1 for v in t0.varnas)
    if up == _UPADESHA_A and stem == "vep":
        return True
    if up == _UPADESHA_B and stem == "zvi":
        return True
    return False


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("athuc")),
        tags={"krt", "upadesha"},
        meta={"upadesha_slp1": "athuc"},
    )
    state.terms.append(pr)
    state.samjna_registry["3.3.89_athuc_attached"] = True
    state.meta.pop(META_ARM_A, None)
    state.meta.pop(META_ARM_B, None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.89",
    sutra_type=SutraType.VIDHI,
    text_slp1="wvitoaTuc",
    text_dev="ट्वितोऽथुच्",
    padaccheda_dev="ट्वितः / अथुच्",
    why_dev="ट्वित्-धातोः अथुच्-प्रत्ययः (भावः — प००२-ए / प००२-ब आर्म्)।",
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
