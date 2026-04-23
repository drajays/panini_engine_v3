"""
1.4.1  आ कडारादेका संज्ञा  (ā kaḍārād ekā saṃjñā)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=14001):** this is the traditional
*eka-saṃjñā* adhikāra: “from here up to 2.2.38, (certain items) have one
technical designation.”

v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("1.4.1", "2.2.38")`` (inclusive).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "1.4.1" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "1.4.1",
        "scope_end" : "2.2.38",
        "text_dev"  : "आ कडारादेका संज्ञा",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "1.4.1",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "A kaDArAd ekA saMjYA",
    text_dev        = "आ कडारादेका संज्ञा",
    padaccheda_dev  = "आ / कडारात् / एका / संज्ञा",
    why_dev         = "१.४.१ इत्यतः २.२.३८ पर्यन्तम् 'एकसंज्ञा' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("1.4.1", "2.2.38"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

