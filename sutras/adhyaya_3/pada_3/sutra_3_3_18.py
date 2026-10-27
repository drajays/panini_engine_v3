"""
3.3.18  भावे  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33018):** *bhāvādhikāraḥ* — scope
through **3.3.112** (आक्रोशे नञ्यनिः), matching v2
``adhikara_prakarana.json`` sequence **23**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return bhava_site(state, vivaksita(state, "artha", "BAva"))


def _open(state: State) -> bool:
    return not any(e.get("id") == "3.3.18" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return _open(state) or _site(state) is not None


def act(state: State) -> State:
    if _open(state):
        state.adhikara_stack.append({"id": "3.3.18", "scope_end": "3.3.112", "text_dev": "भावे"})
    if _site(state) is not None:
        return attach_krt(state, "GaY")
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.18",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "BAve",
    text_dev       = "भावे",
    samagra_slp1   = "pratyayaH paraSca AdyudAttaSca DAtoH BAve kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे कृत् घञ्",
    padaccheda_dev = "भावे",
    why_dev        = "भावाधिकारः — ३.३.१८ तः ३.३.११२ पर्यन्तम्।",
    anuvritti_from = (),
    also_vidhi     = True,          # the adhikāra is also the vidhi (ghañ ← 3.3.16; ktin)
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.18", "3.3.112"),
)

register_sutra(SUTRA)

