"""
3.1.82  स्तम्भुस्तुम्भुस्कम्भुस्कुम्भुस्कुञ्भ्यः श्नुश्च  —  VIDHI

Padaccheda: स्तम्भु-स्तुम्भु-स्कम्भु-स्कुम्भु-स्कुञ्भ्यः श्नुः च

Krt suffix rule from dhatu: स्तम्भुस्तुम्भुस्कम्भुस्कुम्भुस्कुञ्भ्यः श्नुश्च (82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_82_stamBustumBu_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stamBustumBuskamBuskumBuskuYByaH SnuSca",
    text_dev              = "स्तम्भुस्तुम्भुस्कम्भुस्कुम्भुस्कुञ्भ्यः श्नुश्च",
    padaccheda_dev        = "स्तम्भु-स्तुम्भु-स्कम्भु-स्कुम्भु-स्कुञ्भ्यः श्नुः च",
    why_dev               = "धातोः [स्तम्भुस्तुम्भुस्कम्भुस्कुम्भुस्कुञ्भ्यः श्नुश्च]-प्रत्ययः विहितः (३.१.82)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
