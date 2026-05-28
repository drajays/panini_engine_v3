"""
3.2.143  वौ कषलसकत्थस्रम्भः  —  VIDHI

Padaccheda: वौ कष-लस-कत्थ-स्रम्भः

krt-suffix rule: वौ कषलसकत्थस्रम्भः (143)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_143_vO_143"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.143"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vO kazalasakatTasramBaH",
    text_dev              = "वौ कषलसकत्थस्रम्भः",
    padaccheda_dev        = "वौ कष-लस-कत्थ-स्रम्भः",
    why_dev               = "धातोः कृत्-प्रत्ययः [वौ कषलसकत्थस्रम्भः] विहितः (३.२.143)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
