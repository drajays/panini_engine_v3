"""
1.1.58  न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु  —  NIYAMA

Sources consulted:
- ashtadhyayi.com data.txt row i=101058
- Kāśikā: न पदान्तादिकारादीनां विधीनाम् अनुवृत्तिः (पदान्ते असिद्धत्वम्)
- Cross-validation: tests/unit/test_phalAni_santi_as_lat_padanta_lesson.py
  (**6.1.77** blocked at *phalāni*+अन्ति after **6.4.111** *padādi* *a*-lopa);
  tests/unit/test_yAyAvar_yang_varac_purvavidhau_lesson.py (**6.4.64** blocked at
  *vareya* after **6.4.48** *yaṅ* *a*-lopa during *varac* *rūpasiddhi*);
  tests/unit/test_kaNDUti_ktic_vareya_yalopa_lesson.py (**6.1.66** *vyor vali*
  after **6.4.48** when **1.1.58** lifts *sthānivat* block)

Operational role (v3):
  - Registers a niyama gate: prior *anuvṛtti* is blocked in eight contexts,
    including *padānta* (word-final / cross-pada *saṃhitā* operations).
  - Downstream **6.1.77** reads this gate: *para-nimitta* *ac* lopa at *padādi*
    of a following verbal *pada* (**6.4.111** on *as*) does not support *yaṇ*
    on a preceding *prātipadika* (*phalāni santi*, not *phalānyanti*).
  - Downstream **8.4.47** (tripāḍī *dvirvacana*, not **6.** adhyāya *abhyāsa*):
    **6.1.77** *yaṇ* ādeśa is not *sthānivat* for gemination of **other** consonants
    (*madhu*+``ari`` → ``maddhvari``). **1.1.59** covers *ṣaṣṭhādhyāya* *dvirvacana*+``ac``.
  - Downstream **6.4.64** (*vareya* / *varac* *rūpasiddhi*): *para-nimitta* *a* lopa'd by
    **6.4.48** on *yaṅ* before *varac* does not support further *ā*-lopa (*yāyāvar*).
  - Downstream **6.1.66** (*vareya* *y*-lopa): **6.4.48** lupta ``a`` is not *sthānivat*
    for *vyor vali* — ``engine.vareya_1_1_58.aca_sthanivat_blocks_yakaralopa``.

Blindness:
  - cond() reads only state.paribhasha_gates — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_58_na_padAnta_etc"

# The eight operational contexts where the prior anuvṛtti is blocked.
BLOCKED_CONTEXTS: frozenset[str] = frozenset({
    "padAnta",
    "dvirvacana",
    "vareya_lopa",
    "svara",
    "savarNa",
    "anusvAra",
    "dIrgha",
    "jaScara",
})


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id            = "1.1.58",
    sutra_type          = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1           = "na padAntadvirvacanavarey alopasvarasavarNAnusvAradIrgajaScarvidiSu",
    text_dev            = "न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु",
    padaccheda_dev      = "न / पदान्त-द्विर्वचन-वरेय-लोप-स्वर-सवर्ण-अनुस्वार-दीर्घ-जश्चर्-विधिषु",
    why_dev             = "पदान्त-द्विर्वचन-वरेयलोप-स्वर-सवर्ण-अनुस्वार-दीर्घ-जश्चर्-विधिषु पूर्वसूत्रस्य अनुवृत्तिः न — एते प्रसङ्गाः असिद्धवत्।",
    anuvritti_from      = (),
    cond                = cond,
    act                 = act,
)

register_sutra(SUTRA)

__all__ = ["BLOCKED_CONTEXTS", "SUTRA"]
