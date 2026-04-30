"""
6.1.158  अनुदात्तं पदमेकवर्जम्  —  ANUVADA

**Pāṭha:** *anudāttaṃ padam ekavarjam* — in *saṃhitā*, every *pada* except one
is *anudātta* (sentence-level accent sandhi; cross-check: ashtadhyayi-com
``data.txt`` / local ``sutrANi.tsv``).

Narrow v3:
  • ``prakriya_17`` — **Phit** / **6.1.158** closure (``prakriya_17_6_1_158_arm``).
  • ``prakriya_18`` — *sāmanyaḥ* accent note (``prakriya_18_6_1_158_arm``).
  • ``prakriya_20`` — *devam* *kṛdanta* accent note (``prakriya_20_devam_6_1_158_arm``).
  • ``prakriya_26`` — *indra* *sambuddhi* accent note (``prakriya_26_6_1_158_arm``).
  • ``prakriya_28`` — **मेघातिथे मन्महे** accent note (``prakriya_28_6_1_158_arm``).
  • ``prakriya_29`` — **गौरावस्कन्दिन्** accent note (``prakriya_29_6_1_158_arm``).
  • ``prakriya_32`` — tri-vocative accent note (``prakriya_32_6_1_158_arm``).
  • Trace-only (no *svara* columns on the flat tape).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(
        state.meta.get("prakriya_17_6_1_158_arm")
        or state.meta.get("prakriya_18_6_1_158_arm")
        or state.meta.get("prakriya_20_devam_6_1_158_arm")
        or state.meta.get("prakriya_26_6_1_158_arm")
        or state.meta.get("prakriya_28_6_1_158_arm")
        or state.meta.get("prakriya_29_6_1_158_arm")
        or state.meta.get("prakriya_32_6_1_158_arm")
    )


def act(state: State) -> State:
    state.meta.pop("prakriya_26_6_1_158_arm", None)
    state.meta.pop("prakriya_28_6_1_158_arm", None)
    state.meta.pop("prakriya_29_6_1_158_arm", None)
    state.meta.pop("prakriya_32_6_1_158_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.158",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "anudAttaM padamekavarjam",
    text_dev       = "अनुदात्तं पदमेकवर्जम्",
    padaccheda_dev = "अनुदात्तम् / पदम् / एकवर्जम्",
    why_dev        = "वाक्ये अनुदात्त-पद-न्यायः (श्रुति-स्तरः; वर्ण-पटे नास्ति)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
