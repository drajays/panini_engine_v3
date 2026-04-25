"""
4.3.53  तत्र भवः  —  SAMJNA (*taddhita* licence: *saptamī* + *bhava* ‘there’)

**Pāṭha (baked *anuvṛtti*):** after **4.1.82** *samarthānām prathamād vā*, **4.1.83**
*prāg dīvyataḥ aṇ*, carrying **3.1.1–3.1.3**, **4.1.1**, **4.1.76** — a *taddhita*
*pratyaya* is taught after a *saptamī-samartha* *ṅyāp-prātipadika* in the
meaning *bhava* here: **existence** / ‘who stays there’ (*Kāśikā:* *sattā
bhavaty arthaḥ*, not *janma*, which belongs under **4.3.25** *tatra jātaḥ*).
Repetition of *tatra* stops *anuvṛtti* of *tadasya*; *kālāt* *anuvṛtti* ceases
(*Kāśikā:* *kālād iti nivṛttam*).

*Prayoga (śāstra):* *srughne bhavaḥ* → *sraughṇaḥ*; *māthuram*, *rāṣṭriyaḥ*, …

*Engine:* sets ``samjna_registry[SAMJNA_KEY]``.  Caller sets
``META_ELIGIBLE`` when analysis is *saptamī* + *bhava* (residence), and must
clear **``META_JATI_BLOCK``** (or leave it unset) so **4.3.25** *jāti* sense
does not claim the context.  **4.1.83** *adhikāra* must be in effect.
``cond`` does not read paradigm coordinates (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

SAMJNA_KEY = "4.3.53_tatra_bhava_taddhita"
META_ELIGIBLE = "4_3_53_tatra_bhava_eligible"
META_JATI_BLOCK = "4_3_25_tatra_jAta_sense"


def cond(state: State) -> bool:
    if not adhikara_in_effect("4.3.53", state, "4.1.83"):
        return False
    if state.meta.get(META_JATI_BLOCK):
        return False
    if not state.meta.get(META_ELIGIBLE):
        return False
    return state.samjna_registry.get(SAMJNA_KEY) is not True


def act(state: State) -> State:
    state.samjna_registry[SAMJNA_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.3.53",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = (
        "samarthAnAm prathamAt NyAp prAtipadikAt paraH AdyudAttaH "
        "taddhitaH vA prAg dIvyataH aR saptamyArTAt tatra bhavaH"
    ),
    text_dev       = (
        "समर्थानां प्रथमात् ङ्याप्प्रातिपदिकात् परः आद्युदात्तस्तद्धितो वा "
        "प्राग्दीव्यतोऽण् सप्तम्यर्थात् तत्र भवः"
    ),
    padaccheda_dev = "तत्र (अव्ययम्) / भवः (प्रथमा-एकवचनम्)",
    why_dev        = (
        "सप्तमीसमर्थाद् ङ्याप्प्रातिपदिकाद् भवार्थे (सत्तायाम्, न जन्मनि) "
        "तद्धित-प्रत्ययः — कालाद्-अनुवृत्ति-निवृत्तिः, तत्र-पुनर्ग्रहणं "
        "तदस्य-निवृत्त्यर्थम्; जन्मार्थे ४.३.२५ इति भेदः।"
    ),
    anuvritti_from = (
        "3.1.1",
        "3.1.2",
        "3.1.3",
        "4.1.1",
        "4.1.76",
        "4.1.82",
        "4.1.83",
    ),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
