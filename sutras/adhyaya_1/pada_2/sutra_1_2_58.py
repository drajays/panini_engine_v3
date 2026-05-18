"""
1.2.58  जात्याख्यायामेकस्मिन् बहुवचनमन्यतरस्याम्  —  VIBHASHA

*Padaccheda:* **जाति-आख्यायाम्** / **एकस्मिन्** / **बहुवचनम्** / **अन्यतरस्याम्**

When a jāti (genus/class) name refers to a single individual, optionally
(anyatarasyām) it takes plural (bahuvacanam).  E.g., "brāhmaṇāḥ" can
refer to a single Brahmin.  This is the optional-plural paribhāṣā for
jāti-denoting expressions.

Operational role (v3):
  - Registers the gate ``1_2_58_jAtyAkhyAyAm_bahuvacanam`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when determining whether a jāti-name
    in singular reference may optionally take plural agreement.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_58_jAtyAkhyAyAm_bahuvacanam"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.58",
    sutra_type              = SutraType.VIBHASHA,
    vibhasha_default        = True,
    r1_form_identity_exempt = True,
    text_slp1               = "jAtyAKyAyAm ekasmin bahuvacanam anyatarasyAm",
    text_dev                = "जात्याख्यायामेकस्मिन् बहुवचनमन्यतरस्याम्",
    padaccheda_dev          = "जाति-आख्यायाम् / एकस्मिन् / बहुवचनम् / अन्यतरस्याम्",
    why_dev                 = (
        "जातिवाचिनि शब्दे एकस्मिन् अर्थे विवक्षिते बहुवचनम् अन्यतरस्याम् — "
        "एकस्मिन् व्यक्तौ जात्याख्या बहुवचनेन अपि प्रयुज्यते इति विभाषा।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
