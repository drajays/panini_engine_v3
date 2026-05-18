"""
2.3.12  गत्यर्थकर्मणि द्वितीयाचतुर्थ्यौ चेष्टायामनध्वनि  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: गत्यर्थ-कर्मणि / द्वितीया-चतुर्थ्यौ / च / इष्टायाम् / अन-अध्वनि

Śāstra: for the karma (object) of verbs of motion (*gatyartha*), when the
motion is intentional (*ceṣṭā*) and the object is not a road/path (*anadhvan*),
both the second (accusative/dvitīyā) and fourth (dative/caturthī) vibhaktis
are optionally prescribed.

Engine: registers the gatyartha-karma→dvitīyā/caturthī gate. ``cond`` checks
only the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_12_gatyartha_karmani_dvitiya_caturthyau"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.12",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "gatyarTakarmaRi dvitIyAcaturTyO cesTAyAm anaDvani",
    text_dev              = "गत्यर्थकर्मणि द्वितीयाचतुर्थ्यौ चेष्टायामनध्वनि",
    padaccheda_dev        = "गत्यर्थ-कर्मणि / द्वितीया-चतुर्थ्यौ / च / इष्टायाम् / अन-अध्वनि",
    why_dev               = (
        "गत्यर्थ-कर्मणि (इष्टे, अनध्वनि) द्वितीया चतुर्थी च — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1", "2.3.2"),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
