"""
7.2.104  कु तिहोः  —  VIDHI

Padaccheda: कु ति-होः

कु तिहोः (7.2.104)
Pāṭha: ashtadhyayi.com data.txt row i=72104 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_104_ku_104"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.104", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.104"
    return state


from sutras.adhyaya_7.pada_2.sutra_7_2_103 import kim_site, kim_adesha


def _site(state: State):
    return kim_site(state, first=('t', 'h'))


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    i = _site(state)
    return kim_adesha(state, i, "ku", "7.2.104") if i is not None else _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "7.2.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ku tihoH",
    text_dev              = "कु तिहोः",
    samagra_slp1          = "kimaH ti-hoH viBaktO kuH",
    samagra_dev           = "किमः ति-होः विभक्तौ कुः",
    padaccheda_dev        = "कु ति-होः",
    why_dev               = "(सूत्रम् 7.2.104) कु तिहोः।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ('7.2.103',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
