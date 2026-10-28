"""
4.4.35  पक्षिमत्स्यमृगान् हन्ति  —  VIDHI

Padaccheda: पक्षि-मत्स्य-मृगान् हन्ति (क्रियापदम्)

पक्षिमत्स्यमृगान् हन्ति (4.4.35)
Pāṭha: ashtadhyayi.com data.txt row i=44035 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_35_pakzimatsy_35"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.35", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.35"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _sense(state: State):
    if not stem_ends_tape(state):
        return None
    if vivaksita(state, "taddhitArtha", "hanti") and not any(e.get("id") == "4.4.35" for e in state.adhikara_stack):
        return ('hanti', {'stems': ['pakzin', 'Sakuni', 'mayUra', 'tittiri', 'matsya', 'mIna', 'SaPara', 'Sakula', 'mfga', 'hariRa', 'sUkara']})
    return None


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _sense(state) is not None:
        v, only = _sense(state)
        return open_default_frame(state, "4.4.35", v, "4.4.1", "4.4.74", only)
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pakzimatsyamfgAn hanti",
    text_dev              = "पक्षिमत्स्यमृगान् हन्ति",
    samagra_slp1          = "tat pakzi-matsya-mfgAn hanti iti samarTAnAM praTamAt paraH Wak pratyayaH",
    samagra_dev           = "'तत् पक्षि-मत्स्य-मृगान् हन्ति' (इति) समर्थानां प्रथमात् परः ठक् प्रत्ययः",
    padaccheda_dev        = "पक्षि-मत्स्य-मृगान् हन्ति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.35) पक्षिमत्स्यमृगान् हन्ति।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
