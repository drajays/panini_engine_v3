"""
8.2.81  एत ईद्बहुवचने  —  VIDHI

Padaccheda: एतः ईत् बहुवचने

एत ईद्बहुवचने (8.2.81)
Pāṭha: ashtadhyayi.com data.txt row i=82081 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

def cond(state: State) -> bool:
    if not (state.tripadi_zone or state.phase == "tripadi"):
        return False
    if not state.meta.get("adas_stem") or state.meta.get("adas_dm_done"):
        return False
    if not state.meta.get("adas_bahuvacana") or not state.terms:
        return False
    v = state.terms[0].varnas
    return len(v) > 2 and v[0].slp1 == "a" and v[1].slp1 == "d" and v[2].slp1 == "e"


def act(state: State) -> State:
    v = state.terms[0].varnas
    v[2] = mk("I")   # e → ī in bahuvacana, then d → m
    v[1] = mk("m")
    state.meta["adas_dm_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.81",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "eta Idbahuvacane",
    text_dev              = "एत ईद्बहुवचने",
    samagra_slp1          = "padasya pUrvatrAsidDam etaH It bahuvacane adasaH dAt u daH maH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् एतः ईत् बहुवचने अदसः दात् उ दः मः",
    padaccheda_dev        = "एतः ईत् बहुवचने",
    why_dev               = "(सूत्रम् 8.2.81) एत ईद्बहुवचने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
