"""
4.4.100  भक्ताण्णः  —  VIDHI

Padaccheda: भक्तात् णः

भक्ताण्णः (4.4.100)
Pāṭha: ashtadhyayi.com data.txt row i=44100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_100_BaktARRaH_100"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.100", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.100"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _attach(state: State):
    if taddhita_site(state, "sADu", stems=frozenset(['Bakta'])) is not None and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return 'Ra'
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _attach(state) is not None:
        up = _attach(state)
        return attach_taddhita(state, up if isinstance(up, str) else up[0 if policy_pick(state, "4.4.100", len(up)) == 0 else 1])
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BaktARRaH",
    text_dev              = "भक्ताण्णः",
    samagra_slp1          = "tatra sADuH iti BaktAt saMjYAyAm RaH",
    samagra_dev           = "'तत्र साधुः' इति भक्तात् संज्ञायाम् णः",
    padaccheda_dev        = "भक्तात् णः",
    why_dev               = "(सूत्रम् 4.4.100) भक्ताण्णः।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.4.75',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
