"""
1.4.54  स्वतन्त्रः कर्ता  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake svataṃtraḥ kartā* — **1.4.23** *kārake*.

*Śāstra (laghu):* The independently acting agent (svataṃtra — one who acts of
his own will, not impelled by another) receives the technical name *kartṛ-kāraka*.
This is the foundational definitional rule for kartṛ. E.g. *devadatto pacati*.

*Engine:* This is a gate-style definitional rule. ``cond`` fires when
``samjna_registry`` has no entry for ``"kartf"`` yet. Also tags terms bearing
``"svatantra_kartf"``. ``r1_form_identity_exempt = True``.
Pāṭha: ashtadhyayi.com data.txt row i=14054 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_54_karaka_done"
_TRIGGER    = frozenset({"svatantra_kartf"})
_SAMJNA     = "kartf"
_GATE_KEY   = "kartf"


def cond(state: State) -> bool:
    if state.samjna_registry.get(_GATE_KEY) is None:
        return True
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            return True
    return False


def act(state: State) -> State:
    if state.samjna_registry.get(_GATE_KEY) is None:
        state.samjna_registry[_GATE_KEY] = "svatantra"
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            t.tags.add(_SAMJNA)
            t.meta[META_DONE] = True
    state.samjna_registry["1_4_54_kartf"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.54",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'svatantraH kartA',
    text_dev             = 'स्वतन्त्रः कर्ता',
    samagra_slp1         = "AkaqArAt ekA saMjYA kArake svatantraH kartA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा कारके स्वतन्त्रः कर्ता",
    padaccheda_dev       = "स्वतन्त्रः / कर्ता",
    why_dev              = (
        "यः क्रियायां स्वतन्त्रः (स्वेच्छया प्रवर्तते) स कर्तृ-कारक-संज्ञकः। "
        "कर्तृ-कारक-मूल-परिभाषा। चिह्नम्: svatantra_kartf इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
