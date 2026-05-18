"""
1.2.68  भ्रातृपुत्रौ स्वसृदुहितृभ्याम्  —  VIDHI (SAMJNA gate)

*Padaccheda:* **भ्रातृपुत्रौ** / **स्वसृदुहितृभ्याम्**

bhrātṛ (brother) and putra (son) [survive] when paired with svasṛ (sister)
and duhitṛ (daughter) respectively in ekasheṣa.  Male kin terms survive
over their corresponding female kin terms in the single-remainder operation.

Operational role (v3):
  - Registers the gate ``1_2_68_BrAtf_putra`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when resolving ekasheṣa between the
    specific male/female kin-term pairs bhrātṛ/svasṛ and putra/duhitṛ.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_68_BrAtf_putra"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.68",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "BrAtfputrO svasfduhitfByAm",
    text_dev                = "भ्रातृपुत्रौ स्वसृदुहितृभ्याम्",
    padaccheda_dev          = "भ्रातृपुत्रौ / स्वसृदुहितृभ्याम्",
    why_dev                 = (
        "एकशेषे स्वसृ-दुहितृभ्यां सह भ्रातृ-पुत्रौ क्रमेण शिष्येते — "
        "भ्रातृ स्वस्रा सह, पुत्रो दुहित्रा सह — पुरुषवाचिनः एव शिष्यन्ते।"
    ),
    anuvritti_from          = ("1.2.67",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
