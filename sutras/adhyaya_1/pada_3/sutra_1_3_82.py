"""
1.3.82  परेर्मृषः  —  VIDHI

परेर्मृषः — mṛṣ (mfza~) after pari takes PARASMAIPADA: parimṛṣyati, parimṛṣyataḥ, parimṛṣyanti; āmṛṣyate keeps ātmanepada (Kāśikā 1.3.82).
Engine: reads the dhātu's upadeśa and the upasargas before it off the tape (engine/pada_ctx.py); decides the pada; the recipe resolver lets this
decision override the 1.3.78 gate (meta pada_by_sense). No arm flags (Art. 13).
Pāṭha: ashtadhyayi.com data.txt row i=13082 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.pada_ctx import decide, pada_site
from engine.state import State

_ROOTS: frozenset[str] = frozenset(['mfza~'])
_UPASARGAS: frozenset[str] = frozenset(['pari'])
_REGISTRY_KEY = "1_3_82_pada"
_STAMP_KEY = "Parasmaipada_1_3_82"


def cond(state: State) -> bool:
    return pada_site(state, _ROOTS, _UPASARGAS, _STAMP_KEY)


def act(state: State) -> State:
    return decide(state, "Parasmaipada", _STAMP_KEY, _REGISTRY_KEY)


SUTRA = SutraRecord(
    sutra_id="1.3.82",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='parermfzaH',
    text_dev='परेर्मृषः',
    samagra_slp1="pareH mfzaH kartari parasmEpadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="परेः मृषः कर्तरि परस्मैपदम्",
    padaccheda_dev="परेः (पञ्चमी-एकवचन) / मृषः (षष्ठी-एकवचन)",
    why_dev="परेः उत्तरात् मृष्-धातोः परस्मैपदम् — परिमृष्यति (काशिका १.३.८२)।",
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
