"""
1.2.55  योगप्रमाणे च तदभावेऽदर्शनं स्यात्  —  PARIBHASHA

*Padaccheda:* **योग-प्रमाणे** / **च** / **तत्-अभावे** / **अदर्शनम्** / **स्यात्**

"In the case where yoga (connection/rule) is the authority, if that connection
is absent, [the result/word] is not seen/manifested."  This paribhāṣā governs
rule-application absence: when the authority for a form is a yoga (a sūtra
connection), and that yoga is not present, the expected form does not appear.

Operational role (v3):
  - Registers the gate ``1_2_55_yogapramANe`` in both ``paribhasha_gates``
    and ``samjna_registry``.
  - Downstream rules consult this gate when determining whether absence of a
    connecting rule implies absence of the derived form.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
Pāṭha: ashtadhyayi.com data.txt row i=12055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import accent_paribhasha_gate_eligible

_GATE_KEY = "1_2_55_yogapramANe"


def cond(state: State) -> bool:
    return accent_paribhasha_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.55",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = 'yogapramARe ca tadaBAvedarSanaM syAt',
    text_dev                = 'योगप्रमाणे च तदभावेऽदर्शनं स्यात्',
    samagra_slp1            = "yoga-pramARe ca tad-aBAve a-darSanam syAt tat a-Sizyam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev             = "योग-प्रमाणे च तद्-अभावे अ-दर्शनम् स्यात् तत् अ-शिष्यम्",
    padaccheda_dev          = "योग-प्रमाणे / च / तत्-अभावे / अदर्शनम् / स्यात्",
    why_dev                 = (
        "योगः प्रमाणं यस्य तस्मिन् विषये तस्य योगस्य अभावे रूपस्य अदर्शनम् — "
        "योगसम्बन्धाभावे प्रयोगो न दृश्यते इति परिभाषा।"
    ),
    anuvritti_from          = ("1.2.54",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
