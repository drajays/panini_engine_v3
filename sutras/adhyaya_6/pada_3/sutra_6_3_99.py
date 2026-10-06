"""
6.3.99  अषष्ठ्यतृतीयास्थस्यान्यस्य दुगाशीराशाऽऽस्थाऽऽस्थितोत्सुकोतिकारकरागच्छेषु  —  VIDHI

Padaccheda: अ-षष्ठी-अ-तृतीया-स्थस्य अन्यस्य दुक् आशीः-आशा-स्था-आस्थित-उत्सुक-ऊति-कारक-राग-छेषु

अषष्ठ्यतृतीयास्थस्यान्यस्य दुगाशिराशाऽऽस्थाऽऽस्थितोत्सुकोतिकारकरागच्छेषु (6.3.99)
Pāṭha: ashtadhyayi.com data.txt row i=63099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_99_azazWyatft_99"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.99", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'azazWyatftIyAsTasyAnyasya dugASIrASAsTAsTitotsukotikArakarAgacCezu',
    text_dev              = 'अषष्ठ्यतृतीयास्थस्यान्यस्य दुगाशीराशाऽऽस्थाऽऽस्थितोत्सुकोतिकारकरागच्छेषु',
    samagra_slp1          = "uttarapade azazWI-atftIyAsTasya anyasya duk ASIr-ASA-AsTA-AsTita-utsuka-uti-kAraka-rAga-cCezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे अषष्ठी-अतृतीयास्थस्य अन्यस्य दुक् आशीर्-आशा-आस्था-आस्थित-उत्सुक-उति-कारक-राग-च्छेषु",
    padaccheda_dev        = "अ-षष्ठी-अ-तृतीया-स्थस्य अन्यस्य दुक् आशीः-आशा-स्था-आस्थित-उत्सुक-ऊति-कारक-राग-छेषु",
    why_dev               = "(सूत्रम् 6.3.99) अषष्ठ्यतृतीयास्थस्यान्यस्य दुगाशिराशाऽऽस्थाऽऽस्थितोत्सुकोतिकारकरागच्छेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
