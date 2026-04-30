"""
2.1.23  द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः  —  SAMJNA (narrow ``prakriya_38``)

**Pāṭha (cross-check: ``sutrANi.tsv`` / vyākhyā):** *dvitīyā śritātīta-patita-gatātyasta-prāptāpannaiḥ* —
``tat-puruṣa`` compounding with prior member bearing the second-case affix (*dvitīyā*) together with
roots ``śri`` etc. (traditional list).

Narrow v3 (**कष्टश्रितः** ``panini_engine_pipeline`` — ``…/separated_prakriyas/prakriya_38_*.json``):
  • Requires **2.1.3** *samāsa* adhikāra on ``adhikara_stack``.
  • ``prakriya_38_2_1_23_arm`` + ``meta['prakriya_38_dvitIyA_compound_vidhi_note']`` +
    tagged witness Term ``prakriya_38_kaSTazrita_demo`` →
    ``samjna_registry['2.1.23_dvitIyA_zrita_tatpurusa_prakriya_38']``.

No ``varṇa`` mutation (recipe gate only).

**Note:** Edition numbering differs in some OCR dumps (**२.१.२४** vs **२.१.२३**); this file follows the
vyākhyā numbering where this *pāṭha* is **२.१.२३**.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_38_2_1_23_arm"):
        return False
    if not _samasa_adhikara_open(state):
        return False
    if not state.meta.get("prakriya_38_dvitIyA_compound_vidhi_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_38_kaSTazrita_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("2.1.23_dvitIyA_zrita_tatpurusa_prakriya_38"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["2.1.23_dvitIyA_zrita_tatpurusa_prakriya_38"] = True
    state.meta.pop("prakriya_38_2_1_23_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.1.23",
    sutra_type=SutraType.SAMJNA,
    text_slp1="dvitIyA zritAtItapatitagatAtyastaprAptApannaiH",
    text_dev="द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः",
    padaccheda_dev="द्वितीया / श्रित-आतीत-पतित-गत-अत्यस्त-प्राप्त-आपन्नैः",
    why_dev="द्वितीयान्तैः श्रितादिभिः तत्पुरुषः (*prakriya_38*, **कष्टश्रितः**)।",
    anuvritti_from=("2.1.22",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
