"""
1.4.43  दिवः कर्म च  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake divaḥ karma ca* — **1.4.23** *kārake*;
*ca* = also karaṇa.

*Śāstra (laghu):* For the root div (to play/gamble), what is played for
or the object of play receives the saṃjñā *karman*. Also extends the karaṇa
definitional scope. E.g. *akṣair divyati* — akṣa (dice) is the means → karman.

*Engine:* tags bearing ``"div_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_43_karaka_done"
_TRIGGER    = frozenset({"div_karma"})
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
    state.samjna_registry["1_4_43_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.43",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "divaḥ karma ca",
    text_dev             = "दिवः कर्म च",
    padaccheda_dev       = "दिवः / कर्म / च",
    why_dev              = (
        "दिव्-धातोः (क्रीडार्थस्य) यत् क्रीडोपयोगि तत् कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: div_karma इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
