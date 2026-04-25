"""
4.2.113  न द्व्यचः प्राच्यभरतेषु  —  SAMJNA

**Pāṭha:** *na dvyacaḥ prācyabharateṣu* — restriction on certain *taddhita*
teaching in *dvivacana* bases under *prācya* / *bharata* usage (śāstra detail:
see *Kāśikā* on this sūtra).

**Engine:** glass-box *prayoga* note for **śālīya**-style recipes — records once
that the *prācya-bharata* *dvyaca* block is **not** activated for the current
state (no *vibhakti* read — CONSTITUTION Art. 2).  R2: ``samjna_registry`` gains a
fresh entry.
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
    sutra_type      = SutraType.SAMJNA,
    text_slp1       = (
        "samarthAnAm prathamAt NyAp prAtipadikAt paraH AdyudAttaH "
        "taddhitaH vA prAg dIvyataH aR Seze na dvyacaH prAcya-bharatezu"
    ),
    text_dev        = (
        "समर्थानां प्रथमात् ङ्याप्प्रातिपदिकात् परः आद्युदात्तस्तद्धितो वा "
        "प्राग्दीव्यतोऽण् शेषे न द्व्यचः प्राच्यभरतेषु"
    ),
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
