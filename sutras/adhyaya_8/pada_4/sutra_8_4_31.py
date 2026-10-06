"""
8.4.31  हलश्च इजुपधात्  —  VIDHI

Padaccheda: हलः च इच्-उपधात्

हलश्च इजुपधात् (8.4.31)
Pāṭha: ashtadhyayi.com data.txt row i=84031 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_31_halaSca_31"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.31", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "halaSca ijupaDAt",
    text_dev              = "हलश्च इजुपधात्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm halaH ca ic-upaDAt razAByAm upasargAt acaH kfti ReH viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् हलः च इच्-उपधात् रषाभ्याम् उपसर्गात् अचः कृति णेः विभाषा",
    padaccheda_dev        = "हलः च इच्-उपधात्",
    why_dev               = "(सूत्रम् 8.4.31) हलश्च इजुपधात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
