"""
2.4.48  इङश्च  —  VIDHI

Padaccheda: इङः च

Also for ing root.
Pāṭha: ashtadhyayi.com data.txt row i=24048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_48_inga_ca"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.48", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iNaSca",
    text_dev              = "इङश्च",
    samagra_slp1          = "ArDaDAtuke iNaH ca gamiH sani",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आर्धधातुके इङः च गमिः सनि",
    padaccheda_dev        = "इङः च",
    why_dev               = "इङः च (२.४.४८)।",
    anuvritti_from        = ('2.4.46',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
