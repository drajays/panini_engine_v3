"""
3.3.88  ड्वितः क्त्रिः  —  VIDHI (narrow **corrected-v2 P003-A/B/C**)

**Pāṭha:** *ḍvitaḥ ktriḥ* — *ktri* after a *ḍvit* dhātu.

v3: recipe-only arms for ``corrected_prakriyas_v2`` **P003-A** (*paktrimam*),
**P003-B** (*kṛtrimam*), **P003-C** (*uptrimam*). General *ḍvit* scope is **not**
implemented (CONSTITUTION Art. 7).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM_A = "corrected_v2_P003_A_3_3_88_arm"
META_ARM_B = "corrected_v2_P003_B_3_3_88_arm"
META_ARM_C = "corrected_v2_P003_C_3_3_88_arm"
REG_DONE = "3.3.88_corrected_v2_ktr_attached"


def _stem(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas)


def cond(state: State) -> bool:
    if state.samjna_registry.get(REG_DONE):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    st = _stem(t0)
    if st == "pac":
        return True
    if st == "kf":
        return True
    if st == "vap":
        return True
    return False


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ktri")),
        tags={"krt", "upadesha", "kit", "kngiti"},
        meta={"upadesha_slp1": "ktri", "kit": True},
    )
    state.terms.append(pr)
    state.samjna_registry[REG_DONE] = True
    state.meta.pop(META_ARM_A, None)
    state.meta.pop(META_ARM_B, None)
    state.meta.pop(META_ARM_C, None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.88",
    sutra_type=SutraType.VIDHI,
    text_slp1="qvitaH ktriH",
    text_dev="ड्वितः क्त्रिः",
    padaccheda_dev="ड्वितः / क्त्रिः",
    why_dev="ड्वित्-धातोः क्त्रि-प्रत्ययः (प००३ आर्म्)।",
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
