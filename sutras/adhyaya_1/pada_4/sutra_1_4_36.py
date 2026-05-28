"""
1.4.36  स्पृहेरीप्सितः  (spṛher īpsitaḥ)  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake spṛheḥ īpsitaḥ sampradānam* —
**1.4.23** *kārake*; **1.4.32** *sampradānam* (anuvṛtti).

*Śāstra (laghu):* The object desired by the one who longs (spṛhā) receives
the technical name *sampradāna-kāraka*. E.g. *bālāya spṛhayati* — the bāla
(child) is what is longed for, hence sampradāna.

*Engine:* tags bearing ``"spfhA_Ipsita"`` get the saṃjñā ``"sampradAna"``.
``cond`` does NOT read vibhakti/vacana/lakāra/surface or any gold corpus.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_36_karaka_done"
_TRIGGER    = frozenset({"spfhA_Ipsita"})
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
    state.samjna_registry["1_4_36_sampradAna"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.36",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "spfher Ipsitaḥ",
    text_dev             = "स्पृहेरीप्सितः — sampradāna-kāraka",
    padaccheda_dev       = "स्पृहेः / ईप्सितः",
    why_dev              = (
        "स्पृह्-धातोः ईप्सितः (यं प्रति स्पृहा) सम्प्रदान-कारक-संज्ञकः। "
        "चिह्नम्: spfhA_Ipsita इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.32"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
