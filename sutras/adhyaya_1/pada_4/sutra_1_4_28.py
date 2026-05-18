"""
1.4.28  अन्तर्द्धौ येनादर्शनमिच्छति  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake antardhau yenādarśanam icchati (apādānam)* —
**1.4.23** *kārake*; **1.4.24** *apādānam* (anuvṛtti).

*Śāstra:* In contexts of disappearance (antardhāna), the entity from whom
one wishes to become invisible (the "hider-from" — yena adarśanam icchati)
receives the *apādāna* saṃjñā.
Example: *devadattāt antardhīyate* — Devadatta is the apādāna (one hides from him).

*Engine:* A Term carrying ``"antardDau_hider"`` (pipeline-set) gets tag ``"apAdAna"``.
``cond`` reads only structural semantic tags (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_28_apAdAna_antarDau"
META_DONE  = "1_4_28_done"

_TRIGGER: frozenset[str] = frozenset({"antardDau_hider"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.28", state, "1.4.23"):
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
            t.tags.add("apAdAna")
            t.meta[META_DONE] = True
    state.samjna_registry[SAMJNA_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.4.28",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "antarDAu yenAdarSanam icCati",
    text_dev              = "अन्तर्द्धौ येनादर्शनमिच्छति",
    padaccheda_dev        = "अन्तर्द्धौ / येन / अदर्शनम् / इच्छति",
    why_dev               = (
        "अन्तर्धान-प्रसङ्गे येन सकाशाद् अदर्शनम् इच्छति स "
        "अपादान-कारक-संज्ञकः — यथा 'देवदत्तादन्तर्धीयते' इत्यत्र देवदत्तः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.24"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
