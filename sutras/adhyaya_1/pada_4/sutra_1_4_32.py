"""
1.4.32  कर्मणा यमभिप्रैति स सम्प्रदानम्  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake karmaṇā yam abhipraiti sa sampradānam* —
**1.4.23** *kārake*.

*Śāstra:* The entity whom the agent aims at through the action (the intended
beneficiary / recipient) receives the *sampradāna-kāraka* saṃjñā.
Example: *brāhmaṇāya dadāti* — the Brahmin is the sampradāna.

*Engine:* A Term carrying ``"sampradAna_recipient"`` (pipeline-set) gets tag
``"sampradAna"``.  ``cond`` reads only structural semantic tags
(CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_32_sampradAna"
META_DONE  = "1_4_32_done"

_TRIGGER: frozenset[str] = frozenset({"sampradAna_recipient"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.32", state, "1.4.23"):
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
    sutra_id              = "1.4.32",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "karmaRA yam aByaprEti sa sampradAnam",
    text_dev              = "कर्मणा यमभिप्रैति स सम्प्रदानम्",
    padaccheda_dev        = "कर्मणा / यम् / अभिप्रैति / सः / सम्प्रदानम्",
    why_dev               = (
        "कर्मणा यं पदार्थम् अभिप्रैति (अभिलक्षयति) कर्ता, स सम्प्रदान-कारक-संज्ञकः — "
        "यथा 'ब्राह्मणाय ददाति' इत्यत्र ब्राह्मणः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
