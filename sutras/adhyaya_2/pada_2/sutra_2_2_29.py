"""
2.2.29  चार्थे द्वन्द्वः  —  SAMJNA (narrow demo)

Engine scope (v3 glass-box):
  This repository uses several *samāsa* sūtras as **registry stamps** when the
  JSON spine requires them, without implementing a full compound generator.

For ``split_prakriyas_11/P013.json`` we only need a narrow stamp:
  - requires **2.1.3** (*samāsa* adhikāra) on ``adhikara_stack``
  - recipe arms via ``state.meta['prakriya_P013_2_2_29_arm']``
  - witness tags include ``prakriya_P013_mAtApitarO_demo`` on any term

No varṇa mutation.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    if not state.meta.get("prakriya_P013_2_2_29_arm"):
        return False
    if not _samasa_adhikara_open(state):
        return False
    if state.samjna_registry.get("2.2.29_cArthe_dvandva_prakriya_P013"):
        return False
    if not any("prakriya_P013_mAtApitarO_demo" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.samjna_registry["2.2.29_cArthe_dvandva_prakriya_P013"] = True
    state.meta.pop("prakriya_P013_2_2_29_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.29",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "cArthe dvandvaH",
    text_dev       = "चार्थे द्वन्द्वः",
    padaccheda_dev = "च-अर्थे / द्वन्द्वः",
    why_dev        = "च-अर्थे द्वन्द्व-समास-संज्ञा (narrow stamp for P013).",
    anuvritti_from = ("2.1.3",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

