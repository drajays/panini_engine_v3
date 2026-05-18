"""
1.4.50  तथायुक्तं चानीप्सितम्  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake tathāyuktaṃ ca anīpsitam karma* —
**1.4.23** *kārake*; *ca* extends 1.4.49.

*Śāstra (laghu):* Even something unintended (anīpsita), if it is similarly
related (tathāyukta) to the action, still gets the saṃjñā *karman*.
E.g. *stambham āhanti* — the pillar is hit unintentionally but is still karman.

*Engine:* tags bearing ``"anIpsita_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_50_karaka_done"
_TRIGGER    = frozenset({"anIpsita_karma"})
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
    state.samjna_registry["1_4_50_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.50",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "taTAyuktaM cAnIpsitam",
    text_dev             = "तथायुक्तं चानीप्सितम् — karman",
    padaccheda_dev       = "तथा-युक्तम् / च / अनीप्सितम्",
    why_dev              = (
        "तथायुक्तम् अनीप्सितम् अपि (अनभिलषितम् अपि) कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: anIpsita_karma इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.49"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
