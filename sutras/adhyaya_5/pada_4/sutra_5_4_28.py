"""
5.4.28  अवेः कः  —  VIDHI

Padaccheda: अवेः कः

अवेः कः (5.4.28)
Pāṭha: ashtadhyayi.com data.txt row i=54028 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_28_aveH_28"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.28", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.28"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

# AMENDMENT 27: a svārthika sūtra — 5.4.28 svārthe kaḥ (Kāśikā). No sense frame, no samartha-vibhakti (Kāśikā 5.3.1); the optional vā (4.1.82, Kāśikā 5.4.39 vikalpaḥ sarvatrānuvartate) is the "-" reading.


def _attach(state: State):
    if not vivaksita(state, "taddhitArtha", "svArTa"):
        return None
    return ('ka', '-') if taddhita_site(state, None, ok=True, stems=frozenset({"avi"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.28")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.28", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the plain stem stays
        state.meta["declined:5.4.28"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.4.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aveH kaH",
    text_dev              = "अवेः कः",
    samagra_slp1          = "aveH kaH",
    samagra_dev           = "अवेः कः",
    padaccheda_dev        = "अवेः कः",
    why_dev               = "(सूत्रम् 5.4.28) अवेः कः।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
