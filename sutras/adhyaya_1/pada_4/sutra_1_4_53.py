"""
1.4.53  हृक्रोरन्यतरस्याम्  —  SAMJNA (kāraka-saṃjñā, vibhāṣā)

**Pāṭha (baked anuvṛtti):** *kārake hṛ-kroḥ anyatarasyām* —
**1.4.23** *kārake*; *anyatarasyām* = optionally (vibhāṣā).

*Śāstra (laghu):* For the roots hṛ (to take) and kṛ (to do/make) in the causative,
the agent can optionally be karman or kartṛ — the choice is the speaker's.
E.g. *devadattena/devadattam hārayati*.

*Engine:* tags bearing ``"hf_kf_anyatara"`` get both ``"karman"`` and
``"kartf"`` tags (the pipeline marks optionality). ``r1_form_identity_exempt = True``.
Pāṭha: ashtadhyayi.com data.txt row i=14053 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_53_karaka_done"
_TRIGGER    = frozenset({"hf_kf_anyatara"})


def cond(state: State) -> bool:
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            return True
    return False


def act(state: State) -> State:
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            # Optional: mark both; pipeline resolves which vibhāṣā branch is active.
            t.tags.add("karman")
            t.tags.add("kartf")
            t.meta[META_DONE] = True
    state.samjna_registry["1_4_53_anyatara"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.53",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'hfkroranyatarasyAm',
    text_dev             = 'हृक्रोरन्यतरस्याम्',
    samagra_slp1         = "AkaqArAt ekA saMjYA kArake hf-kroH anyatarasyAm karma aRi kartA saH RO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा कारके हृ-क्रोः अन्यतरस्याम् कर्म अणि कर्ता सः णौ",
    padaccheda_dev       = "हृ-क्रोः / अन्यतरस्याम्",
    why_dev              = (
        "हृ-कृ-धात्वोः णि-प्रयोगे प्रयोज्यः कर्म वा कर्ता वा विकल्पेन। "
        "चिह्नम्: hf_kf_anyatara इति।"
    ),
    anuvritti_from       = ("1.4.23", "1.4.52"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
