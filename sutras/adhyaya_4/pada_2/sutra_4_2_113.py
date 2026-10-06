"""
4.2.113  न द्व्यचः प्राच्यभरतेषु  —  SAMJNA

**Pāṭha:** *na dvyacaḥ prācyabharateṣu* — restriction on certain *taddhita*
teaching in *dvivacana* bases under *prācya* / *bharata* usage (śāstra detail:
see *Kāśikā* on this sūtra).

**Engine:** glass-box *prayoga* note for **śālīya**-style recipes — records once
that the *prācya-bharata* *dvyaca* block is **not** activated for the current
state (no *vibhakti* read — CONSTITUTION Art. 2).  R2: ``samjna_registry`` gains a
fresh entry.
Pāṭha: ashtadhyayi.com data.txt row i=42113 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

SAMJNA_KEY = "4.2.113_prAcya_bharata_dvyaca_note"


def cond(state: State) -> bool:
    if not adhikara_in_effect("4.2.113", state, "4.1.82"):
        return False
    if state.samjna_registry.get(SAMJNA_KEY) is not None:
        return False
    # Glass-box *prayoga* is for *dvyaca* / *prācyabhārata* tracks; *śālā* ākāra-anta
    # *taddhita* recipe does not activate this — *COND-FALSE* (SKIPPED) when flagged.
    if state.meta.get("prakriya_sAlIya"):
        return False
    return True


def act(state: State) -> State:
    state.samjna_registry[SAMJNA_KEY] = "not_activated"
    return state


SUTRA = SutraRecord(
    sutra_id        = "4.2.113",
    sutra_type      = SutraType.PRATISHEDHA,
    text_slp1       = (
        'na dvyacaH prAcyaBaratezu'
    ),
    text_dev        = (
        'न द्व्यचः प्राच्यभरतेषु'
    ),
    samagra_slp1    = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA na dvi-acaH prAcya-Baratezu aR gotre iYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev     = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा न द्वि-अचः प्राच्य-भरतेषु अण् गोत्रे इञः",
    padaccheda_dev  = "न / द्व्यचः / प्राच्यभरतेषु (सप्तमी-बहुवचनम्)",
    why_dev         = (
        "द्व्यचः-प्राच्यभरत-निषेधः अत्र प्रवृत्तो न — एकवचन-शाला-प्रक्रियायाम् "
        "अनुमानिकं चिह्नम्।"
    ),
    anuvritti_from  = ("4.1.82", "4.2.92"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)
