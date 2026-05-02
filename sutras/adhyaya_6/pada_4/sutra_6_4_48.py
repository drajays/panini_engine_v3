"""
6.4.48  अतो लोपः  —  ANUVADA (trace-only slice)

Narrow **P026** note: *ato lopaḥ* would delete a stem-final *a* before a
following *a*-class context; on **vadh** there is no such *a*, so this step is
a śāstrīya audit in the JSON’s teaching order (no *varṇa* rewrite).

Pipelines arm ``state.meta['6_4_48_P026_trace_arm']`` once.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("6_4_48_P026_trace_arm"))


def act(state: State) -> State:
    state.meta["6_4_48_P026_trace_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.48",
    sutra_type=SutraType.ANUVADA,
    text_slp1="ato lopaH",
    text_dev="अतो लोपः",
    padaccheda_dev="अतः / लोपः",
    why_dev="अकारान्त-अङ्गस्य परे अकारादौ लोपः — इह वध्-प्रकृतौ न प्रवर्तते (ट्रेस्)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
