"""
4.4.77  धुरो यड्ढकौ  —  VIDHI

Padaccheda: धुरः यत्-ढकौ

धुरो यड्ढकौ (4.4.77)
Pāṭha: ashtadhyayi.com data.txt row i=44077 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_77_Duro_77"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.77", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.77"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _attach(state: State):
    if taddhita_site(state, "vahati", stems=frozenset(['Dur'])) is not None:
        return ('yat', 'Qak')
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _attach(state) is not None:
        up = _attach(state)
        return attach_taddhita(state, up if isinstance(up, str) else up[0 if policy_pick(state, "4.4.77", len(up)) == 0 else 1])
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Duro yaqQakO",
    text_dev              = "धुरो यड्ढकौ",
    samagra_slp1          = "tat vahati iti DuraH yat-QakO",
    samagra_dev           = "'तत् वहति' इति धुरः यत्-ढकौ",
    padaccheda_dev        = "धुरः यत्-ढकौ",
    why_dev               = "(सूत्रम् 4.4.77) धुरो यड्ढकौ।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.4.75',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
