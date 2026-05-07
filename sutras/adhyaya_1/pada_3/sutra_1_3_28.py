"""
1.3.28  आङो यमहनः  —  PARIBHASHA (narrow: corrected-v2 **P010** *āyacchate*)

*Śāstra (laghu):* when **āṅ** precedes *yam* / *han*, *ātmanepada* *prayoga* is
triggered (pedagogical registry here; *tin* choice remains recipe-driven via **3.4.78**).

Engine: ``corrected_v2_P010_1_3_28_arm`` + tape ``[A~N, yam-dhātu]`` (witness *upadeśa*).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_META_ARM = "corrected_v2_P010_1_3_28_arm"


def _witness(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    up0 = (t0.meta.get("upadesha_slp1") or "").strip()
    if up0 != "A~N":
        return False
    if "dhatu" not in t1.tags:
        return False
    return "".join(v.slp1 for v in t1.varnas) == "yam"


def cond(state: State) -> bool:
    if not state.meta.get(_META_ARM):
        return False
    return _witness(state)


def act(state: State) -> State:
    if not cond(state):
        return state
    state.paribhasha_gates["1.3.28_Anga_yamhan_atmanepada"] = True
    state.samjna_registry["1.3.28_P010_Anga_yam"] = True
    state.meta.pop(_META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.28",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="ANgo yamhanos tu karmaRi",
    text_dev="आङो यमहनः",
    padaccheda_dev="आङः / यमहनः",
    why_dev="आङ्-पूर्वयोः यम्-हन्-धात्वोः संबन्धे आत्मनेपद-प्रकरणार्थः (प०१०)।",
    anuvritti_from=("1.3.27",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
