"""
1.1.12  अदसो मात्  (adaso mAt)  —  PARIBHASHA

**Pāṭha authority:** [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data) ``sutraani/data.txt`` row
**i = 11012**: ``s`` = अदसो मात्, ``e`` (Velthuis, one token) = ``adasomaat``; ``an`` from **1.1.11**
(*pragṛhyam*), ``type`` = *pragṛhya-saṃjñā* in that index.

v3 **text_slp1** = ``"adaso mAt"`` (spaced SLP1; compact = ``adasomAt``), not the index’s
one-word ``e`` string. Same phonemic string as the ashtadhyayi row when compacted.

**Scholarly note:** the ashtadhyayi index classifies 1.1.12 as *pragṛhya* *saṃjñā*; the engine
uses ``SutraType.PARIBHASHA`` + R3 *gate* (no extra ``samjna_registry`` key for this file) for *aś* *it* /
*upadeśa* *prayoga* until *vidhi* apply **1.1.11** in *prayoga*.

**Śāstra (Kāśikā *vṛtti*):** in the *aś* *it* / *upadeśa* *prakaraṇa*, the *aś* of *adas*
(sarvānāma *aś* class) and the *m* / *māt* reading that **1.1.11**–scope rules use for
*pragṛhya* in *dvivacana* — *vidhi* that touch *aś* *lopa*, *aś* *it*, and *aś* / *aś*–*sup* *sandhi* on
*etad* / *adas* *aṅga* consult this gate; v3 only sets the *paribhāṣā* *breadcrumb* here
(see **1.3.2**–**1.3.9**).

See also **1.1.13** (``sutra_1_1_13``) — *śe* ( *aś* / *ś* locus in the *pragṛhya* *prayoga* *prakaraṇa* );
**1.1.14** (``sutra_1_1_14``) *nipāta ekājanāṅ*; **1.1.100** (``sutra_1_1_100``) — *Kāśikā* *na mātrā samāse*.

CONSTITUTION Art. 2: *cond* does not read *vibhakti* / *vacana* coordinates; only
*State* *markers* and *registry* (no *reference* JSON under the engine *data/* tree).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

GATE_KEY: str = "1.1.12_adaso_mAt"


def adaso_mAt_gate_is_set(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


# ═══════════════════════════════════════════════════════
# Sūtra — *paribhāṣā*; once in *saṃjñā*/*upadeśa* preflight.
# ═══════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active" : True,
        "pATha"  : "1.1.12",
    }
    return state


_WHY = (
    "अदस्-कृताव् अश्-इत्पथे मात्-सम्बन्धः, द्विवचन-प्रगृह्य-काले च; "
    "उपदेश-वृत्ताव् इति परिभाषा।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.12",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "adaso mAt",
    text_dev       = "अदसो मात्",
    padaccheda_dev = "अदसः मात्",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
