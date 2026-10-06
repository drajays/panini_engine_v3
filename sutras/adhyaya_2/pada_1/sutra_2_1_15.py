"""
2.1.15  अनुर्यत्समया  —  VIDHI

**Pāṭha:** The avyaya *anu* combines with a subanta to form an
avyayībhāva samāsa when the sense is *samaya* (along with / following).

Example: *vṛkṣam anu* → *anuvṛkṣam* ("along the tree").

v3 narrow slice: gate-marks the compound with key
``2_1_15_anu_samaya``.
Pāṭha: ashtadhyayi.com data.txt row i=21015 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_15_anu_samaya"

_ANU_TAGS: frozenset[str] = frozenset({"avyaya", "nipata"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") == "anu" and _ANU_TAGS & t.tags:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'anuryatsamayA',
    text_dev              = 'अनुर्यत्समया',
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA avyayIBAvaH anuH yatsamayA lakzaRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा अव्ययीभावः अनुः यत्समया लक्षणेन",
    padaccheda_dev        = "अनुः / यत् / समया",
    why_dev               = "अनु-अव्यय-पूर्वकः समयार्थे अव्ययीभावः (२.१.१५)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
