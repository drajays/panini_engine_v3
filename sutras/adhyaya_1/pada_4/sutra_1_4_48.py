"""
1.4.48  उपान्वध्याङ्वसः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake upa-anu-adhi-āṅ-vasaḥ karma* —
**1.4.23** *kārake*.

*Śāstra (laghu):* When vas (to dwell) is prefixed by upa, anu, adhi, or ā,
the place of dwelling becomes *karman*. E.g. *grāmam upavasat*.

*Engine:* tags bearing ``"upa_anu_aDi_A_vas_karma"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
Pāṭha: ashtadhyayi.com data.txt row i=14048 (Art. 14).
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
    text_slp1            = 'upAnvaDyANvasaH',
    text_dev             = 'उपान्वध्याङ्वसः',
    samagra_slp1         = "AkaqArAt ekA saMjYA kArake upa-anu-aDi-AN-vasaH ADAraH karma",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा कारके उप-अनु-अधि-आङ्-वसः आधारः कर्म",
    padaccheda_dev       = "उप-अनु-अधि-आङ् / वसः",
    why_dev              = (
        "उप-अनु-अधि-आङ्-पूर्वक-वस्-धातोः यः आवासस्थानम् तत् कर्म-कारक-संज्ञकम्। "
        "चिह्नम्: upa_anu_aDi_A_vas_karma इति।"
    ),
    apavada_of     = ("1.4.45",),   # अपवाद of 1.4.45 — sutra_ref_out resolver.apavada_of
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
