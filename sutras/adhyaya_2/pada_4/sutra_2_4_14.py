"""
2.4.14  न दधिपयआदीनि  —  VIDHI

Padaccheda: न दधि-पय-आदीनि

NOT dadhi, payas etc. in dvandva.
Pāṭha: ashtadhyayi.com data.txt row i=24014 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_14_na_dadhi_paya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.14",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na daDipayaAdIni",
    text_dev              = "न दधिपयआदीनि",
    samagra_slp1          = "na daDi-paya-AdIni ekavacanam dvandvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न दधि-पय-आदीनि एकवचनम् द्वन्द्वः",
    padaccheda_dev        = "न दधि-पय-आदीनि",
    why_dev               = "न दधि-पय-आदीनि (२.४.१४)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
