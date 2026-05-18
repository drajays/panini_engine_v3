"""
1.4.51  अकथितं च  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake akathitaṃ ca karma* —
**1.4.23** *kārake*; *ca* extends 1.4.49–50.

*Śāstra (laghu):* What is implied but not explicitly stated (akathita) by a
two-object verb still gets the saṃjñā *karman* (the "second" object of dvi-karma
verbs). E.g. *gāṃ doghti payaḥ* — gāṃ is akathita karman; *nī, vah, hṛ*, etc.

*Engine:* tags bearing ``"akaTita_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_51_karaka_done"
_TRIGGER    = frozenset({"akaTita_karma"})
_SAMJNA     = "karman"


def cond(state: State) -> bool:
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            return True
    return False


def act(state: State) -> State:
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            t.tags.add(_SAMJNA)
            t.meta[META_DONE] = True
    state.samjna_registry["1_4_51_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.51",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "akaTitaM ca",
    text_dev             = "अकथितं च — karman",
    padaccheda_dev       = "अकथितम् / च",
    why_dev              = (
        "अकथितम् (द्विकर्मक-धातोः अनभिधेयं यत् कारकम्) तत् कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: akaTita_karma इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.49"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
