"""
2.1.40  सप्तमी शौण्डैः  —  VIDHI

Padaccheda: सप्तमी शौण्डैः

saunda etc. with saptami forms tatpurusha compound.
Pāṭha: ashtadhyayi.com data.txt row i=21040 (Art. 14).
Kāśikā: सप्तम्यन्तं शौण्डादिभिः सह समस्यते, तत्पुरुषश्च समासो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.samasa_attach import pair, run, mark, name
_SAUNDADI = frozenset({"SORqa", "DUrta", "kitava", "vyAqa", "pravIRa", "saMvIta", "antar", "aDi", "pawu", "aDipawu", "paRqita", "kuSala", "capala", "nipuRa"})   # Kāśikā's śauṇḍādi list

def _site(state: State):
    return pair(state, "2.1.40", vib="saptamI", uttara_names=_SAUNDADI)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return state
    return mark(state, list(s), "tatpurusha", "2.1.40")


SUTRA = SutraRecord(
    sutra_id              = "2.1.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamI SORqEH",
    text_dev              = "सप्तमी शौण्डैः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH saptamI SORqEH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः सप्तमी शौण्डैः",
    padaccheda_dev        = "सप्तमी शौण्डैः",
    why_dev               = "सप्तम्यन्तस्य शौण्ड-आदिभिः सह तत्पुरुषः (२.१.४०)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
