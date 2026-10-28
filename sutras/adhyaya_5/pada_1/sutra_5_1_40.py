"""
5.1.40  पुत्राच्छ च  —  VIDHI

Padaccheda: पुत्रात् छ (लुप्तप्रथमान्तनिर्देशः) च

पुत्राच्छ च (5.1.40)
Pāṭha: ashtadhyayi.com data.txt row i=51040 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_40_putrAcCa_40"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.40", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.40"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return ("Ca", "yat") if arhiya_site(state, "5.1.38", stems=frozenset({"putra"})) is not None else None      # ca: and the yat that 5.1.39 gives a dvyac


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.40")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.40", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.40"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "putrAcCa ca",
    text_dev              = "पुत्राच्छ च",
    samagra_slp1          = "tasya nimittaM saMyogotpAtO iti putrAt yat CaH ca",
    samagra_dev           = "'तस्य निमित्तं संयोगोत्पातौ' इति पुत्रात् यत् छः च",
    padaccheda_dev        = "पुत्रात् छ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 5.1.40) पुत्राच्छ च।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19', '5.1.39'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
