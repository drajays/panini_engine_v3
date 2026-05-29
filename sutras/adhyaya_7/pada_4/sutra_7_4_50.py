"""
7.4.50  तासस्त्योर्लोपः  —  VIDHI

*tāsi*-vikaraṇa (``tAsi_vikaraṇa``) Term that ends in ``…A``+``s`` → drop
the final ``s`` when the following tiṅ Term begins with ``s`` (i.e., *si* from
*sip* for 2sg, or *ty* from *asti*).

Gate: ``tasa_lopa_recipe``; completion registered in ``samjna_registry``.

*luṭ* 2sg (si) path:
  [BU, i+t+A+s, si] → [BU, i+t+A, si]
Final form: भवितासि.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_50_tAsastyorl_50"


def _find_tasi_before_si(state: State) -> int | None:
    """Find tAsi_vikaraṇa term ending in …A+s where next term starts with s."""
    for i in range(len(state.terms) - 1):
        t = state.terms[i]
        if not t.meta.get("tAsi_vikaraṇa"):
            continue
        vs = t.varnas
        if len(vs) < 2:
            continue
        if vs[-1].slp1 != "s":
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas:
            continue
        if nxt.varnas[0].slp1 == "s":
            return i
    return None


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not state.meta.get("tasa_lopa_recipe"):
        return False
    return _find_tasi_before_si(state) is not None


def act(state: State) -> State:
    i = _find_tasi_before_si(state)
    if i is not None:
        t = state.terms[i]
        # Drop the final s from tAs → tA
        if t.varnas and t.varnas[-1].slp1 == "s":
            t.varnas = t.varnas[:-1]
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tAsastyorlopaH",
    text_dev              = "तासस्त्योर्लोपः",
    padaccheda_dev        = "तास्-अस्त्योः लोपः",
    why_dev               = "तासि-विकरणस्य स्-लोपः सि-परे — लुट् २sg कोशः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
