"""
2.1.51  तद्धितार्थोत्तरपदसमाहारे च  —  SAMJNA (narrow ``prakriya_42``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=21051):** *taddhitārthottarapada-samāhāre ca* — *subanta* compounding
when a *taddhita* sense is in play (``…/separated_prakriyas/prakriya_42_*.json`` *pañcendra* arc).

Narrow v3:
  • **2.1.3** *samāsa* *adhikāra* on ``adhikara_stack``.
  • ``prakriya_42_2_1_51_arm`` + ``meta['prakriya_42_taddhitartha_samAhAra_note']`` +
    witness ``Term`` tagged ``prakriya_42_paYcendra_demo`` →
    ``samjna_registry['2.1.51_taddhitartha_samAhAra_prakriya_42']``.

**Edition note:** Some OCR JSONs label this *pāṭha* as **2.1.50**; in *ashtadhyayi-com* **2.1.50** is
*दिक्संख्ये संज्ञायाम्* — different rule.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    armed_42 = bool(state.meta.get("prakriya_42_2_1_51_arm"))
    armed_11 = bool(state.meta.get("prakriya_P011_2_1_51_arm"))
    if not (armed_42 or armed_11):
        return False
    if not _samasa_adhikara_open(state):
        return False
    note_ok = bool(state.meta.get("prakriya_42_taddhitartha_samAhAra_note")) or bool(
        state.meta.get("prakriya_P011_taddhitartha_samAhAra_note")
    )
    if not note_ok:
        return False
    if not state.terms:
        return False
    if not any(
        ("prakriya_42_paYcendra_demo" in t.tags) or ("prakriya_P011_paYcagoRiH_demo" in t.tags)
        for t in state.terms
    ):
        return False
    if state.samjna_registry.get("2.1.51_taddhitartha_samAhAra_prakriya_42"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["2.1.51_taddhitartha_samAhAra_prakriya_42"] = True
    state.meta.pop("prakriya_42_2_1_51_arm", None)
    state.meta.pop("prakriya_P011_2_1_51_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.1.51",
    sutra_type=SutraType.SAMJNA,
    text_slp1="taddhitArthottarapadasamAhAre ca",
    text_dev="तद्धितार्थोत्तरपदसमाहारे च",
    padaccheda_dev="तद्धितार्थ-उत्तरपद-समाहारे च",
    why_dev="तद्धितार्थे सुबन्त-समाहारः (*prakriya_42*, **पञ्चेन्द्र**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
