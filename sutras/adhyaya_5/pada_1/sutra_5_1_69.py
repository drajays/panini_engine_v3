"""
5.1.69  कडङ्करदक्षिणाच्छ च  —  VIDHI

Padaccheda: कडङ्गर-दक्षिणात् छ (लुप्तप्रथमान्तनिर्देशः) च

कडङ्गरदक्षिणाच्छ च (5.1.69)
Pāṭha: ashtadhyayi.com data.txt row i=51069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_69_kaqaNgarad_69"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.69", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.69"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return ("Ca", "yat") if arhiya_site(state, "5.1.63", stems=frozenset({"kaqaNkara", "dakziRA"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.69")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.69", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.69"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'kaqaNkaradakziRAcCa ca',
    text_dev              = 'कडङ्करदक्षिणाच्छ च',
    samagra_slp1          = "tad arhati iti kaqaNkara-dakziRAt CaH yat ca",
    samagra_dev           = "'तद् अर्हति' (इति)  कडङ्कर-दक्षिणात् छः यत् च",
    padaccheda_dev        = "कडङ्गर-दक्षिणात् छ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 5.1.69) कडङ्गरदक्षिणाच्छ च।",
    anuvritti_from        = ('5.1.18',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
