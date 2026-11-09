"""
8.2.73  तिप्यनस्तेः  —  VIDHI

Padaccheda: तिपि अन्-अस्तेः

तिप्यनस्तेः (8.2.73)
Pāṭha: ashtadhyayi.com data.txt row i=82073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _site(state: State):
    """the pada's last letter when a tip/sip was lopa'd (6.1.68) and the pada ends in s."""
    if not state.tripadi_zone or len(state.terms) != 1 or state.meta.get("tin_lopa_of") not in ("tip",):
        return None
    vs = state.terms[0].varnas
    return vs[-1] if vs and vs[-1].slp1 == "s" and "tin_lopa_8_2_7x_done" not in vs[-1].tags else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    v = _site(state)
    state.terms[0].varnas[-1] = mk("d")      # tipi: nityam d (acakād bhavān)
    state.terms[0].varnas[-1].tags.add("tin_lopa_8_2_7x_done")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tipyanasteH",
    text_dev              = "तिप्यनस्तेः",
    samagra_slp1          = "padasya pUrvatrAsidDam tipi anasteH saH daH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् तिपि अनस्तेः सः दः",
    padaccheda_dev        = "तिपि अन्-अस्तेः",
    why_dev               = "(सूत्रम् 8.2.73) तिप्यनस्तेः।",
    anuvritti_from        = ('8.1.1',),
    apavada_of            = ("8.2.66",),      # sip/tip: d (and ru) instead of the general s → ru
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
