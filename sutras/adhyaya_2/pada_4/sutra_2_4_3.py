"""
2.4.3  अनुवादे चरणानाम्  —  VIDHI

Padaccheda: अनुवादे / चरणानाम्

Śāstra: in an anuvāda (citation / mention context), a dvandva of Vedic
recitation branches (caraṇa) takes ekavacana.

Engine: sets gate "2_4_3_anuvade_carana_ekavacana".
Pāṭha: ashtadhyayi.com data.txt row i=24003 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import samasa_lakara_gate_eligible

_GATE = "2_4_3_anuvade_carana_ekavacana"


def cond(state: State) -> bool:
    return samasa_lakara_gate_eligible(state, _GATE)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.3",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = 'anuvAde caraRAnAm',
    text_dev       = 'अनुवादे चरणानाम्',
    samagra_slp1   = "anuvAde caraRAnAm ekavacanam dvandvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "अनुवादे चरणानाम् एकवचनम् द्वन्द्वः",
    padaccheda_dev = "अनुवादे / चरणानाम्",
    why_dev        = "अनुवाद-प्रसङ्गे चरण-द्वन्द्वः एकवचने भवति।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
