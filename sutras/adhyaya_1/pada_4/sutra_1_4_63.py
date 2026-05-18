"""
1.4.63  आदरानादरयोः सदसती  (ādarānādarayoḥ sad-asatī)  —  SAMJNA

The words sat (सत्) and asat (असत्) get the gati-saṃjñā when used in the
sense of ādarа (respect) or anādara (disrespect).

E.g., "sat-kṛ" (to honour) and "asat-kṛ" (to dishonour) — here sat/asat
function as gatis modifying the verb root kṛ.

v3: registers samjna_registry["gati_sad_asati"] with the frozenset {"sat","asat"}.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_SAD_ASATI: frozenset[str] = frozenset({"sat", "asat"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_sad_asati") is None


def act(state: State) -> State:
    state.samjna_registry["gati_sad_asati"] = _SAD_ASATI
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _SAD_ASATI
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.63",
    sutra_type=SutraType.SAMJNA,
    text_slp1="AdarAnAdarayoH sadасаtI",
    text_dev="आदरानादरयोः सदसती",
    padaccheda_dev="आदर-अनादरयोः / सत्-असती",
    why_dev="आदरानादरयोः 'सत्' 'असत्' शब्दौ गति-संज्ञकौ — सत्-सूचिः गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
