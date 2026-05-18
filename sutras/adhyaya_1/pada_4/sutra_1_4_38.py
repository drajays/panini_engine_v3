"""
1.4.38  क्रुधद्रुहोरुपसृष्टयोः कर्म  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake kruddha-druhayor upasṛṣṭayoḥ karma* —
**1.4.23** *kārake*.

*Śāstra (laghu):* When krudh or druh are used with an *upasarga* (verbal prefix),
the target of anger becomes *karman* (not sampradāna as in 1.4.37).
E.g. *devadattam abhikrudhyati*.

*Engine:* tags bearing ``"kruDa_druha_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_38_karaka_done"
_TRIGGER    = frozenset({"kruDa_druha_karma"})
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
    state.samjna_registry["1_4_38_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.38",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "kruDadruhOrupasṛṣṭayoḥ karma",
    text_dev             = "क्रुधद्रुहोरुपसृष्टयोः कर्म",
    padaccheda_dev       = "क्रुध-द्रुहोः / उपसृष्टयोः / कर्म",
    why_dev              = (
        "क्रुध्-द्रुह्-धात्वोः उपसर्गसहितयोः यत् कर्म तत् कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: kruDa_druha_karma इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
