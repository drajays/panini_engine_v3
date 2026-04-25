"""
4.2.92  शेषे  —  ADHIKARA (*śeṣādhikāraḥ*)

**Pāṭha (baked *anuvṛtti*):** *samarthānām prathamāt ṅyāp-prātipadikāt paraḥ
ādyudāttaḥ taddhitaḥ vā prāg dīvyataḥ aṇ śeṣe*.

**Śāstra (laghu):** from here, *taddhita* affixes taught (*gha* &c.) take
**remaining** senses (*śeṣa*) — i.e. other than the block from *apatyādi*
(**4.1.92** …) through the *catur-artha* cluster already assigned; they still
participate in the broader *jāta* / *prokta* / *āgata* / *nivāsa* / *kṛta* …
sense families (**4.3.25**, **101**, **74**, **89**, **38**, …).  *Kāśikā:*
*śeṣa ity adhikāro 'yam*; *upayuktād anyaḥ śeṣaḥ*.

**Scope:** **4.2.92** through **4.3.134** (inclusive), per *Kāśikā* / Vasu on
*śeṣe* as *lakṣaṇa* + *adhikāra*.

*Examples (illustrative):* *cākṣuṣam*, *śrāvaṇaḥ*, *daṛṣadaḥ* → *dārṣadaḥ*,
*aulūkhalaḥ*, *āśvaḥ*, *cāturam*, *cāturdśam*, …
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.2.92" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.2.92",
        "scope_end" : "4.3.134",
        "text_dev"  : "शेषे",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "4.2.92",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = (
        "samarthAnAm prathamAt NyAp prAtipadikAt paraH AdyudAttaH "
        "taddhitaH vA prAg dIvyataH aR Seze"
    ),
    text_dev        = (
        "समर्थानां प्रथमात् ङ्याप्प्रातिपदिकात् परः आद्युदात्तस्तद्धितो वा "
        "प्राग्दीव्यतोऽण् शेषे"
    ),
    padaccheda_dev  = "शेषे (सप्तमी-एकवचनम्)",
    why_dev         = (
        "अपत्यादि-चतुरर्थ-पर्यन्तेभ्यो व्यतिरिक्तेऽर्थे तद्धिताः — "
        "शेषाधिकारः ४.२.९२ तः ४.३.१३४ पर्यन्तम्; जातादिषु तु साकल्यम्।"
    ),
    anuvritti_from  = (
        "3.1.1",
        "3.1.2",
        "3.1.3",
        "4.1.1",
        "4.1.76",
        "4.1.82",
        "4.1.83",
    ),
    cond            = cond,
    act             = act,
    adhikara_scope  = ("4.2.92", "4.3.134"),
)

register_sutra(SUTRA)
