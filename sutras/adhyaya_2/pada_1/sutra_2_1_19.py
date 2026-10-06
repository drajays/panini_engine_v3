"""
2.1.19  संख्या वंश्येन  (saṃkhyā vaṃśyena)  —  VIDHI

**Pāṭha:** A *saṃkhyā* (numeral) word combines with a *vaṃśya*
(lineage/dynasty) word to form an avyayībhāva samāsa.

Example: *pañca vaṃśyena* → *pañcavaṃśyam* ("in respect of five of the
lineage").

v3 narrow slice: gate-marks the compound with key
``2_1_19_sankhya_vamshya``.
Pāṭha: ashtadhyayi.com data.txt row i=21019 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_19_sankhya_vamshya"

_SANKHYA_TAGS: frozenset[str] = frozenset({"sankhya", "samkhya"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    has_sankhya = any(_SANKHYA_TAGS & t.tags for t in state.terms)
    has_vamshya = any("vaMSya" in (t.meta.get("upadesha_slp1") or "") or
                      "vamshya" in t.tags for t in state.terms)
    return has_sankhya and has_vamshya


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyA vaMSyena",
    text_dev              = "संख्या वंश्येन",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA avyayIBAvaH saMKyA vaMSyena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा अव्ययीभावः संख्या वंश्येन",
    padaccheda_dev        = "संख्या / वंश्येन",
    why_dev               = "संख्यावाचिशब्दस्य वंश्यशब्देन सह अव्ययीभावः (२.१.१९)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
