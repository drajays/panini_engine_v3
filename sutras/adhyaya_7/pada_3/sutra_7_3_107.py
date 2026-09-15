"""
7.3.107  अम्बाऽर्थनद्योर्ह्रस्वः  —  VIDHI

Padaccheda: अम्बा-अर्थ-नद्योः · ह्रस्वः

In सम्बुद्धि, a stem meaning *mother* or one with the **नदी** saṃjñā (1.4.3)
takes its **short** vowel:

    नदी + सु    (सम्बुद्धि)
    नदि + सु    this sūtra
    नदि         6.1.69 एङ्ह्रस्वात् सम्बुद्धेः drops the सु

Without it the सु survived to the tripāḍī and गave नदीः for हे नदि.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 73107 · अम्बाऽर्थनद्योर्ह्रस्वः
              padaccheda: अम्बा-अर्थ-नद्योः ह्रस्वः
              anuvṛtti:   64001: अङ्गस्य | 73106: सम्बुद्धौ
  Source #2 — Kāśikā 7.3.107 udāharaṇa:
                हे अम्ब
                हे अक्क
                हे अल्ल
  Cross-check — surface pinned by: tests/regression/test_shabda_paradigms.py
  Reference record: sutra_ref_out/7_3_107.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_SHORTEN = {"I": "i", "U": "u", "A": "a"}
_DONE = "7_3_107_hrasva_done"


def _target(state: State):
    """(aṅga, affix) for a नदी stem before सम्बुद्धि, still long."""
    if len(state.terms) < 2:
        return None
    anga, affix = state.terms[-2], state.terms[-1]
    if "nadi" not in anga.tags or "sambuddhi" not in affix.tags:
        return None
    if anga.meta.get(_DONE) or not anga.varnas:
        return None
    if anga.varnas[-1].slp1 not in _SHORTEN:
        return None
    return anga, affix


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    found = _target(state)
    if found is None:
        return state
    anga, _affix = found
    anga.varnas[-1] = mk(_SHORTEN[anga.varnas[-1].slp1])
    anga.meta[_DONE] = True
    state.meta["__why_now_dev__"] = (
        "सम्बुद्धौ नदी-संज्ञकस्य अन्त्य-स्वरस्य ह्रस्वः (नदी → नदि); "
        "ततः ६.१.६९ एङ्ह्रस्वात् सम्बुद्धेः इति सु-लोपः।"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.107",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ambArTanadyorhrasvaH",
    text_dev       = "अम्बाऽर्थनद्योर्ह्रस्वः",
    padaccheda_dev = "अम्बा-अर्थ-नद्योः · ह्रस्वः",
    why_dev        = "सम्बुद्धौ अम्बार्थस्य नदी-संज्ञकस्य च अन्त्य-स्वरस्य ह्रस्वः (हे नदि)।",
    anuvritti_from = ("7.3.106",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
