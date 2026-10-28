"""
4.4.79  एकधुराल्लुक् च  —  VIDHI

Padaccheda: एकधुरात् लुक् च

एकधुराल्लुक् च (4.4.79)
Pāṭha: ashtadhyayi.com data.txt row i=44079 (Art. 14).
"""
# DEFERRED: not yet real — reason, missing feature and the stage that finishes it are in docs/DEFERRED_SUTRAS.md
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_79_ekaDurAllu_79"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.79", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.79"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
from engine.luk import take_away
def _attach(state: State):
    if taddhita_site(state, "vahati", stems=frozenset(['ekaDurA'])) is not None:
        return 'Ka'
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _attach(state) is not None:
        up = _attach(state)
        luk = policy_pick(state, "4.4.79", 2) == 1      # "ca": the kha, and (vacanasāmarthyāt, in one reading) its luk — ekadhurīṇaḥ, ekadhuraḥ
        state = attach_taddhita(state, up if isinstance(up, str) else up[0])
        return take_away(state, len(state.terms) - 1, "luk") if luk else state
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekaDurAlluk ca",
    text_dev              = "एकधुराल्लुक् च",
    samagra_slp1          = "tat vahati iti ekaDurAt KaH luk ca",
    samagra_dev           = "'तत् वहति' इति एकधुरात् खः लुक् च",
    padaccheda_dev        = "एकधुरात् लुक् च",
    why_dev               = "(सूत्रम् 4.4.79) एकधुराल्लुक् च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.4.75',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
