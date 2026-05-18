"""
1.4.26  पराजेरसोढः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake parājeh asoḍhaḥ (apādānam)* —
**1.4.23** *kārake*; **1.4.24** *apādānam* (anuvṛtti).

*Śāstra:* For the verb *parāji* (to defeat / be defeated), the entity that
cannot endure (asoḍha — the one who is overcome) receives the *apādāna* saṃjñā.
Example: *devadattāt parājayate* — Devadatta is the asoḍha/apādāna.

*Engine:* A Term carrying ``"asoDya_parAji"`` (pipeline-set) gets tag ``"apAdAna"``.
``cond`` reads only structural semantic tags (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_26_apAdAna_parAji"
META_DONE  = "1_4_26_done"

_TRIGGER: frozenset[str] = frozenset({"asoDya_parAji"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.26", state, "1.4.23"):
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
    sutra_id              = "1.4.26",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "parAjeH asoDaH",
    text_dev              = "पराजेरसोढः",
    padaccheda_dev        = "पराजेः / असोढः",
    why_dev               = (
        "परा-जि-धातोः प्रयोगे योऽसोढः (यं पराजयते) स अपादान-कारक-संज्ञकः — "
        "यथा 'देवदत्तात् पराजयते' इत्यत्र देवदत्तः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.24"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
