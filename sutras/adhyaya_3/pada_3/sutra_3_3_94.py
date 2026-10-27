"""
3.3.94  स्त्रियां क्तिन्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33094):** *strī-adhikāraḥ (prathamaḥ)*
— scope through **3.3.112** (आक्रोशे नञ्यनिः), matching v2
``adhikara_prakarana.json`` sequence **25**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return bhava_site(state, vivaksita(state, "artha", "BAva"), vivaksita(state, "linga", "strI"))


def _open(state: State) -> bool:
    return not any(e.get("id") == "3.3.94" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return _open(state) or _site(state) is not None


def act(state: State) -> State:
    if _open(state):
        state.adhikara_stack.append({"id": "3.3.94", "scope_end": "3.3.112", "text_dev": "स्त्रियां क्तिन्"})
    if _site(state) is not None:
        return attach_krt(state, "ktin")
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.94",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'striyAM ktin',
    text_dev       = 'स्त्रियां क्तिन्',
    samagra_slp1   = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm ktin kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् क्तिन् कृत्",
    padaccheda_dev = "स्त्रियाम् / क्तिन्",
    why_dev        = "स्त्र्यधिकारः (प्रथमः) — ३.३.९४ तः ३.३.११२ पर्यन्तम्।",
    anuvritti_from = (),
    also_vidhi     = True,          # the adhikāra is also the vidhi (ghañ ← 3.3.16; ktin)
    apavada_of     = ("3.3.18", "3.3.56", "3.3.57", "3.3.90"),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.94", "3.3.112"),
)

register_sutra(SUTRA)

