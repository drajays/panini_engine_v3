"""
1.4.25  भीत्रार्थानां भयहेतुः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake bhītrārthānāṃ bhayahetuḥ (apādānam)* —
**1.4.23** *kārake*; **1.4.24** *apādānam* (anuvṛtti).

*Śāstra:* For roots meaning "to fear" (bhī, tras, etc.), the cause of fear
receives the *apādāna* saṃjñā.  Example: *siṃhād bibheti* — lion is the
bhayahetu and gets apādāna.

*Engine:* A Term carrying ``"Baya_hetu"`` (pipeline-set) gets tag ``"apAdAna"``.
``cond`` reads only structural semantic tags (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_25_apAdAna_Baya"
META_DONE  = "1_4_25_done"

_TRIGGER: frozenset[str] = frozenset({"Baya_hetu"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.25", state, "1.4.23"):
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
    sutra_id              = "1.4.25",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "BItrArTAnAM BayahetuH",
    text_dev              = "भीत्रार्थानां भयहेतुः",
    padaccheda_dev        = "भीत्रार्थानाम् / भयहेतुः",
    why_dev               = (
        "भीत्रादि-धातूनाम् अर्थे यो भयहेतुः स अपादान-कारक-संज्ञकः — "
        "यथा 'सिंहाद् बिभेति' इत्यत्र सिंहः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.24"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
