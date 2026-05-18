"""
1.4.30  जनिकर्तुः प्रकृतिः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake janikartuḥ prakṛtiḥ (apādānam)* —
**1.4.23** *kārake*; **1.4.24** *apādānam* (anuvṛtti).

*Śāstra:* For the root *jan* (to be born / to originate), the *prakṛti*
(original material cause / source) of the agent of birth (jani-kartṛ)
receives the *apādāna* saṃjñā.
Example: *mṛttikāyāḥ ghaṭo jāyate* — mṛttikā (clay) is the prakṛti/apādāna.

*Engine:* A Term carrying ``"jani_prakrti"`` (pipeline-set) gets tag ``"apAdAna"``.
``cond`` reads only structural semantic tags (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_30_apAdAna_jani"
META_DONE  = "1_4_30_done"

_TRIGGER: frozenset[str] = frozenset({"jani_prakrti"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.30", state, "1.4.23"):
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
    sutra_id              = "1.4.30",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "janikartuH prakftiH",
    text_dev              = "जनिकर्तुः प्रकृतिः",
    padaccheda_dev        = "जनि-कर्तुः / प्रकृतिः",
    why_dev               = (
        "जनि-धातोः कर्तुः या प्रकृतिः (उपादान-कारणम्) सा अपादान-कारक-संज्ञका — "
        "यथा 'मृत्तिकायाः घटो जायते' इत्यत्र मृत्तिका।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.24"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
