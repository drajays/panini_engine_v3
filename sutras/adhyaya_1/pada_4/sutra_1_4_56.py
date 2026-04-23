"""
1.4.56  प्राग्रीश्वरान्निपाताः  (prāg rīśvarān nipātāḥ)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=14056):** opens the traditional
*nipāta-saṃjñā* adhikāra (“before *rīśvara*, (these) are nipātas”).

Per legacy span metadata, the scope runs through **1.4.97** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("1.4.56", "1.4.97")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "1.4.56" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "1.4.56",
        "scope_end" : "1.4.97",
        "text_dev"  : "प्राग्रीश्वरान्निपाताः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "1.4.56",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "prAg rISvarAt nipAtAH",
    text_dev        = "प्राग्रीश्वरान्निपाताः",
    padaccheda_dev  = "प्राक् / रीश्वरात् / निपाताः",
    why_dev         = "१.४.५६ इत्यतः १.४.९७ पर्यन्तं 'निपात' संज्ञाधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("1.4.56", "1.4.97"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

