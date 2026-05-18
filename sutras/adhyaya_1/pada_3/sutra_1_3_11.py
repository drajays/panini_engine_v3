"""
1.3.11  स्वरितेनाधिकारः  —  ADHIKARA

*Padaccheda:* *svaritena* (तृतीया) / *adhikāraḥ* (प्रथमा).

*Content:* The adhikāra (scope) marked by svarita accent governs rules 1.3.12–1.3.93,
the ātmanepada-assignment block.  This rule opens that gate.

*Engine:* registers gate "1_3_11_svaritena_aDikAraH" in paribhasha_gates and
samjna_registry.  cond is True whenever the gate has not yet been registered.
r1_form_identity_exempt=True because no surface change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_3_11_svaritena_aDikAraH"


def cond(state: State) -> bool:
    return _GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.11",
    sutra_type=SutraType.ADHIKARA,
    text_slp1="svaritena aDikAraH",
    text_dev="स्वरितेनाधिकारः",
    padaccheda_dev="स्वरितेन (तृतीया) / अधिकारः (प्रथमा)",
    why_dev=(
        "स्वरितेन चिह्नितस्य अधिकारस्य विषयः १.३.१२–१.३.९३ इत्येषु आत्मनेपद-नियमेषु।"
    ),
    anuvritti_from=(),
    adhikara_scope=("1.3.12", "1.3.93"),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
