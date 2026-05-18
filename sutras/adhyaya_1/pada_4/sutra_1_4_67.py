"""
1.4.67  पुरोऽव्ययम्  (puro 'vyayam)  —  SAMJNA

The word "puras" (in front) is an avyaya (indeclinable) and gets the
gati-saṃjñā.  E.g., "puro-kṛ" (to place in front), "puro-dhā" (to keep
in front — whence the compound purohita).

v3: registers samjna_registry["gati_puras"] = frozenset({"puras"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_PURAS: frozenset[str] = frozenset({"puras"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_puras") is None


def act(state: State) -> State:
    state.samjna_registry["gati_puras"] = _PURAS
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _PURAS
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.67",
    sutra_type=SutraType.SAMJNA,
    text_slp1="puro 'vyayam",
    text_dev="पुरोऽव्ययम्",
    padaccheda_dev="पुरः / अव्ययम्",
    why_dev="'पुरस्' अव्ययं गति-संज्ञकम् — 'puras' गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
