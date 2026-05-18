"""
1.4.55  तत्प्रयोजको हेतुश्च  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake tat-prayojako hetuś ca kartā* —
**1.4.23** *kārake*; **1.4.54** *kartā*; *ca* extends.

*Śāstra (laghu):* The *hetu* (motivating cause/causer), who prompts (prayojaka)
the agent (tat = the kartṛ of 1.4.54), also receives the saṃjñā *kartṛ*.
This covers the causative progenitor. E.g. *devadattaḥ odanaṃ kārayati* —
Devadatta (the causer) is kartā by this rule.

*Engine:* tags bearing ``"prayojaka_hetu"`` get ``"kartf"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_55_karaka_done"
_TRIGGER    = frozenset({"prayojaka_hetu"})
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
    state.samjna_registry["1_4_55_kartf"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.55",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "tatprayojako hetuS ca",
    text_dev             = "तत्प्रयोजको हेतुश्च — kartṛ",
    padaccheda_dev       = "तत्-प्रयोजकः / हेतुः / च",
    why_dev              = (
        "यः कर्तारं प्रयोजयति (हेतुः/प्रेरकः) स अपि कर्तृ-कारक-संज्ञकः। "
        "णिजन्त-प्रयोजक-कर्तुः संज्ञा। चिह्नम्: prayojaka_hetu इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.54"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
