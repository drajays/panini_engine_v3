"""
1.4.61  ऊर्यादिच्विडाचश्च  (ūryādi-cvi-ḍācaś ca)  —  SAMJNA

The ūry-ādi words (a gaṇa), the cvi-suffix forms, and the ḍāc-suffix forms
also get the gati-saṃjñā.

ūry-ādi members (selected; SLP1): Ury, tiras, antarA, hAs, hA, hiMs,
viHs, AvIs, AkUs, etc.  These adverbial/compound members combine with
karoति/bhavati and obtain gati-saṃjñā enabling kṛt/taddhita behaviour.

v3: extends samjna_registry["gati_set"] with the ūry-ādi members; also
    registers samjna_registry["gati_uryadiR"] as the ūry-ādi-specific frozenset.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_URYA_ADI: frozenset[str] = frozenset({
    "Ury", "tiras", "antarA", "hAs", "hiMs", "viHs", "AvIs", "AkUs",
    "AzIs", "sAt", "sat", "vibA", "AgUs",
})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_uryadiR") is None


def act(state: State) -> State:
    state.samjna_registry["gati_uryadiR"] = _URYA_ADI
    # Extend gati_set if it already exists
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _URYA_ADI
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.61",
    sutra_type=SutraType.SAMJNA,
    text_slp1="UryAdicviDAcaS ca",
    text_dev="ऊर्यादिच्विडाचश्च",
    padaccheda_dev="ऊर्य-आदि / च्वि / डाच् / च",
    why_dev="ऊर्यादयः, च्व्यन्ताः, डाचन्ताश्च गति-संज्ञकाः — ऊर्यादि-सूचिः गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
