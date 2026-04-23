"""
2.1.3  प्राक् कडारात् समासः  (prāk kaḍārāt samāsaḥ)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=21003):** opens the traditional
*samāsa* adhikāra.  The classical anchor phrase is “from here up to 2.2.38,
compounding (samāsa) (is in scope).”

Per legacy span metadata, the scope runs through **2.2.38** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.1.3", "2.2.38")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.1.3",
        "scope_end" : "2.2.38",
        "text_dev"  : "प्राक् कडारात् समासः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.1.3",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "prAk kaDArAt samAsaH",
    text_dev        = "प्राक् कडारात् समासः",
    padaccheda_dev  = "प्राक् / कडारात् / समासः",
    why_dev         = "२.१.३ इत्यतः २.२.३८ पर्यन्तं 'समास' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.1.3", "2.2.38"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

