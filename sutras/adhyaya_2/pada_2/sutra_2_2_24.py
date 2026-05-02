"""
2.2.24  अनेकमन्यपदार्थे  —  SAMJNA (narrow for P024 bahuvrīhi)

Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com ``data.txt`` i=20224):
  *anekam anyapadārthe* — names the *bahuvrīhi* class when several members
  denote another entity’s meaning.

v3 narrow slice:
  • recipe arms: ``state.meta["P024_2_2_24_arm"] == True`` (P024)
                 or ``state.meta["P027_2_2_24_arm"] == True`` (P027)
  • effect: register ``samjna_registry["2.2.24_anekam_anyapadartha"]`` once.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    arm = bool(state.meta.get("P024_2_2_24_arm")) or bool(state.meta.get("P027_2_2_24_arm"))
    return arm and not bool(state.samjna_registry.get("2.2.24_anekam_anyapadartha"))


def act(state: State) -> State:
    state.samjna_registry["2.2.24_anekam_anyapadartha"] = True
    state.meta.pop("P024_2_2_24_arm", None)
    state.meta.pop("P027_2_2_24_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.24",
    sutra_type=SutraType.SAMJNA,
    text_slp1="anekam anyapadArTe",
    text_dev="अनेकमन्यपदार्थे",
    padaccheda_dev="अनेकम् / अन्य-पद-अर्थे",
    why_dev="बहुव्रीहौ अनेकेन अन्य-पदार्थे (P024 डेमो) — संज्ञा-चिह्ननम्।",
    anuvritti_from=("2.2.23",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
