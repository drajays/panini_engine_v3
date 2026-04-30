"""
4.1.88  द्विगोर्लुगनपत्ये  —  SAMJNA (narrow ``prakriya_42``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41088):** *dvigor lug anapatye* — *luk* of a *taddhita*
suffix after a *dvigu* when the sense is not *apatya* / when conditions match (scholia link **अनपत्ये**).

Narrow v3 (**पञ्चेन्द्र** `panini_engine_pipeline` — *aṇ* *luk* after *dvigu* *paYcendra*):
  • **4.1.76** *taddhita* *adhikāra* on ``adhikara_stack``.
  • ``prakriya_42_4_1_88_arm`` + ``meta['prakriya_42_dvigu_anapatye_note']`` +
    witness ``Term`` tagged ``prakriya_42_paYcendra_demo`` →
    ``samjna_registry['4.1.88_dvigor_lug_anapatye_prakriya_42']``.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _taddhita_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_42_4_1_88_arm"):
        return False
    if not _taddhita_adhikara_open(state):
        return False
    if not state.meta.get("prakriya_42_dvigu_anapatye_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_42_paYcendra_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("4.1.88_dvigor_lug_anapatye_prakriya_42"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["4.1.88_dvigor_lug_anapatye_prakriya_42"] = True
    state.meta.pop("prakriya_42_4_1_88_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="4.1.88",
    sutra_type=SutraType.SAMJNA,
    text_slp1="dvigorluganapatye",
    text_dev="द्विगोर्लुगनपत्ये",
    padaccheda_dev="द्विगोः / लुक् / अनपत्ये",
    why_dev="द्विगोः परस्य तद्धितस्य लुक् (*devatā*, न अपत्ये) (*prakriya_42*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
