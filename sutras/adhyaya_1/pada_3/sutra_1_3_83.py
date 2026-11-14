"""
1.3.83  व्याङ्परिभ्यो रमः  —  VIDHI

व्याङ्परिभ्यो रमः — ram (ramu~) after vi / ā / pari takes PARASMAIPADA: viramati, āramati, pariramati; abhiramate is ātmanepada (Kāśikā 1.3.83).
Engine: reads the dhātu's upadeśa and the upasargas before it off the tape (engine/pada_ctx.py); decides the pada; the recipe resolver lets this
decision override the 1.3.78 gate (meta pada_by_sense). No arm flags (Art. 13).
Pāṭha: ashtadhyayi.com data.txt row i=13083 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.pada_ctx import decide, pada_site
from engine.state import State

_ROOTS: frozenset[str] = frozenset(['ramu~'])
_UPASARGAS: frozenset[str] = frozenset(['A', 'AN', 'pari', 'vi'])
_REGISTRY_KEY = "1_3_83_pada"
_STAMP_KEY = "Parasmaipada_1_3_83"


def cond(state: State) -> bool:
    return pada_site(state, _ROOTS, _UPASARGAS, _STAMP_KEY)


def act(state: State) -> State:
    return decide(state, "Parasmaipada", _STAMP_KEY, _REGISTRY_KEY)


SUTRA = SutraRecord(
    sutra_id="1.3.83",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="vyANpariByo ramaH",
    text_dev="व्याङ्परिभ्यो रमः",
    samagra_slp1="vi-AN-pariByaH ramaH kartari parasmEpadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="वि-आङ्-परिभ्यः रमः कर्तरि परस्मैपदम्",
    padaccheda_dev="वि-आङ्-परिभ्यः (पञ्चमी-बहुवचन) / रमः (षष्ठी-एकवचन)",
    why_dev="वि-आङ्-परिभ्यः उत्तरात् रम्-धातोः परस्मैपदम् — विरमति, आरमति, परिरमति (काशिका १.३.८३)।",
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
