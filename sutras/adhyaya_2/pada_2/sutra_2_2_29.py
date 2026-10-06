"""
2.2.29  चार्थे द्वन्द्वः  —  SAMJNA (dvandva compound)

Engine scope (v3 glass-box):
  Fires when any Term carries the ``dvandva`` tag and the samāsa adhikāra (2.1.3)
  is open on ``adhikara_stack``. No arm flag needed.
Pāṭha: ashtadhyayi.com data.txt row i=22029 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _samasa_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    if not any("dvandva" in t.tags for t in state.terms):
        return False
    if not _samasa_adhikara_open(state):
        return False
    return not bool(state.samjna_registry.get("2.2.29_cArthe_dvandva"))


def act(state: State) -> State:
    state.samjna_registry["2.2.29_cArthe_dvandva"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.29",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'cArTe dvandvaH',
    text_dev       = 'चार्थे द्वन्द्वः',
    samagra_slp1   = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA ca-arTe dvandvaH anekam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा च-अर्थे द्वन्द्वः अनेकम्",
    padaccheda_dev = "च-अर्थे / द्वन्द्वः",
    why_dev        = "च-अर्थे द्वन्द्व-समास-संज्ञा (narrow stamp for P013).",
    anuvritti_from = ("2.1.3",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

