"""
8.2.40  झषस्तथोर्धोऽधः  —  VIDHI (narrow demo)

Demo slice (रुणद्धि .md):
  When a jhaṣ phoneme (here: 'D' = ध्) precedes 't' (from ti), change that 't'
  to 'D' (ध्). This creates the trigger for 8.4.53 (jhalām jaś jhaśi) on the
  preceding consonant.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_2_40_jhas_tatho_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "D" and vs[i + 1].slp1 == "t":
            return i + 1
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    j = _find(state)
    if j is None:
        return state
    t = state.terms[0]
    t.varnas[j] = mk("D")
    t.meta["8_2_40_jhas_tatho_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.40",
    sutra_type=SutraType.VIDHI,
    text_slp1="Jhazastatho rDho aDaH",
    text_dev="झषस्तथोर्धोऽधः",
    padaccheda_dev="झषः / त-थोः / (र्धः) / अधः",
    why_dev="झष्-पूर्वे त्/थ् का ध्-आदेशः (डेमो: रुणद्धि)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

