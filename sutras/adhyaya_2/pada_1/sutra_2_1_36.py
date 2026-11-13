"""
2.1.36  चतुर्थी तदर्थार्थबलिहितसुखरक्षितैः  —  SAMJNA (narrow ``prakriya_39``)

**Pāṭha (cross-check: ``sutrANi.tsv`` / vyākhyā):** *caturthī tadarthārthabalihitasukharakṣitaiḥ* —
``tat-puruṣa`` compounding with a prior member bearing the dative (*caturthī*) under the listed
conditions.

Narrow v3 (**यूपदारु** ``…/separated_prakriyas/prakriya_39_*.json`` ``panini_engine_pipeline``):
  • Requires **2.1.3** *samāsa* adhikāra on ``adhikara_stack``.
  • ``prakriya_39_2_1_36_arm`` + ``meta['prakriya_39_catvarTI_compound_vidhi_note']`` +
    at least one witness Term tagged ``prakriya_39_yUpadAru_demo`` →
    ``samjna_registry['2.1.36_catvarTI_tad_artha_prakriya_39']``.

No ``varṇa`` mutation (recipe gate only).
Pāṭha: ashtadhyayi.com data.txt row i=21036 (Art. 14).
Kāśikā: तदर्थ अर्थ बलि हित सुख रक्षित इत्येतैः सह चतुर्थ्यन्तं समस्यते, तत्पुरुषश्च समासो भवति।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _old_site(state: State) -> bool:
    if not _samasa_adhikara_open(state):
        return False
    if not state.meta.get("prakriya_39_catvarTI_compound_vidhi_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_39_yUpadAru_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("2.1.36_catvarTI_tad_artha_prakriya_39"):
        return False
    return True


def _old_cond(state: State) -> bool:
    return _old_site(state)


def _old_act(state: State) -> State:
    if not _old_site(state):
        return state
    state.samjna_registry["2.1.36_catvarTI_tad_artha_prakriya_39"] = True
    return state


from engine.samasa_attach import pair, run, mark, name
_TADARTHA = frozenset({"arTa", "bali", "hita", "suKa", "rakzita"})   # the sūtra's own list (tadartha is the pūrvapada's purpose)

def _site(state: State):
    return pair(state, "2.1.36", vib="caturTI", uttara_names=_TADARTHA)


def cond(state: State) -> bool:
    return _site(state) is not None or _old_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _old_act(state)
    return mark(state, list(s), "tatpurusha", "2.1.36")


SUTRA = SutraRecord(
    sutra_id="2.1.36",
    sutra_type=SutraType.VIDHI,
    text_slp1='caturTI tadarTArTabalihitasuKarakzitEH',
    text_dev='चतुर्थी तदर्थार्थबलिहितसुखरक्षितैः',
    samagra_slp1="AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH caturTI tadarTa-arTa-bali-hita-suKa-rakzitEH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः चतुर्थी तदर्थ-अर्थ-बलि-हित-सुख-रक्षितैः",
    padaccheda_dev="चतुर्थी / तदर्थ-अर्थ-बलि-हित-सुख-रक्षितैः",
    why_dev="चतुर्थ्यन्तैः तदर्थादिभिः तत्पुरुषः (*prakriya_39*, **यूपदारु**)।",
    anuvritti_from=("2.1.35",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
