"""
5.1.112  समापनात् सपूर्वपदात्  —  VIDHI

Padaccheda: समापनात् स-पूर्वपदात्

समापनात् सपूर्वपदात् (5.1.112)
Pāṭha: ashtadhyayi.com data.txt row i=51112 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_112_samApanAt_112"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.112", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.112"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return "Ca" if taddhita_site(state, None, ok=sense_in(state, "5.1.109"), tag="samAsa", final=lambda f: f.endswith("samApana") and f != "samApana") is not None else None      # SHORTCUT S35: sapūrvapada = lex:samAsa + final


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.112")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.112", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samApanAt sapUrvapadAt",
    text_dev              = "समापनात् सपूर्वपदात्",
    samagra_slp1          = "tad asya prayojanam iti samApanAt sapUrvapadAt CaH",
    samagra_dev           = "'तद् अस्य प्रयोजनम्' (इति) समापनात् सपूर्वपदात् छः",
    padaccheda_dev        = "समापनात् स-पूर्वपदात्",
    why_dev               = "(सूत्रम् 5.1.112) समापनात् सपूर्वपदात्।",
    anuvritti_from        = ('5.1.18',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
