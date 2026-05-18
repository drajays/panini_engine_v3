"""
1.4.47  अभिनिविशश्च  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake abhi-ni-viśaś ca karma* —
**1.4.23** *kārake*; *ca* extends 1.4.46.

*Śāstra (laghu):* When abhi and ni precede viś (to enter), the destination
(the place entered into) becomes *karman*. E.g. *grāmam abhiniviśate*.

*Engine:* tags bearing ``"aBi_ni_viS_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_47_karaka_done"
_TRIGGER    = frozenset({"aBi_ni_viS_karma"})
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
    state.samjna_registry["1_4_47_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.47",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "aBiniviSaS ca",
    text_dev             = "अभिनिविशश्च — karman",
    padaccheda_dev       = "अभि-नि-विशः / च",
    why_dev              = (
        "अभि-नि-पूर्वक-विश्-धातोः यत् गन्तव्यस्थानम् तत् कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: aBi_ni_viS_karma इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.46"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
