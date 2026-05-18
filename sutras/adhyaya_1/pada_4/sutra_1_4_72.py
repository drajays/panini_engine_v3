"""
1.4.72  विभाषा कृञि  (vibhāṣā kṛñi)  —  VIBHASHA

The word "tiras" optionally (vibhāṣā) gets the gati-saṃjñā when used with
the root kṛ (kṛñ, do/make).  Thus "tiras-kṛ" may or may not be treated
as a gati + kṛ compound; both derivations are acceptable.

This is an optional rule (vibhāṣā): the gate defaults to the preferred
reading (tiras is treated as a gati with kṛ), but recipes may fork
the derivation.

v3: registers samjna_registry["gati_tiras_kRni_vibhasha"] = True.
    vibhasha_default = True means the gati reading is the preferred option.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_tiras_kRni_vibhasha") is None


def act(state: State) -> State:
    state.samjna_registry["gati_tiras_kRni_vibhasha"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.72",
    sutra_type=SutraType.VIBHASHA,
    text_slp1="viBAzA kRRi",
    text_dev="विभाषा कृञि",
    padaccheda_dev="विभाषा / कृञि",
    why_dev="कृञि 'तिरस्' विभाषया गति-संज्ञकः — ऐच्छिकः पक्षः।",
    anuvritti_from=("1.4.60", "1.4.71"),
    r1_form_identity_exempt=True,
    vibhasha_default=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
