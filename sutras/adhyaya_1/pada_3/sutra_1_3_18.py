"""
1.3.18  परिव्यवेभ्यः क्रियः  —  VIDHI

परिव्यवेभ्यः क्रियः — krī (qukrIY) after pari / vi / ava takes ātmanepada: parikrīṇīte, vikrīṇīte, avakrīṇīte (Kāśikā 1.3.18; 'bahuvi krīṇāti vanam': only these upasargas).
Engine: reads the dhātu's upadeśa and the upasargas before it off the tape (engine/pada_ctx.py); decides the pada; the recipe resolver lets this
decision override the 1.3.78 gate (meta pada_by_sense). No arm flags (Art. 13).
Pāṭha: ashtadhyayi.com data.txt row i=13018 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.pada_ctx import decide, pada_site
from engine.state import State

_ROOTS: frozenset[str] = frozenset(['qukrIY'])
_UPASARGAS: frozenset[str] = frozenset(['ava', 'pari', 'vi'])
_REGISTRY_KEY = "1_3_18_pada"
_STAMP_KEY = "Atmanepada_1_3_18"


def cond(state: State) -> bool:
    return pada_site(state, _ROOTS, _UPASARGAS, _STAMP_KEY)


def act(state: State) -> State:
    return decide(state, "Atmanepada", _STAMP_KEY, _REGISTRY_KEY)


SUTRA = SutraRecord(
    sutra_id="1.3.18",
    sutra_type=SutraType.VIDHI,
    text_slp1='parivyaveByaH kriyaH',
    text_dev='परिव्यवेभ्यः क्रियः',
    samagra_slp1="pari-vi-aveByaH kriyaH Atmanepadam",
    samagra_dev="परि-वि-अवेभ्यः क्रियः आत्मनेपदम्",
    padaccheda_dev="परि-वि-अवेभ्यः (पञ्चमी-बहुवचन) / क्रियः (षष्ठी)",
    why_dev="परि-वि-अवेभ्यः उत्तरात् क्रीञ्-धातोः आत्मनेपदम् — परिक्रीणीते, विक्रीणीते, अवक्रीणीते (काशिका १.३.१८)।",
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
