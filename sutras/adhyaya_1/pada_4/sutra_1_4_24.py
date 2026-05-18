"""
1.4.24  ध्रुवमपायेऽपादानम्  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake dhruvaṃ apāye apādānam* — **1.4.23** *kārake*.

*Śāstra:* The fixed point (dhruva) from which something departs (apāya) receives
the technical name *apādāna-kāraka*.  Examples: *grāmād āgacchati*, *vṛkṣāt
parṇaṃ patati*.

*Engine:* A Term carrying the pipeline-set tag ``"apadAna_source"`` receives the
kāraka tag ``"apAdAna"``.  ``cond`` reads only structural semantic tags —
no vibhakti / vacana / surface reads (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_24_apAdAna"
META_DONE  = "1_4_24_done"

# Source tag set by the pipeline to flag apādāna candidates.
_TRIGGER: frozenset[str] = frozenset({"apadAna_source"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.24", state, "1.4.23"):
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
    sutra_id              = "1.4.24",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "DruvamapAye apAdAnam",
    text_dev              = "ध्रुवमपायेऽपादानम्",
    padaccheda_dev        = "ध्रुवम् / अपाये / अपादानम्",
    why_dev               = (
        "यस्मादपाय: तद् ध्रुवम् अपादान-कारक-संज्ञकम् — यथा 'ग्रामादागच्छति' "
        "इत्यत्र ग्राम: अपादानम्।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
