"""
5.1.37  तेन क्रीतम्  —  SAMJNA (narrow ``prakriya_43``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=50137):** *tena krītam* — ``Ra`` (*ṭak*) after a stem in the sense
‘bought with / by means of that’.

Narrow v3 (**पञ्चशष्कुलम्** ``…/separated_prakriyas/prakriya_43_*.json`` ``panini_engine_pipeline``):
  • **4.1.76** *taddhita* *adhikāra* on ``adhikara_stack``.
  • ``prakriya_43_5_1_37_arm`` + ``meta['prakriya_43_tena_krItam_note']`` +
    witness ``Term`` tagged ``prakriya_43_paYcaSazkulam_demo`` →
    ``samjna_registry['5.1.37_tena_krItam_prakriya_43']``.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _taddhita_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    armed_43 = bool(state.meta.get("prakriya_43_5_1_37_arm"))
    armed_11 = bool(state.meta.get("prakriya_P011_5_1_37_arm"))
    if not (armed_43 or armed_11):
        return False
    if not _taddhita_adhikara_open(state):
        return False
    note_ok = bool(state.meta.get("prakriya_43_tena_krItam_note")) or bool(
        state.meta.get("prakriya_P011_tena_krItam_note")
    )
    if not note_ok:
        return False
    if not state.terms:
        return False
    if not any(
        ("prakriya_43_paYcaSazkulam_demo" in t.tags) or ("prakriya_P011_paYcagoRiH_demo" in t.tags)
        for t in state.terms
    ):
        return False
    if state.samjna_registry.get("5.1.37_tena_krItam_prakriya_43"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["5.1.37_tena_krItam_prakriya_43"] = True
    state.meta.pop("prakriya_43_5_1_37_arm", None)
    state.meta.pop("prakriya_P011_5_1_37_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="5.1.37",
    sutra_type=SutraType.SAMJNA,
    text_slp1="tena krItam",
    text_dev="तेन क्रीतम्",
    padaccheda_dev="तेन क्रीतम्",
    why_dev="तेन क्रीतम् इत्यर्थे ठक्-प्रत्ययः (*prakriya_43*, **पञ्चशष्कुलम्**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
