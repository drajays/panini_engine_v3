"""
6.1.158  अनुदात्तं पदमेकवर्जम्  —  ANUVADA

**Pāṭha:** *anudāttaṃ padam ekavarjam* — in *saṃhitā*, every *pada* except one
is *anudātta* (sentence-level accent sandhi; cross-check: ashtadhyayi-com
``data.txt`` / local ``sutrANi.tsv``).

Narrow v3:
  • ``prakriya_17`` — **Phit** / **6.1.158** closure (``phit_6_1_158_recipe``).
  • ``prakriya_18`` — *sāmanyaḥ* accent note (``sama_6_1_158_recipe``).
  • ``prakriya_20`` — *devam* *kṛdanta* accent note (``devam_6_1_158_recipe``).
  • ``prakriya_26`` — *indra* *sambuddhi* accent note (``indra_6_1_158_recipe``).
  • ``prakriya_28`` — **मेघातिथे मन्महे** accent note (``megha_6_1_158_recipe``).
  • ``prakriya_29`` — **गौरावस्कन्दिन्** accent note (``gaura_6_1_158_recipe``).
  • ``prakriya_32`` — tri-vocative accent note (``trivoc_6_1_158_recipe``).
  • Trace-only (no *svara* columns on the flat tape).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(
        state.meta.get("phit_6_1_158_recipe")
        or state.meta.get("sama_6_1_158_recipe")
        or state.meta.get("devam_6_1_158_recipe")
        or state.meta.get("indra_6_1_158_recipe")
        or state.meta.get("megha_6_1_158_recipe")
        or state.meta.get("gaura_6_1_158_recipe")
        or state.meta.get("trivoc_6_1_158_recipe")
    )


def act(state: State) -> State:
    state.meta.pop("indra_6_1_158_recipe", None)
    state.meta.pop("megha_6_1_158_recipe", None)
    state.meta.pop("gaura_6_1_158_recipe", None)
    state.meta.pop("trivoc_6_1_158_recipe", None)
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
