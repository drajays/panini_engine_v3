"""
3.1.62  अचः कर्मकर्तरि  —  SAMJNA (narrow ``prakriya_35``)

**Pāṭha (cross-check: ``sutrANi.tsv``):** *acaḥ karma-kartari* — affixation condition involving
*karma/kartari* of vowel-grade alternation (*ac* rules).

Narrow v3 (*घृतस्पृक्* commentary spine):
  • After **1.3.1** stamps ``spfS`` dhātu under ``prakriya_35_spfSa_kvin_demo``, ``prakriya_35_3_1_62_arm``
    registers ``samjna_registry['3.1.62_ac_karmakartari_prakriya_35']`` (glass-box anchor for *kvín*
    neighbourhood — full **३.१.६२** selection scope is not modelled).

No ``varṇa`` mutation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_35_3_1_62_arm"):
        return False
    if not state.samjna_registry.get("1.3.1_prakriya_35_spfSa"):
        return False
    if state.samjna_registry.get("3.1.62_ac_karmakartari_prakriya_35"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["3.1.62_ac_karmakartari_prakriya_35"] = True
    state.meta.pop("prakriya_35_3_1_62_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.62",
    sutra_type=SutraType.SAMJNA,
    text_slp1="acaH karmakartari",
    text_dev="अचः कर्मकर्तरि",
    padaccheda_dev="अचः / कर्मकर्तरि",
    why_dev="अच्-प्रकरणे कर्म-कर्तरि प्रत्ययार्थः (*prakriya_35*, संक्षेप-अङ्कनम्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
