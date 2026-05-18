"""
1.4.40  प्रत्याङ्भ्यां श्रुवः पूर्वस्य कर्ता  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake prati-āṅ-bhyāṃ śruvaḥ pūrvasya kartā* —
**1.4.23** *kārake*.

*Śāstra (laghu):* When the root śru (to hear/promise) is preceded by *prati*
or *ā*, the agent of the *prior* action (the one who promised earlier) receives
the saṃjñā *kartṛ*.

*Engine:* tags bearing ``"prati_A_Sru_purva"`` get ``"kartf"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_40_karaka_done"
_TRIGGER    = frozenset({"prati_A_Sru_purva"})
_SAMJNA     = "kartf"


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
    state.samjna_registry["1_4_40_kartf"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.40",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "pratyAGByAM SruvaH pUrvasya kartA",
    text_dev             = "प्रत्याङ्भ्यां श्रुवः पूर्वस्य कर्ता",
    padaccheda_dev       = "प्रति-आङ्भ्याम् / श्रुवः / पूर्वस्य / कर्ता",
    why_dev              = (
        "प्रति-आङ्-पूर्वक-श्रु-धातोः पूर्वकर्ता (यः पूर्वं श्रुतवान्) "
        "कर्तृ-कारक-संज्ञकः। चिह्नम्: prati_A_Sru_purva इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
