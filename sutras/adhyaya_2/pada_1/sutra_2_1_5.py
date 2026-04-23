"""
2.1.5  अव्ययीभावः  (avyayībhāvaḥ)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=21005):** opens the traditional
*avyayībhāva* adhikāra.

Per legacy span metadata, the scope runs through **2.1.21** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.1.5", "2.1.21")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.1.5" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.1.5",
        "scope_end" : "2.1.21",
        "text_dev"  : "अव्ययीभावः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.1.5",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "avyayIBAvaH",
    text_dev        = "अव्ययीभावः",
    padaccheda_dev  = "अव्ययीभावः",
    why_dev         = "२.१.५ इत्यतः २.१.२१ पर्यन्तम् 'अव्ययीभाव' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.1.5", "2.1.21"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

