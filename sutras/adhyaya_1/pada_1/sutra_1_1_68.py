"""
1.1.68  स्वं रूपं शब्दस्याशब्दसंज्ञा  —  ANUVADA (trace-only framing)

Classical role: interpretive clarification — "A word denotes its own form
unless it is a technical term (aśabda-saṃjñā)."

Engine role (narrow):
  This sūtra is frequently cited in JSON pipelines as an INPUT/SIDDHI frame.
  It does not perform a phonemic rewrite, nor does it install a gate needed
  elsewhere in v3.  We therefore model it as ANUVADA: it records an audit step
  once per derivation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not bool(state.meta.get("1_1_68_svadrupa_audit_done"))


def act(state: State) -> State:
    state.meta["1_1_68_svadrupa_audit_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.68",
    sutra_type=SutraType.ANUVADA,
    text_slp1="svaM rUpaM SabdasyASabdasamjYA",
    text_dev="स्वं रूपं शब्दस्याशब्दसंज्ञा",
    padaccheda_dev="स्वम् / रूपम् / शब्दस्य / अशब्द-संज्ञा",
    why_dev="शब्दः स्व-रूप-पर्यायः (अशब्द-संज्ञा-अपवादः) — डेमो-आडिट्।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

