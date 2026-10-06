"""
3.1.42  अभ्युत्सादयांप्रजनयांचिकयांरमयामकः पावयांक्रियाद्विदामक्रन्निति च्छन्दसि  —  VIDHI

Padaccheda: अभ्युत्सादयाम् प्रजनयाम् चिकयाम् रमयाम् अकः (तिङ्) पावयांक्रियात् (तिङ्) विदामक्रन् (तिङ्) इति छन्दसि

Krt suffix rule from dhatu: अभ्युत्सादयांप्रजनयांचिकयांरमयामकः (42)
Pāṭha: ashtadhyayi.com data.txt row i=31042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_42_aByutsAdayAM_42"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.42", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'aByutsAdayAMprajanayAMcikayAMramayAmakaH pAvayAMkriyAdvidAmakranniti cCandasi',
    text_dev              = 'अभ्युत्सादयांप्रजनयांचिकयांरमयामकः पावयांक्रियाद्विदामक्रन्निति च्छन्दसि',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH aByutsAdayAm prajanayAm cikayAm ramayAm akaH pAvayAMkriyAt vidAmakran iti Candasi Am anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः अभ्युत्सादयाम् प्रजनयाम् चिकयाम् रमयाम् अकः पावयांक्रियात् विदामक्रन् इति छन्दसि आम् अन्यतरस्याम्",
    padaccheda_dev        = "अभ्युत्सादयाम् प्रजनयाम् चिकयाम् रमयाम् अकः (तिङ्) पावयांक्रियात् (तिङ्) विदामक्रन् (तिङ्) इति छन्दसि",
    why_dev               = "धातोः [अभ्युत्सादयांप्रजनयांचिकयांरमयामकः]-प्रत्ययः विहितः (३.१.42)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
