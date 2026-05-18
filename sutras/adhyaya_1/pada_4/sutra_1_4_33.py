"""
1.4.33  रुच्यर्थानां प्रीयमाणः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake rucyarthānāṃ prīyamāṇaḥ (sampradānam)* —
**1.4.23** *kārake*; **1.4.32** *sampradānam* (anuvṛtti).

*Śāstra:* For roots meaning "to please / to like" (ruc, etc.), the entity
who is pleased (prīyamāṇa) receives the *sampradāna* saṃjñā.
Example: *bālāya modakā rocate* — the child (bāla) is the prīyamāṇa/sampradāna.

*Engine:* A Term carrying ``"prIyamANa_ruci"`` (pipeline-set) gets tag
``"sampradAna"``.  ``cond`` reads only structural semantic tags
(CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_33_sampradAna_ruci"
META_DONE  = "1_4_33_done"

_TRIGGER: frozenset[str] = frozenset({"prIyamANa_ruci"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.33", state, "1.4.23"):
        return False
    for t in state.terms:
        if META_DONE in t.meta:
            continue
        if _TRIGGER & t.tags:
            return True
    return False


def act(state: State) -> State:
    for t in state.terms:
        if META_DONE in t.meta:
            continue
        if _TRIGGER & t.tags:
            t.tags.add("sampradAna")
            t.meta[META_DONE] = True
    state.samjna_registry[SAMJNA_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.4.33",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "rucyarTAnAM prIyamARaH",
    text_dev              = "रुच्यर्थानां प्रीयमाणः",
    padaccheda_dev        = "रुचि-अर्थानाम् / प्रीयमाणः",
    why_dev               = (
        "रुच्यर्थ-धातूनां प्रयोगे यः प्रीयमाणः (यस्य रोचते) स सम्प्रदान-कारक-संज्ञकः — "
        "यथा 'बालाय मोदकाः रोचन्ते' इत्यत्र बालः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.32"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
