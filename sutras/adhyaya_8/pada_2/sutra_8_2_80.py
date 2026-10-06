"""
8.2.80  अदसोऽसेर्दादु दो मः  —  VIDHI

Padaccheda: अदसः अ-सेः दात् उ (लुप्तप्रथमान्तनिर्देशः) दः मः

अदसोऽसेर्दादु दो मः (8.2.80)
Pāṭha: ashtadhyayi.com data.txt row i=82080 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

def _target(state: State):
    """(term, index of the vowel after the stem's d) for an adas pada, else None."""
    if not state.meta.get("adas_stem") or state.meta.get("adas_dm_done"):
        return None
    if state.meta.get("adas_sau_au") or not state.terms:
        return None   # अ-सेः: not before su (असौ)
    t = state.terms[0]
    if len(t.varnas) > 2 and t.varnas[0].slp1 == "a" and t.varnas[1].slp1 in ("d", "s"):
        return t
    return None


_U = {"a": "u", "A": "U", "O": "U"}   # the vowel after d: hrasva → u, dīrgha/au → ū


def cond(state: State) -> bool:
    if not (state.tripadi_zone or state.phase == "tripadi"):
        return False
    t = _target(state)
    return t is not None and t.varnas[1].slp1 == "d" and t.varnas[2].slp1 in _U


def act(state: State) -> State:
    t = _target(state)
    t.varnas[2] = mk(_U[t.varnas[2].slp1])
    t.varnas[1] = mk("m")
    state.meta["adas_dm_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.80",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'adasoserdAdu do maH',
    text_dev              = 'अदसोऽसेर्दादु दो मः',
    samagra_slp1          = "padasya pUrvatrAsidDam adasaH aseH dAt u daH maH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् अदसः असेः दात् उ दः मः",
    padaccheda_dev        = "अदसः अ-सेः दात् उ (लुप्तप्रथमान्तनिर्देशः) दः मः",
    why_dev               = "(सूत्रम् 8.2.80) अदसोऽसेर्दादु दो मः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
