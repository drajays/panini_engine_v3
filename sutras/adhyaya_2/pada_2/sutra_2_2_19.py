"""
2.2.19  उपपदमतिङ्खि  —  SAMJNA (narrow *glass-box*)

Śāstra summary: an *upapada* is compounded with a related *pada* that does not end
in a *tiṅ* affix — licensing *samāsa* of the *upapada* frame (e.g. *ratna* + *śas*
with *√dhā* + *kvip* in ``prakriya_22``).

Engine:
  Recipe arms ``state.meta['2_2_19_upapada_atiNg_arm']`` once internal *sup* and
  *kṛt* are on the tape; **act** records a registry flag and clears the arm.
  Structural *padasaṅkara* is handled by the recipe (CONSTITUTION Art. 7).

``cond`` / ``act`` do not read *vibhakti* / surface gold.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("2_2_19_upapada_atiNg_arm"))


def act(state: State) -> State:
    if not cond(state):
        return state
    state.samjna_registry["2.2.19_upapada_atiNg"] = True
    state.meta.pop("2_2_19_upapada_atiNg_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.19",
    sutra_type=SutraType.SAMJNA,
    text_slp1="upapadam atiNgi",
    text_dev="उपपदमतिङ्खि",
    padaccheda_dev="उपपदम् / अतिङ्खि",
    why_dev="उपपद-समासार्थं संज्ञा-अनुमोदनम् (प्रक्रिया-२२)।",
    anuvritti_from=("2.1.3",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
