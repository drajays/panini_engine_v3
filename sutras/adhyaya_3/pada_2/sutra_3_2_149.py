"""
3.2.149  अनुदात्तेतश्च हलादेः  —  VIDHI

Padaccheda: अनुदात्त-इतः च हल्-आदेः

krt-suffix rule: अनुदात्तेतश्च हलादेः (149)
Pāṭha: ashtadhyayi.com data.txt row i=32149 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_149_anudAtteta_149"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.149", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.149"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.149",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAttetaSca halAdeH",
    text_dev              = "अनुदात्तेतश्च हलादेः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu anudAttetaH ca halAdeH kft akarmakAt yuc",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु अनुदात्तेतः च हलादेः कृत् अकर्मकात् युच्",
    padaccheda_dev        = "अनुदात्त-इतः च हल्-आदेः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अनुदात्तेतश्च हलादेः] विहितः (३.२.149)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
