"""
5.1.28  अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्  —  SAMJNA (narrow ``prakriya_43``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=50128):** *adhyardhapūrvadvigor lug saṃjñāyām* — *luk* of ``ṭak``
when the prior formation is a *dvigu* (under **संज्ञा**, not a proper-name reading).

Narrow v3 (**पञ्चशष्कुलम्** ``panini_engine_pipeline``): after **5.1.37** has registered *ṭak* intent,
``prakriya_43_5_1_28_arm`` + ``meta['prakriya_43_dvigu_Tak_luk_note']`` + witness ``prakriya_43_paYcaSazkulam_demo``
→ ``samjna_registry['5.1.28_advigu_Tak_luk_prakriya_43']``.

Requires ``samjna_registry['5.1.37_tena_krItam_prakriya_43']`` from **5.1.37** on the same spine.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _taddhita_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    armed_43 = bool(state.meta.get("prakriya_43_5_1_28_arm"))
    armed_11 = bool(state.meta.get("prakriya_P011_5_1_28_arm"))
    if not (armed_43 or armed_11):
        return False
    if not _taddhita_adhikara_open(state):
        return False
    note_ok = bool(state.meta.get("prakriya_43_dvigu_Tak_luk_note")) or bool(
        state.meta.get("prakriya_P011_dvigu_Tak_luk_note")
    )
    if not note_ok:
        return False
    if not state.samjna_registry.get("5.1.37_tena_krItam_prakriya_43"):
        return False
    if not state.terms:
        return False
    if not any(
        ("prakriya_43_paYcaSazkulam_demo" in t.tags) or ("prakriya_P011_paYcagoRiH_demo" in t.tags)
        for t in state.terms
    ):
        return False
    if state.samjna_registry.get("5.1.28_advigu_Tak_luk_prakriya_43"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["5.1.28_advigu_Tak_luk_prakriya_43"] = True
    state.meta.pop("prakriya_43_5_1_28_arm", None)
    state.meta.pop("prakriya_P011_5_1_28_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="5.1.28",
    sutra_type=SutraType.SAMJNA,
    text_slp1="adhyardhapUrvadvigorlugasaFjJAyAm",
    text_dev="अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्",
    padaccheda_dev="अध्यर्ध-पूर्व-द्विगोः / लुक् / संज्ञायाम्",
    why_dev="द्विगोः परस्य ठकि लुक् (*saṃjñā*, *prakriya_43*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
