"""
1.4.52  गतिबुद्धिप्रत्यवसानार्थशब्दकर्माकर्मकाणामणि कर्ता स णौ  —  SAMJNA

**Pāṭha (baked anuvṛtti):** *kārake gati-buddhi-pratyavasāna-artha-śabda-karma-
akarmakāṇām aṇi kartā sa ṇau* — **1.4.23** *kārake*.

*Śāstra (laghu):* For verbs of motion, cognition, consumption, speaking, and
for karma/akarmaka verbs, the agent (kartā) in the causative (ṇi/ṇau/ṇic)
construction retains the saṃjñā *kartṛ*. E.g. *devadattena grāmam gamayati* —
devadatta is kartā in the causative.

*Engine:* tags bearing ``"gati_buddhi_NI_kartf"`` get ``"kartf"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_52_karaka_done"
_TRIGGER    = frozenset({"gati_buddhi_NI_kartf"})
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
    state.samjna_registry["1_4_52_kartf"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.52",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "gatibudDipratyavasAnArTaSabdakarmAkarmakARAm aRi kartA sa Ro",
    text_dev             = "गतिबुद्धिप्रत्यवसानार्थशब्दकर्माकर्मकाणामणि कर्ता स णौ",
    padaccheda_dev       = "गति-बुद्धि-प्रत्यवसान-अर्थ-शब्द-कर्म-अकर्मकाणाम् / अणि / कर्ता / सः / णौ",
    why_dev              = (
        "गति-बुद्धि-आदि-धातूनां णि-प्रयोगे यः कर्ता (प्रयोज्यः) स कर्तृ-कारक-संज्ञकः। "
        "चिह्नम्: gati_buddhi_NI_kartf इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
