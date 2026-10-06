"""
2.4.6  जातिरप्राणिनाम्  —  VIDHI

Padaccheda: जातिः / अप्राणिनाम्

Śāstra: in dvandva compounds of non-animate beings (aprāṇin), a jāti
(genus/species) compound takes ekavacana.

Engine: sets gate "2_4_6_jati_apranin_ekavacana".
Pāṭha: ashtadhyayi.com data.txt row i=24006 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import samasa_lakara_gate_eligible

_GATE = "2_4_6_jati_apranin_ekavacana"


def cond(state: State) -> bool:
    return samasa_lakara_gate_eligible(state, _GATE)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.6",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = 'jAtiraprARinAm',
    text_dev       = 'जातिरप्राणिनाम्',
    samagra_slp1   = "jAtiH a-prARinAm ekavacanam dvandvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "जातिः अ-प्राणिनाम् एकवचनम् द्वन्द्वः",
    padaccheda_dev = "जातिः / अप्राणिनाम्",
    why_dev        = "अप्राणि-जाति-द्वन्द्वे एकवचनम्।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
