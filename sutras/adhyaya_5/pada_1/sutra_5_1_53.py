"""
5.1.53  आढकाचितपात्रात् खोऽन्यतरस्याम्  —  VIDHI

Padaccheda: आढक-आचित-पात्रात् खः अन्यतरयाम्

आढकाचितपात्रात् खोऽन्यतरयाम् (5.1.53)
Pāṭha: ashtadhyayi.com data.txt row i=51053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_53_AQakAcitap_53"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.53", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.53"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return ("Ka", "-") if arhiya_site(state, "5.1.52", stems=frozenset({"AQaka", "Acita", "pAtra"})) is not None else None      # anyatarasyām: or the ṭhañ that stays


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.53")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.53", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.53"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'AQakAcitapAtrAt KonyatarasyAm',
    text_dev              = 'आढकाचितपात्रात् खोऽन्यतरस्याम्',
    samagra_slp1          = "tat samBavati  avaharati pacati iti AQaka-Acita-pAtrAt anyatarasyAm KaH",
    samagra_dev           = "'तत् सम्भवति , अवहरति, पचति' (इति) आढक-आचित-पात्रात् अन्यतरस्याम् खः",
    padaccheda_dev        = "आढक-आचित-पात्रात् खः अन्यतरयाम्",
    why_dev               = "(सूत्रम् 5.1.53) आढकाचितपात्रात् खोऽन्यतरयाम्।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
