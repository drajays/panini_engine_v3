"""
1.4.65  अन्तरपरिग्रहे  (antara-parigrahe)  —  SAMJNA

The word "antar" gets the gati-saṃjñā when used in the sense of
parigraha (enclosure / inside), e.g., "antar-dhā" (to hide inside),
"antar-kṛ" (to put inside).

v3: registers samjna_registry["gati_antar_parigrahe"] = frozenset({"antar"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_ANTAR: frozenset[str] = frozenset({"antar"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_antar_parigrahe") is None


def act(state: State) -> State:
    state.samjna_registry["gati_antar_parigrahe"] = _ANTAR
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _ANTAR
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.65",
    sutra_type=SutraType.SAMJNA,
    text_slp1="antaraparigrahe",
    text_dev="अन्तरपरिग्रहे",
    padaccheda_dev="अन्तर् / परिग्रहे",
    why_dev="परिग्रहे 'अन्तर्' शब्दो गति-संज्ञकः — 'antar' गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
