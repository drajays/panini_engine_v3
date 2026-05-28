"""
3.2.159  दाधेट्सिशदसदो रुः  —  VIDHI

Padaccheda: दा-धेट्-सि-शद-सदः रुः

krt-suffix rule: दाधेट्सिशदसदो रुः (159)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_159_dADewsiSad_159"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_159_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.159"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.159",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dADewsiSadasado ruH",
    text_dev              = "दाधेट्सिशदसदो रुः",
    padaccheda_dev        = "दा-धेट्-सि-शद-सदः रुः",
    why_dev               = "धातोः कृत्-प्रत्ययः [दाधेट्सिशदसदो रुः] विहितः (३.२.159)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
