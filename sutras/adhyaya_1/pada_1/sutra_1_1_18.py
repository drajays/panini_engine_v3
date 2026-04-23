"""
1.1.18  ऊँ  (U.N)  —  PARIBHASHA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11018, ``e`` = ``on``-style *oon* for ऊम् / ऊँ):** *Kāśikā*
*pragṛhya* for the *nipāta* *Ū* with *anunāsika* / *candrabindu* (the *Oṃkāra* *ākṛti* in *śabda* *śāstra*
reading) under the *Śākalya*/**1.1.16**/**1.1.17** chain.  v3 ``text_slp1`` = ``U.N`` = ऊ + nasal mark
(SLP1: ``U`` + ``.N`` = candrabindu in ``joiner`` terms where applicable) — same morpheme as the index ``s`` line.

*anuvṛtti* in *data*: from **1.1.11**, **1.1.16**, **1.1.17**; v3: ``1.1.11``, ``1.1.16``, ``1.1.17`` in
``anuvritti_from`` (metadata; engine does not resolve *it* *paths* in *act*).

v3: R3 *paribhāṣā* *gate*; *pragṛhya* *prayoga* for *Ū* + *m̐* in *pāda* *prayoga* uses this key in *cond* in *vidhi* *later*.

CONSTITUTION Art. 2: *cond* does not read *vibhakti* / *vacana*; no blocked *data/* path in *sūtra* text.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

GATE_KEY: str = "1.1.18_UM"  # ऊ + candrabindu; ``U`` + ``.N`` in SLP1 strings


def Um_pragfhya_gate_is_set(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active": True,
        "pATha": "1.1.18",
    }
    return state


_WHY = (
    "ऊङ्-उन्मीलित-ऊँ-निपाते, प्रगृह्य-नियतः, इति।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.18",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "U.N",
    text_dev       = "ऊँ",
    padaccheda_dev = "ऊँ",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11", "1.1.16", "1.1.17"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
