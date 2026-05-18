"""
1.4.48  उपान्वध्याङ्वसः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake upa-anu-adhi-āṅ-vasaḥ karma* —
**1.4.23** *kārake*.

*Śāstra (laghu):* When vas (to dwell) is prefixed by upa, anu, adhi, or ā,
the place of dwelling becomes *karman*. E.g. *grāmam upavasat*.

*Engine:* tags bearing ``"upa_anu_aDi_A_vas_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_48_karaka_done"
_TRIGGER    = frozenset({"upa_anu_aDi_A_vas_karma"})
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
    state.samjna_registry["1_4_48_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.48",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "upAnvaDyAGvasaH",
    text_dev             = "उपान्वध्याङ्वसः — karman",
    padaccheda_dev       = "उप-अनु-अधि-आङ् / वसः",
    why_dev              = (
        "उप-अनु-अधि-आङ्-पूर्वक-वस्-धातोः यः आवासस्थानम् तत् कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: upa_anu_aDi_A_vas_karma इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
