"""
8.1.18  अनुदात्तं सर्वमपादादौ  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=81018):** *anudāttaṃ sarvam apādādau* —
*anudāttaṃ sarvam apādādau ityadhikāraḥ* (scope through **8.1.74**
विभाषितं विशेषवचने बहुवचनम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.1.18" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.1.18",
        "scope_end" : "8.1.74",
        "text_dev"  : "अनुदात्तं सर्वमपादादौ",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.1.18",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "anudAttaM sarvam apAdAdau",
    text_dev       = "अनुदात्तं सर्वमपादादौ",
    padaccheda_dev = "अनुदात्तम् / सर्वम् / अपादादौ",
    why_dev        = "अनुदात्तं सर्वमपादादौ इत्यधिकारः — ८.१.१८ तः ८.१.७४ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.1.18", "8.1.74"),
)

register_sutra(SUTRA)

