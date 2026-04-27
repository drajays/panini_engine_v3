"""
1.1.10  नाज्झलौ  (nAjjhalau)  —  PARIBHASHA

**Śāstra (GRETIL pāṭha):** *a* in the *aç* ( *a* + *it* ) sequence of a *upadeśa* and
the *jhal* consonants are **out of the scope** of a preceding *aś* ( *a* + *c*
) *it* *pratyāhāra* *denotation* — i.e. they are **not** the *a* and *hala*
members meant when an earlier rule (e.g. *aś* *it* for *lopa*) is read across
*pratyāhāra* boundaries.  (Anchor for the *iṭ*-*prakaraṇa*, **1.3.2**–**1.3.9**.)

**Prayoga reading (*ac*–*hal*):** an *ac* letter and a *hal* letter are **never**
*savarṇa* to each other (*na + ac + halau*).  The operational mirror lives in
``phonology.savarna.is_savarna`` (so **6.1.101** and other *savarṇa*-sensitive
*vidhi*s do not treat e.g. *a*+*h* or *i*+*ś* as homorganic pairs).

v3 records an interpretive **gate** in ``paribhasha_gates`` (R3) so *vidhi*
*cond* paths that assign *it* to varṇas in *upadeśa* can align with the pāṭha
without reading *vibhakti* / target forms.

See also **1.1.11** (``sutra_1_1_11``) for *pragṛhya* in *dvivacana*; **1.1.12**
(``sutra_1_1_12``) for *adaso māt* ( *aś* in *sarvān. adas* *it*); **1.1.13**
(``sutra_1_1_13``) for *śe* ( *pragṛhya* *prayoga* off in the *aś* / *ś* locus);
**1.1.14** (``sutra_1_1_14``) *nipāta ekājanāṅ*; **1.1.100** (``sutra_1_1_100``) *Kāśikā* *na mātrā samāse*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# R3: consult from *it* rules; key must be unique under ``paribhasha_gates`` .
GATE_KEY: str = "1.1.10_nAjjhalau"


def nAjjhalau_gate_is_set(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


# ══════════════════════════════════════════════════════════
# Sūtra — universal paribhāṣā, registered once in preflight.
# ══════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active": True,
        "pATha": "1.1.10",
    }
    return state


_WHY = (
    "उपदेशे 'अश् इत्' पाठ-विषये अज्-झलः न, इति परिभाषा; इत्प्रकरण-पद्धतेः।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.10",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "nAjjhalau",
    text_dev       = "नाज्झलौ",
    padaccheda_dev = "न अज्-झलौ",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
