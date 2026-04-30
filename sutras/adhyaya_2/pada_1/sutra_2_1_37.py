"""
2.1.37  पञ्चमी भयेन  —  SAMJNA (narrow ``prakriya_39``)

**Pāṭha (cross-check: ``sutrANi.tsv`` / vyākhyā):** *pañcamī bhayena* — ``tat-puruṣa`` compounding
with a prior member bearing the ablative (*pañcamī*) before ``bhaya``.

Narrow v3 (**वृकभयम्** ``…/separated_prakriyas/prakriya_39_*.json`` ``panini_engine_pipeline``):
  • Requires **2.1.3** *samāsa* adhikāra on ``adhikara_stack``.
  • ``prakriya_39_2_1_37_arm`` + ``meta['prakriya_39_paYcamI_compound_vidhi_note']`` +
    witness Terms tagged ``prakriya_39_vfkaBhaya_demo`` →
    ``samjna_registry['2.1.37_paYcamI_bhayena_prakriya_39']``.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_39_2_1_37_arm"):
        return False
    if not _samasa_adhikara_open(state):
        return False
    if not state.meta.get("prakriya_39_paYcamI_compound_vidhi_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_39_vfkaBhaya_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("2.1.37_paYcamI_bhayena_prakriya_39"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["2.1.37_paYcamI_bhayena_prakriya_39"] = True
    state.meta.pop("prakriya_39_2_1_37_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.1.37",
    sutra_type=SutraType.SAMJNA,
    text_slp1="paYcamI bhayena",
    text_dev="पञ्चमी भयेन",
    padaccheda_dev="पञ्चमी / भयेन",
    why_dev="पञ्चम्यन्तैः भयेन सह तत्पुरुषः (*prakriya_39*, **वृकभयम्**)।",
    anuvritti_from=("2.1.36",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
