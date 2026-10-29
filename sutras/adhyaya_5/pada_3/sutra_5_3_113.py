"""
5.3.113  व्रातच्फञोरस्त्रियाम्  —  VIDHI

Padaccheda: व्रातच्-फञोः अ-स्त्रियाम्

व्रातच्फञोरस्त्रियाम् (5.3.113)
Pāṭha: ashtadhyayi.com data.txt row i=53113 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_113_vrAtacPaYo_113"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.113", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.113"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    return "Yya" if taddhita_site(state, None, ok=True, tag="vrAta") is not None else None      # SHORTCUT S55: vrāta by the caller's lex: tag; the cphañ-anta stems and astriyām are not modelled


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.113")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.113", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.113"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vrAtacPaYorastriyAm",
    text_dev              = "व्रातच्फञोरस्त्रियाम्",
    samagra_slp1          = "vrAta-cPaYoH astriyAm YyaH",
    samagra_dev           = "व्रात-च्फञोः अस्त्रियाम् ञ्यः",
    padaccheda_dev        = "व्रातच्-फञोः अ-स्त्रियाम्",
    why_dev               = "(सूत्रम् 5.3.113) व्रातच्फञोरस्त्रियाम्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
