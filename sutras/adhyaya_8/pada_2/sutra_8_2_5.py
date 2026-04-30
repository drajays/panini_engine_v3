"""
8.2.5  एकादेश उदात्तेनोदात्तः  —  SAMJNA (narrow)

**Pāṭha:** *ekādeśa udāttenodāttaḥ* — an *ekādeśa* replacement is *udātta*
when conditioned by an *udātta* (accent *śāstra*; v3 has no *svara* column on
the phonetic tape).

Narrow v3:
  • ``prakriya_16`` — यद् + जस् → ये tail: arms ``state.meta['8_2_5_ye_yad_jas_arm']``.
  • ``prakriya_20`` — *devam* *ekādeśa* accent (``prakriya_20_devam_8_2_5_arm``).

Common:
  • Fires only in **Tripāḍī** (``state.tripadi_zone`` after **8.2.1**).
  • Registers the current flat surface under ``samjna_registry['ekadesa_udatta_8_2_5']``
    for audit (one application per derivation).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    if not (
        state.meta.get("8_2_5_ye_yad_jas_arm")
        or state.meta.get("prakriya_20_devam_8_2_5_arm")
    ):
        return False
    if "ekadesa_udatta_8_2_5" in state.samjna_registry:
        return False
    return True


def act(state: State) -> State:
    surface = state.flat_slp1()
    state.samjna_registry["ekadesa_udatta_8_2_5"] = frozenset({surface})
    state.meta.pop("8_2_5_ye_yad_jas_arm", None)
    state.meta.pop("prakriya_20_devam_8_2_5_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.5",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "ekAdeSa udAttenodAttaH",
    text_dev       = "एकादेश उदात्तेनोदात्तः",
    padaccheda_dev = "एकादेशः उदात्तेन उदात्तः",
    why_dev        = "एकादेशस्य उदात्तत्वम् — वर्ण-पटे अनुदात्तादि नास्ति; संज्ञा-अङ्कनम्।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
