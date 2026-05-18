"""
1.4.44  परिक्रयणे सम्प्रदानमन्यतरस्याम्  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake parikrayaṇe sampradānam anyatarasyām* —
**1.4.23** *kārake*; **1.4.32** *sampradānam*; *anyatarasyām* = optionally.

*Śāstra (laghu):* When hiring/renting (parikrayaṇa), the price given receives
the saṃjñā *sampradāna* optionally (as an alternative to karaṇa).
E.g. *śatena parikrīṇāti* — the śata (hundred) is the price → sampradāna.

*Engine:* tags bearing ``"parikaraNa_sAmpr"`` get ``"sampradAna"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_44_karaka_done"
_TRIGGER    = frozenset({"parikaraNa_sAmpr"})
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
    state.samjna_registry["1_4_44_sampradAna"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.44",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "parikrayaRe sampradAnam anyatarasyAm",
    text_dev             = "परिक्रयणे सम्प्रदानमन्यतरस्याम्",
    padaccheda_dev       = "परिक्रयणे / सम्प्रदानम् / अन्यतरस्याम्",
    why_dev              = (
        "परिक्रयणे (भृत्यपरिग्रहे) यत् मूल्यं दीयते तत् सम्प्रदान-कारक-संज्ञकम् "
        "विकल्पेन। चिह्नम्: parikaraNa_sAmpr इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.32"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
