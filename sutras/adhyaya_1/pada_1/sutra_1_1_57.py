"""
1.1.57  अचः परस्मिन् पूर्वविधौ  —  PARIBHASHA (narrow P025)

*Acaḥ parasmin pūrvavidhau* — an *ac* (vowel) elided by a *pūrva-vidhi* is
*sthānivat* for purposes of a following *para* rule.

v3: installs ``paribhasha_gates["1.1.57_aca_parasmin_purvavidhau"]`` once for the
P025 *ṇic* / *upadhā* blocking illustration.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "1.1.57_aca_parasmin_purvavidhau"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.57",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="acaH parasmin pUrvavidhO",
    text_dev="अचः परस्मिन् पूर्वविधौ",
    padaccheda_dev="अचः / परस्मिन् / पूर्वविधौ",
    why_dev="पूर्वविधि-लोपितस्य अचः स्थानिवत्-भावः (P025)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
