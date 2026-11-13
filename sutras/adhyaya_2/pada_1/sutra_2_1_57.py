"""
2.1.57  विशेषणं विशेष्येण बहुलम्  —  VIDHI

Padaccheda: विशेषणम् विशेष्येण बहुलम्

Adjective with adjective (visesana+visesya) bahula karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=21057 (Art. 14).
Kāśikā: विशेषणवाचि सुबन्तं विशेष्यवाचिना समानाधिकरणेन सुबन्तेन सह बहुलं समस्यते, तत्पुरुषश्च समासो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.samasa_attach import pair, run, mark, name


def _site(state: State):
    return pair(state, "2.1.57", same_vib=True, purva=lambda t: "lex:viSezaRa" in t.tags)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return state
    return mark(state, list(s), "tatpurusha", "2.1.57")


SUTRA = SutraRecord(
    sutra_id              = "2.1.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viSezaRaM viSezyeRa bahulam",
    text_dev              = "विशेषणं विशेष्येण बहुलम्",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH viSezaRam viSezyeRa bahulam samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः विशेषणम् विशेष्येण बहुलम् समानाधिकरणेन",
    padaccheda_dev        = "विशेषणम् विशेष्येण बहुलम्",
    why_dev               = "विशेषणं विशेष्येण बहुलं कर्मधारयः (२.१.५७)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
