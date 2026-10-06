"""
2.2.11  पूरणगुणसुहितार्थसदव्ययतव्यसमानाधिकरणेन  —  SAMJNA

पदच्छेदः  पूरण-गुण-सुहित-अर्थ-सत्-अव्यय-तव्य-समान-अधिकरणेन

अनुवृत्तिः  षष्ठी 2.2.8

Kāśikā summary: the *samāna-adhikaraṇa* (same-locus/coreferential) compound
is a *karmadhāraya* when the prior member is one of: a *pūraṇa* (ordinal
in -ama, -tha), *guṇa* (quality word), *suhita-artha* (well-being word),
*sat* (the participle), *avyaya* (indeclinable), *tavya* (gerundive), or a
*samāna-adhikaraṇa* element.  This sūtra names the *karmadhāraya* saṃjñā for
such compounds.  Examples: *paṭu-brāhmaṇaḥ* (the clever Brahmin),
*priya-sakhaḥ* (dear friend).

Engine (narrow, mechanically blind):
  Gate key ``2_2_11_karmadharaya_gate``.  Recipe arms
  ``state.meta['2_2_11_arm']`` and tags a Term with ``karmadharaya_context``
  indicating one of the listed categories.  Registry stamp records the
  karmadhāraya saṃjñā.
Pāṭha: ashtadhyayi.com data.txt row i=22011 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_KD_TAGS = frozenset({
    "purana_ordinal", "guna_word", "suhita_artha", "sat_participle",
    "avyaya", "tavya_gerundive", "karmadharaya_context",
})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_11_karmadharaya_gate") is True:
        return False
    return any(not _KD_TAGS.isdisjoint(t.tags) for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates["2_2_11_karmadharaya_gate"] = True
    state.samjna_registry["2_2_11_karmadharaya"] = True
    state.samjna_registry["karmadharaya"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.11",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1=(
        'pUraRaguRasuhitArTasadavyayatavyasamAnADikaraRena'
    ),
    text_dev='पूरणगुणसुहितार्थसदव्ययतव्यसमानाधिकरणेन',
    samagra_slp1="AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH pUraRa-guRa-suhitArTa-sadavyaya-tavya-samAnADikaraRena zazWI na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः पूरण-गुण-सुहितार्थ-सदव्यय-तव्य-समानाधिकरणेन षष्ठी न",
    padaccheda_dev=(
        "पूरण-गुण-सुहित-अर्थ-सत्-अव्यय-तव्य-समान-अधिकरणेन"
    ),
    why_dev=(
        "पूरणादिभिः समानाधिकरणेन कर्मधारयसंज्ञा — पटुब्राह्मणः, प्रियसखः इत्यादि।"
    ),
    anuvritti_from=("2.2.8",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
