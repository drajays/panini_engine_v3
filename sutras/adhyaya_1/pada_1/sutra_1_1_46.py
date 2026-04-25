"""
1.1.46  आद्यन्तौ टकितौ  —  PARIBHĀṢĀ

पदच्छेदः  आदि-अन्तौ (प्रथमा-द्विवचनम्), टकितौ (प्रथमा-द्विवचनम्)

*Āgama-sthāna-nirṇaya*: a **ṭit** augment is stationed **before** its substrate
(*āgamin*); a **kit** augment **after** the *āgamin*.  Complements **1.1.47**
(*mit* after last *ac*).  Recorded as an **R3** gate for trace and for *vidhi*
that splice augments (e.g. **6.4.71** *aṭ*, **7.3.40** *ṣuk*).

See ``phonology.agama_placement_1_1_46`` for order constants without ``State``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY: str = "1.1.46_Adyantau_takitau"


def adyantau_takitau_paribhasha_set(state: State) -> bool:
    """True once **1.1.46** has been applied in this *prakriyā* clone."""
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active": True,
        "pATha": "1.1.46",
        "tit_before_agamin": True,
        "kit_after_agamin": True,
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.46",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "AdyantO TakitO",
    text_dev       = "आद्यन्तौ टकितौ",
    padaccheda_dev = "आदि-अन्तौ (प्रथमा-द्विवचनम्), टकितौ (प्रथमा-द्विवचनम्)",
    why_dev        = (
        "टित्-आगमः आगमिनः पूर्वम्, कित्-आगमः आगमिनः अनन्तरम् इति स्थाननिर्णयः।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
