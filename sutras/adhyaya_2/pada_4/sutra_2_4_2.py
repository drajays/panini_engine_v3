"""
2.4.2  द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम्  —  VIDHI

Padaccheda: द्वन्द्वः / च / प्राणि-तूर्य-सेनाङ्गानाम्

Śāstra: a dvandva compound of living beings (prāṇi), musical instruments
(tūrya), or parts of an army (senāṅga) also takes ekavacana (singular).

Engine: sets gate "2_4_2_dvandva_pranituryasena_ekavacana".
Pāṭha: ashtadhyayi.com data.txt row i=24002 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import samasa_lakara_gate_eligible

_GATE = "2_4_2_dvandva_pranituryasena_ekavacana"


def cond(state: State) -> bool:
    return samasa_lakara_gate_eligible(state, _GATE)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.2",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = 'dvandvaSca prARitUryasenANgAnAm',
    text_dev       = 'द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम्',
    samagra_slp1   = "dvandvaH ca prARi-tUrya-senA-aNgAnAm ekavacanam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "द्वन्द्वः च प्राणि-तूर्य-सेना-अङ्गानाम् एकवचनम्",
    padaccheda_dev = "द्वन्द्वः / च / प्राणि-तूर्य-सेनाङ्गानाम्",
    why_dev        = "प्राणि-तूर्य-सेनाङ्गानाम् द्वन्द्वः एकवचने भवति।",
    anuvritti_from = ("2.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
