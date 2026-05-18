"""
1.4.46  अधिशीङ्स्थाऽऽसां कर्म  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake adhi-śīṅ-sthā-āsāṃ karma* —
**1.4.23** *kārake*.

*Śāstra (laghu):* When adhi is prefixed to śī (to lie/sleep), sthā (to stand),
or ās (to sit), the *locus* (ādhāra) in/on which the action occurs becomes the
*karman* (instead of adhikaraṇa). E.g. *kaṭam adhiśete* — kaṭa (mat) is karman.

*Engine:* tags bearing ``"aDiSIN_sTa_As_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_46_karaka_done"
_TRIGGER    = frozenset({"aDiSIN_sTa_As_karma"})
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
    state.samjna_registry["1_4_46_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.46",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "aDiSINsTAAsAM karma",
    text_dev             = "अधिशीङ्स्थाऽऽसां कर्म",
    padaccheda_dev       = "अधि-शीङ्-स्था-आसाम् / कर्म",
    why_dev              = (
        "अधि-पूर्वक-शीङ्-स्था-आस्-धातूनां यः आधारः स कर्म-कारक-संज्ञकः। "
        "चिह्नम्: aDiSIN_sTa_As_karma इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
