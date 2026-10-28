"""
5.1.17  परिखाया ढञ्  —  VIDHI

Padaccheda: परिखायाः ढञ्

परिखाया ढञ् (5.1.17)
Pāṭha: ashtadhyayi.com data.txt row i=51017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_17_pariKAyA_17"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.17", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.17"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, group_open, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _attach(state: State):
    if taddhita_site(state, 'syAt', stems=frozenset(['pariKA'])) is not None:
        return 'QaY'
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _attach(state) is not None:
        up = _attach(state)
        return attach_taddhita(state, up if isinstance(up, str) else up[0 if policy_pick(state, "5.1.17", len(up)) == 0 else 1])
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "5.1.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pariKAyA QaY",
    text_dev              = "परिखाया ढञ्",
    samagra_slp1          = "tat asya syAt iti taTA tat asmin syAt iti iti pariKAyAH QaY",
    samagra_dev           = "'तत् अस्य स्यात् इति' (तथा)  'तत् अस्मिन् स्यात् इति' (इति) परिखायाः ढञ्",
    padaccheda_dev        = "परिखायाः ढञ्",
    why_dev               = "(सूत्रम् 5.1.17) परिखाया ढञ्।",
    anuvritti_from        = ('5.1.1',),
    apavada_of     = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
