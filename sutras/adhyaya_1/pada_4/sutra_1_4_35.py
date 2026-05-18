"""
1.4.35  धारेरुत्तमर्णः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake dhāreḥ uttamarṇaḥ (sampradānam)* —
**1.4.23** *kārake*; **1.4.32** *sampradānam* (anuvṛtti).

*Śāstra:* For the root *dhṛ* (to owe / to hold a debt), the creditor
(uttamarṇa — the superior debtor, i.e. one to whom money is owed) receives
the *sampradāna* saṃjñā.
Example: *devadattāya śataṃ dhārayati* — Devadatta is the uttamarṇa/sampradāna
(the creditor to whom the hundred is owed).

*Engine:* A Term carrying ``"uttamarNa_DArI"`` (pipeline-set) gets tag
``"sampradAna"``.  ``cond`` reads only structural semantic tags
(CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_35_sampradAna_DAri"
META_DONE  = "1_4_35_done"

_TRIGGER: frozenset[str] = frozenset({"uttamarNa_DArI"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.35", state, "1.4.23"):
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
    sutra_id              = "1.4.35",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "DAreH uttamarRaH",
    text_dev              = "धारेरुत्तमर्णः",
    padaccheda_dev        = "धारेः / उत्तमर्णः",
    why_dev               = (
        "धारि-धातोः (ऋणे प्रयुक्तस्य) प्रसङ्गे उत्तमर्णः (ऋणदाता) "
        "सम्प्रदान-कारक-संज्ञकः — यथा 'देवदत्ताय शतं धारयति' इत्यत्र देवदत्तः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.32"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
