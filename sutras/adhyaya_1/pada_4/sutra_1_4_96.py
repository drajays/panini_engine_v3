"""
1.4.96  अपिः पदार्थसम्भावनान्ववसर्गगर्हासमुच्चयेषु  —  VIDHI

*Padaccheda:* *apiḥ* (prathamā),
*padārtha-sambhāvanā-anvavasarga-garhā-samuccayeṣu* (saptamī-bahuvacanam).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *api* is a *karmapravacanīya* in five senses: *padārtha* (mere
word-sense), *sambhāvanā* (supposition), *anvavasarga* (permission),
*garhā* (censure), *samuccaya* (aggregation / addition).

*Engine:* sets paribhāṣā gate for *api-in-these-five-senses*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_96_api_padArTA_di"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.96",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "apiH padArTa-saMBAvanA-anvavasarga-garhA-samuccayezwu",
    text_dev             = "अपिः पदार्थसम्भावनान्ववसर्गगर्हासमुच्चयेषु",
    padaccheda_dev       = "अपिः / पदार्थ-सम्भावना-अन्ववसर्ग-गर्हा-समुच्चयेषु",
    why_dev              = (
        "पदार्थ-सम्भावना-अन्ववसर्ग-गर्हा-समुच्चय-अर्थेषु वर्तमानः 'अपि' "
        "कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
