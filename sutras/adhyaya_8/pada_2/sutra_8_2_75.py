"""
8.2.75  दश्च  —  VIDHI

Padaccheda: दः च

दश्च (8.2.75)
Pāṭha: ashtadhyayi.com data.txt row i=82075 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _site(state: State):
    """the pada's last letter when a tip/sip was lopa'd (6.1.68) and the pada ends in d."""
    if not state.tripadi_zone or len(state.terms) != 1 or state.meta.get("tin_lopa_of") not in ("sip",):
        return None
    vs = state.terms[0].varnas
    return vs[-1] if vs and vs[-1].slp1 == "d" and "tin_lopa_8_2_7x_done" not in vs[-1].tags else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    from engine.vikalpa import policy_pick
    v = _site(state)
    if policy_pick(state, "8.2.75", 2) == 0:         # ru (abhinaḥ) / the d (abhinat): Kāśikā 8.2.75, "dakāro vā"
        r = mk("r")
        r.tags.add("ru_intermediate")
        state.terms[0].varnas[-1] = r
    else:
        state.terms[0].varnas[-1] = mk("d")
    state.terms[0].varnas[-1].tags.add("tin_lopa_8_2_7x_done")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "daSca",
    text_dev              = "दश्च",
    samagra_slp1          = "padasya pUrvatrAsidDam daH ca sipi ruH vA DAtoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् दः च सिपि रुः वा धातोः",
    padaccheda_dev        = "दः च",
    why_dev               = "(सूत्रम् 8.2.75) दश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
