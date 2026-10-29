"""
5.1.98  तेन यथाकथाचहस्ताभ्यां णयतौ  —  VIDHI

Padaccheda: तेन यथाकथाच-हस्ताभ्याम् ण-यतौ

तेन यथाकथाचहस्ताभ्यां णयतौ (5.1.98)
Pāṭha: ashtadhyayi.com data.txt row i=51098 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_98_tena_98"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.98", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.98"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    ok = vivaksita(state, "taddhitArtha", "tenadIyate") or vivaksita(state, "taddhitArtha", "tenakArya")
    for stem, up in (("yaTAkaTAcA", "Ra"), ("hasta", "yat")):
        if taddhita_site(state, None, ok=ok, stems=frozenset({stem})) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.98")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.98", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena yaTAkaTAcahastAByAM RayatO",
    text_dev              = "तेन यथाकथाचहस्ताभ्यां णयतौ",
    samagra_slp1          = "tena dIyate kAryam iti yaTAkaTAca-hastAByAm Ra-yatO",
    samagra_dev           = "'तेन दीयते, कार्यम्' (इति) यथाकथाच-हस्ताभ्याम् ण-यतौ",
    padaccheda_dev        = "तेन यथाकथाच-हस्ताभ्याम् ण-यतौ",
    why_dev               = "(सूत्रम् 5.1.98) तेन यथाकथाचहस्ताभ्यां णयतौ।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
