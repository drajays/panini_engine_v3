"""
1.1.21  (ādyantavad ekasmin)  —  PARIBHĀṢĀ; *devanāgarī* = ``_TEXT_DEV`` (ashtadhyayi *i* 11021 *s* line).

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11021):** in a single locus (*ekasmin*), (treat) as *ādi*–*anta*-
*vat* for *vyapadeśa* / *atideśa* *prayoga* — the *jñāpaka* *paribhāṣā* that underwrites *ādyantavad*
*atideśa* (index ``type`` includes *आद्यन्तवदतिदेशः*).

v3: **R3** *paribhāṣā* *gate* in ``paribhasha_gates``; *vidhi* that needs this *śāstrīya* *nimitta* may
consult ``aadyantavad_ekasmin_paribhasha_set`` (CONSTITUTION Art. 2: *cond* does not read
*vibhakti*).  No *Term* mutation.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

GATE_KEY: str = "1.1.21_Adyantavad_ekasmin"

# *s* (i=11021) — exact orthography.
_TEXT_DEV: str = "\u0906\u0926\u094d\u092f\u0928\u094d\u0924\u0935\u0926\u0947\u0915\u0938\u094d\u092e\u093f\u0928\u094d"


def aadyantavad_ekasmin_paribhasha_set(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active": True,
        "pATha": "1.1.21",
    }
    return state


_WHY = (
    "एक-व्यपदेश-स्थाने आदि-ऽन्त-वद्-भावः, अतिदेश-तात्पर्यम्।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.21",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "Adyantavad ekasmin",
    text_dev       = _TEXT_DEV,
    padaccheda_dev = "आदि-अन्तवत् / एकस्मिन्",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
