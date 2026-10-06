"""
6.3.54  हिमकाषिहतिषु च  —  VIDHI

Padaccheda: हिम-काषि-हतिषु च

हिमकाषिहतिषु च (6.3.54)
Pāṭha: ashtadhyayi.com data.txt row i=63054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_54_himakAziha_54"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.54", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "himakAzihatizu ca",
    text_dev              = "हिमकाषिहतिषु च",
    samagra_slp1          = "uttarapade hima-kAzi-hatizu ca treH pAdasya pad",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे हिम-काषि-हतिषु च त्रेः पादस्य पद्",
    padaccheda_dev        = "हिम-काषि-हतिषु च",
    why_dev               = "(सूत्रम् 6.3.54) हिमकाषिहतिषु च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
