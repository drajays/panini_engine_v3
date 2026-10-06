"""
3.4.111  लङः शाकटायनस्यैव  —  VIDHI

Padaccheda: लङः शाकटायनस्य एव

krt-suffix rule: लङः शाकटायनस्यैव
Pāṭha: ashtadhyayi.com data.txt row i=34111 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_111_laNaH_111"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.111", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "laNaH SAkawAyanasyEva",
    text_dev              = "लङः शाकटायनस्यैव",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH lasya laNaH SAkawAyanasya eva JeH jus AtaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः लस्य लङः शाकटायनस्य एव झेः जुस् आतः",
    padaccheda_dev        = "लङः शाकटायनस्य एव",
    why_dev               = "धातोः प्रत्ययः (३.4.111)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
