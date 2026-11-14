"""
1.3.22  समवप्रविभ्यः स्थः  —  VIDHI

समवप्रविभ्यः स्थः — ṣṭhā (zWA) after sam / ava / pra / vi takes ātmanepada: saṃtiṣṭhate, avatiṣṭhate, pratiṣṭhate, vitiṣṭhate (Kāśikā 1.3.22).
Engine: reads the dhātu's upadeśa and the upasargas before it off the tape (engine/pada_ctx.py); decides the pada; the recipe resolver lets this
decision override the 1.3.78 gate (meta pada_by_sense). No arm flags (Art. 13).
Pāṭha: ashtadhyayi.com data.txt row i=13022 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.pada_ctx import decide, pada_site
from engine.state import State

_ROOTS: frozenset[str] = frozenset(['zWA'])
_UPASARGAS: frozenset[str] = frozenset(['ava', 'pra', 'sam', 'vi'])
_REGISTRY_KEY = "1_3_22_pada"
_STAMP_KEY = "Atmanepada_1_3_22"


def cond(state: State) -> bool:
    return pada_site(state, _ROOTS, _UPASARGAS, _STAMP_KEY)


def act(state: State) -> State:
    return decide(state, "Atmanepada", _STAMP_KEY, _REGISTRY_KEY)


SUTRA = SutraRecord(
    sutra_id="1.3.22",
    sutra_type=SutraType.VIDHI,
    text_slp1='samavapraviByaH sTaH',
    text_dev='समवप्रविभ्यः स्थः',
    samagra_slp1="sam-ava-pra-viByaH sTaH Atmanepadam",
    samagra_dev="सम्-अव-प्र-विभ्यः स्थः आत्मनेपदम्",
    padaccheda_dev="सम्-अव-प्र-वि-भ्यः (पञ्चमी) / स्थः (षष्ठी)",
    why_dev="सम्-अव-प्र-विभ्यः उत्तरात् स्था-धातोः आत्मनेपदम् — संतिष्ठते, अवतिष्ठते, प्रतिष्ठते, वितिष्ठते (काशिका १.३.२२)।",
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
