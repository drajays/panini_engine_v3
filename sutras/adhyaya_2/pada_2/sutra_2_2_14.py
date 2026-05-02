"""
2.2.14  कर्तरि च  —  SAMJNA (narrow for P023 bahuvrīhi)

Context (as used in split_prakriyas_11/P023.json):
  Bahuvrīhi intent (*anekam anyapadārthe*) is asserted, yielding a compound
  prātipadika like ``dyu-kAma`` (“desiring heaven”, denoting another).

v3 narrow slice:
  - recipe arms: ``state.meta["P023_2_2_14_bahuvrihi_arm"] == True``
  - effect: register a bahuvrīhi saṃjñā marker in ``samjna_registry``.

This module does not attempt full samāsa formation; pipelines may perform
structural merges (recorded in trace) after asserting the intent.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("P023_2_2_14_bahuvrihi_arm")) and not bool(
        state.samjna_registry.get("2.2.14_bahuvrihi")
    )


def act(state: State) -> State:
    state.samjna_registry["2.2.14_bahuvrihi"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.14",
    sutra_type=SutraType.SAMJNA,
    text_slp1="kartari ca",
    text_dev="कर्तरि च",
    padaccheda_dev="कर्तरि / च",
    why_dev="बहुव्रीहौ अनेकेन अन्यपदार्थे (P023 डेमो) — संज्ञा-चिह्ननम्।",
    anuvritti_from=("2.2.13",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

