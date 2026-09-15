"""
8.3.23  मोऽनुस्वारः  —  VIDHI (narrow demo)

Narrow v3 (संगसीष्ट / ``saGgasIzwa``):
  Replace a non-pada-final ``m`` before a *jhal* consonant with anusvāra ``M``
  in a single merged *pada* (``sam`` + ``gam``… → ``saM`` + ``g``…).

Engine:
  - recipe arms ``state.meta['8_3_23_m_o_anuswara_arm']``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 83023 · मोऽनुस्वारः
              padaccheda: मः अनुस्वारः
              anuvṛtti:   81016: पदस्य | 82108: संहितायाम् | 83022: हलि
              adhikāra:   8.2.1
  Source #2 — Kāśikā 8.3.23 udāharaṇa:
                कुण्डं हसति
                वनं याति
                वनं हसति
  Gloss (sa) — पदान्तस्य मकारस्य अनुस्वारः आदेशः भवति, परे हलि।
  Cross-check — surface pinned by: tests/unit/test_saGgasIzwa_sam_gam_ashir_ling.py
  Reference record: sutra_ref_out/8_3_23.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import JHAL


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_3_23_mo_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 != "m":
            continue
        if vs[i + 1].slp1 in JHAL:
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("M")
    t.meta["8_3_23_mo_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.23",
    sutra_type=SutraType.VIDHI,
    text_slp1="mo'nusvAraH",
    text_dev="मोऽनुस्वारः",
    padaccheda_dev="मः / अनुस्वारः",
    why_dev="अपदान्त-मकारस्य झलि परे अनुस्वारः — सम्+ग… (डेमो)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
