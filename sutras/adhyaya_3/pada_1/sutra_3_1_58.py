"""
3.1.58  जृस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च  —  VIDHI

Padaccheda: जॄ-स्तम्भु-म्रुचु-म्लुचु-ग्रुचु-ग्लुचु-ग्लुञ्चु-श्विभ्यः च

Krt suffix rule from dhatu: जृस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च (58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_58_jfstamBumruc_58"


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
    state.meta["krt_kind"] = "3.1.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jfstamBumrucumlucugrucuglucugluYcuSviByaSca",
    text_dev              = "जृस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च",
    padaccheda_dev        = "जॄ-स्तम्भु-म्रुचु-म्लुचु-ग्रुचु-ग्लुचु-ग्लुञ्चु-श्विभ्यः च",
    why_dev               = "धातोः [जृस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च]-प्रत्ययः विहितः (३.१.58)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
