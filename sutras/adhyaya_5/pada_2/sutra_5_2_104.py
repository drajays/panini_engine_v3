"""
5.2.104  सिकताशर्कराभ्यां च  —  VIDHI

Padaccheda: सिकता-शर्कराभ्याम् च

सिकताशर्कराभ्यां च (5.2.104)
Pāṭha: ashtadhyayi.com data.txt row i=52104 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_104_sikatASark_104"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.104", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.104"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _site(state: State, **kw):
    return taddhita_site(state, None, ok=sense_in(state, "5.2.94"), **kw)


def _attach(state: State):
    if vivaksita(state, "arthaViSeSa", "deSa") and _site(state, stems=frozenset({'sikatA', 'SarkarA'})) is not None:
        return ('aR', '-', 'H:5.2.105')
    if _site(state, stems=frozenset({'sikatA', 'SarkarA'})) is not None:
        return ('aR', '-')
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.104")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.104", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside; matup (5.2.94) stays and the generic 5.2.115 – 117 are barred
        state.meta["declined:5.2.104"] = True
        state.meta["special_aside"] = True
        return state
    if up.startswith("H:"):                        # handed on to the next sūtra of the chain (ca): matup waits for it
        state.meta["declined:5.2.104"] = True
        state.meta["hold:" + up[2:]] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sikatASarkarAByAM ca",
    text_dev              = "सिकताशर्कराभ्यां च",
    samagra_slp1          = "tat asya asmin astIti iti deSe sikatA-SarkarAByAmaR",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) सिकता-शर्कराभ्यामण्",
    padaccheda_dev        = "सिकता-शर्कराभ्याम् च",
    why_dev               = "(सूत्रम् 5.2.104) सिकताशर्कराभ्यां च।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.94', '5.2.115'),
    also_vidhi     = True,          # a vā / ca reading that changes no letter (stands aside, hands on) must still reach act: effective_candidates keeps it
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
