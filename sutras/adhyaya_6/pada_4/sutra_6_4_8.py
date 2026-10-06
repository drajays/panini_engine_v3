"""
6.4.8  सर्वनामस्थाने चासम्बुद्धौ  —  VIDHI

Operational role (v3.6, neuter a-stems like ज्ञानानि):
  After 7.1.72 inserts nuṃ (n) on the aṅga, when the following pratyaya
  is `sarvanamasthana` and NOT sambuddhi, lengthen the aṅga's upadhā-vowel.

Minimal implementation (v3.6):
  - after nuṃ-āgama in our neuter demos, the aṅga ends with a final 'n'
    (the surviving consonant of nuṃ). Lengthen the upadhā vowel immediately
    before that final consonant (e.g. ... a n → ... A n).

This yields: jYAna + n + i → jYAnAn + i → ज्ञानानि (after joiner).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64008 · सर्वनामस्थाने चासम्बुद्धौ
              padaccheda: सर्वनामस्थाने च अ-सम्बुद्धौ
              anuvṛtti:   63111: दीर्घः | 64001: अङ्गस्य | 64003: नामि | 64007: नोपधायाः
  Source #2 — Kāśikā 6.4.8 udāharaṇa:
                राजा
                राजानम्
                सामानि तिष्ठन्ति
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhut_lung.py
  Reference record: sutra_ref_out/6_4_8.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _niyama_stem(anga) -> bool:
    """6.4.12's four: -in, -han (the root हन्), -pūṣan, -aryaman."""
    flat = "".join(v.slp1 for v in anga.varnas)
    return flat.endswith(("in", "pUzan", "aryaman")) or (flat.endswith("han") and "han_dhatu" in anga.tags)


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if "sarvanamasthana" not in pr.tags:
        return False
    if "sambuddhi" in pr.tags:
        return False
    if anga.meta.get("sarvanamasthana_upadha_dirgha_done"):
        return False
    if len(anga.varnas) < 3:
        return False
    # Expect final 'n' (nuṃ's surviving consonant) and an upadhā-vowel
    # immediately before it.
    if anga.varnas[-1].slp1 != "n":
        return False
    # 6.4.12 इन्हन्पूषार्यम्णां शौ (niyama): for these four stems the dīrgha is only before śi (and, by 6.4.13, su):
    # योगिनौ, वृत्रहणौ, पूषणौ, अर्यमणौ — not *योगीनौ*.
    if _niyama_stem(anga) and (pr.meta.get("upadesha_slp1") or "").strip() != "Si":
        return False
    if anga.varnas[-2].slp1 not in {"a", "i", "u"}:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    _dirgha = {"a": "A", "i": "I", "u": "U"}
    anga.varnas[-2] = mk(_dirgha[anga.varnas[-2].slp1])
    anga.meta["sarvanamasthana_upadha_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.8",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'sarvanAmasTAne cAsambudDO',
    text_dev       = 'सर्वनामस्थाने चासम्बुद्धौ',
    samagra_slp1   = "naH aNgasya upaDAyAH asambudDO sarvanAmasTAne dIrGaH",
    samagra_dev    = "नः अङ्गस्य उपधायाः असम्बुद्धौ सर्वनामस्थाने दीर्घः",
    padaccheda_dev = "सर्वनामस्थाने च असम्बुद्धौ",
    why_dev        = "असम्बुद्धि-सर्वनामस्थाने परे नपुंसक-अङ्गस्य उपधा-अकारस्य दीर्घः (ज्ञानानि)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

