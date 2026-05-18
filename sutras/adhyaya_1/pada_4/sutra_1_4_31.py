"""
1.4.31  भुवः प्रभवः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake bhuvaḥ prabhavaḥ (apādānam)* —
**1.4.23** *kārake*; **1.4.24** *apādānam* (anuvṛtti).

*Śāstra:* For the root *bhū* (to become / to originate), the *prabhava*
(source of origin) receives the *apādāna* saṃjñā.
Example: *himavataḥ gaṅgā prabhavati* — Himavat is the prabhava/apādāna.

*Engine:* A Term carrying ``"praBava_bhu"`` (pipeline-set) gets tag ``"apAdAna"``.
``cond`` reads only structural semantic tags (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_31_apAdAna_bhu"
META_DONE  = "1_4_31_done"

_TRIGGER: frozenset[str] = frozenset({"praBava_bhu"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.31", state, "1.4.23"):
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
    sutra_id              = "1.4.31",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "BuvaH praBavaH",
    text_dev              = "भुवः प्रभवः",
    padaccheda_dev        = "भुवः / प्रभवः",
    why_dev               = (
        "भू-धातोः प्रसङ्गे यः प्रभवः (उद्गम-स्थानम्) स अपादान-कारक-संज्ञकः — "
        "यथा 'हिमवतः गङ्गा प्रभवति' इत्यत्र हिमवत्।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.24"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
