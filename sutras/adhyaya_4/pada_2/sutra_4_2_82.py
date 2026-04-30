"""
4.2.82  वरणादिभ्यश्च  —  SAMJNA (narrow ``prakriya_46``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=42082):** *varaṇādibhyaś ca* — *luk* of *taddhita* **after** bases of the *varaṇādi-gaṇa* (includes **गोद**). Machine **anuvṛtti** links ``लुप्`` to **4.2.81** (*janapade lup*, i=42081).

**Edition note:** Some commentaries/OCR label this rule “**4.2.81**”; on ashtadhyayi-com **4.2.81** is *janapade lup* (42081). The **varaṇādi** *luk* rule is **4.2.82** here.

**Engine:** glass-box note ``samjna_registry['4.2.82_varaNAdi_luk_prakriya_46']`` — recipe gate only; no ``varṇa`` mutation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _taddhita_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_46_4_2_82_arm"):
        return False
    if not _taddhita_adhikara_open(state):
        return False
    if not state.meta.get("prakriya_46_varaNAdi_luk_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_46_godau_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("4.2.82_varaNAdi_luk_prakriya_46"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["4.2.82_varaNAdi_luk_prakriya_46"] = True
    state.meta.pop("prakriya_46_4_2_82_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="4.2.82",
    sutra_type=SutraType.SAMJNA,
    text_slp1="varaRAdibhyaSca",
    text_dev="वरणादिभ्यश्च",
    padaccheda_dev="वरणादिभ्यः / च",
    why_dev=(
        "वरणाद्यन्ताद् अण्-लुपि चिह्नम् (*prakriya_46*); **4.2.81** इत्यत्र *जनपदे लुप्* पृथक्।"
    ),
    anuvritti_from=("4.2.81",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
