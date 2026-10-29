"""
5.1.110  विशाखाषाढादण् मन्थदण्डयोः  —  VIDHI

Padaccheda: विशाखा-आषाढात् अण् मन्थ-दण्डयोः

विशाखाऽऽषाढादण् मन्थदण्डयोः (5.1.110)
Pāṭha: ashtadhyayi.com data.txt row i=51110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_110_viSAKAzA_110"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.110", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.110"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    for stem, said in (("viSAKA", vivaksita(state, "arthaViSeSa", "manTa")), ("AzAQA", vivaksita(state, "arthaViSeSa", "daRqa"))):
        ok = sense_in(state, "5.1.109") and said      # SHORTCUT S35: yathāsaṅkhya as two vivakṣā values (viśākhā – mantha, āṣāḍhā – daṇḍa)
        if taddhita_site(state, None, ok=ok, stems=frozenset({stem})) is not None:
            return "aR"
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.110")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.110", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'viSAKAzAQAdaR manTadaRqayoH',
    text_dev              = 'विशाखाषाढादण् मन्थदण्डयोः',
    samagra_slp1          = "tat asya prayojanam iti viSAKA-AzAQAt manTa-daRqayoH aR",
    samagra_dev           = "'तत् अस्य प्रयोजनम्' (इति) विशाखा-आषाढात् मन्थ-दण्डयोः अण्",
    padaccheda_dev        = "विशाखा-आषाढात् अण् मन्थ-दण्डयोः",
    why_dev               = "(सूत्रम् 5.1.110) विशाखाऽऽषाढादण् मन्थदण्डयोः।",
    anuvritti_from        = ('5.1.18',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
