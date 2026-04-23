"""
1.1.100  (scheduling id)  न मात्रा समासे  (na mAtrA samAse)  —  PARIBHASHA

**Not a Pāṇini *sūtra* number** — the engine uses **``1.1.100``** so the **canonical** **1.1.14** slot
remains *nipāta ekājanāṅ* (``sutra_1_1_14``).  This rule is the *Kāśikā* *vṛtti* *na mātrā samāse*:
*anuvṛtti* of *pragṅhyam* (**1.1.11**): the *pragṅhya* *prayoga* does **not** ( *na* ) apply in a
*mātrā* (measure-name) *samāsa*.

v3: **R3** *paribhāṣā* *gate*; *vidhi* for *pada* / *samāsa* *prayoga* may consult the key
(CONSTITUTION Art. 2: *cond* does not read *vibhakti* here).

**Order:** scheduled in the recipe **after** canonical **1.1.14**, **before** **1.1.15** *ot*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

GATE_KEY: str = "1.1.100_KaSika_na_mAtrA_samAse"


def mAtrA_samAse_kaSika_paribhasha_set(state: State) -> bool:
    """True after the *Kāśikā* *mātrā*/*samāsa* *pragṛhya* *bādha* *gate* is set in preflight."""
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active": True,
        "pATha": "1.1.100",
    }
    return state


_WHY = (
    "प्रगृह्यं मात्रा-समासे न, द्वि-तृ-तुर्यादि-नामानि, "
    "उत्सर्ग-बाधः (काशिका-वृत्ति)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.100",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "na mAtrA samAse",
    text_dev       = "न मात्रासमासे",
    padaccheda_dev = "न मात्रा समासे",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11", "1.1.13"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
