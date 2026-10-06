"""
6.1.145  गोष्पदं सेवितासेवितप्रमाणेषु  —  VIDHI

Padaccheda: गोष्पदम् सेविता-आसेवित-प्रमाणेषु

गोष्पदं सेवितासेवितप्रमाणेषु (6.1.145)
Pāṭha: ashtadhyayi.com data.txt row i=61145 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_145_gozpadaM_145"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.145", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gozpadaM sevitAsevitapramARezu",
    text_dev              = "गोष्पदं सेवितासेवितप्रमाणेषु",
    samagra_slp1          = "saMhitAyAm suwkAtpUrvaH gozpadam sevita-asevita-pramARezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् सुट्कात्पूर्वः गोष्पदम् सेवित-असेवित-प्रमाणेषु",
    padaccheda_dev        = "गोष्पदम् सेविता-आसेवित-प्रमाणेषु",
    why_dev               = "(सूत्रम् 6.1.145) गोष्पदं सेवितासेवितप्रमाणेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
