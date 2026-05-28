"""
3.4.59  अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ  —  VIDHI

Padaccheda: अव्यये अयथाभिप्रेताख्याने कृञः क्त्वा-णमुँल्ौ

krt-suffix rule: अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_59_avyayeyaT_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("3_4_59_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyaye'yaTABipretAKyAne kfYaH ktvARamulO",
    text_dev              = "अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ",
    padaccheda_dev        = "अव्यये अयथाभिप्रेताख्याने कृञः क्त्वा-णमुँल्ौ",
    why_dev               = "धातोः प्रत्ययः (३.4.59)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
