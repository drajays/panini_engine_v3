"""
1.4.71  तिरोऽन्तर्द्धौ  (tiro 'ntarddho)  —  SAMJNA

The word "tiras" gets the gati-saṃjñā specifically when used in the sense
of antardhāna (concealment/disappearance), e.g., "tiras-dhā" (to conceal),
"tiras-kṛ" (to put behind / to disrespect).

v3: registers samjna_registry["gati_tiras_antarddha"] = frozenset({"tiras"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_TIRAS: frozenset[str] = frozenset({"tiras"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_tiras_antarddha") is None


def act(state: State) -> State:
    state.samjna_registry["gati_tiras_antarddha"] = _TIRAS
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _TIRAS
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.71",
    sutra_type=SutraType.SAMJNA,
    text_slp1="tiro 'ntardDAv",
    text_dev="तिरोऽन्तर्द्धौ",
    padaccheda_dev="तिरः / अन्तर्द्धौ",
    why_dev="अन्तर्द्धौ 'तिरस्' गति-संज्ञकः — 'tiras' गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
