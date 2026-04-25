"""
4.2.71  ओरञ्  —  SAMJNA (*o* + *aṇ* licence under **4.1.82**)

**Pāṭha (baked):** *samarthānām prathamāt ṅyāp-prātipadikāt paraḥ ādyudāttaḥ
taddhitaḥ vā prāg dīvyataḥ aṇ śeṣe oḥ aṇ* — *aṇ* after an *o*-final base in the
*śeṣa* block (**4.2.92** … **4.3.134** in the śāstra); *anuvṛtti* from **4.2.92**
is not re-opened here — **4.1.82** *samarthādhikāra* is the engine’s scope gate
for this file (so **4.2.71** < **4.2.92** in the Aṣṭādhyāyī order still parses).

**Engine:** one-shot audit in ``samjna_registry`` — ``True`` iff the first
*prātipadika* ``Term``’s last phoneme is SLP1 ``o`` (so *aṇ* from *o* is live);
``False`` for bases like *śālā* (ā-anta), without reading *vibhakti* (Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

SAMJNA_KEY = "4.2.71_or_aR_applicable"


def cond(state: State) -> bool:
    if not adhikara_in_effect("4.2.71", state, "4.1.82"):
        return False
    if state.samjna_registry.get(SAMJNA_KEY) is not None:
        return False
    # *O*rantād eva *ora*-*aR*; आकारादौ (शाला) *prayoga* न — COND-FALSE, no vacuous
    # registry row (display as SKIPPED in *trace* when recipe schedules audit).
    if state.terms and state.terms[0].varnas and state.terms[0].kind == "prakriti":
        if state.terms[0].varnas[-1].slp1 != "o":
            return False
    return True


def act(state: State) -> State:
    applicable = False
    if state.terms and state.terms[0].kind == "prakriti":
        t0 = state.terms[0]
        if t0.varnas and t0.varnas[-1].slp1 == "o":
            applicable = True
    state.samjna_registry[SAMJNA_KEY] = applicable
    return state


SUTRA = SutraRecord(
    sutra_id        = "4.2.71",
    sutra_type      = SutraType.SAMJNA,
    text_slp1       = (
        "samarthAnAm prathamAt NyAp prAtipadikAt paraH AdyudAttaH "
        "taddhitaH vA prAg dIvyataH aR Seze oH aR"
    ),
    text_dev        = (
        "समर्थानां प्रथमात् ङ्याप्प्रातिपदिकात् परः आद्युदात्तस्तद्धितो वा "
        "प्राग्दीव्यतोऽण् शेषे ओरञ्"
    ),
    padaccheda_dev  = "ओः (षष्ठी-एकवचनम्) / अञ् (प्रथमा-एकवचनम्)",
    why_dev         = (
        "ओकारान्ताद् अण्-प्रत्ययः शेषार्थे; आकारान्ते (शाला) अत्र न प्रवृत्तिः — "
        "संज्ञा-निर्णयः मात्रम्।"
    ),
    anuvritti_from  = ("4.1.82", "4.1.83", "4.2.92"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)
