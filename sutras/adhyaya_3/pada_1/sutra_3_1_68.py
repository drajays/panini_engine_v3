"""
3.1.68  सार्वधातुके कर्तरि धातोः शप्  —  VIDHI

*Padaccheda:* *kartari* (saptamī), *śap* (prathamā); *sārvadhātake* **3.1.67** *anuvṛtti*.

*Anuvṛtti:* *pratyayaḥ* **3.1.1**; *paraś ca* **3.1.2**; *ādyudāttaś ca* **3.1.3**; *dhātoḥ* **3.1.91** *adhikāra*.

*Śāstra:* *śap* *vikaraṇa* between *dhātu* and a following *sārvadhātuka* affix in *kartari* (*it* **1.3.3**/**1.3.8**;
*lopa* **1.3.9**; *guṇa* **6.1.97** — separate rules).

*Engine:* inserts a ``Sap`` *pratyaya* ``Term`` immediately after the *dhātu* when ``vikarana_sap_3_1_68`` says so;
requires **3.1.91** on ``adhikara_stack`` (*dhātoḥ*) and *kartari* licence (**3.4.69** or recipe meta).
Does **not** implement *divādi*
*apavāda* (*śyan* etc.).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_3.pada_1.vikarana_sap_3_1_68 import (
    SAP_INSERT_TAG,
    find_sap_insertion_dhatu_index,
)


def cond(state: State) -> bool:
    return find_sap_insertion_dhatu_index(state) is not None


def act(state: State) -> State:
    i = find_sap_insertion_dhatu_index(state)
    assert i is not None
    sap = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sap"),
        tags={"pratyaya", "vikarana", "upadesha", SAP_INSERT_TAG},
        meta={"upadesha_slp1": "Sap"},
    )
    state.terms.insert(i + 1, sap)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.68",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = (
        "pratyayaH, para z ca, AdyudAttaz ca, DAtA — "
        "sArvadhAtuke kartrA DAtaH Sap"
    ),
    text_dev       = "सार्वधातुके कर्तरि धातोः शप् (३.१.६७, ३.१.९१-अधिकारे)",
    padaccheda_dev = "सार्वधातुके (३.१.६७) / कर्तरि / धातोः / शप्",
    why_dev        = (
        "कर्तरि सार्वधातुके परे विकरण-शप्-आगमः; अपवादाः ३.१.६९ इत्यादौ पृथक्।"
    ),
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.67", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
