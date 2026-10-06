"""
7.2.78  ईडजनोर्ध्वे च  —  VIDHI

Padaccheda: ईड-जनोः ध्वे (लुप्तषष्ठ्यन्तनिर्देशः) च

ईडजनोर्ध्वे च (7.2.78)
Pāṭha: ashtadhyayi.com data.txt row i=72078 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_78_IqajanorDv_78"


from sutras.adhyaya_7.pada_2.sutra_7_2_77 import iT_act, iT_site

_ROOTS = frozenset({"Iqa~", "janI~", "ISa~"})      # ca: īśaḥ too takes iṭ before dhve (ISiDve); its se is 7.2.77


def cond(state: State) -> bool:
    return iT_site(state, _ROOTS, True) is not None


def act(state: State) -> State:
    iT_act(state, _ROOTS, True)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.78",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "IqajanorDve ca",
    text_dev              = "ईडजनोर्ध्वे च",
    samagra_slp1          = "aNgasya IqajanoH Dve ca iw valAdeH sArvaDAtuke se",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ईडजनोः ध्वे च इट् वलादेः सार्वधातुके से",
    padaccheda_dev        = "ईड-जनोः ध्वे (लुप्तषष्ठ्यन्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 7.2.78) ईडजनोर्ध्वे च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
