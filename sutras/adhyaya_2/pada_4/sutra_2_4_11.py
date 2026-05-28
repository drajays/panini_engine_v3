"""
2.4.11  गवाश्वप्रभृतीनि च  —  VIDHI

Padaccheda: गव-अश्व-प्रभृतीनि च

Cow, horse etc. also in dvandva compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_11_gava_asva"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gavASvapraBftIni ca",
    text_dev              = "गवाश्वप्रभृतीनि च",
    padaccheda_dev        = "गव-अश्व-प्रभृतीनि च",
    why_dev               = "गव-अश्व-आदीनि च द्वन्द्वे (२.४.११)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
