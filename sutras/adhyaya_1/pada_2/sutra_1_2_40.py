"""
1.2.40  उदात्तस्वरितपरस्य सन्नतरः  —  SAMJNA (narrow ``prakriya_33`` / ``prakriya_34``)

**Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com sutra index):**
*udātta-svarita-parasya sannataraḥ* — the vowel/accent immediately following an *udātta* or
*svarita* is *sannatara* (relative depression), conditioning **saṃhitā** accent behaviour.

Narrow v3:
  • ``prakriya_33`` (*मातरोऽपः*): ``meta['prakriya_33_ekazruti_na_upapatti_note']`` +
    ``prakriya_33_1_2_40_arm`` + tag ``prakriya_33_mAtaro_apaH_accent_demo`` →
    ``samjna_registry['1.2.40_sannatara_prakriya_33']``.
  • ``prakriya_34`` (**अध्यापक क्व**): ``terms[0]`` ``prakriya_34_aDyApaka_sarvAnudAtta_note`` (**8.1.19**) +
    ``terms[1]`` ``prakriya_34_kv_svarita_note`` (**6.1.185**) + ``prakriya_34_1_2_40_arm`` →
    ``samjna_registry['1.2.40_sannatara_prakriya_34']``.

``cond`` does not read surface Devanāgarī targets — only ``meta`` arms + ``Term.tags``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site_prakriya_33(state: State) -> bool:
    if not state.meta.get("prakriya_33_1_2_40_arm"):
        return False
    if not state.meta.get("prakriya_33_ekazruti_na_upapatti_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_33_mAtaro_apaH_accent_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("1.2.40_sannatara_prakriya_33"):
        return False
    return True


def _site_prakriya_34(state: State) -> bool:
    if not state.meta.get("prakriya_34_1_2_40_arm"):
        return False
    if len(state.terms) < 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if "prakriya_34_aDyApaka_kv_demo" not in t0.tags:
        return False
    if not t0.meta.get("prakriya_34_aDyApaka_sarvAnudAtta_note"):
        return False
    if not t1.meta.get("prakriya_34_kv_svarita_note"):
        return False
    if state.samjna_registry.get("1.2.40_sannatara_prakriya_34"):
        return False
    return True


def cond(state: State) -> bool:
    return _site_prakriya_33(state) or _site_prakriya_34(state)


def act(state: State) -> State:
    if _site_prakriya_34(state):
        state.samjna_registry["1.2.40_sannatara_prakriya_34"] = True
        state.meta.pop("prakriya_34_1_2_40_arm", None)
        return state
    if _site_prakriya_33(state):
        state.samjna_registry["1.2.40_sannatara_prakriya_33"] = True
        state.meta.pop("prakriya_33_1_2_40_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.40",
    sutra_type=SutraType.SAMJNA,
    text_slp1="udAttasvaritaparasya sannataraH",
    text_dev="उदात्तस्वरितपरस्य सन्नतरः",
    padaccheda_dev="उदात्त-स्वरित-परस्य / सन्नतरः",
    why_dev="उदात्त-स्वरित-परः सन्नतरः (*prakriya_33* / *34*, *śruti*-स्तरः)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
