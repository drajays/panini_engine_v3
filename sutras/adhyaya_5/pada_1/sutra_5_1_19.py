"""
5.1.19  आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51019):** *prāg-ārhīya ṭhag-adhikāraḥ*
— scope through **5.1.63** (तद् अर्हति), matching v2
``adhikara_prakarana.json`` sequence **40**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.1.19" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.1.19",
        "scope_end" : "5.1.63",
        "text_dev"  : "आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.1.19",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "A arhAt a-gopuccha-saNKyA-parimANAt Wak",
    text_dev       = "आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्",
    padaccheda_dev = "आ / अर्हात् / अ-गोपुच्छ-संख्या-परिमाणात् / ठक्",
    why_dev        = "प्रागार्हीयः ठगधिकारः — ५.१.१९ तः ५.१.६३ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.1.19", "5.1.63"),
)

register_sutra(SUTRA)

