"""
1.4.34  श्लाघह्नुङ्स्थाशपां ज्ञीप्स्यमानः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake ślāgha-hnu-sthā-śapāṃ jñīpsyamānaḥ (sampradānam)* —
**1.4.23** *kārake*; **1.4.32** *sampradānam* (anuvṛtti).

*Śāstra:* For the roots ślāgh (to boast / praise), hnu (to conceal), sthā (to
stand / relate to), śap (to curse), the entity who desires to know
(jñīpsyamāna — the intended witness/addressee) receives the *sampradāna* saṃjñā.
Example: *gurave ślāghate* — the guru is the jñīpsyamāna/sampradāna.

*Engine:* A Term carrying ``"jYIpsya_slAga"`` (pipeline-set) gets tag
``"sampradAna"``.  ``cond`` reads only structural semantic tags
(CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_34_sampradAna_slAga"
META_DONE  = "1_4_34_done"

_TRIGGER: frozenset[str] = frozenset({"jYIpsya_slAga"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.34", state, "1.4.23"):
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
    sutra_id              = "1.4.34",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "SlAgahnuNsTASapAM jYIpsyamAnaH",
    text_dev              = "श्लाघह्नुङ्स्थाशपां ज्ञीप्स्यमानः",
    padaccheda_dev        = "श्लाघ-ह्नुङ्-स्था-शपाम् / ज्ञीप्स्यमानः",
    why_dev               = (
        "श्लाघ-ह्नु-स्था-शप्-धातूनां प्रयोगे यो ज्ञीप्स्यमानः (यस्मै ज्ञापयितुम् "
        "इच्छति) स सम्प्रदान-कारक-संज्ञकः — यथा 'गुरवे श्लाघते' इत्यत्र गुरुः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.32"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
