"""
4.1.82  समर्थानां प्रथमाद्वा  —  ADHIKARA (*samarthādhikāraḥ*)

**Pāṭha (full *anuvṛtti* baked, *Kāśikā* order of *pada*s):**
*samarthānām prathamāt ṅyāp-prātipadikāt paraḥ ādyudāttaḥ taddhitaḥ vā*.

**Adhikāra:** within the *taddhita* domain (**4.1.76**), after **4.1.1**
*ṅyāp-prātipadikāt*, carrying **3.1.1** *pratyayaḥ*, **3.1.2** *paraḥ*, **3.1.3**
*ādyudāttaḥ* — the *taddhita* affix taught in an *artha-jñāpaka* rule is
**optionally** (*vā*) placed after the *pada* denoted by the **first**
(*prathama*) *samartha* among the mutually meaningful words in that rule’s
reading (not by surface *prayoga* order).  *Mahābhāṣya:* *arthābhidhāne yat
samartham*; *taddhita* applies to *samartha-bahu* after *saṃdhi-kārya*, not to
a bare *prātipadika* alone.

Scope through **5.2.140** (*ahaṃ-śubhamor-yus*), matching v2
``adhikara_prakarana.json`` sequence **33**.  After **5.2.140**, *vā* alone
continues (*Kāśikā*); *samarthānām prathamāt* do not.

*Kāśikā:* *pūrvasūtrād anyatarasyāṃ grahaṇam anuvartate* (**4.1.81**) — when
*samāsa* is possible, *taddhita*, *samāsa*, or neither may obtain (*upagor
apatyam* / *upagvapatyam* / *aupagavaḥ*).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.82" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.1.82",
        "scope_end" : "5.2.140",
        "text_dev"  : "समर्थानां प्रथमाद्वा",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "4.1.82",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = (
        "samarthAnAm prathamAt NyAp prAtipadikAt paraH "
        "AdyudAttaH taddhitaH vA"
    ),
    text_dev        = (
        "समर्थानां प्रथमात् ङ्याप्प्रातिपदिकात् परः आद्युदात्तः तद्धितः वा"
    ),
    padaccheda_dev  = (
        "समर्थानाम् (षष्ठी-बहुवचनम्) / प्रथमात् (पञ्चमी-एकवचनम्) / "
        "ङ्याप्-प्रातिपदिकात् / परः / आद्युदात्तः / तद्धितः / वा (अव्ययम्)"
    ),
    why_dev         = (
        "अर्थज्ञापकसूत्रे समर्थेषु यः प्रथमः पदार्थः, तेन निर्दिष्टात् "
        "पदात् परः तद्धितः विकल्पेन (महाभाष्य-सामर्थ्यम्, कृतसंधिकार्यपरम्) — "
        "४.१.८२ तः ५.२.१४० पर्यन्तं समर्थाधिकारः; ४.१.८१ तः अन्यतरस्याम् अनुवृत्तिः।"
    ),
    anuvritti_from  = ("3.1.1", "3.1.2", "3.1.3", "4.1.1", "4.1.76"),
    cond            = cond,
    act             = act,
    adhikara_scope  = ("4.1.82", "5.2.140"),
)

register_sutra(SUTRA)
