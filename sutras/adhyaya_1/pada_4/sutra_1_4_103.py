"""
1.4.103  सुपः  (supaḥ)  —  PARIBHASHA

*Padaccheda:* *supaḥ* (ṣaṣṭhī).

*Anuvṛtti:* **1.4.101** *tiṅaḥ trīṇi trīṇi*; **1.4.1** *ekasañjñā*.

*Śāstra:* The 21 *sup* endings (seven triplets: nominative through locative,
plus vocative) listed in **4.1.2** receive the name *sup*.  This *paribhāṣā*
is fundamental: it enables downstream rules (notably **1.4.104**) to use
the *sup-saṃjñā*.

*Engine:* sets ``paribhasha_gates["1_4_103_supaH"]`` once.  Downstream rules
check this gate before assigning *vibhakti* tags via **1.4.104**.
``cond`` never reads vibhakti/vacana/lakāra/surface/data/reference.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_103_supaH"


def _has_sarv_eligible_non_napumsaka_sup(state: State) -> bool:
    """
    True when a sup term has 'sup_sarvanamasthana_eligible' tag AND the stem
    is non-napumsaka.  In that case 1.1.43 handles the vibhakti saṃjñā, not 1.4.103.
    """
    has_sarv_sup = any(
        t.kind == "pratyaya" and "sup" in t.tags and "sup_sarvanamasthana_eligible" in t.tags
        for t in state.terms
    )
    if not has_sarv_sup:
        return False
    # Check that stem is non-napumsaka
    for t in state.terms:
        if "prātipadika" in t.tags or t.kind == "prakriti":
            if "napuṃsaka" in t.tags:
                return False
    return True


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # When 1.1.43 will handle this (non-napumsaka + sarvanamasthana-eligible sup),
    # 1.4.103 should not fire — 1.1.43 is the apavāda for those cells.
    if _has_sarv_eligible_non_napumsaka_sup(state):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.103",
    sutra_type           = SutraType.PARIBHASHA,
    text_slp1            = "supaH",
    text_dev             = "सुपः",
    padaccheda_dev       = "सुपः (षष्ठी — सुप्-प्रत्ययानाम्)",
    why_dev              = (
        "एकविंशति-सुप्-प्रत्ययानाम् 'सुप्' संज्ञा; "
        "अनेन १.४.१०४ 'विभक्ति'-संज्ञा-विधाने सुप्-समुच्चयः साधु।"
    ),
    anuvritti_from       = ("1.4.1", "1.4.101"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
