"""
7.3.118  औत्  —  VIDHI

Padaccheda: औत्

औत् (7.3.118)
Pāṭha: ashtadhyayi.com data.txt row i=73118 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

def _site(state: State):
    """इदुद्भ्यामङ्गात् ङेः औत् — an i/u-final aṅga that is neither nadī (7.3.116/117) nor ghi (7.3.119 takes it with its own at): सख्यौ, पत्यौ."""
    if len(state.terms) < 2:
        return None
    anga, pr = state.terms[-2], state.terms[-1]
    if "sup" not in pr.tags or "prātipadika" not in anga.tags or not anga.varnas:
        return None
    if (pr.meta.get("upadesha_slp1") or "").strip() != "Ni" or pr.meta.get("ngi_to_au_done"):
        return None
    if "nadi" in anga.tags or "ghi" in anga.tags or anga.varnas[-1].slp1 not in {"i", "u"}:
        return None
    return pr


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    pr = _site(state)
    pr.varnas = [mk("O")]
    pr.meta["ngi_to_au_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "Ni")
    pr.meta["upadesha_slp1"] = "O"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.118",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "Ot",
    text_dev              = "औत्",
    samagra_slp1          = "idudByAmaNgAt NeH Ot",
    samagra_dev           = "इदुद्भ्यामङ्गात् ङेः औत्",
    padaccheda_dev        = "औत्",
    why_dev               = "(सूत्रम् 7.3.118) औत्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
