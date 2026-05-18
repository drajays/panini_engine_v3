"""
1.4.77  नित्यं हस्ते पाणावुपयमने  (nityaṃ haste pāṇāv upayamane)  —  SAMJNA

The words "haste" (in the hand) and "pāṇau" (in the palm) invariably
(nityam) get the gati-saṃjñā in the sense of upayamana (taking by the
hand in marriage / accepting).

E.g., "haste-kṛ" (to take by the hand) in the marriage ritual context.

v3: registers samjna_registry["gati_haste_panau"] = frozenset({"haste","pARau"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_HASTE_PANAU: frozenset[str] = frozenset({"haste", "pARau"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_haste_panau") is None


def act(state: State) -> State:
    state.samjna_registry["gati_haste_panau"] = _HASTE_PANAU
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _HASTE_PANAU
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.77",
    sutra_type=SutraType.SAMJNA,
    text_slp1="nityaM haste pARAvupayamane",
    text_dev="नित्यं हस्ते पाणावुपयमने",
    padaccheda_dev="नित्यम् / हस्ते / पाणौ / उपयमने",
    why_dev="उपयमने नित्यं 'हस्ते' 'पाणौ' गति-संज्ञकौ — गति-सेटे योज्येते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
