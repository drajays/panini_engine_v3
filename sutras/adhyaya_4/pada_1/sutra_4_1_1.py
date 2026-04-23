"""
4.1.1  ङ्याप्प्रातिपदिकात्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41001):** *prātipadikādhikāraḥ* — scope
through **5.4.160**.

This is modelled as an adhikāra (v2: ``adhikara_prakarana.json`` sequence 29):
from here, rules operate “from a prātipadika” until 5.4.160.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.1.1",
        "scope_end" : "5.4.160",
        "text_dev"  : "ङ्याप्प्रातिपदिकात्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "NyAp prAtipadikAt",
    text_dev       = "ङ्याप्प्रातिपदिकात्",
    padaccheda_dev = "ङी-आप्-प्रातिपदिकात्",
    why_dev        = "प्रातिपदिकाधिकारः — ४.१.१ तः ५.४.१६० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.1", "5.4.160"),
)

register_sutra(SUTRA)
