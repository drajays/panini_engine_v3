"""
1.3.84  उपाच्च  —  VIDHI

उपाच्च — ram (ramu~) after upa takes PARASMAIPADA: uparamati (devadattam uparamati = he makes stop) (Kāśikā 1.3.84).
Engine: reads the dhātu's upadeśa and the upasargas before it off the tape (engine/pada_ctx.py); decides the pada; the recipe resolver lets this
decision override the 1.3.78 gate (meta pada_by_sense). No arm flags (Art. 13).
Pāṭha: ashtadhyayi.com data.txt row i=13084 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.pada_ctx import decide, pada_site
from engine.state import State

_ROOTS: frozenset[str] = frozenset(['ramu~'])
_UPASARGAS: frozenset[str] = frozenset(['upa'])
_REGISTRY_KEY = "1_3_84_pada"
_STAMP_KEY = "Parasmaipada_1_3_84"


def cond(state: State) -> bool:
    return pada_site(state, _ROOTS, _UPASARGAS, _STAMP_KEY)


def act(state: State) -> State:
    return decide(state, "Parasmaipada", _STAMP_KEY, _REGISTRY_KEY)


SUTRA = SutraRecord(
    sutra_id="1.3.84",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="upAcca",
    text_dev="उपाच्च",
    samagra_slp1="upAt ca kartari parasmEpadam ramaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="उपात् च कर्तरि परस्मैपदम् रमः",
    padaccheda_dev="उपात् (पञ्चमी-एकवचन) / च",
    why_dev="उपात् उत्तरात् रम्-धातोः परस्मैपदम् — उपरमति (काशिका १.३.८४)।",
    anuvritti_from=("1.3.12", "1.3.83"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
