"""
2.4.19  तत्पुरुषोऽनञ् कर्मधारयः  (tatpuruṣo'nañ karmadhārayaḥ)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=24019):** opens the traditional
*tatpuruṣe napuṃsaka* adhikāra (span for certain napuṃsaka behaviour in
tatpuruṣa / karmadhāraya compounds).

Per legacy span metadata, the scope runs through **2.4.25** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.4.19", "2.4.25")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.4.19" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.4.19",
        "scope_end" : "2.4.25",
        "text_dev"  : "तत्पुरुषोऽनञ् कर्मधारयः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.4.19",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "tatpuruzo'naY karmadhArayaH",
    text_dev        = "तत्पुरुषोऽनञ् कर्मधारयः",
    padaccheda_dev  = "तत्पुरुषः / अ-नञ् / कर्मधारयः",
    why_dev         = "२.४.१९ इत्यतः २.४.२५ पर्यन्तं 'तत्पुरुषे नपुंसक' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.4.19", "2.4.25"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

