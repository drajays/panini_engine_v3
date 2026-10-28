"""
4.3.3  तवकममकावेकवचने  —  VIDHI

Padaccheda: तवक-ममकौ एकवचने

तवकममकावेकवचने (4.3.3)
Pāṭha: ashtadhyayi.com data.txt row i=43003 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_3_tavakamama_3"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.3", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.3"
    return state



from phonology.varna import parse_slp1_upadesha_sequence
from engine.vivaksha import vivaksita
_ADESHA = {"yuzmad": "tavaka", "asmad": "mamaka"}


def _site(state: State):
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if ((t.meta.get("upadesha_slp1") or "") in _ADESHA and "taddhita" in pr.tags
                and (pr.meta.get("upadesha_slp1") or "") in ("KaY", "aR") and not t.meta.get("4_3_2_adesha")):
            return i
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None and vivaksita(state, "ekavacana", "ekavacana")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        t = state.terms[_site(state)]
        t.varnas = list(parse_slp1_upadesha_sequence(_ADESHA[t.meta["upadesha_slp1"]]))
        t.meta["4_3_2_adesha"] = True          # the one ādeśa this stem takes: 4.3.2 stands aside
        return state
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.3.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tavakamamakAvekavacane",
    text_dev              = "तवकममकावेकवचने",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA tavaka-mamakO ekavacane yuzmad-asmadoH KaY tasmin aRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा तवक-ममकौ एकवचने युष्मद्-अस्मदोः खञ् तस्मिन् अणि",
    padaccheda_dev        = "तवक-ममकौ एकवचने",
    why_dev               = "(सूत्रम् 4.3.3) तवकममकावेकवचने।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.3.2',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
