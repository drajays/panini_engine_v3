"""
3.2.116  हशश्वतोर्लङ् च  —  VIDHI

Padaccheda: ह-शश्वतोः लङ् च

krt-suffix rule: हशश्वतोर्लङ् च (116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_116_haSaSvator_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_116_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "haSaSvatorlaN ca",
    text_dev              = "हशश्वतोर्लङ् च",
    padaccheda_dev        = "ह-शश्वतोः लङ् च",
    why_dev               = "धातोः कृत्-प्रत्ययः [हशश्वतोर्लङ् च] विहितः (३.२.116)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
