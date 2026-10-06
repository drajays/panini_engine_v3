"""
1.4.49  कर्तुरीप्सिततमं कर्म  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake kartur īpsitatamaṃ karma* —
**1.4.23** *kārake*.

*Śāstra (laghu):* What the agent (kartṛ) most desires to accomplish (īpsitatamaṃ)
is the *karman* (object). This is the fundamental definitional rule for karman.
E.g. *odanam pacati* — food (odana) is the most desired result → karman.

*Engine:* tags bearing ``"kartfr_Ipsita_kArman"`` get ``"karman"``.
``r1_form_identity_exempt = True``.
Pāṭha: ashtadhyayi.com data.txt row i=14049 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_49_karaka_done"
_TRIGGER    = frozenset({"kartfr_Ipsita_kArman"})
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
    state.samjna_registry["1_4_49_karman"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.49",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'karturIpsitatamaM karma',
    text_dev             = 'कर्तुरीप्सिततमं कर्म',
    samagra_slp1         = "AkaqArAt ekA saMjYA kArake kartuH Ipsitatamam karma",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा कारके कर्तुः ईप्सिततमम् कर्म",
    padaccheda_dev       = "कर्तुः / ईप्सिततमम् / कर्म",
    why_dev              = (
        "कर्तुः यत् ईप्सिततमम् (अत्यन्त-ऐच्छिकम्) तत् कर्म-कारक-संज्ञकम्। "
        "कर्म-कारक-मूल-परिभाषा। चिह्नम्: kartfr_Ipsita_kArman इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
