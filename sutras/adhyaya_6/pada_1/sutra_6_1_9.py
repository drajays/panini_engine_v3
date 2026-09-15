"""
6.1.9  सन्‍यङोः  —  VIDHI (narrow)

Glass-box: marks yaG term as reduplication-trigger so later rules can operate.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61009 · सन्यङोः
              padaccheda: सन्-यङोः
              anuvṛtti:   61008: धातोः अनभ्यासस्य | 61001: एकाचः द्वे प्रथमस्य | 61002: अजादेः द्वितीयस्य
  Source #2 — Kāśikā 6.1.9 udāharaṇa:
                सन्यङोरिति च षष्ठ्यन्तमेतत्
                पिपक्षति
                पिपतिषति
  Cross-check — surface pinned by: tests/unit/test_aabhyam_idam_7_2_113.py, tests/unit/test_mAtApitarO_dvandva_split_prakriyas.py, tests/unit/test_tinanta_abhavisyat_lrg.py
  Reference record: sutra_ref_out/6_1_9.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    # Fire once when a yaG term exists.
    if state.samjna_registry.get("6.1.9_sanyango"):
        return False
    return any((t.meta.get("upadesha_slp1") or "").strip() == "yaG" for t in state.terms)


def act(state: State) -> State:
    # Absorb yaG into the dhātu as a trailing 'y' and remove the yaG term.
    if any((t.meta.get("upadesha_slp1") or "").strip() == "yaG" for t in state.terms):
        for i, t in enumerate(state.terms[:-1]):
            if "dhatu" not in t.tags:
                continue
            nxt = state.terms[i + 1]
            if (nxt.meta.get("upadesha_slp1") or "").strip() != "yaG":
                continue
            t.varnas.append(parse_slp1_upadesha_sequence("y")[0])
            del state.terms[i + 1]
            break
    state.samjna_registry["6.1.9_sanyango"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.9",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sanyangoH",
    text_dev       = "सन्‍यङोः",
    padaccheda_dev = "सन्-यङोः",
    why_dev        = "यङ्-प्रसङ्गे द्वित्व-प्रवृत्तिः (ग्लास-बॉक्स् marker)।",
    anuvritti_from = ("6.1.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

