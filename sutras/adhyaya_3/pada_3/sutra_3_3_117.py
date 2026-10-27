"""
3.3.117  करणाधिकरणयोश्च  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33117):** *karaṇādhikaraṇayoḥ*
adhikāra — scope through **3.3.125** (खनो घ च), matching v2
``adhikara_prakarana.json`` sequence **26**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    if state.vivaksha.get("krt"):
        return None         # the speaker asked for a named kṛt family (kṛtya 3.1.95, ṇvul-tṛc 3.1.133): lyuṭ is not what was meant
    return bhava_site(state, vivaksita(state, "artha", "karaRa")) or bhava_site(state, vivaksita(state, "artha", "aDikaraRa"))


def _open(state: State) -> bool:
    return not any(e.get("id") == "3.3.117" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return _open(state) or _site(state) is not None


def act(state: State) -> State:
    if _open(state):
        state.adhikara_stack.append({"id": "3.3.117", "scope_end": "3.3.125", "text_dev": "करणाधिकरणयोश्च"})
    if _site(state) is not None:
        return attach_krt(state, "lyuw")
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.117",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'karaRADikaraRayoSca',
    text_dev       = 'करणाधिकरणयोश्च',
    samagra_slp1   = "pratyayaH paraSca AdyudAttaSca DAtoH karaRADikaraRayoH karaRa-aDikaraRayoH ca kft lyuw",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "प्रत्ययः परश्च आद्युदात्तश्च धातोः करणाधिकरणयोः करण-अधिकरणयोः च कृत् ल्युट्",
    padaccheda_dev = "करण-अधिकरणयोः / च",
    why_dev        = "करणाधिकरणयोः इत्यधिकारः — ३.३.११७ तः ३.३.१२५ पर्यन्तम्।",
    anuvritti_from = (),
    also_vidhi     = True,          # the adhikāra is also the vidhi: lyuṭ in karaṇa / adhikaraṇa
    apavada_of     = ("3.3.18",),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.117", "3.3.125"),
)

register_sutra(SUTRA)

