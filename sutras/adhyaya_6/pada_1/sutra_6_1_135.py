"""
6.1.135  सुट् कात् पूर्वः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61135):** *suṭ kāt pūrvaḥ* —
*sūṭkātpūrva ityadhikāraḥ* (scope through **6.1.154**
मस्करमस्करिणौ वेणुपरिव्राजकयोः).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.1.135" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.1.135",
        "scope_end" : "6.1.154",
        "text_dev"  : "सुट् कात् पूर्वः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.135",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "suT kAt pUrvaH",
    text_dev       = "सुट् कात् पूर्वः",
    padaccheda_dev = "सुट् / कात् / पूर्वः",
    why_dev        = "सूट्कात्पूर्व इत्यधिकारः — ६.१.१३५ तः ६.१.१५४ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.1.135", "6.1.154"),
)

register_sutra(SUTRA)

