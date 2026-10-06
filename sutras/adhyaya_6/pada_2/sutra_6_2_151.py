"""
6.2.151  मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः  —  VIDHI

Padaccheda: मन्-क्तिन्-व्याख्यान-शयन-आसन-स्थान-याजक-आदि-क्रीताः

मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः (6.2.151)
Pāṭha: ashtadhyayi.com data.txt row i=62151 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_151_manktinvyA_151"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.151", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.151"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.151",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "manktinvyAKyAnaSayanAsanasTAnayAjakAdikrItAH",
    text_dev              = "मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः",
    samagra_slp1          = "uttarapadAdiH antaH man-ktin-vyAKyAna-Sayana-Asana-sTAna-yAjakAdi-krItAH kArakAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः मन्-क्तिन्-व्याख्यान-शयन-आसन-स्थान-याजकादि-क्रीताः कारकात्",
    padaccheda_dev        = "मन्-क्तिन्-व्याख्यान-शयन-आसन-स्थान-याजक-आदि-क्रीताः",
    why_dev               = "(सूत्रम् 6.2.151) मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
