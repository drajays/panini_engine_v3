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

Real branch (docs/SAMASA_MACHINE.md slice 2): a saṅkhyā pūrvapada and a samānādhikaraṇa uttarapada, vivakṣā samāhāra → tatpuruṣa.
Kāśikā: तद्धितार्थे विषय उत्तरपदे च परतः समाहारे चाभिधेये दिक्संख्ये समानाधिकरणेन सुपा सह समस्येते, तत्पुरुषश्च समासो भवति।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _old_site(state: State) -> bool:
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


def _old_cond(state: State) -> bool:
    return _old_site(state)


def _old_act(state: State) -> State:
    if not _old_site(state):
        return state
    state.samjna_registry["2.1.51_taddhitartha_samAhAra_prakriya_42"] = True
    return state


from engine.samasa_attach import pair, run, mark, name
from engine.vivaksha import vivaksita


def _site(state: State):
    return pair(state, "2.1.51", same_vib=True, purva=lambda t: "lex:saNKyA" in t.tags) if vivaksita(state, "arthaViSeSa", "samAhAra") else None


def cond(state: State) -> bool:
    return _site(state) is not None or _old_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _old_act(state)
    return mark(state, list(s), "tatpurusha", "2.1.51")


SUTRA = SutraRecord(
    sutra_id="2.1.51",
    sutra_type=SutraType.VIDHI,
    text_slp1='tadDitArTottarapadasamAhAre ca',
    text_dev='तद्धितार्थोत्तरपदसमाहारे च',
    samagra_slp1="AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH tadDitArTa-uttarapada-samAhAre ca samAnADikaraRena diksaNKye",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः तद्धितार्थ-उत्तरपद-समाहारे च समानाधिकरणेन दिक्सङ्ख्ये",
    padaccheda_dev="तद्धितार्थ-उत्तरपद-समाहारे च",
    why_dev="तद्धितार्थे सुबन्त-समाहारः (*prakriya_42*, **पञ्चेन्द्र**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
