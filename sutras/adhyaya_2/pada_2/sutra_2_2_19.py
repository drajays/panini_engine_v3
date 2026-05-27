"""
2.2.19  उपपदमतिङ्खि  —  SAMJNA (upapada compound)

Śāstra summary: an *upapada* is compounded with a related *pada* that does not end
in a *tiṅ* affix — licensing *samāsa* of the *upapada* frame (e.g. *ratna* + *śas*
with *√dhā* + *kvip* in ``prakriya_22``).

Fires when any Term carries the ``upapada`` tag (structural environment set by
the pipeline before calling this sūtra).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not any("upapada" in t.tags for t in state.terms):
        return False
    return not bool(state.samjna_registry.get("2.2.19_upapada_atiNg"))


def act(state: State) -> State:
    state.samjna_registry["2.2.19_upapada_atiNg"] = True
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
