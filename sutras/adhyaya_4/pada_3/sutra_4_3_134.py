"""
4.3.134  तस्य विकारः  —  SAMJNA (narrow ``prakriya_44``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=43134):** *tasya vikāraḥ* — *taddhita* licence in the sense of a modification /
derivative (*vikāra*) of that (*tasya*) — e.g. fruit (*फलम्*) from the tree (*आमलकी*).

Narrow v3 (**आमलकम्** ``…/separated_prakriyas/prakriya_44_*.json``):
  • **4.1.76** *taddhita* *adhikāra* on ``adhikara_stack``.
  • ``prakriya_44_4_3_134_arm`` + ``meta['prakriya_44_tasya_vikAra_note']`` +
    witness ``Term`` tagged ``prakriya_44_Amalakam_demo`` →
    ``samjna_registry['4.3.134_tasya_vikAra_prakriya_44']``.

**Edition note:** JSON ``ordered_sutra_sequence`` lists **4.3.132**, which in *ashtadhyayi-com* is a different
rule (*कौपिञ्जलहास्तिपदादण्*). The commentary ``panini_engine_pipeline`` cites **तस्य विकारः** — **4.3.134**.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _taddhita_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_44_4_3_134_arm"):
        return False
    if not _taddhita_adhikara_open(state):
        return False
    if not state.meta.get("prakriya_44_tasya_vikAra_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_44_Amalakam_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("4.3.134_tasya_vikAra_prakriya_44"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["4.3.134_tasya_vikAra_prakriya_44"] = True
    state.meta.pop("prakriya_44_4_3_134_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="4.3.134",
    sutra_type=SutraType.SAMJNA,
    text_slp1="tasya vikAraH",
    text_dev="तस्य विकारः",
    padaccheda_dev="तस्य विकारः",
    why_dev="विकारार्थे तद्धितः (*prakriya_44*, **आमलकम्**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
