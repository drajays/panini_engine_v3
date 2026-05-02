"""
6.1.11  लुङि  —  PARIBHASHA (narrow gate: *luṅ* reduplication frame)

Operational JSON **P037** cites *dvitva* under *luṅ*(*i*): this engine slice
records eligibility and arms the existing **6.1.1** *dvitva* hook (recipe must
still call **6.1.1** with ``6_1_1_dvitva_arm`` afterwards).

COND: ``state.meta['P037_6_1_11_lugi_arm']`` and ``lakara == 'luG'``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "P037_6_1_11_lugi_dvitva"


def cond(state: State) -> bool:
    if GATE_KEY in state.paribhasha_gates:
        return False
    if not state.meta.get("P037_6_1_11_lugi_arm"):
        return False
    return (state.meta.get("lakara") or "").strip() == "luG"


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.meta.pop("P037_6_1_11_lugi_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.11",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="luGi",
    text_dev="लुङि",
    padaccheda_dev="लुङि",
    why_dev="लुङ-प्रकरणे द्वित्व-प्रवृतौ ग्लास-बॉक्स् द्वारः (P037)।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
