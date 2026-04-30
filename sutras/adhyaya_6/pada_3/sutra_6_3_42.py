"""
6.3.42  पुंवत् कर्मधारयजातीयदेशीयेषु  —  SAMJNA (narrow ``prakriya_37``)

**Pāṭha (cross-check: ``sutrANi.tsv``):** *puṃvat karma-dhāraya-jātīya-deśīyeṣu* — prior member of a
*karma-dhāraya* compound may receive masculine-like treatment (*puṃvat*).

Narrow v3 (**पाचिका** → **पाचक** stage in ``panini_engine_pipeline``):
  • Requires ``samjna_registry['1.2.42_karmadhAraya_prakriya_37']`` from **1.2.42**.
  • ``prakriya_37_6_3_42_arm`` registers ``samjna_registry['6.3.42_puMvaw_prakriya_37']``.

Full morphophonemic **ङीप्**→``पācaka`` substitution is not modelled — registry-only slice.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_37_6_3_42_arm"):
        return False
    if not state.samjna_registry.get("1.2.42_karmadhAraya_prakriya_37"):
        return False
    if state.samjna_registry.get("6.3.42_puMvaw_prakriya_37"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["6.3.42_puMvaw_prakriya_37"] = True
    state.meta.pop("prakriya_37_6_3_42_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.3.42",
    sutra_type=SutraType.SAMJNA,
    text_slp1="puMvaw karmaDArayajAtIyadeSIyezu",
    text_dev="पुंवत् कर्मधारयजातीयदेशीयेषु",
    padaccheda_dev="पुंवत् / कर्मधारय-जातीय-देशीयेषु",
    why_dev="कर्मधारये पूर्वपदस्य पुंवद्भावः (*prakriya_37*, संक्षेप-अङ्कनम्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
