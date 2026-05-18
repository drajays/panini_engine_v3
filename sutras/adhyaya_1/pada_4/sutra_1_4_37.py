"""
1.4.37  क्रुधद्रुहेर्ष्याऽसूयार्थानां यं प्रति कोपः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake kruddha-druha-irṣyā-asūyā-arthānāṃ
yaṃ prati kopaḥ sampradānam* — **1.4.23** *kārake*; **1.4.32** *sampradānam*.

*Śāstra (laghu):* For verbs meaning anger/envy (krudh, druh, irṣy, asūy),
the entity *toward which* the anger is directed receives the saṃjñā
*sampradāna*.  E.g. *devadattāya krudhyati*.

*Engine:* tags bearing ``"kruDa_kopaprApta"`` get ``"sampradAna"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_37_karaka_done"
_TRIGGER    = frozenset({"kruDa_kopaprApta"})
_SAMJNA     = "sampradAna"


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
    state.samjna_registry["1_4_37_sampradAna"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.37",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "kruDadruhersyA asUyArTAnAM yaM prati kopaH",
    text_dev             = "क्रुधद्रुहेर्ष्याऽसूयार्थानां यं प्रति कोपः — sampradāna",
    padaccheda_dev       = "क्रुध-द्रुह-ईर्ष्या-असूया-अर्थानाम् / यम् / प्रति / कोपः",
    why_dev              = (
        "क्रुध्-द्रुह्-ईर्ष्या-असूया-अर्थक-धातूनां यस्मिन् कोपः स सम्प्रदान-संज्ञकः। "
        "चिह्नम्: kruDa_kopaprApta इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.32"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
