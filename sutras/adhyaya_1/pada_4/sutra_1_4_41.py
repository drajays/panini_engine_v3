"""
1.4.41  अनुप्रतिगृणश्च  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake anu-prati-gṛṇaś ca sampradānam* —
**1.4.23** *kārake*; **1.4.32** *sampradānam*; *ca* extends 1.4.40.

*Śāstra (laghu):* When the root gṝ/gṛ (to swallow/receive) is preceded by
*anu* or *prati*, the recipient receives the saṃjñā *sampradāna*.
E.g. *devadattāya anugṛhṇāti*.

*Engine:* tags bearing ``"anu_prati_grNa"`` get ``"sampradAna"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_41_karaka_done"
_TRIGGER    = frozenset({"anu_prati_grNa"})
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
    state.samjna_registry["1_4_41_sampradAna"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.41",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "anupratigṛRaS ca",
    text_dev             = "अनुप्रतिगृणश्च — sampradāna",
    padaccheda_dev       = "अनु-प्रति-गृणः / च",
    why_dev              = (
        "अनु-प्रति-पूर्वक-गृ-धातोः यस्मै ददाति स सम्प्रदान-कारक-संज्ञकः। "
        "चिह्नम्: anu_prati_grNa इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.32", "1.4.40"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
