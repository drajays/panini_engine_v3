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
Pāṭha: ashtadhyayi.com data.txt row i=42092 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import frame_open, stem_ends_tape
from engine.vivaksha import vivaksita


def _open(state: State) -> bool:
    return not any(e.get("id") == "4.2.92" for e in state.adhikara_stack)


def _framed(state: State) -> bool:
    return stem_ends_tape(state) and vivaksita(state, "taddhitArtha", "Seza") and not frame_open(state, "Seza")


def cond(state: State) -> bool:
    return _open(state)


def act(state: State) -> State:
    if _open(state):
        entry = {"id": "4.2.92", "scope_end": "4.3.168", "text_dev": "Seza"}
        if _framed(state):
            entry["artha"] = "Seza"      # aṇ comes from 4.1.83 under the frame
        state.adhikara_stack.append(entry)
    return state


SUTRA = SutraRecord(
    sutra_id        = "4.2.92",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = (
        'Seze'
    ),
    text_dev        = (
        'शेषे'
    ),
    samagra_slp1    = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA Seze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev     = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा शेषे",
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
    also_vidhi     = True,          # the sense-frame is opened by the loop: the speaker's taddhitArtha
    cond            = cond,
    act             = act,
    adhikara_scope  = ("4.2.92", "4.3.134"),
)

register_sutra(SUTRA)
