"""
3.2.154  लषपतपदस्थाभूवृषहनकमगमशॄभ्य उकञ्  —  VIDHI

Padaccheda: लष-पत-पद-स्था-भू-वृष-हन-कम-गम-शॄभ्य उकञ्

krt-suffix rule: लषपतपदस्थाभूवृषहनकमगमशॄभ्य उकञ् (154)
Pāṭha: ashtadhyayi.com data.txt row i=32154 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_154_lazapatapa_154"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.154", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.154"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.154",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lazapatapadasTABUvfzahanakamagamaSFBya ukaY",
    text_dev              = "लषपतपदस्थाभूवृषहनकमगमशॄभ्य उकञ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu laza-pata-pada-sTA-BU-vfza-hana-kama-gama-SFBya ukaY kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु लष-पत-पद-स्था-भू-वृष-हन-कम-गम-शॄभ्य उकञ् कृत्",
    padaccheda_dev        = "लष-पत-पद-स्था-भू-वृष-हन-कम-गम-शॄभ्य उकञ्",
    why_dev               = "धातोः कृत्-प्रत्ययः [लषपतपदस्थाभूवृषहनकमगमशॄभ्य उकञ्] विहितः (३.२.154)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
