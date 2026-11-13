"""
2.1.52  संख्यापूर्वो द्विगुः  —  VIDHI

Padaccheda: संख्या-पूर्वः द्विगुः

samkhya-purva (numeral-first) compound is called dvigu.
Pāṭha: ashtadhyayi.com data.txt row i=21052 (Art. 14).
Kāśikā: तद्धितार्थोत्तरपदसमाहारे चेत्यत्र यः संख्यापूर्वः समासः स द्विगुसंज्ञो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _members(state: State):
    """The members of a tatpuruṣa that a taddhitārtha-uttarapada-samāhāra vidhi (2.1.51) made, whose pūrvapada is a saṅkhyā."""
    if state.meta.get("samasa_vidhi") != "2.1.51" or "dvigu" in state.meta.get("samasa_kind", ""):
        return []
    ms = [t for t in state.terms if "samasa_member" in t.tags]
    return ms if ms and "lex:saNKyA" in ms[0].tags else []


def cond(state: State) -> bool:
    return bool(_members(state))


def act(state: State) -> State:
    for t in _members(state):
        t.tags |= {"dvigu", "lex:dvigu"}
    state.meta["samasa_kind"] = "tatpurusha dvigu"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyApUrvo dviguH",
    text_dev              = "संख्यापूर्वो द्विगुः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH saMKyA-pUrvaH dviguH samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः संख्या-पूर्वः द्विगुः समानाधिकरणेन",
    padaccheda_dev        = "संख्या-पूर्वः द्विगुः",
    why_dev               = "संख्या-पूर्वः द्विगुः समासः (२.१.५२)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
