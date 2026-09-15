"""
7.3.116  ङेराम्नद्याम्नीभ्यः  —  VIDHI

Padaccheda: ङेः · आम् · नदी-आप्-नीभ्यः

After **नदी** (1.4.3), आप् or नी, the सप्तमी एकवचन affix ङि is replaced by आम्.
Everything after that is ordinary sandhi:

    नदी + इ     (ङि, after 1.3.8/1.3.9 drop the ṅ)
    नदी + आम्   this sūtra
    नद्याम्      6.1.77 इको यणचि

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 73116 · ङेराम्नद्याम्नीभ्यः
              padaccheda: ङेः आम् नदी-आम्-नीभ्यः
              anuvṛtti:   64001: अङ्गस्य
  Source #2 — Kāśikā 7.3.116 udāharaṇa:
                कुमारी + ङि → कुमार्याम्
                गौरी + ङि → गौर्याम्
                ब्रह्मबन्धू + ङि → ब्रह्मबन्ध्वाम्
  Cross-check — surface pinned by: tests/regression/test_shabda_paradigms.py
  Reference record: sutra_ref_out/7_3_116.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_DONE = "7_3_116_Am_adesha_done"


def _target(state: State):
    """(aṅga, affix) when नदी + ङि is on the tape and आम् is still owed."""
    if len(state.terms) < 2:
        return None
    anga, affix = state.terms[-2], state.terms[-1]
    if "nadi" not in anga.tags or "sup" not in affix.tags:
        return None
    if affix.meta.get(_DONE) or not affix.varnas:
        return None
    if (affix.meta.get("upadesha_slp1") or "") != "Ni":
        return None
    # After the ṅ has gone (1.3.8 → 1.3.9); the ādeśa replaces the affix, not
    # an it-marker that is about to be dropped.
    if affix.varnas[0].slp1 == "N":
        return None
    return anga, affix


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    found = _target(state)
    if found is None:
        return state
    _anga, affix = found
    affix.varnas[:] = [mk("A"), mk("m")]
    affix.meta[_DONE] = True
    state.meta["__why_now_dev__"] = (
        "नदी-संज्ञकात् परे ङेः स्थाने आम् इति आदेशः; ततः ६.१.७७ इको यणचि इति यण् "
        "(नदी + आम् → नद्याम्)।"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.116",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "GerAmnadyAmnIByaH",
    text_dev       = "ङेराम्नद्याम्नीभ्यः",
    padaccheda_dev = "ङेः · आम् · नदी-आप्-नीभ्यः",
    why_dev        = "नदी-आप्-नी-शब्देभ्यः परस्य ङेः (सप्तमी-एकवचनस्य) स्थाने आम् (नद्याम्)।",
    anuvritti_from = ("7.3.111",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
