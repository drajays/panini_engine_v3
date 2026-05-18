"""
1.4.75  अनत्याधान उरसिमनसी  (anatyādhāna urasi-manasī)  —  SAMJNA

The words "urasi" (on the chest) and "manasi" (in the mind) get the
gati-saṃjñā when used without the meaning of anatyādhāna (excessive
burden / overloading).

v3: registers samjna_registry["gati_urasi_manasi"] = frozenset({"urasi","manasi"}).
Note: "manasi" overlaps with 1.4.66 but in a different semantic context;
both registrations are kept separate.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_URASI_MANASI: frozenset[str] = frozenset({"urasi", "manasi"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_urasi_manasi") is None


def act(state: State) -> State:
    state.samjna_registry["gati_urasi_manasi"] = _URASI_MANASI
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _URASI_MANASI
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.75",
    sutra_type=SutraType.SAMJNA,
    text_slp1="anatyADAna urasi-manasI",
    text_dev="अनत्याधान उरसिमनसी",
    padaccheda_dev="अनत्याधाने / उरसि-मनसी",
    why_dev="अनत्याधाने 'उरसि' 'मनसि' गति-संज्ञकौ — गति-सेटे योज्येते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
