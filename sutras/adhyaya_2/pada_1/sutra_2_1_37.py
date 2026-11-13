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
Pāṭha: ashtadhyayi.com data.txt row i=21037 (Art. 14).
Kāśikā: पञ्चम्यन्तं सुबन्तं भयशब्देन सुबन्तेन सह समस्यते विभाषा, तत्पुरुषश्च समासो भवति।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _old_site(state: State) -> bool:
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


def _old_cond(state: State) -> bool:
    return _old_site(state)


def _old_act(state: State) -> State:
    if not _old_site(state):
        return state
    state.samjna_registry["2.1.37_paYcamI_bhayena_prakriya_39"] = True
    return state


from engine.samasa_attach import pair, run, mark, name


def _site(state: State):
    return pair(state, "2.1.37", vib="paYcamI", uttara_names=frozenset({"Baya"}))


def cond(state: State) -> bool:
    return _site(state) is not None or _old_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _old_act(state)
    return mark(state, list(s), "tatpurusha", "2.1.37")


SUTRA = SutraRecord(
    sutra_id="2.1.37",
    sutra_type=SutraType.VIDHI,
    text_slp1='paYcamI Bayena',
    text_dev='पञ्चमी भयेन',
    samagra_slp1="AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH paYcamI Bayena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः पञ्चमी भयेन",
    padaccheda_dev="पञ्चमी / भयेन",
    why_dev="पञ्चम्यन्तैः भयेन सह तत्पुरुषः (*prakriya_39*, **वृकभयम्**)।",
    anuvritti_from=("2.1.36",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
