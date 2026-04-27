"""
1.1.13  शे  (Se)  —  PARIBHASHA

**Śāstra (GRETIL pāṭha):** *śe* (loc. *śa*), read with *anuvṛtti* from the *pragṛhya* block
(**1.1.11**, **1.1.12**): the *Kāśikā* *vṛtti* uses this to mark the *aś* / *ś* *locus*
where the *pragṛhya* *prayoga* ( *dvivacana* *ī*…*au*; *etad*–*adas* *māt* ) is **not** to be
taken in *samāsa* / *sup* *sandhi* *prakaraṇa* that are governed by the *śit* / *aś* *it*
conventions.  v3 records a **paribhāṣā** *gate* only (R3); *vidhi* *cond* will consult the
key when *ś*-initial *aṅga* / *pratyaya* *prayoga* is implemented ( **6.1.88** –style).

For the *Kāśikā* *prayoga* where the **7.1.39** *śe* residue *e* (*asme*, *tve*, *me*, …)
is *pragṛhya* before external *ac*, see ``SHE_PRAGHYA_TAG_ARM_META`` on ``State`` and
``sutra_1_1_11._tag_she_pragrahya_residue``.

See also **1.1.14** (``sutra_1_1_14``) *nipāta ekājanāṅ*; **1.1.100** (``sutra_1_1_100``) *na mātrā samāse* ( *Kāśikā* ).

CONSTITUTION Art. 2: *cond* inspects only *State* *markers* (no *vibhakti* / *vacana* in *cond*).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

GATE_KEY: str = "1.1.13_Se"


def Se_gate_is_set(state: State) -> bool:
    """True after **1.1.13** *śe* has been applied in the preflight once."""
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


# ═══════════════════════════════════════════════════════
# Sūtra — *paribhāṣā*; once in *saṃjñā* preflight.
# ═══════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active": True,
        "pATha": "1.1.13",
    }
    return state


_WHY = (
    "प्रगृह्य-परिच्छेदे 'श' इत्यादौ न प्रयोगः, "
    "समास-सुप्-काले; उपदेश-वृत्ताव् इति।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.13",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "Se",
    text_dev       = "शे",
    padaccheda_dev = "शे",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.12",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
