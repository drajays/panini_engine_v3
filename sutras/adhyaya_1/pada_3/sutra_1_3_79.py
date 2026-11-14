"""
1.3.79  अनुपराभ्यां कृञः  —  VIDHI

अनुपराभ्यां कृञः — kṛñ (qukfY) after anu / parā takes PARASMAIPADA (apavāda of the ātmanepada of 1.3.72 / 1.3.32): anukaroti, parākaroti (Kāśikā 1.3.79).
Engine: reads the dhātu's upadeśa and the upasargas before it off the tape (engine/pada_ctx.py); decides the pada; the recipe resolver lets this
decision override the 1.3.78 gate (meta pada_by_sense). No arm flags (Art. 13).
Pāṭha: ashtadhyayi.com data.txt row i=13079 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.pada_ctx import decide, pada_site
from engine.state import State

_ROOTS: frozenset[str] = frozenset(['qukfY'])
_UPASARGAS: frozenset[str] = frozenset(['anu', 'parA'])
_REGISTRY_KEY = "1_3_79_pada"
_STAMP_KEY = "Parasmaipada_1_3_79"


def cond(state: State) -> bool:
    return pada_site(state, _ROOTS, _UPASARGAS, _STAMP_KEY)


def act(state: State) -> State:
    return decide(state, "Parasmaipada", _STAMP_KEY, _REGISTRY_KEY)


SUTRA = SutraRecord(
    sutra_id="1.3.79",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="anuparAByAM kfYaH",
    text_dev="अनुपराभ्यां कृञः",
    samagra_slp1="anu-parAByAm kfYaH kartari parasmEpadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="अनु-पराभ्याम् कृञः कर्तरि परस्मैपदम्",
    padaccheda_dev="अनु-पराभ्याम् (पञ्चमी-द्विवचन) / कृञः (षष्ठी-एकवचन)",
    why_dev="अनु-पराभ्याम् उत्तरात् कृञ्-धातोः परस्मैपदम् — अनुकरोति, पराकरोति (काशिका १.३.७९)।",
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
