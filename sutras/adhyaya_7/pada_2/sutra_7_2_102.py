"""
7.2.102  त्यदादीनामः  —  VIDHI

Operational role (v3.7, for `tad`-like tyadādi pronouns):
  When an aṅga is tagged `tyadadi`, replace its final consonant (HAL) with
  the vowel 'a'.

This is a narrow implementation sufficient for तद्:
  tad (t-a-d) → ta (t-a-a) and 6.1.97 will collapse the double 'a'.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 72102 · त्यदादीनामः
              padaccheda: त्यद्-आदीनाम् अः
              anuvṛtti:   64001: अङ्गस्य | 72084: विभक्तौ
  Source #2 — Kāśikā 7.2.102 udāharaṇa:
                त्यद् — स्यः
                तद् — सः
                यद् — यः
  Cross-check — surface pinned by: tests/unit/test_ye_yad_jas.py
  Reference record: sutra_ref_out/7_2_102.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL, mk


def _matches(state: State) -> bool:
    if not state.terms:
        return False
    anga = state.terms[0]
    if "anga" not in anga.tags or "tyadadi" not in anga.tags:
        return False
    if not anga.varnas:
        return False
    if anga.meta.get("tyadadi_a_adesha_done"):
        return False
    if "idam_m_7_2_108" in anga.tags:
        return False  # 7.2.108 (apavāda): the final m stands
    if (anga.meta.get("upadesha_slp1") or "").strip() in ("kim", "idam") and "napuṃsaka" in anga.tags and any(
        "sup" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() in ("s~", "am") for t in state.terms[1:]
    ):
        return False  # kim + neuter su/am: sup is luk'd (7.1.23), so no ādeśa
    if anga.varnas[-1].slp1 not in HAL:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[0]
    if "".join(v.slp1 for v in anga.varnas) == "adas":
        state.meta["adas_stem"] = True   # read by 7.1.11 / 7.2.106-107 / 8.2.80-81
        if any("bahuvacana" in t.tags for t in state.terms[1:]):
            state.meta["adas_bahuvacana"] = True   # the sup's own saṃjñā, for 8.2.81
    anga.varnas[-1] = mk("a")
    anga.meta["tyadadi_a_adesha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.102",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'tyadAdInAmaH',
    text_dev       = 'त्यदादीनामः',
    padaccheda_dev = "त्यदादीनाम् अः",
    why_dev        = "त्यदादि-गण-शब्दानां विभक्ति-प्रत्यये परे अन्त्य-हल्-स्थानि अकार-आदेशः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

