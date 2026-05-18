"""
7.4.51  रि च  —  VIDHI

*tāsi*-vikaraṇa (``tAsi_vikaraṇa``) Term that ends in ``…A``+``s`` → drop
the final ``s`` when the following tiṅ Term begins with ``r``.

Gate: ``7_4_51_arm``; completion registered in ``samjna_registry``.

This is the *luṭ* 3du (rau) and 3pl (ras) path:
  [BU, i+t+A+s, rO] → [BU, i+t+A, rO]   (3du)
  [BU, i+t+A+s, ras] → [BU, i+t+A, ras]  (3pl)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_51_ri_51"


def _find_tasi_before_r(state: State) -> int | None:
    """Find tAsi_vikaraṇa term ending in …A+s where next term starts with r."""
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
        if nxt.varnas[0].slp1 == "r":
            return i
    return None


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not state.meta.get("7_4_51_arm"):
        return False
    return _find_tasi_before_r(state) is not None


def act(state: State) -> State:
    i = _find_tasi_before_r(state)
    if i is not None:
        t = state.terms[i]
        # Drop the final s from tAs → tA
        if t.varnas and t.varnas[-1].slp1 == "s":
            t.varnas = t.varnas[:-1]
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ri ca",
    text_dev              = "रि च",
    padaccheda_dev        = "रि च",
    why_dev               = "तासि-विकरणस्य स्-लोपः रि-परे — लुट् ३du/३pl कोशः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
