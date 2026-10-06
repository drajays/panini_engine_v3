"""
3.2.182  दाम्नीशसयुयुजस्तुतुदसिसिचमिहपतदशनहः करणे  —  VIDHI

Padaccheda: दाप्-नी-शस-यु-युज-स्तु-तुद-सि-सिच-मिह-पत-दश-नहः करणे

krt-suffix rule: दाम्नीशसयुयुजस्तुतुदसिसिचमिहपतदशनहः करणे (182)
Pāṭha: ashtadhyayi.com data.txt row i=32182 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_182_dAmnISasay_182"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.182", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.182"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.182",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dAmnISasayuyujastutudasisicamihapatadaSanahaH karaRe",
    text_dev              = "दाम्नीशसयुयुजस्तुतुदसिसिचमिहपतदशनहः करणे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne dAp-nI-Sasa-yu-yuja-stu-tuda-si-sica-miha-pata-daSa-nahaH karaRe kft zwran",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने दाप्-नी-शस-यु-युज-स्तु-तुद-सि-सिच-मिह-पत-दश-नहः करणे कृत् ष्ट्रन्",
    padaccheda_dev        = "दाप्-नी-शस-यु-युज-स्तु-तुद-सि-सिच-मिह-पत-दश-नहः करणे",
    why_dev               = "धातोः कृत्-प्रत्ययः [दाम्नीशसयुयुजस्तुतुदसिसिचमिहपतदशनहः करणे] विहितः (३.२.182)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
