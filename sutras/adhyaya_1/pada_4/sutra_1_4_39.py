"""
1.4.39  राधीक्ष्योर्यस्य विप्रश्नः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake rādh-īkṣ-yoḥ yasya vipraśnaḥ karma* —
**1.4.23** *kārake*.

*Śāstra (laghu):* For verbs rādh (to accomplish/satisfy) and īkṣ (to look/inquire),
the object of inquiry or satisfaction receives the saṃjñā *karman*.
E.g. *devadattam rādhyati* (he satisfies Devadatta).

*Engine:* tags bearing ``"rADA_viprazna"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_39_karaka_done"
_TRIGGER    = frozenset({"rADA_viprazna"})
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
    state.samjna_registry["1_4_39_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.39",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "rADIkSyor yasya vipraznaH",
    text_dev             = "राधीक्ष्योर्यस्य विप्रश्नः — karman",
    padaccheda_dev       = "राध-ईक्ष्योः / यस्य / विप्रश्नः",
    why_dev              = (
        "राध्-ईक्ष्-धात्वोः यस्य विप्रश्नः (जिज्ञासा/साधनम्) तत् कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: rADA_viprazna इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
