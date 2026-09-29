"""
6.1.16  ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च  —  VIDHI

Padaccheda: ग्रहि-ज्या-वयि-व्यधि-वष्टि-विचति-वृश्चति-पृच्छति-भृज्जतीनाम् ङ्-इति च

ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च (6.1.16)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import samprasarana_site
from engine.state import State
from sutras.adhyaya_1.pada_1.sutra_1_1_45 import META_TARGETS

# the roots as they stand after it-lopa / 6.1.64 (वयि is वे's liṭ ādeśa)
_STEMS = frozenset({"grah", "jyA", "vay", "vyaD", "vaS", "vyac", "vraSc", "vrasc", "pracC", "praC", "pratC", "Brasj"})


def cond(state: State) -> bool:
    return samprasarana_site(state, _STEMS, ngit=True) is not None


def act(state: State) -> State:
    ti, vi = samprasarana_site(state, _STEMS, ngit=True)
    state.meta[META_TARGETS] = [(ti, vi)]          # 1.1.45 इग्यणः सम्प्रसारणम्
    state.terms[ti].meta["samprasarana_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,       # marks the yaṇ; 1.1.45 changes it
    text_slp1             = "grahijyAvayivyaDivazwivicativfScatipfcCatiBfjjatInAM Niti ca",
    text_dev              = "ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च",
    padaccheda_dev        = "ग्रहि-ज्या-वयि-व्यधि-वष्टि-विचति-वृश्चति-पृच्छति-भृज्जतीनाम् ङ्-इति च",
    why_dev               = "ग्रह्-ज्या-वयि-व्यध्-वश्-व्यच्-व्रश्च्-प्रच्छ्-भ्रस्जां यणः सम्प्रसारणं किति ङिति च (वृश्चति, पृच्छति, गृह्यते)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
