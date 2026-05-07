"""
3.1.92  तत्रोपपदं सप्तमीस्थम्  —  SAMJNA (narrow: corrected-v2 **P005-A/B**)

*Śāstra (laghu):* in *upapada* constructions the prior *pada* bearing a *saptamī*
*sup* gets the *upapada* designation.

Engine (glass-box rows):

* ``corrected_v2_P005_A_3_1_92_arm`` — ``[kuru, sup, car]`` → tag ``kuru``.
* ``corrected_v2_P005_B_3_1_92_arm`` — ``[upasara, sup, jan~]`` → tag ``upasara``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_META_ARM_A = "corrected_v2_P005_A_3_1_92_arm"
_META_ARM_B = "corrected_v2_P005_B_3_1_92_arm"


def _witness_a(state: State) -> bool:
    if not state.meta.get(_META_ARM_A):
        return False
    if len(state.terms) < 3:
        return False
    t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
    if (t0.meta.get("upadesha_slp1") or "").strip() != "kuru":
        return False
    if "sup" not in t1.tags:
        return False
    if "dhatu" not in t2.tags:
        return False
    if (t2.meta.get("upadesha_slp1") or "").strip() != "car":
        return False
    return True


def _witness_b(state: State) -> bool:
    if not state.meta.get(_META_ARM_B):
        return False
    if len(state.terms) < 3:
        return False
    t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
    if (t0.meta.get("upadesha_slp1") or "").strip() != "upasara":
        return False
    if "sup" not in t1.tags:
        return False
    if "dhatu" not in t2.tags:
        return False
    if (t2.meta.get("upadesha_slp1") or "").strip() != "jan~":
        return False
    return True


def cond(state: State) -> bool:
    if not state.terms:
        return False
    if "upapada" in state.terms[0].tags:
        return False
    return _witness_a(state) or _witness_b(state)


def act(state: State) -> State:
    if _witness_a(state):
        state.terms[0].tags.add("upapada")
        state.samjna_registry["3.1.92_P005_A_upapada"] = True
        state.meta.pop(_META_ARM_A, None)
        return state
    if _witness_b(state):
        state.terms[0].tags.add("upapada")
        state.samjna_registry["3.1.92_P005_B_upapada"] = True
        state.meta.pop(_META_ARM_B, None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.92",
    sutra_type=SutraType.SAMJNA,
    text_slp1="tatro papadaM saptamIsTam",
    text_dev="तत्रोपपदं सप्तमीस्थम्",
    padaccheda_dev="तत्र / उपपदम् / सप्तमीस्थम्",
    why_dev="उपपद-प्रकरणे सप्तम्यर्थक-पदस्य उपपद-संज्ञा (प००५-अ/ब)।",
    anuvritti_from=("3.1.88",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
