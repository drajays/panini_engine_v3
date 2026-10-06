"""
3.3.16  पदरुजविशस्पृशो घञ्  —  VIDHI

Padaccheda: पदरुज-विश-स्पृशः घञ्

krt-suffix rule: पदरुजविशस्पृशो घञ्

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 33016 · पदरुजविशस्पृशो घञ्
              padaccheda: पदरुज-विश-स्पृशः घञ्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ्
  Source #2 — Kāśikā 3.3.16 udāharaṇa:
                इत उत्तरं त्रिष्वपि कालेषु प्रत्ययाः
                पदादिभ्यो धातुभ्यो घञ् प्रत्ययो भवति
                पद्यतेऽसौ पादः
  Cross-check — surface pinned by: tests/unit/test_bhattikavya_1_1.py, tests/unit/test_paceran_vidhi_liG_pac_Ja.py, tests/unit/test_tinanta_bhavatu_lot.py
  Reference record: sutra_ref_out/3_3_16.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_16_padarujavi_16"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.16", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.16"
    if state.meta.get("krt_upadesha_slp1") == "GaY" and not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    ):
        from engine.state import Term
        from phonology.varna import parse_slp1_upadesha_sequence
        state.terms.append(Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("GaY")),
            tags={"pratyaya", "krt", "upadesha", "ardhadhatuka"},
            meta={"upadesha_slp1": "GaY", "it_markers": {"G", "Y"}},
        ))
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "padarujaviSaspfSo GaY",
    text_dev              = "पदरुजविशस्पृशो घञ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH pada-ruja-viSa-spfSaH GaY kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः पद-रुज-विश-स्पृशः घञ् कृत्",
    padaccheda_dev        = "पदरुज-विश-स्पृशः घञ्",
    why_dev               = "धातोः प्रत्ययः (३.3.16)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
